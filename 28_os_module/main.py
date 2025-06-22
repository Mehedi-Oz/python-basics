import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 10):
    os.mkdir(f"data/Number{i+1}")

    if i == 5:
        os.mkdir(f"data/Number5/readme.md")
