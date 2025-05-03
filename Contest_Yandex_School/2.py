def evaluate(s: str) -> int:
    s = s.replace(' ', '')
    stack = []
    result = 0
    op = '+'
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] in '+-':
            op = s[i]
            i += 1
        else:
            # Parse sign
            sign = 1
            j = i
            while j < n and s[j] in '+-':
                if s[j] == '-':
                    sign *= -1
                j += 1
            i = j
            
            # Parse term: number or '('
            if i < n and s[i] == '(':
                stack.append((result, op))
                result = 0
                op = '+'
                i += 1
            else:
                # Parse number
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num *= sign
                
                # Apply current operator
                if op == '+':
                    result += num
                else:
                    result -= num
        
        # Check for closing parenthesis
        while i < n and s[i] == ')':
            prev_res, prev_op = stack.pop()
            if prev_op == '+':
                prev_res += result
            else:
                prev_res -= result
            result = prev_res
            i += 1
    
    return result