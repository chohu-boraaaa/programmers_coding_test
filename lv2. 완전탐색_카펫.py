def solution(brown, yellow):
    answer = []
    
    for i in range(1,yellow+1):
        if yellow % i == 0:
            length = i + 2
            width = int(yellow/i) + 2
            if (length*width-yellow) == brown:
                answer = [width, length]
                break
    
    return answer
