from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing
from akinator.Files.base import import_data, export_data

print("Привет, " + input("Как тебя зовут?\n") + ". Я Акинатор, я хочу угадать твоих персонажей, отвечай на вопросы да или нет.")


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
    if input("Хотите ли вы выйти?\n") == "да":
        break
if input("Хотите ли вы сохранить?\n") == "да":
    export_data('trees/test tree connects.txt', 'trees/test tree.txt', nodes)
