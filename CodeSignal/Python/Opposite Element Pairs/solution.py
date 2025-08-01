# You are provided with an array of n integers, with n ranging from 1 to 100, inclusive. The task necessitates that you return an array of tuples, where each tuple comprises a pair of an element and its 'opposite' element.

def solution(numbers):
  result = []
  n = len(numbers)
  for i in range(n):
    result.append((numbers[i], numbers[n - i - 1]))
  return result
  
