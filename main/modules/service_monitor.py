import hashlib 
import psutil
import re

from signatures.microsoft_services import microsoft_services
# from modules.detection import detection

class service:
    def __init__(self, logger, interval):
        self.services = []
        self.logger = logger
        self.service_name = None
        self.verified_count = 0
        self.unverified_count = 0
        self.interval = interval


    def base_service_name(self):
        # removes ending numbers on some services names that require it

        pattern = r"^(.+?)_\w+$"        
        match = re.match(pattern, self.service_name)
        
        if match:
            return match.group(1)
        
        return self.service_name
        

    def get_services(self):
        # gets all services on the machine

        try:
            for service in psutil.win_service_iter():
                service_info = service.as_dict()
                self.services.append(service_info)
        except psutil.AccessDenied:
            pass


    def calculate_hash(self, input):
        input_string = str(input)  
        return hashlib.sha256(input_string.encode("utf-8")).hexdigest()


    def valid_service(self, service):
        # returns true if current hash is in whitelisted services

        self.service_name = service['name']
        hash = self.base_service_name()

        hash_value = self.calculate_hash(hash)
        return hash_value in microsoft_services


    def service_security_event(self, service):
        # service security event handler

        self.logger.info("!! Security event service triggered (Unverified-services) !!")
        self.logger.info("Name: {}\nDisplay name: {}\nName: {}\nUser launched: {}\nBinpath: {}\nStatus: {}\nDescription: {}".format(
                service['name'],
                service['display_name'],
                service['name'],
                service['username'],
                service['binpath'],
                service['status'],
                service['description'].replace(".", "\n           "))
        )

        # check = detection(None, None, self.logger)
        # check_stop = input(f"!! Stop and uninstall {self.service_name} y/n? !! ")
        # if check_stop == "y".lower():
        #     check.remove_service()
            

    def main(self):
        while 1:
            self.verified_count = 0
            self.unverified_count = 0
            self.services.clear()   
            
            self.get_services()
            for service in self.services:
                if self.valid_service(service):
                    self.verified_count += 1
                else:
                    self.unverified_count += 1
                    self.service_security_event(service)

            self.logger.info(f"Verified Services: {self.verified_count}/261" )
            self.logger.info(f"Unverified Services: {self.unverified_count}/261\n")
            print(f"CONSOLE Verified Services: {self.verified_count}/261" )
            print(f"CONSOLE Unverified Services: {self.unverified_count}/261\n")
            import time # single import
            time.sleep(self.interval)
            
