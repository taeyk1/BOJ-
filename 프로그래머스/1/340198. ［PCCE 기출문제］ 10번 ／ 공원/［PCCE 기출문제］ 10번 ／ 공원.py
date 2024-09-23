def solution(mats, park):
    result = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == '-1':
                result = max(result, search(park, i, j))
    answer = []
    if not result in mats:
        for i in mats:
            if i <= result:
                answer.append(i)
        if len(answer) == 0:
            return -1
        return max(answer)
    else:
        return result

def search(park, row, col):
    max_row, max_col = 0, 0
    for i in range(row, len(park)):
        if park[i][col] == '-1':
            max_row+=1
        else:
            break
    for i in range(col, len(park[0])):
        if park[row][i] == '-1':
            max_col+=1
        else:
            break
    
    search_result = min(max_row, max_col)
    for i in range(row, row+search_result):
        for j in range(col, col+search_result):
            if not park[i][j] == '-1':
                return 0
    return search_result