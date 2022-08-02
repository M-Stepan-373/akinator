from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing
from akinator.Files.base import import_data


nodes = import_data('trees/test tree.txt', 'trees/test tree connects.txt')
print(nodes)
while True:
    akinator = Akinator(nodes[0])
    while True:
        node_type, text = akinator.turn.definition()
        if node_type:
            a = question(text)
            akinator.Turn(a)
        else:
            yes, new_answer, new_question = guessing(text)
            if not yes:
                akinator.turn.transformation(new_question, new_answer, nodes)
            break
