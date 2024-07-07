from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        
        for num in arr:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        l = {}
        for key, value in dict.items():
            if value in l:
                return False
            l[value] = 1
            
        
        return True