# id_list에는 사용자들의 아이디가 입력되게 해야 함
# report에는 muzi가 frodo를 신고했다면 "muzi frodo" 이런식으로 입력되게 해야 함
def solution(id_list, report, k):
    num = dict()
    warn = []
    answer = []
    for i in id_list:
        num[i]=0
    for j in set(report):
        num[id_list[id_list.index(j.split(" ")[1])]]=num[id_list[id_list.index(j.split(" ")[1])]]+1
    for h in id_list:
        if num[h] >= k: 
          warn.append(h)
    
    call = dict()
    call1 = dict()
    for i in id_list:
      call[i] = []
    for j in report:
      call[j.split(" ")[0]].append(j.split(" ")[1])

    for i in id_list:
      call1[i] = set(call[i]) & set(warn)
    
    for i in id_list:
      answer.append(len(call1[i]))
    
    return answer
