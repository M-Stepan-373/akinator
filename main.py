from akinator.Files.akinator import Akinator
from akinator.Files.shell import question, guessing
from akinator.Files.base import import_data, export_data


print("Привет, Я Акинатор и я хочу угадать любой предмет или персонажа,")
print("которого ты загадаешь. Отвечай на вопросы да или нет.")
library = input("Введите название нужной вам базы данных:")

nodes = import_data("trees/" + library + "_base.txt", "trees/" + library + "_connects.txt")

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
    while True:
        action = input("0 - перезапустить\n1 - сбросить последний шаг и перезапустить\n2"
                       " - выйти без сохранения\n3 - выйти с сохранением\n")
        if action == '0':
            export_data("trees/" + library + "_base.txt", "trees/" + library + "_connects.txt", nodes)
            break
        if action == '1':
            nodes = import_data("trees/" + library + "_base.txt", "trees/" + library + "_connects.txt")
            break
        if action == '2':
            break
        if action == '3':
            export_data("trees/" + library + "_base.txt", "trees/" + library + "_connects.txt", nodes)
            break

    # Это условие нужно чтобы выйти из основного цикла
    if action == '2' or action == '3':
        break
