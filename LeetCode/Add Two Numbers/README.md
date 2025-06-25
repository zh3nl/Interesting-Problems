# 2. Add Two Numbers (Medium)

## Intuition
My basic intuition for this problem is that we have to iterate through each pair of node from l1 and l2 and sum them together. When summing two nodes, we must consider the following cases:
1. Adding two numbers results in a number greater than 9, which means that we have to carry over. Note that carry can only be 0 or 1, since the largest sum between the carry and the two numbers is 19. 
2. The length of one linked list is greater than the other. Looking at the provided test cases, we should set the linked list that was depleted to 0 and continue our iteration.
3. One of the linked list is an empty linked list. This can be solved using conditional checks that are already in our algorithm.

## Algorithm: 
1. Create the linked list for our result.
2. The carry should be initialized to 0.
3. Iterate through each node of l1 and l2
   - Set x to the value of l1's current node or 0 if l1 is depleted.
   - Set y to the value of l2's current nodeor 0 if l2 is depleted.
   - Sum x, y, and carry
   - Divide carry by 10 to determine what we need to carry over.
   - Create a new node with the current digit sum value using modulo and set it to curr.next. Advance curr to curr.next
   - Advance l1 and l2 if they are not null. 
5. Return result.next (since the first node of result is a dummy head).

## Runtime Analysis
Time Complexity: O(max(m, n)), where m is the length of l1 and n is the length of l2. 
Space Complexity: O(1). 
