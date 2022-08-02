def question(text: str) -> bool:
    if input(text + "?\n") == "да":
        return True
    else:
        return False


def guessing(answer: str) -> (bool, str, str):
    if input(answer + "?\n") == "да":
        return True, None, None
    else:
        return False, input("Что ты загадал?\n"), input("Чем " + answer + " отличается от вашего ответа?\n")
