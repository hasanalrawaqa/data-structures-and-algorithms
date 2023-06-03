import pytest
from queue import Queue

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_enqueue_multiple_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.peek() == 2

def test_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() is True

def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()

def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()
