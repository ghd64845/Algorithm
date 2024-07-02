class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        ans = ''
        
        for char in s:
            print(stack)
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_num, ans))
                ans = ''
                curr_num = 0
            elif char == ']':
                num, prev_char = stack.pop()
                ans = prev_char + num * ans
            else:
                ans += char
        
        return ans