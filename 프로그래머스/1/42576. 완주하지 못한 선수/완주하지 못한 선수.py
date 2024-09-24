def solution(participant, completion):
    dict = {i:0 for i in set(participant)}
    for i in participant:
        dict[i]+=1
    for i in completion:
        dict[i]-=1
    
    return sorted(dict, key=lambda x : dict[x], reverse=True)[0]
