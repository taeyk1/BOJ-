def solution(s):
    answer = True
    p_count, y_count = 0, 0
    for char in s.lower():
        if char == 'p':
            p_count+=1
        elif char == 'y':
            y_count+=1
    
    if p_count != y_count:
        answer = False
    
    return answer