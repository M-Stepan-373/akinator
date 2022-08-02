def question(text: str) -> bool:
    if input(text + "?") == "да":
        return True
    else:
        return False


def guessing(answer: str) -> (bool, str, str):
    if input(answer + "?") == "да":
        return True, None, None
    else:
        return False, input("Что ты загадал?"), input("Чем " + answer + " отличается от вашего ответа?")
