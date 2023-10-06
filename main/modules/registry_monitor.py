import winreg
import win32api
import win32event

from modules.clean_up import clean

REG_NOTIFY_CHANGE_LAST_SET = win32api.REG_NOTIFY_CHANGE_LAST_SET
KEY_READ = winreg.KEY_READ
KEY_WRITE = winreg.KEY_WRITE

class registry:
    def __init__(self, logger, subkey=None):
        self.event_handle = win32event.CreateEvent(None, 0, 0, None)
        self.registry_key = winreg.HKEY_LOCAL_MACHINE 
        self.baseline_values = {}
        self.subkey = subkey
        self.logger = logger
        self.clean = clean(None, self.logger)


    def key_changed(self, value_name, change_type, value_data=None):
        # handles each event triggered from procees_changes and logs the detection event outcome
        # if no change in last set time, we know the key has been deleted else the same checks as processes_changes are done  

        if change_type == REG_NOTIFY_CHANGE_LAST_SET:
            if value_name not in self.baseline_values:
                self.logger.info(f"New key added: {self.subkey} - {value_name} - {value_data}")
                print(f"\nCONSOLE Key Added:\nCONSOLE Path - {self.subkey}\nCONSOLE Name - {value_name} - {value_data}")
                check_remove = input("CONSOLE Approve this added key; Would you like to remove this newly added key? (y/n) ")
                if check_remove == "y".lower():
                    action = "delete"
                    self.clean.registry_fix(action, value_name, self.baseline_values[value_name], self.registry_key, self.subkey, self.baseline_values)

            elif value_data != self.baseline_values[value_name]:                   
                self.logger.info(f"Key modified: {self.subkey} - {value_name} - {value_data}")
                self.logger.info(f"Old key value - {self.baseline_values[value_name]}")
                print(f"\nCONSOLE Key modified:\nCONSOLE Path - {self.subkey}\nCONSOLE Name - {value_name} - {value_data}")
                print(f"CONSOLE Old key value - {self.baseline_values[value_name]}")
                check_restore = input("CONSOLE Approve this modified key; Would you like to restore the orginal value? (y/n) ")
                if check_restore == "y".lower():
                    action = "restore"
                    self.clean.registry_fix(action, value_name, self.baseline_values[value_name], self.registry_key, self.subkey, self.baseline_values)

        else:
            self.logger.info(f"Key deleted: {self.subkey} - {value_name}")
            print(f"CONSOLE Key deleted:\nCONSOLE Path - {self.subkey}\nCONSOLE Name - {value_name}")


    def processes_changes(self, current_values):
        # first checks if the key is in the base line data (new)
        # then check if there is a change in size from the baseline (deleted)
        # then checks the value data of the key compared to the value data stored in the base line data (modified)

        deleted_values = set(self.baseline_values.keys()) - set(current_values.keys())
        for deleted_value in deleted_values:
            self.key_changed(deleted_value, None, None)
            self.baseline_values = current_values

        for value_name, value_data in current_values.items():
            if value_name not in self.baseline_values:
                self.key_changed(value_name, REG_NOTIFY_CHANGE_LAST_SET, value_data)
                self.baseline_values = current_values

            elif value_data != self.baseline_values[value_name]:
                self.key_changed(value_name, REG_NOTIFY_CHANGE_LAST_SET, value_data)

        

    def query(self):
        # opens the key path and iterates though each key in the path and adds it to a dictonary as a key pair
        # creates a new local values dictonary each time queried to reduce chance of false flags 

        current_values = {}
        with winreg.OpenKey(self.registry_key, self.subkey, 0, KEY_READ) as key:
            index = 0
            while 1:
                try:
                    value_name, value_data, _ = winreg.EnumValue(key, index)
                    current_values[value_name] = value_data
                    index += 1
                except WindowsError:
                    break

        self.processes_changes(current_values)


    def create_baseline(self):
        # opens the key path and iterates though each key in the path and adds a dictonary as a key pair
        # creates a baseline to detected changes from

        with winreg.OpenKey(self.registry_key, self.subkey, 0, KEY_READ) as key:
            index = 0
            while 1:
                try:
                    value_name, value_data, _ = winreg.EnumValue(key, index)
                    self.baseline_values[value_name] = value_data
                    index += 1
                except OSError:
                    break


    def monitor(self):
        # opens up the key path for monitoring and creates and event handler to capture event changes
        # monitors for changes in last set time and then pairs each change with a event handle 
        # if WAIT_OBJECT_0 then there has been changes in the path
        # queries the change and resets for the next change

        # might change this to with open key
        key = winreg.OpenKey(self.registry_key, self.subkey, 0, KEY_READ)
        win32api.RegNotifyChangeKeyValue(key, True, REG_NOTIFY_CHANGE_LAST_SET, self.event_handle, True)
        self.create_baseline()

        try:
            while 1:
                event = win32event.WaitForSingleObject(self.event_handle, 5000)
                if event == win32event.WAIT_OBJECT_0:
                    win32api.RegQueryInfoKey(key)[2]
                    self.query()
                    win32api.RegNotifyChangeKeyValue(key, True, REG_NOTIFY_CHANGE_LAST_SET, self.event_handle, True)
                    
                import time # single import
                time.sleep(0.5)

        except Exception as e:
            self.logger.info(f"!! An error while monitoring the registry {e} !!")
        finally:
            win32api.CloseHandle(self.event_handle)
            winreg.CloseKey(key)

