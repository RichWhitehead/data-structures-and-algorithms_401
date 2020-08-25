# How Insertion Sort Works

1. The first step involves the comparison of the element in question with its adjacent element.
2. If at every comparison reveals that the element in question can be inserted at a particular position, then space is created for it by shifting the other elements one position to the right and inserting the element at the suitable position.
3. This procedure is repeated until all elements in the array is at their correct position.

Consider the following array: `8,4,23,42,16,15`

1st Pass: Compare 8 with 4, this comparison shows that 8 > 4. The array will swap in this order: `4,8,23,42,16,15`

2nd Pass: Start with the second element which is 8 an it's already swapped so we will move to the next element. 

The third element is 23 and we will compare it with 8. Since 23 > 8 no swapping is needed.

2nd Pass: This looks like: `4,8,23,42,16,15`

3rd Pass: Now we start the 3rd pass which is 42.

Now 42 > 16 and 42 > 15. Since 15 is the lowest array we now swap 42 with 15.

The element will change to reflect `4,8,15,16,42,23`

4th Pass: We move on to the next array which is 16.

Now 16 < 42 so, no swapping is needed and the element will remain the same.

5th Pass: We now look at the next array which is 42. 42 > 23 so we swap the two and the final element will be `4,8,15,16,23,42`.

Finally we will check the last array of the element which is 42. The array is now sorted.



