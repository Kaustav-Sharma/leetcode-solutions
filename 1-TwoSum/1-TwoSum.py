# Last updated: 22/10/2026, 4:44:13 pm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i