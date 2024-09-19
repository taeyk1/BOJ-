def solution(s):
    s = s.split()
    stack = []
    for i in s:
        if i != 'Z':
            stack.append(int(i))
        else:
            stack.pop()
            
    return sum(stack)