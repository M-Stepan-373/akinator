def question(text: str) -> bool:
    if is_yes(text + "?"):
        return True
    else:
        return False


def guessing(answer: str) -> (bool, str, str):
    if is_yes(answer + "?") == True:
        return True, None, None
    else:
        old_answer = input("Кого/что ты загадал?\n")
        return False, old_answer, input("Что верно про " + old_answer + ", но неверно про " + answer + "?\n")


def is_yes(text):
    while True:
        answer = input(text + "\n").lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Пожалуйста, отвечайте только да или нет на данный вопрос.")

