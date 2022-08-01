from akinator.Files.tree import Node
from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing

nodes = [Node(None, None, None, "Кот")]
nodes[0].transformation("Оно лает", "Собака", nodes)

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
