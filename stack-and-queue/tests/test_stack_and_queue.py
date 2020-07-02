from stack_and_queue.stack_and_queue import Node, Stack, Queue

import pytest


def test_Node_exist():
    assert Node
    
def test_Stack_exist():
    assert Stack
    
def test_queue_exist():
    assert Queue
    
def test_one_push_one_node():
    stack = Stack()
    expected = 'a'
    stack.push('a')
    actual = stack.top.value
    assert actual == expected
    
def test_one_push_two_node():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    expected = 'b'
    actual = stack.top.value
    assert actual == expected
    
def test_one_push_three_node():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    expected = 'c'
    actual = stack.top.value
    assert actual == expected

def test_pop_error():
    stack = Stack()
    with pytest.raises(AttributeError) as err:
        assert stack.pop()
    assert str(err.value) == 'The stack is empty'
    

    

