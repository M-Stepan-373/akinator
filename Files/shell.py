def question(question: str) -> bool:
    if input(question + "?") == "да":
        return True
    else:
        return False

def guessing(answer: str) -> (bool, str, str):
    if input(answer + "?") == "да":
        return True, None, None
    else:
        return False, input("Что ты загадал?"), input("Что отличает это от " + answer + "?")
