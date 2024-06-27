class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        max_cnt = 0
        n = len(nums)
        f_cnt = 0
        
        while r < n:     
            
            if nums[r] == 0:
                f_cnt += 1
            
            while f_cnt > k:
                if nums[l] == 0:
                    f_cnt -= 1
                l += 1
                
            max_cnt = max(max_cnt, r - l + 1)
            r += 1
            
        return max_cnt
    