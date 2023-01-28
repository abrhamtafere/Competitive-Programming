class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                tmp = ""
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack.pop()
                for j in tmp: stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)
