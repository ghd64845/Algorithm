class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiou"
        chars = list(s)
        start_idx = 0
        end_idx = len(chars) - 1
        
        
        while start_idx < end_idx:
            if chars[start_idx].lower() not in vowel:
                start_idx += 1
            elif chars[end_idx].lower() not in vowel:
                end_idx -= 1
            else:
                tmp = chars[start_idx]
                chars[start_idx] = chars[end_idx]
                chars[end_idx] = tmp
                start_idx += 1
                end_idx -= 1
        
        return "".join(chars)