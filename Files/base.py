from akinator.Files.tree import Node


def import_data(file: str, file_connect: str):
    nodes = []
    f = open(file, 'r')
    strings = f.readlines()
    f.close()
    f = open(file_connect, 'r')
    strings_connects = f.readlines()
    f.close()
    for i in range(0, len(strings)-1, 2):
        if strings[i] == 'answer\n':
            nodes.append(Node(len(nodes), None, None, None, strings[i+1][0:-1]))
        else:
            nodes.append(Node(len(nodes), strings[i+1][0:-1], None, None, None))
    for i in range(len(nodes)):
        if nodes[i].answer is None:
            nodes[i].left = nodes[int(strings_connects[i+1])]
            nodes[i].right = nodes[int(strings_connects[i])]
    return nodes


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
            f_2.write('0\n0\n')
    f_2.close()
