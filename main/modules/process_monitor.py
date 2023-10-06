import time
import psutil 

def process_monitor(logger):
    # tried to make it optimised as possible by only comparing pids on the fly 
    # also skips printing on the first iteration

    base_processes = set()
    first = True  

    while 1:
        try:
            new_processes = set()

            for process in psutil.process_iter():
                try:
                    new_processes.add(process.pid)
                except:
                    pass

            # compares each pid with the last base of processes
            for pid in new_processes:
                if pid not in base_processes:
                    try:
                        process = psutil.Process(pid)
                        if not first:
                            logger.info(f"New Process > {pid} Name: {process.name()}\nLaunch command: {process.cmdline()}\n")
                            print(f"CONSOLE New Process > {pid} Name: {process.name()}\nLaunch command: {process.cmdline()}\n")

                    except:
                        pass 

            first = False 
            base_processes = new_processes
            time.sleep(1.5)
        except:
            pass

