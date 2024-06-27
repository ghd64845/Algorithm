class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        A = [0] 
        tmp = 0
        for i in gain:
            tmp += i
            A.append(tmp)
            
        return max(A)
        
        