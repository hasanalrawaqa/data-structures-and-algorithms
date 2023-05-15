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

#tests for insertion
def test_append():
    ll = LinkedList()
    ll.append(1)
    assert str(ll) == "1 -> NULL"

def test_append_multiple_nodes():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3 -> NULL"

def test_insert_before_middle_node():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert_before(2, 1.5)
    assert str(ll) == "1 -> 1.5 -> 2 -> 3 -> NULL"

def test_insert_before_first_node():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert_before(1, 0.5)
    assert str(ll) == "0.5 -> 1 -> 2 -> 3 -> NULL"

def test_insert_after_middle_node():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1.5)  
    ll.insert(1)
    ll.insert_after(1.5, 1.7)
    assert str(ll) == "1 -> 1.5 -> 1.7 -> 2 -> 3 -> NULL"

def test_insert_after_last_node():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert_after(3, 3.5)
    assert str(ll) == "1 -> 2 -> 3 -> 3.5 -> NULL"

