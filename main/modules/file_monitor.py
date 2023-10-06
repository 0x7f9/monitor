import time
import os
import win32file
import win32security
import threading 

from . import *
from modules.detection import detection

class monitor:
    def __init__(self, path, logger, download_file, isolated_path, spider_dir=None):
        self.spider_dir = spider_dir
        self.malware_hashes = set()
        self.path = path
        self.handle = None
        self.contents = None
        self.old_name = None
        self.logger = logger
        self.isolated_path = isolated_path
        self.download_file = download_file
        self.detect = detection(self.malware_hashes, self.isolated_path, self.logger)


    def get_handle(self):
        handle = win32file.CreateFile(
            self.path,
            FILE_LIST_DIRECTORY,
            FILE_SHARE_READ | 
            FILE_SHARE_WRITE |
            FILE_SHARE_DELETE,
            None,
            OPEN_EXISTING,
            FILE_FLAG_BACKUP_SEMANTICS,
            None
        )
        return handle
    
    
    def get_changes(self):
        changes = win32file.ReadDirectoryChangesW(
            self.handle,
            1024,
            True,
            FILE_NOTIFY_CHANGE_ATTRIBUTES |
            FILE_NOTIFY_CHANGE_DIR_NAME |
            FILE_NOTIFY_CHANGE_FILE_NAME |
            FILE_NOTIFY_CHANGE_LAST_WRITE |
            FILE_NOTIFY_CHANGE_SECURITY |
            FILE_NOTIFY_CHANGE_SIZE,
            None,
            None
        )
        return changes


    def get_username(self, path_filename):
        # returns the username associated with the file change

        if os.path.exists(path_filename):
            file_security = win32security.GetFileSecurity(path_filename, win32security.OWNER_SECURITY_INFORMATION)
            sid = file_security.GetSecurityDescriptorOwner()
            account, _, _ = win32security.LookupAccountSid(None, sid)
            return account
        else:
            return "unknow"

    
    def monitor_handle(self, handle, filename, path_filename, username):
        # detecting what changes occurred after being notified

        if handle == FILE_ACTION_ADDED:
            self.logger.info(f"+ User: {username} Created: {path_filename}")
            self.detect.valid_name(path_filename, filename)

        elif handle == FILE_ACTION_REMOVED:
            self.logger.info(f"- User: {username} Deleted: {path_filename}")

        elif handle == FILE_ACTION_MODIFIED:
            self.logger.info(f"! User: {username} Modified: {filename}")
            self.detect.security_event(path_filename, filename)
                                    
        elif handle == FILE_RENAMED_FROM:
            self.old_name = filename

        elif handle == FILE_RENAMED_TO:
            self.logger.info(f"User: {username} renamed: [{self.old_name}] to: [{filename}]")
            self.detect.valid_name(path_filename, filename)

        else:
            self.logger.info(f"? Unknown action: {path_filename}")


    def read_downloaded_hashes(self, malware_hashes):
        with open(malware_hashes, "r") as file:
            for line in file:
                if line.startswith("#"):
                    continue
                hash_value = line.strip()
                self.malware_hashes.add(hash_value)
                

    def main(self):
        # this just gets passed into detection but need to load early
        self.read_downloaded_hashes(self.download_file)

        if self.spider_dir is True:
            path = self.path
            spider = threading.Thread(target=self.detect.os_spider, args=(path,))

            # start along side self.runner
            spider.start()

            # block main thread from starting while checking files
            # spider.join() 

        # monitoring checking for changes in set paths
        try:
            self.handle = self.get_handle()

            while 1:
                for handle, filename in self.get_changes():
                    path_filename = os.path.join(self.path, filename)
                    filename = os.path.basename(path_filename)
                    username = self.get_username(path_filename)
                    self.monitor_handle(handle, filename, path_filename, username)

            time.sleep(1) # -_- 

        except Exception as e:
            self.logger.info(f"!! Error during main runtime !!: {e}")

