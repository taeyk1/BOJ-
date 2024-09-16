def solution(record):
    current_list = {}
    result = []
    answer = []
    for row in record:
        record_list = row.split()
        if record_list[0] == 'Enter':
            current_list[record_list[1]] = record_list[2]
            result.append(' '.join(record_list[0:2]))
        elif record_list[0] == 'Leave':
            result.append(' '.join(record_list[0:2]))
        else:
            current_list[record_list[1]] = record_list[2]
                          
    for i in result:
        state, id = i.split()
        if state == 'Enter':
            answer.append(f"{current_list[id]}님이 들어왔습니다.")
        else:
            answer.append(f"{current_list[id]}님이 나갔습니다.")
            
    return answer