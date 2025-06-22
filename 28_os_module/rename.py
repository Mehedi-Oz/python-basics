import os

for i in range(0, 10):
    os.rename(f"data/{i+1} folder", f"data/{i+1}-folder")
