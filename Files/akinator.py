class Akinator:
    def __init__(self, root: 'Node'):
        self.turn = root

    def Turn(self, answer: bool):
        """
        Это метод переводит turn на следущую вершину в завизимости от ответа пользователя

        answer - это ответ пользователя
        """
        if answer:
            self.turn = self.turn.right
        else:
            self.turn = self.turn.left
