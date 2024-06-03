import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
    
        if str1 + str2 != str2 + str1:
            return ans
        else:
            gdcVal = math.gcd(len(str1), len(str2))
            ans += str2[:gdcVal]
        return ans

