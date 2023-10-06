import threading
import requests
import sys
import os
import ctypes

from modules.service_monitor import service
from modules.file_monitor import monitor
from modules.registry_monitor import registry
from modules.process_monitor import process_monitor
from modules.logger import monitor_logger, service_logger, process_logger, registry_logger
from main.signatures.registry_paths import registry_keys

BASE_SERVICE_INTERVAL = 120 
BASE_ISOLATED_PATH = "C:\\Users\\Public"
CONFIG_FILE = "config.txt"
STORED_PATHS = set()
AUTO_DOWNLOAD = False
NEED_CONFIG = False
SPIDER = False
PATHS = [
    "C:\\Users\\dev\\AppData\\Local\\Temp"
         
    # add hard coded directorys to monitor here
    # these paths will get loaded into the config file
]  


if not os.path.isfile(CONFIG_FILE):
    NEED_CONFIG = True


def get_admin(hide):
    # prompts the user for admin, detects if the user inputs yes or no
    # if yes ShellExecuteW spawns a new windows with admin and the old process is killed

    windll = ctypes.windll
    try:
        if windll.shell32.IsUserAnAdmin():
             return True
        
        get_input = input(f"Admin needed for detection clean up; Give admin? (y/n) ").lower()
        if get_input == "n":
            if hide == 0:
                windll.shell32.ShellExecuteW(None, None, sys.executable, " ".join(sys.argv), None, hide)
                print("Spawning new process with hidden flag")
                os._exit(0)
            return 
        
        check = windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, hide)
        if not check >= 32:
            return 
        
        print(f"Spawning new process with ADMIN {'and hidden flags' if hide == 0 else ''}")
        os._exit(0)
    except:
        return 


def download_hashes(url, malware_file):
    # will send a get request for the raw data on the webpage and save it to a file

    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        # check the Content-Type before downloading to ensure we only have text 
        # this is a good secuirty check to ensure we are only getting raw text and not .exe files
        content_type = response.headers.get("Content-Type", "")
        required = "text/plain"
        
        if not content_type.startswith(required):
            print("Unsafe Content-Type:", content_type)
            return
  
        with open(malware_file, "w", encoding="utf-8") as file:
            file.write(content) 

        monitor_logger.info("+ Malware hash file updated")
        print("CONSOLE + Malware hash file updated")
    except requests.exceptions.RequestException as e:
        monitor_logger.info(f" !! Error download new hashes !!: {e}")


def make_config(AUTO_DOWNLOAD=None):
    # creates a config file with a set template and writes static paths to the config

    print(f"+ Config file made {CONFIG_FILE}")
    with open(CONFIG_FILE, "w") as file:
        file.write("# CONFIG FILE\n")
        file.write("# If saved everything will load on next monitoring session\n")
        file.write("# Service interval checking timer is in seconds\n")
        file.write(f"# Isolated path = {BASE_ISOLATED_PATH}\n")
        file.write(f"# Interval = {BASE_SERVICE_INTERVAL}\n")

        if AUTO_DOWNLOAD == True:
            file.write(f"# Auto Download = {True}\n\n")
        else:
            file.write(f"# Auto Download = {False}\n\n")

        file.write("# Monitor config file (add directories like below)\n")
        file.write("# ;C:\\Users\\dev\n")
        file.write("# ;C:\\Users\\dev\\AppData\\Local\n\n")
        
        for path in PATHS:
            file.write(f";{path}")
            STORED_PATHS.add(path)

        file.write(f"\n\n")


def save_config(path=None):
    if path == None:
        return
    
    with open(CONFIG_FILE, "a") as file:
        if path not in STORED_PATHS:
            file.write(f";{path}\n")
        STORED_PATHS.add(path)


def load_config():
    config = {}
    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                if line.startswith("# Isolated path ="):
                    config["ISOLATED_PATH"] = line.split(" = ")[1].strip()

                elif line.startswith("# Interval ="):
                    config["INTERVAL"] = line.split(" = ")[1].strip()

                elif line.startswith("# Auto Download ="):
                    config["DOWNLOAD"] = line.split(" = ")[1].strip()

                elif line.startswith(";"):
                    path = line.strip().strip(";")
                    if path not in PATHS:
                        PATHS.append(path)
        return config
    except:
        print("!! Possibly no config found !!")
        if NEED_CONFIG:
            make_config(None)


