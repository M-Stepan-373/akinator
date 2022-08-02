def question(text: str) -> bool:
    if is_yes(text + "?"):
        return True
    else:
        return False

def guessing(answer: str) -> (bool, str, str):
    if is_yes(answer + "?") == "да":
        return True, None, None
    else:
        return False, input("Что ты загадал?\n"), input("Чем " + answer + " отличается от вашего ответа?\n")

def is_yes(text):
    answer = ""
    while True:
        answer = input(text + "\n").lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Пожалуйста, говорите да или нет.")
