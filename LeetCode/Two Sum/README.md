# 1. Two Sum  (Easy)

## Initial intuition
In order to return the indices of the elements that sum up to our target, I should iterate through the array once and keep track of the index of 1 of the 2 numbers that will make up the pair we return. This can be done using a hashmap, which will store the index of the complement of the elements we iterate through. If a complement already exist in the hashmap, we have found our solution. 

## Algorithm Overview
* Declare a hashmap
* Iterate through nums using a for loop
* For each element, check if the complement of the element exists in our hashmap. If so, return the element and its complement as a list. If not, add the current element as the key and its index as the value in the hashmap.

## Runtime Analysis
* Time Complexity: O(n)
* Space Complexity: O(n)
