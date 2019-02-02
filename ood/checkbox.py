from __future__ import annotations
from typing import List
from pprint import pprint
from enum import Enum


class State(Enum):
    CHECKED = '+'
    UNCHECKED = ' '
    PARTIAL = '-'


class Checkbox:

    def __init__(self, label: str, state: State = State.UNCHECKED, parent: Checkbox = None):
        self.label = label
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child: Checkbox):
        self.children.append(child)
        child.parent = self

    def check(self):

        def fix_parents(current):
            if current is None:
                return
            else:
                current.state = State.CHECKED if all(
                    child.state == State.CHECKED for child in current.children) else State.PARTIAL
                fix_parents(current.parent)

        def fix_children(current):
            if current.children is None:
                return
            for child in current.children:
                if child.state != State.CHECKED:
                    child.state = State.CHECKED
                    fix_children(child)

        if self.state == State.CHECKED:
            return
        else:
            self.state = State.CHECKED
            fix_children(self)
            fix_parents(self.parent)

    def uncheck(self):

        def fix_parents(current):
            if current is None:
                return
            else:
                current.state = State.UNCHECKED if all(
                    child.state == State.UNCHECKED for child in current.children) else State.PARTIAL
                fix_parents(current.parent)

        def fix_children(current):
            if current.children is None:
                return
            for child in current.children:
                if child.state != State.UNCHECKED:
                    child.state = State.UNCHECKED
                    fix_children(child)

        if self.state == State.CHECKED:
            return
        else:
            self.state = State.CHECKED
            fix_children(self)
            fix_parents(self.parent)

    @classmethod
    def update_state(cls):
        for child in cls.children:
            if child.state in [State.PARTIAL, State.UNCHECKED]:
                return State.PARTIAL
        return State.CHECKED

    @staticmethod
    def render(item: Checkbox, to_string: List = [], indent='\t', depth=1):
        for child in item.children:
            to_string.append(f"{indent*depth}[{child.state.value}] {child.label}")
            item.render(child, to_string, depth=depth + 1)

    def __repr__(self):
        to_string = [f"[{self.state.value}] {self.label}"]

        Checkbox.render(self, to_string)

        return '\n'.join(to_string)


tasks = [
    Checkbox(label='Task A'),
    Checkbox(label='Task B'),
    Checkbox(label='Task C'),
]

tasks[0].add_child(Checkbox(label='A.1'))
tasks[0].add_child(Checkbox(label='A.2'))
tasks[0].add_child(Checkbox(label='A.3'))

tasks[1].add_child(Checkbox(label='B.1'))
tasks[1].add_child(Checkbox(label='B.2'))

tasks[2].add_child(Checkbox(label='C.2'))

tasks[0].children[0].add_child(Checkbox(label='A.1.1'))
tasks[0].children[0].add_child(Checkbox(label='A.1.2'))

tasks[1].children[0].add_child(Checkbox(label='B.1.1'))
tasks[1].children[0].add_child(Checkbox(label='B.1.2'))
tasks[1].children[0].add_child(Checkbox(label='B.1.3'))

tasks[0].children[0].children[0].check()
tasks[0].children[0].children[0].uncheck()

for task in tasks:
    pprint(task)

