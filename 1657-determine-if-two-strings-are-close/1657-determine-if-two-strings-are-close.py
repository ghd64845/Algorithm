from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        
        sorted_dict1 = sorted(dict1.values())
        sorted_dict2 = sorted(dict2.values())
        
        
        keys_match = set(dict1.keys()) == set(dict2.keys())
        
        return sorted_dict1 == sorted_dict2 and keys_match