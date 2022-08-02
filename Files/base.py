from akinator.Files.tree import Node


def import_data(file: str, file_connect: str):
    nodes = []
    f = open(file, 'r', encoding='utf-8')
    strings = f.readlines()
    f.close()
    f = open(file_connect, 'r')
    strings_connects = f.readlines()
    f.close()
    for i in range(0, len(strings)-1, 2):
        if strings[i] == 'answer':
            nodes.append(Node(len(nodes), None, None, None, strings[i+1]))
        else:
            nodes.append(Node(len(nodes), strings[i+1], None, None, None))
    for i in range(len(nodes)):
        if nodes[i].answer is None:
            nodes[i].left = nodes[int(strings_connects[i+1])]
            nodes[i].right = nodes[int(strings_connects[i])]
    return nodes




def export_data(file: str):

    pass