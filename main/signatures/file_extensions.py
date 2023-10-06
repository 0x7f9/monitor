# Adding \b helps avoid false positives when searching for specific file extensions
# files extensions in here will trigger a hash scan when found

file_extensions = [    
    r"\.dll\b",                                              # Detect dynamic-link libraries 
    r"\.exe\b",                                              # Detect executable files
    r"\.bat\b",                                              # Detect batch files
    r"\.ps1\b",                                              # Detect PowerShell scripts
    r"\.js\b",                                               # Detect JavaScript files
    r"\.vbs\b",                                              # Detect VBScript files
    r"\.scr\b",                                              # Detect screen saver files
    r"\.wsf\b",                                              # Detect Windows Script Files
    r"\.msi\b",                                              # Detect Windows Installer packages
    r"\.log\b",                                              # Detect log files


    # Add more file extensions here
]

