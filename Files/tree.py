from typing import Optional

class Node:
    question: Optional[str]
    left: Optional["Node"]
    right: Optional["Node"]
    answer: Optional[str]

    def __init__(self, question: Optional[str], left: Optional["Node"], right: Optional['Node'], answer: Optional[str]):
        self.question = question
        self.left = left
        self.right = right
        self.answer = answer

    def transformation(self, question: str, new_answer: str, nodes: list):
        nodes.append([Node('', None, None, new_answer)])
        nodes.append([Node('', None, None, self.answer)])
        self.answer = ''
        self.question = question
        self.left = nodes[-1]
        self.right = nodes[-2]

    def definition(self):
        if self.answer is None:
            return True, self.question
        else:
            return False, self.answer
