# Матрешка из архивов, в каждом внутри запароленый архив и README.txt с ключом в base64
# unrar - консольный winrar
import base64
import os

os.chdir("archive")
while True:
    password = ""
    files = os.listdir(os.curdir)
    files.remove("README.txt")
    file = files[0]
    with open("README.txt") as f:
        s = f.readline()
        print(s)
        password = base64.b64decode(s).decode()
        print(password)
    os.remove("README.txt")
    print(os.popen(f"unrar l -p\"{password}\" {file}").read()) # список файлов
    print(os.popen(f"unrar x -p\"{password}\" {file}").read()) # распаковка
    os.remove(f"{file}")
