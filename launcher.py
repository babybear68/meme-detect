import sys
from download import download
from upload import upload
from detect import detect

def main():
    operations = {"download": download, "upload": upload, "detect": detect}
    operations[sys.argv[1]](*sys.argv[2:])

if __name__ == "__main__":
    main()
