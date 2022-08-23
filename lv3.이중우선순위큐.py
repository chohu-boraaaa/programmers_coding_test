def solution(operations):
    b = []
    answer = []
    for a in operations:
        if a[0] == "I":
            b.append(int(a.split(" ")[1]))
        elif a[0] == "D":
            if b != []:
                if int(a.split(" ")[1]) == 1:
                    b.remove(max(b))
                elif int(a.split(" ")[1]) == -1:
                    b.remove(min(b))
    
    if b == []:
        answer = [0,0]
    else:
        answer = [max(b), min(b)]
    return answer
