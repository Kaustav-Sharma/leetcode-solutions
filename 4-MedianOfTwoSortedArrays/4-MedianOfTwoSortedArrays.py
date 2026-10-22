# Last updated: 22/10/2026, 4:44:07 pm
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        total = len(merged)
        if total % 2 != 0:
            return float(merged[total // 2])
        else:
            mid_right = total // 2
            mid_left = mid_right - 1
            return (merged[mid_left] + merged[mid_right]) / 2.0