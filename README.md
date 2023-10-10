# Monitoring Tool 

A real time Python monitoring tool for tracking changes on Windows machines. Monitors marked file directories, Windows registry changes, and new processes with detailed logs whenever a change is detected

**Usage**
```bash
# Install needed packages
python pip install -r requirements.txt

# Download lastest malware hashes
# -a flag enables automatic downloads
python main.py update [-a]

# Registry paths are hard coded for now
# Add file directories to be monitored by marking
python main.py mark <directory>

# Start monitor
# -h flag hides the command prompt
python main.py start [-h]

# List all marked directories
python main.py list

# Clear all marked directories
python main.py clear
```

**Features**  

- Option to scan all current files and folders in marked directories
- Detects unknown system services by comparing each one to a list of verified services at a set interval
- Detects changes made in marked directories (Added, Modified, and Deleted)
- Detects random named files and unwanted extensions
- Detects changes made in system registry (Added, Modified, and Deleted)
- Detects newly spawned processes
- Adjustable config file

**Detection and Clean Up**  

- Option to restore modified registry values
- Option to remove newly added registry keys
- File contents are scanned for commonly known malware patterns found in stager/dopper files 
- All file types are hashed and compared againts a list of updated malware hashes
- Commonly used malware parent process handles are forced closed
- File gets renamed with .malz extension and moved with the current state of the log file into a zipped folder
- The zipped folder gets copied into a set quarantine directory for further analysis
- All orignal files are removed
  
