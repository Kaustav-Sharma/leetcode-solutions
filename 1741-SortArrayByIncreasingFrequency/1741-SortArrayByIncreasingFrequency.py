# Last updated: 22/10/2026, 6:46:47 pm
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        a = {}
        for i in nums:
            a[i] = a.get(i, 0) + 1
        return sorted(nums, key=lambda x: (a[x], -x))