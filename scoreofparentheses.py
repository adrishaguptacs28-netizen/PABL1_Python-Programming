class Solution:
    def scoreOfParentheses(self, s):
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    score += 1 << depth   # same as 2^depth
        
        return score


# Driver code
if __name__ == "__main__":
    s = "()()"
    obj = Solution()
    print(obj.scoreOfParentheses(s))
