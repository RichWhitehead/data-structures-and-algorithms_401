# FIFO Animal Shelter

# Author: Richard Whitehead

# Challenge
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.

# Implement the following methods:

enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return None.
Example Input ---> Output:
enqueue(value) Internal state before:
[cat2]->[dog1]->[cat1]
Input
"dog3", "dog" Internal state after:
[dog3]->[cat2]->[dog1]->[cat1]

# Approach & Efficiency
For the enqueue(animal) method time big O(1), space big O(1) For the dequeue(pref) method time big O(n), space big O(n)

# Sources 



# Solution