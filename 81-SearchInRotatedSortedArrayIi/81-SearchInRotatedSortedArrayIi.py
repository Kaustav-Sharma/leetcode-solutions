# Last updated: 11/11/2026, 7:19:44 pm
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return True
            return False

        while len(nums) > 2 and nums[0] == nums[-1]:
            if nums[0]==target:
                return True
            nums = nums[1:-1]
        a=min(nums)
        b=nums.index(a)
        if min(nums)!=nums[0]:
            if target>nums[-1]:
                nums=nums[:b]
                ans=binary_search(nums,target)
            else:
                nums=nums[b:]
                ans=binary_search(nums,target)
        else:
            ans=binary_search(nums,target)

        if ans:
            return True
        else:
            return False