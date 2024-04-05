import os

show_expected_result = False
show_hints = False

def file_info():
    total = 0
    folder = "deps"
    dirlist = os.listdir(folder)
    for f in dirlist:
        if os.path.isfile(os.path.join(folder, f)) and f.endswith(".txt"):
            fsize = os.path.getsize(os.path.join(folder, f))
            total += fsize
    return total
