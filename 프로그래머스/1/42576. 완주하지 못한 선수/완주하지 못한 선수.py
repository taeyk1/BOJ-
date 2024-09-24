def solution(participant, completion):
    dict = {i:0 for i in set(participant)}
    for i in participant:
        dict[i]+=1
    for i in completion:
        dict[i]-=1
    
    return sorted(dict.items(), key=lambda x : x[1], reverse=True)[0][0]
