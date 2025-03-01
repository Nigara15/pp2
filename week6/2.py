import os 
import string
#1
def lll(path):
    directories=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
    files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]

    print("Directories:", directories)
    print("Files:", files)
    print("All Items:", os.listdir(path))

path='.'
lll(path)

#2
def check(path):
    print("Exisits", os.path.exists(path))
    print("Readable", os.access(path, os.R_OK))
    print("Writable", os.access(path, os.W_OK))
    print("Executable", os.access(path, os.X_OK))

path="text.txt"
check(path)

#3
def pathh(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist")

path="text.txt"
pathh(path)

#4
def count(f):
    with open(f,'r') as file:
        return sum(1 for _ in file)
    
f='text.txt'
print(count(f))

#5
def w(f,items):
    with open(f,"w") as file:
        for item in items:
            file.write(f"{item}\n")

items=["Python", "C++","Java"]
w("text.txt",items)

#6
def generate():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt","w") as file:
            file.write(f"This is {letter}.txt\n")

generate()

#7
def copy(S,D):
    with open(S,"r") as src, open(D,"w") as dest:
        dest.write(src.read())

copy("source.txt","destination.txt")

#8
def deletee(f):
    if os.path.exists(f) and os.access(f,os.W_OK):
        os.remove(f)
        print(f"File{f} deleted successfully")
    else:
        print("File doe not exist or is  ot writeable")

deletee("text.txt")