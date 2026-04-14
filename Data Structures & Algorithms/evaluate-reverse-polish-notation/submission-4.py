OPERATOR_MAPPING = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int (x / y)
}


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            
            if operator := OPERATOR_MAPPING.get(token, False):
                if len(stack) <= 1:
                    raise ValueError("applying operator to invalid stack size")
                num2 = stack.pop()
                num1 = stack.pop()
                
                stack.append(operator(num1, num2))
                
        ans = stack.pop()
        return ans