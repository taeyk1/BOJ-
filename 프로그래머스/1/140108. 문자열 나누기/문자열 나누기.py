def solution(s):
    x_count, not_x_count, answer = 0, 0, 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            x_count+=1
        else: 
            not_x_count+=1
        if x_count == not_x_count:
            answer+=1
            if i != len(s)-1:
                x = s[i+1]
                x_count, not_x_count = 0, 0
        elif x_count != not_x_count and i == len(s)-1:
            answer+=1
    return answer