class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        result = []

        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= highest:
                result.append(True)
            else:
                result.append(False)
        
        return result
