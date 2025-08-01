# Task
You are given an input array consisting of n integers ranging from 0 to 100, inclusive, where n represents the length of the array. Your task is to return a new array of tuples. Each tuple should consist of an element from the input array paired with its geometrical mean with the 'opposite' element. The 'opposite' element of any element in the array is defined as the element at the corresponding position from the end of the array.

Assume that the geometrical mean of two numbers, a and b, is calculated as: sqrt(a×b), where sqrt stands for square root.

# Notes
* If the length of the array, n, is odd, the middle element is considered to be its own 'opposite'.
* The elements of the input array will be in the range from 0 to 100, inclusive.
* Calculate the geometrical mean to two decimal places. For example, the geometrical mean of 2 and 8 is 4.00 (since sqrt(2×8)=4).
* Round down to two decimal places. For instance, the geometrical mean of 2 and 8 is 4.00, not 4.472.
