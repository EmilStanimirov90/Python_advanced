import os

files = {}
directory = '../'


def get_files(folder, level):
    if level < 0:
        return
    for el in os.listdir(folder):
        file = os.path.join(folder, el)
        if os.path.isfile(file):
            extension = el.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(el)
        else:
            get_files(file, level - 1)


# for el in os.listdir(directory):
#     file = os.path.join(directory, el)
#     if os.path.isfile(file):
#         ext = el.split('.')[-1]
#         if ext not in files:
#             files[ext] = []
#         files[ext].append(el)
#     else:
#         for element in os.listdir(file):
#             filename = os.path.join(file, el)
#             if os.path.isfile(filename):
#                 ext = element.split('.')[-1]
#                 if ext not in files:
#                     files[ext] = []
#                 files[ext].append(element)

get_files(directory, 1)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")
