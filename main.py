import os


def clean(path):
    print("before clean:",'=='*20)
    os.system("sudo du -sh " + path)
    os.system("sudo rm -rf " + path)
    print("after clean:")
    os.system("sudo du -sh " + path)


if __name__ == "__main__":
    paths = ["/System/Library/Speech/Voices/", "/private/var/log/",
             "/private/var/folders/", "/private/var/tmp/TM*", "~/Library/Caches/"]
    for path in paths:
        clean(path)
