from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing, is_yes
from akinator.Files.base import import_data, export_data

print("Привет, " + input("Как тебя зовут?\n") +
      ". Я Акинатор, я хочу угадать твоих персонажей, отвечай на вопросы да или нет.")

nodes = import_data('trees/test tree.txt', 'trees/test tree connects.txt')
while True:
    akinator = Akinator(nodes[0])
    while True:
        node_type, text = akinator.turn.check_leaf()
        if node_type:
            a = question(text)
            akinator.go_node(a)
        else:
            yes, new_answer, new_question = guessing(text)
            if not yes:
                akinator.turn.transformation(new_question, new_answer, nodes)
            break
    if is_yes("Хотите ли вы выйти?"):
        break
if is_yes("Хотите ли вы сохранить?"):
    export_data('trees/test tree.txt', 'trees/test tree connects.txt', nodes)
