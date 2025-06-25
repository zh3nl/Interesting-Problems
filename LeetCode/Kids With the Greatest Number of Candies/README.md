# 1431: Kids With the Greatest Number of Candies (Easy)

## Intuition
To find whether the kid given the extra candies will have the greatest number of candies among the group, you must first find the highest number of candies a kid has without the extra candies.
Then, for each kid in the array, determine if the candies they already, plus the extra candies, will be greater than or equal to the highest number of candies we found (without extras). 

## Algorithm
1. Find the max value of the candies array
2. Iterate through the array, and determine if candies[i] + extraCandies >= max value
   - If greater than or equal to, set the corresponding index on the result array to be True
   - If not, set the index to false
4. return the result array

## Asymtotic Analysis
Time Complexity: O(n)
Space Complexity: O(n)
