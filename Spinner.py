import subprocess

Vertical = "|"
Horizontal = "—"
Slash = "/"
BackSlash = "\\"

TheStuff = (Vertical,Slash,Horizontal,BackSlash)

while True:
    for i in TheStuff:
        print(i)
        subprocess.call("clear")