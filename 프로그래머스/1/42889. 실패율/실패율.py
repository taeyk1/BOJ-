def solution(N, stages):
    stages.sort()
    result = { i:0 for i in range(1, N+1)}
    total = len(stages)
    
    for i in stages:
        if i < N+1:
            result[i]+=1
            
    for i in result.keys():
        temp = result[i]
        result[i] = result[i]/total
        total-=temp
        if total == 0:
            break
        
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(result)
    answer = [i[0] for i in result]
    
    return answer