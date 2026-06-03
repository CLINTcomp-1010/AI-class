try:
    with open("samplefile.txt", "r") as fh:
        content = fh.read()
        sp = content.split()
        num = len(sp)
        print("number of words:",num)
        sp2 = content.split("\n")
        num2 = len(sp2)
        print("number of lines:",num2)

except FileNotFoundError:
    print("file not found!")
except PermissionError:
    print("You do not access to such file")
except OSError:
    print("This file may be currupted")
except IsADirectoryError:
    print("This file is a Directory")
except:
    print("ERROR! consult your programmer :)")