class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        cnt = 0
        
        for num in nums:
            if (num in m) and m[num] > 0:
                m[num] -= 1
                cnt += 1
            else:
                if k - num in m:
                    m[k - num] += 1
                else:
                    m[k - num] = 1
        return cnt
    
    