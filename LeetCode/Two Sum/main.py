class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap:
                return [i, hashmap[pair]]
            else:
                hashmap[nums[i]] = i

        return []
        
