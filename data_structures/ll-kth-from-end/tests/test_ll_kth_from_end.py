import pytest

from linked_list import Node, LinkedList

linked_list = LinkedList()
values = ['a', 'b', 'c', 'd','e']

for el in values:
    linked_list.insert(el)

def test_list_nodes_order():
    assert "e, d, c, b, a" == linked_list.__str__()

def test_list_1_elem():
    linked_list = LinkedList()
    linked_list.insert('z')
    assert linked_list.kth_from_end(0) == 'z'
    assert linked_list.kth_from_end(-1) == 'z'
    with pytest.raises(Exception):  # Pass in the expected error
        linked_list.kth_from_end(2)
