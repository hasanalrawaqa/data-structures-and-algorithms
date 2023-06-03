import pytest
from stack import Stack

def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_push_multiple_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1

def test_empty_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty() is True

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()
