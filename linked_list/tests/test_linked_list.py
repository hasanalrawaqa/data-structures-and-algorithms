import pytest
from linked_list.linked_list import LinkedList, Node

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
    
    #  Code Challenge 07 Testing:
    
def test_kth_from_end_greater_than_length():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)

    with pytest.raises(Exception):
        assert ll.kthFromEnd(6)

def test_kth_from_end_same_as_length():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)

    assert ll.kthFromEnd(4) == 1

def test_kth_from_end_not_positive_integer():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)

    with pytest.raises(ValueError):
        assert ll.kthFromEnd(-2)

def test_kth_from_end_size_1():
    ll = LinkedList()
    ll.head = Node(5)

    assert ll.kthFromEnd(0) == 5

def test_kth_from_end_happy_path():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)

    assert ll.kthFromEnd(2) == 3    

