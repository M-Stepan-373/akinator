def import_data(file: str):
    f = open('text tree.txt', 'r')
    "nodes = file.readlines()"
    print(f.readlines())
    f.close()


def export_data(file: str, file_2:str, nodes):
    f_1 = open(file, 'w')
    f_2 = open(file_2, 'w')
    for i in nodes:
        a, b = i.definition()
        if a:
            f_1.write("question\n")
        else:
            f_1.write("answer\n")
        f_1.write(b + '\n')
    f_1.close()
    for i in nodes:
        a, b = i.definition()
        if a:
            f_2.write(str(i.right.number) + '\n')
            f_2.write(str(i.left.number) + '\n')
        else:
            f_2.write('0' + '\n' + '0' + '\n')
    f_2.close()
