import os
import time

def Run():
    try:
        print("running Python script")
        os.system("py main.py")
        time.sleep(3)
        print("running javaScript code")
        os.system("node apiHandle.js")
    except ValueError as err:
        print(err)


# Run()

