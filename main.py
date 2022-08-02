from akinator.Files.tree import Node
from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing
from akinator.Files.base import import_data, export_data

nodes = [Node(0, '', None, None, "Кот")]
nodes[0].transformation("Оно лает", "Собака", nodes)
print("Привет, " + input("Как тебя зовут?\n") + ". Я Акинатор, я хочу угадать твоих персонажей, отвечай на вопросы да или нет.")


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
    if input("Хотите ли вы выйти?\n") == "да":
        break
if input("Хотите ли вы сохранить?\n") == "да":
    export_data('trees/test tree connects.txt', 'trees/test tree.txt', nodes)
