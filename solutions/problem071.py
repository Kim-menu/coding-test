def solution(table, languages, preference):
    JOB_DICT = dict()
    for job in table:
        temp_list = job.split()
        job_name = temp_list[0]
        JOB_DICT[job_name] = dict()
        for i in range(1, 6):
            JOB_DICT[job_name][temp_list[i]] = 6-i
    total_list = []
    for job_name in JOB_DICT.keys():
        result = 0
        for i in range(len(languages)):
            if languages[i] in JOB_DICT[job_name].keys():
                result += JOB_DICT[job_name][languages[i]]*preference[i]
        total_list.append((result, job_name))
    total_list.sort(key = lambda x : x[1])
    total_list.sort(key = lambda x : -x[0])
    answer = total_list[0][1]
    return answer