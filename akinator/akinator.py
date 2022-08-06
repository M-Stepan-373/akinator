from .tree import Node


class Akinator:
    def __init__(self, root: 'Node'):
        self.turn = root

    def go_node(self, answer: bool):
        """
        Это метод переводит turn на следущую вершину дерева в завизимости от ответа пользователя

        answer - это ответ пользователя(если да, то вправо, иначе влево)
        """
        if answer:
            self.turn = self.turn.right
        else:
            self.turn = self.turn.left
