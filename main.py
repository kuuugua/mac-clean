import os

print(os.getcwd())
print(os.system("ls -lh"))

os.system("sudo rm -f  /System/Library/Speech/Voices/*")
os.system("sudo rm -rf /private/var/log/*")
os.system("sudo rm -rf /private/var/folders/")
os.system("rm -rf /private/var/tmp/TM*")
os.system("rm -rf  ~/Library/Caches/*")