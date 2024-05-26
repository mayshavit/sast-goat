import os

# Using os.execl()
os.execl("/bin/ls", "ls", "-l", "/path/to/directory")


os.execvp("ls", ["ls", "-l", "/path/to/directory"])
