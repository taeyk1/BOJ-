def solution(land):
    for row in range(1, len(land)):
        for current_col in range(4):
            before_value = land[row][current_col]
            for roatate_col in range(4):
                if current_col != roatate_col:
                    land[row][current_col] = max(land[row][current_col],before_value+land[row-1][roatate_col])
            
    answer = max(land[-1])
    return answer

        