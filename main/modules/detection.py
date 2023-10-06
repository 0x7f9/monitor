import os
import hashlib
import re
import enchant
import concurrent.futures
import multiprocessing
import threading

from signatures.file_extensions import file_extensions
from signatures.malware_patterns import malware_patterns
from modules.clean_up import clean

class detection:
    def __init__(self, malware_hashes=None, isolated_path=None, logger=None):
        self.logger = logger
        self.isolated_path = isolated_path
        self.malware_hashes = malware_hashes
        self.processed_files = set()
        self.cores_to_use  = multiprocessing.cpu_count() - 2
        self.threads = concurrent.futures.ThreadPoolExecutor(max_workers=self.cores_to_use)
        self.clean = clean(self.isolated_path, self.logger)


    def __del__(self):
        self.stop_threads()


    def security_event(self, path_filename, filename):
        if path_filename is None:
            return
        
        if os.path.isdir(path_filename):
            return

        if filename in self.processed_files:
            return 

        try:            
            self.processed_files.add(filename)
            self.dumper(path_filename)    
            self.scan_file(path_filename, filename)
                
        except Exception:
            self.logger.info("!! Error during security event !!")
            pass
            

    def valid_word(self, word):
        english_dict = enchant.Dict("en_US")
        return english_dict.check(word)
    

    def valid_name(self, path_filename, filename):
        # checks if the file name contains any bad file entensions 
        # checks name contains correct values before detecting if its a valid word 

        for extension in file_extensions:
            if re.search(extension, filename, re.IGNORECASE):
                self.logger.info(f"!! File extension is not allowed {extension} !!")
                self.logger.info(f"!! {filename} File extension is not allowed !!")

                # .exe is high risk so we go straight to deleting/coping
                extension_pattern = r"\.exe\b"   
                if extension == extension_pattern:
                    self.clean.security_event_copy(path_filename, filename, self.contents)
                    return # so we dont try and scan
                
                self.security_event(path_filename, filename)        


        base_name, _ = os.path.splitext(filename)
        cleaned_base_name = re.sub(r"[^a-zA-Z0-9\s]+$", "", base_name)
        words = cleaned_base_name.split()

        if all(self.valid_word(word) for word in words):
            self.logger.info(f"{filename} is valid")
            return 
        
        self.logger.info(f"!! Potential security event (Suspicious name) !!")
        self.security_event(path_filename, filename)        


    def dumper(self, path_filename):
        self.contents = None
        with open(path_filename, "r", encoding="utf-8") as f:
            self.contents = f.read()
            if len(self.contents) == 0:
                return

 
    def scan_file(self, path_filename, filename):
        self.logger.info(f"Scanning {filename}")
        self.logger.info(f"Path {path_filename}")

        hash_thread = threading.Thread(target=self.compare_hashes, args=(path_filename, filename))
        malware_thread = threading.Thread(target=self.detect_malware_strings, args=(path_filename, filename))
        hash_thread.start()
        malware_thread.start()
        hash_thread.join()
        malware_thread.join()

        self.logger.info("Scan complete\n")

    def compare_hashes(self, path_filename, filename):
        # returns hashes and compares the sha-256 hash againts a list

        try:
            sha256_hash = hashlib.sha256()
            md5_hash = hashlib.md5()

            # read in 64kb at a time
            with open(path_filename, "rb") as f:
                for block in iter(lambda: f.read(65536), b""):
                    sha256_hash.update(block)
                    md5_hash.update(block)

            self.logger.info(f"MD5 HASH: {md5_hash.hexdigest()}")
            self.logger.info(f"SHA-256 HASH: {sha256_hash.hexdigest()}")

            hash = sha256_hash.hexdigest()
            if hash in self.malware_hashes:
                self.logger.info(f"!! Malware hash match found !!: {hash}")
                self.clean.security_event_copy(path_filename, filename, self.contents)
                return

            return self.logger.info("File was not matched with a malware hash")
        except:
            self.logger.info("File is unable to be matched with a malware hash")

        
    def detect_malware_strings(self, path_filename, filename):
        # detects common malware string patterns in the scanned file contents

        try:
            for pattern in malware_patterns:
                if re.search(pattern, self.contents):
                    self.logger.info("!! Common malware string found in file !!")
                    self.logger.info(f"!! Pattern found: {pattern} !!")
                    print(f"CONSOLE Pattern found: {pattern}\nPATH: {path_filename}\n")  
                    self.clean.security_event_copy(path_filename, filename, self.contents)
                    return

            return self.logger.info("Found no patterns in file contents.")
        except:
            self.logger.info("File is unable to be pattern matched")
 

    def os_spider(self, path):
        # list all files and folders in the current directory and then submits all files to a thread pool to be scanned 
        # for every security event. if its a directory it will recall it self to search that directory

        try:
            files = os.listdir(path)
            futures = []

            for file in files:
                file_path = os.path.join(path, file)

                # submit files to the thread pool
                if os.path.isfile(file_path):
                    future = self.threads.submit(self.security_event, file_path, file)
                    futures.append(future)

                elif os.path.isdir(file_path):
                    self.os_spider(file_path) 

            concurrent.futures.wait(futures)
        except Exception:
            pass


    def stop_threads(self):
        self.threads.shutdown()

