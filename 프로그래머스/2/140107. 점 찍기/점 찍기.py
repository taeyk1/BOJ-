def solution(k, d):
    answer = 0
    a, b, r_2 = 0, 0, (d/k)**2
    
    while a**2 <= r_2:
        answer+= 1 + int((r_2 - a**2)**(1/2))
        a+=1

    return answer