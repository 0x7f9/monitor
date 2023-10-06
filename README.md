# Monitoring Tool 

A real time Python monitoring tool for tracking changes on windows machines. 

**Usage**
```bash
# Install needed packages
python pip install -r requirements.txt

# Download lastest malware hashes
# Using the -a flag enables automatic downloads
python main.py update [-a]

# Registry paths are hard coded for now
# Add file directories to be monitored by marking
python main.py mark <directory>

# Start monitor
# Using the -h flag hides the command prompt
python main.py start [-h]
```

**Features**  

- Detects unknow system services by comparing each one to a list of verified services at an interval
- Detects changes made in set directory (Added, Modified, and Deleted)
- Detects random named files and unwanted extensions
- Detects changes made in system registry (Added, Modified, and Deleted)
- Detects newly spawned processes
- Option to scan current files and folders in marked directories for security events
- Adjustable config file

**Detection and Clean Up**  

- Option to restore modified registry values
- Option to remove newly added registry keys
- File contents are scanned for commonly known malware patterns found in stager/dopper files 
- All file types are hashed and compared againts a list of updated malware hashes
- Commonly used parent process handles get forced closed and explorer.exe gets restarted
- File gets renamed with .malz extension and moved with the current state of log file into a ziped folder
- Ziped folder gets copied into a set quarantine directory for further analysis
- All orignal files are removed
  
