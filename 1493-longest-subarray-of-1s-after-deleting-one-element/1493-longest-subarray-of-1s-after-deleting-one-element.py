class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        l, r = 0, 0
        max_val = 0
        n = len(nums)
        count = 0
        
        while r < n:
            if nums[r] == 0:
                count += 1
            
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            max_val = max(max_val, r - l)
            r += 1
        
        return max_val