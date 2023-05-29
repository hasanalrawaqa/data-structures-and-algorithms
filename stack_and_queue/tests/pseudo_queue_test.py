import pytest
from pseudo_queue import PseudoQueue

def test_enqueue_single_value():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.dequeue() == 5

def test_enqueue_multiple_values():
    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 15
    assert queue.dequeue() == 20

def test_enqueue_and_dequeue():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.dequeue() == 5
    assert queue.dequeue() == 10
    queue.enqueue(20)
    assert queue.dequeue() == 15
    assert queue.dequeue() == 20

def test_dequeue_empty_queue():
    queue = PseudoQueue()
    with pytest.raises(Exception):
        queue.dequeue()

def test_enqueue_and_dequeue_alternate():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.dequeue() == 5
    queue.enqueue(10)
    assert queue.dequeue() == 10
    queue.enqueue(15)
    assert queue.dequeue() == 15

def test_enqueue_empty_value():
    queue = PseudoQueue()
    queue.enqueue('')
    assert queue.dequeue() == ''
