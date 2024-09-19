def solution(survey, choices):
    table_1, table_2, table_3, table_4 = {'R':0,'T':0}, {'C':0,'F':0}, {'J':0,'M':0}, {'A':0,'N':0}
    for i in range(0, len(survey)):
        if 'R' in survey[i] or 'T' in survey[i]:
            choice(survey, choices, i, table_1)
        if 'C' in survey[i] or 'F' in survey[i]:
            choice(survey, choices, i, table_2)
        if 'J' in survey[i] or 'M' in survey[i]:
            choice(survey, choices, i, table_3)
        if 'A' in survey[i] or 'N' in survey[i]:
            choice(survey, choices, i, table_4)
            
    list = [table_1, table_2, table_3, table_4]
    answer = []
    for table in list:
        keys = [i for i in table.keys()]
        vals = [i for i in table.values()]
        if vals[0] >= vals[1]:
            answer.append(keys[0])
        else:
            answer.append(keys[1])
        
    return ''.join(answer)

def choice(survey, choices, i, table):
    if choices[i] <= 3:
         table[survey[i][0]] += (4 - choices[i])
    elif choices[i] >= 5:
         table[survey[i][1]] += (choices[i] - 4)
            