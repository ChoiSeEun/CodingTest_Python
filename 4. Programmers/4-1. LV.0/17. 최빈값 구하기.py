from collections import Counter

def solution(array):
    answer = 0
    counters = Counter(array)
    counters = counters.most_common(len(array))
    if len(counters)>=2 and counters[0][1]==counters[1][1]:
        answer = -1
    else:
        answer = counters[0][0]
    return answer