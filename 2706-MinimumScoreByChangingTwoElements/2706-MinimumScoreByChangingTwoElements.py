# Last updated: 19/11/2026, 10:06:33 am
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return min((nums[-2]-nums[1]),(nums[-1]-nums[2]),(nums[-3]-nums[0]))
    