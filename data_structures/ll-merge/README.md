# Function to merge two linked lists.  
# Author: Richard Whitehead
# Challenge

- Write a function called merge_lists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. 

- Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

Example Input ---> Output:
Input:

lis1: head -> [1] -> [3] ->[2]->x
list2: head -> [5] -> [9] ->[4]->x Output:
head -> [1] -> [5] -> [3] -> [9] -> [2]->[4] ->x
Input:

lis1: head -> [1] -> [3] ->x
list2: head -> [5] -> [9] ->[4]->x Output:
head -> [1] -> [5] -> [3] -> [9] ->[4] ->x
Input:

lis1: head -> [1] -> [3] ->[2] ->x
list2: head -> [5] -> [9] ->x Output:
head -> [1] -> [5] -> [3] -> [9] ->[2] ->x  

# Approach & Efficiency

merge_list(list1, list2) function space Big O(1), time Big O(n) 

# Solution  (White Board)

https://docs.google.com/document/d/1EmZ39Rl8jQD9wyzOuphappyDzh_9nnCI6J3g9ADIYDU/edit?usp=sharing

# Sources 

https://codereview.stackexchange.com/questions/113670/merge-two-linked-lists-in-python

https://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/

https://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/

https://www.educative.io/edpresso/how-to-merge-two-sorted-linked-lists-in-python