from typing import Optional


class Node:
    """
    Класс Node описывает объект содержащий информацию о вопросах и ответах(база данных из этих объектов и состоит)

    question это вопрос (в случае если объект Node содержит информацию о ответе, остаётся пустым)

    left и right содержат информацию об ответах на вопрос(left - нет, right - да)
    (в случае если объект Node содержит информацию о ответе, остаётся пустым
    иначе содержит информацию о ссылках на ответы или вопросы следуючие за вопросами)

    answer это ответ (в случае если объект Node содержит информацию о вопросе, остаётся пустым)
    """
    question: Optional[str]
    left: Optional["Node"]
    right: Optional["Node"]
    answer: Optional[str]
    number: Optional[int]

    def __init__(self, number: Optional[int], question: Optional[str], left: Optional["Node"],
                 right: Optional['Node'], answer: Optional[str]):
        self.number = number
        self.question = question
        self.left = left
        self.right = right
        self.answer = answer

    def transformation(self, question: str, new_answer: str, nodes: list):
        """
        Если Акинатор угадал неправильно,
        записывает в массив базы данных новый вопрос и ответ на него.

        question это новый вопрос от пользователя

        new_answer это новый персонаж(ответ ДА на вопрос параметра question)

        nodes это база данных всех вопросов и ответов
        """
        nodes.append(Node(len(nodes), '', None, None, new_answer))
        nodes.append(Node(len(nodes), '', None, None, self.answer))
        self.answer = None
        self.question = question
        self.left = nodes[-1]
        self.right = nodes[-2]

    def check_leaf(self):
        """
        check_leaf проверяет является ли объект класса Node вопросом или конечным ответом
        """
        if self.answer is None:
            return True, self.question
        else:
            return False, self.answer
