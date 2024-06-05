class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        
        tmp = 1
        for i in range(length):
            ans.append(tmp)
            tmp *= nums[i]
        
        tmp = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= tmp
            tmp *= nums[i]
        
        return ans