import os

folders = os.listdir("data")
print(folders)

print(os.getcwd())
os.chdir("data")
print(os.getcwd())

for folder in folders:
    print(folder, os.listdir(f"data/{folder}"))
