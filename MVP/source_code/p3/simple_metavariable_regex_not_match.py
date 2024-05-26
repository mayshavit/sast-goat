import os

def shutdown():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /s /t 0')
    elif os.name == 'posix':  # For Linux and macOS
        os.system('sudo shutdown now hopa')
    else:
        print("Unsupported operating system.")

shutdown()
