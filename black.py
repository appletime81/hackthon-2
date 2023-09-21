import os


all_py_files = list()
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        if name.endswith(".py"):
            all_py_files.append(os.path.join(root, name))

for py_file in all_py_files:
    os.system(f"black '{py_file}'")
