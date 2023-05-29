import pytest
from queue import Queue

def test_enqueue_single_value():
    queue = Queue()
    queue.enqueue(5)
    assert queue.peek() == 5

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
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.peek() == 2

def test_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1

def test_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    assert queue.is_empty() == False

def test_dequeue_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()

def test_peek_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()
