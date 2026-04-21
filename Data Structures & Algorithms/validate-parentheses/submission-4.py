class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')' : '(', '}': '{', ']' : '['}
        for c in s:
            # print(stack)
            # stack.append(c)
            # # if c in pairs:
            # # else:
            # if len(stack)>0 and stack[-1] in pairs and pairs[stack[-1]] == c:
            #     stack.pop() 
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                        return False 
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()

        return True if len(stack) == 0 else False
