# Last updated: 11/11/2026, 7:01:17 pm
class Solution:
    def search(self, nums: list[int], target: int) -> int:
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
                    return mid
            return -1

        a=min(nums)
        b=nums.index(a)
        if min(nums)!=nums[0]:
            if target>nums[-1]:
                nums=nums[:b]
                ans=binary_search(nums,target)
            else:
                nums=nums[b:]
                ans=binary_search(nums,target)
                if ans!=-1:
                    ans+=b
        else:
            ans=binary_search(nums,target)
            
        return ans