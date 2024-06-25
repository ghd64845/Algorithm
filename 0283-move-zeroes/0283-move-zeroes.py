class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        n = len(nums)
        
        while start <= end and end < n:
            if nums[start] == 0 and nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end += 1
            elif nums[start] != 0:
                start += 1
                end += 1
            else:
                end += 1
            