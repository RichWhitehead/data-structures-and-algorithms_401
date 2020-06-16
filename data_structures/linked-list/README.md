# Implementation: Linked Lists
Linked List is a linear data structure. It is a series of connected "nodes" that contains the "address" of the next node. Each node can store a data point which may be a number, a string or any other type of data.

# Author: Richard Whitehead
# Code-Challenge
Create a Node classes and LinkedList class that will have a singly linked list properties like adding element to the beginning of the linked list, check for the existence of the element in the list and print all list elements as a string

# Approach & Efficiency
for the insert() function big O(1) because we can add new element only at the beginning of the list

for the includes() function big O(N) because I used a while loop to iterate over all linked list elements until element won't be found

for the str() it is also big O(N) because I also used a while loop in my solution to iterate over the list

# API
.insert() - takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
.includes() - takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
.str - takes in no arguments and returns a string representing all the values in the Linked List
# Credits and Sources
https://stackoverflow.com/questions/280243/python-linked-list
Shout out to Thomas Sherer who help me with this challenge.
