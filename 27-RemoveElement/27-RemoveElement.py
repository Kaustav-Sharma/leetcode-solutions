# Last updated: 22/10/2026, 4:43:56 pm
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)