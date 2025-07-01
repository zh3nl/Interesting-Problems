# 9. Palindrome Number (Easy)

## Intuition
To solve this proble, we can take advantage of the modulo operator to build the reverse of the input. Since we are building the number in reverse, we would have to multiply the current reverse
number by 10 before adding the remainder (since the digit we add from each iteration must be in the ones place). Then, compare the reverse with the original and return the boolean accordingly. 

## Algorithm
* While x is greater than 0, multiply the current reverse by 10 and add the remainder of x
* Compare reverse and original 

## Asymtotic Analysis
* Time Complexity: O(log n)
* Space Complexity: O(1)
