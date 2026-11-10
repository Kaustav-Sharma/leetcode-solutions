# Last updated: 10/11/2026, 5:37:37 pm
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:]+nums[:n-k]