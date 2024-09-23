def solution(land):
    for row in range(1, len(land)):
        for current_col in range(4):
            land[row][current_col] = land[row][current_col] + max(land[row-1][:current_col] + land[row-1][current_col+1:])
    return max(land[-1])

        