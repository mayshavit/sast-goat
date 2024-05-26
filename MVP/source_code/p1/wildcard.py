import os

os.system("tar -czf archive.tar.gz *") # violates CKV3_SAST_2 - option 1

os.popen("tar -czf archive.tar.gz *")  # violates CKV3_SAST_2 - option 2

os.popen3("tar -czf archive.tar.gz *") # violates CKV3_SAST_2 - option 3