def service_():
    service_logger.info("Started service monitoring..")
    checker = service(service_logger, int(SERVICE_INTERVAL))
    checker.main()
    service_logger.info(f"Checking services again in {SERVICE_INTERVAL} seconds")


def monitor_():
    monitor_logger.info("Started file monitoring..")
    for path in PATHS:
        _monitor = monitor(path, monitor_logger, download_path, ISOLATED_PATH, SPIDER=SPIDER)
        monitor_thread = threading.Thread(target=_monitor.main)
        monitor_thread.start()


def registry_():
    registry_logger.info("Started registry monitoring..")
    for subkey in registry_keys:
        _registry = registry(registry_logger, subkey)
        thread = threading.Thread(target=_registry.monitor)
        thread.start()


def process_():
    process_logger.info("Started process monitoring..")
    process_thread = threading.Thread(target=process_monitor, args=(process_logger,))
    process_thread.start()   


if __name__ == "__main__":
    if not len(sys.argv) >= 2:
        print("Help: python pywimmon.py <UPDATE | LIST | MARK | START [-h]> ")
        sys.exit()
    else:
        command = sys.argv[1]

    load_config()

    current_pid = os.getpid()
    print(f"DEBUG PID: {current_pid}")

    # MalwareBazaar recent malware samples (SHA256 hashes)
    # malware hashes are updated daily
    url = "https://bazaar.abuse.ch/export/txt/sha256/recent/"
    download_path = os.path.join("signatures", "malware_hashes.txt")

    user_data = load_config()
    ISOLATED_PATH = user_data.get("ISOLATED_PATH", BASE_ISOLATED_PATH)
    SERVICE_INTERVAL = user_data.get("INTERVAL", BASE_SERVICE_INTERVAL)
    ENABLE_AUTO_DOWNLOAD = user_data.get("DOWNLOAD", AUTO_DOWNLOAD)

    if command == "update":
        print("CONSOLE Trying to download updated malware hash file...")
        if len(sys.argv) > 2 and sys.argv[2] == "-a":
            AUTO_DOWNLOAD = True
            make_config(AUTO_DOWNLOAD=AUTO_DOWNLOAD) 

        download_hashes(url, download_path)

    elif command == "list":
        for item in PATHS:
            print(f"CONSOLE + MARKED {item}")
    
    elif command == "clear":
        PATHS.clear()
        with open(CONFIG_FILE, "w") as file:
            file.write("")
        print("CONSOLE !! All MARKED directories cleared !!")

    elif command.startswith("start"):
        load_config()
        
        hide = 1
        if len(sys.argv) > 2 and sys.argv[2] == "-h":
            hide = 0 

        if not get_admin(hide):
            print("CONSOLE Monitor: NOT running as admin")
        else:
            print("CONSOLE Monitor: Running as admin")

        check_spider = input("\nCheck for security events; Would you like to search current path files? (y/n) ")
        if check_spider == "y".lower():
            SPIDER = True

        # it comes from the config files as a string
        if ENABLE_AUTO_DOWNLOAD == "True":
            print("CONSOLE Trying to download updated malware hash file...")
            download_hashes(url, download_path)
    
        monitor_logger.info(f"Started{' hidden' if hide == 0 else ' unhidden'} monitoring mode")
        print(f"CONSOLE !! Started{' hidden' if hide == 0 else ' unhidden'} monitoring mode !!")
        print("CONSOLE !! Started monitoring registry !!")
        print("CONSOLE !! Started monitoring MARKED directories !!")
        print("CONSOLE !! Started monitoring window services !!")
        print("CONSOLE !! close out of the terminal to stop  !!")
        
        process_()
        registry_() 
        monitor_()
        service_()

    elif command == "mark":
        if len(sys.argv) != 3:
            print("Help: python pywimmon.py <MARK> <path-to-watch>")
            sys.exit()

        path = sys.argv[2]
        if path not in PATHS:
            print(f"MARKED '{path}' ")
            PATHS.append(path)
            save_config(path=path)
        else:
            print(f"'{path}' is in MARKED paths already")
