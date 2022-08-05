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
    for i in range(0, len(strings_connects) - 1, 2):
        if strings[i] == 'answer\n':
            nodes.append(Node(len(nodes), None, None, None, strings[i+1][:-1]))
        else:
            nodes.append(Node(len(nodes), strings[i+1][:-1], None, None, None))
    for i in range(len(nodes)):
        if nodes[i].answer is None:
            nodes[i].left = nodes[int(strings_connects[2 * i])]
            nodes[i].right = nodes[int(strings_connects[2 * i + 1])]
    return nodes


def export_data(file: str, file_connect: str, nodes: List[Node]):
    File = open(file, 'w')
    File_connect = open(file_connect, 'w')
    for i in range(len(nodes)):
        if nodes[i].left is None:
            File.write("answer\n")
            File.write(nodes[i].answer + '\n')
            File_connect.write('0' + '\n')
            File_connect.write('0' + '\n')
        else:
            File.write("question\n")
            File.write(nodes[i].question + '\n')
            File_connect.write(str(nodes[i].left.number) + '\n')
            File_connect.write(str(nodes[i].right.number) + '\n')
    File_connect.close()
    File.close()
