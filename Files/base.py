from akinator.Files.tree import Node
from typing import List


def import_data(file: str, file_connect: str) -> List[Node]:
    nodes = []
    f = open(file, 'r')
    strings = f.readlines()
    f.close()
    f = open(file_connect, 'r')
    strings_connects = f.readlines()
    f.close()
    for i in range(0, len(strings) - 1, 2):
        if strings[i] == 'answer\n':
            nodes.append(Node(len(nodes), None, None, None, strings[i + 1][:-1]))
        else:
            nodes.append(Node(len(nodes), strings[i + 1][:-1], None, None, None))
    for i in range(len(nodes)):
        if nodes[i].answer is None:
            nodes[i].right = nodes[int(strings_connects[i + 1])]
            nodes[i].left = nodes[int(strings_connects[i])]
    return nodes


def export_data(file: str, file_connect: str, nodes: List[Node]):
    File = open(file, 'w')
    File_connect = open(file_connect, 'w')
    a, b = nodes[0].check_leaf()
    if a:
        File.write("question\n")
    else:
        File.write("answer\n")
    File.write(b + '\n')
    for i in nodes:
        a, b = i.check_leaf()
        if a:
            File_connect.write(str(i.left.number) + '\n')
            a, b = i.left.check_leaf()
            if a:
                File.write("question\n")
            else:
                File.write("answer\n")
            File.write(b + '\n')
            File_connect.write(str(i.right.number) + '\n')
            a, b = i.right.check_leaf()
            if a:
                File.write("question\n")
            else:
                File.write("answer\n")
            File.write(b + '\n')
        else:
            File_connect.write('0\n0\n')
    File_connect.close()
    File.close()
