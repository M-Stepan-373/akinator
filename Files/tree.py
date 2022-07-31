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

    def transformation(self, question: str, new_ansqwer: str):
        pass
