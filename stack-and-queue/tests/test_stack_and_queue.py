from stack_and_queue.stack_and_queue import Node, Stack, Queue


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
    expected = 'b'
    stack.push('b')
    actual = stack.top.value
    assert actual == expected
    
def test_one_push_three_node():
    stack = Stack()
    expected = 'c'
    stack.push('c')
    actual = stack.top.value
    assert actual == expected
    

    

