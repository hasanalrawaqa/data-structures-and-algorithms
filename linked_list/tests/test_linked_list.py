import pytest
from linked_list.linked_list import LinkedList

def test_empty_list():
    ll = LinkedList()
    assert ll.head is None

def test_insert_one_node():
    ll = LinkedList()
    ll.insert(1)
    assert ll.head.value == 1

def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 3
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 1

def test_includes():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True
    assert ll.includes(4) == False

