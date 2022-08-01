class Akinator():
    def __init__(self, root: 'Node'):
        self.turn = root

    """
    Это метод переводит turn на следущую вершину в завизимости от ответа пользователя
    
    answer - это ответ пользователя
    """
    def Turn(self, answer: bool):
        if answer:
            self.turn = self.turn.right
        else:
            self.turn = self.turn.left
