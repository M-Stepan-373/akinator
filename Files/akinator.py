class Akinator():
    def __init__(self, root: 'Node'):
        self.turn = root

    def first_turn(self) -> (str, bool):
        if self.turn.definition() is True:
            return self.turn.question, True
        else:
            return self.turn.answer, False

    def second_turn(self, answer: bool):
        if answer == True:
            self.turn = self.turn.right
        else:
            self.turn = self.turn.left
