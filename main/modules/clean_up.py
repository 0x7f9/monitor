import os
import shutil
import zipfile
import psutil
import subprocess
import winreg    

KEY_WRITE = winreg.KEY_WRITE
REG_SZ = winreg.REG_SZ
REG_DWORD = winreg.REG_DWORD

class clean:
    def __init__(self, isolated_path, logger):
        self.isolated_path = isolated_path
        self.logger = logger


    def close_process(self):
        # goes through a list of process and tries to force close out the process
        # restarts Windows Explorer/windows manager after closing it out 
        # detects own pid and checks againts each process to not kill itself

        self.logger.info("Closing out common parent handles")
        process_list = ["notepad.exe", "explorer.exe", "cmd.exe", "powershell.exe"]
        current_pid = os.getpid()
        processes = set()

        for process in psutil.process_iter():
            try:
                processes.add(process.pid)
            except:
                pass
                
        for pid in processes:
            try:
                process = psutil.Process(pid)
                name = process.name()

                if name.lower() in process_list and pid != current_pid:      
                    process.terminate()
                    process.wait()
                    self.logger.info(f"Closed: {name} PID: {pid}")

                    if name.lower() == "explorer.exe":
                        subprocess.Popen(["explorer.exe"])
                        self.logger.info("Restarted Windows Explorer")

            except:
                self.logger.info(f"!! Error closing process !!: {name}")


    def registry_fix(self, action, value_name, value_data, registry_key, subkey, baseline_values=None):
        # this will restore the baseline values or delete keys registry based on the action passed in to the detection class
        # it can take string (bytes REG_SZ) and (0,1 DWORD) values to restore

        try:
            with winreg.OpenKey(registry_key, subkey, 0, KEY_WRITE) as key:
                if action == "restore":
                    # if the value data is string we encode 
                    if isinstance(value_data, str):
                        value_data = value_data.encode('utf-16-le')

                    value_type = REG_SZ if isinstance(value_data, bytes) else REG_DWORD
                    winreg.SetValueEx(key, value_name, 0, value_type, value_data)                    
                    baseline_values[value_name] = value_data
                    self.logger.info("Orignal value has been restored")
                    print("CONSOLE Orignal value has been restored")

                elif action == "delete":
                    winreg.DeleteKey(key, "")
                    self.logger.info(f"Key has been Deleted: {subkey}")
                    print(f"CONSOLE Key has been Deleted: {subkey}")

        except Exception as e:
             self.logger.info(f"!! Error fixing registry change {e} !!")
             pass


    def security_event_copy(self, path_filename, filename, contents):
        # copies detected files to isolated directory and handles clean up for security event detections
        # changes the file name and compress contents for security reasons
        # closes out of certain proccess for secuirty reasons

        base_name = os.path.splitext(filename)[0]
        log_file = "logging/monitor.log"
        stored_file = f"stored_{base_name}.zip"
        path = os.path.join(self.isolated_path, stored_file)
 
        self.close_process()
        try:
            with zipfile.ZipFile(stored_file, "w", zipfile.ZIP_DEFLATED) as zipped:
                zipped.writestr(f"{base_name}.malz", contents)
                zipped.write(log_file, f"{log_file}")

            shutil.copy(stored_file, self.isolated_path)
            self.logger.info(f"+ File copied to: {path}")

            os.remove(stored_file)
            os.remove(path_filename)
            
        except Exception as e:
            self.logger.info(f"!! Error during security event copy !!: {e}")
            pass

            