def solution(id_list, report, k):
    report_list = {}
    num_reported = {}
    num_mail = {}
    answer = []
    for user_id in id_list:
        report_list[user_id] = []
        num_reported[user_id] = 0
        num_mail[user_id] = 0
    
    for i in report:
        user_id, reported_user_id = i.split()
        if not user_id in report_list[reported_user_id]:
            report_list[reported_user_id].append(user_id)
    
    for reported_user_id, user_id_list in report_list.items():
        num_reported[reported_user_id] = len(user_id_list)
    
    for reported_user_id, num_r in num_reported.items():
        if num_r >= k:
            for user_id in report_list[reported_user_id]:
                num_mail[user_id] += 1
                
    for i in num_mail.values():
        answer.append(i)

    return answer