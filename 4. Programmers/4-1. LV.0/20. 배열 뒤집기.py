def solution(num_list):
    reverse_list = [num_list[i] for i in range(len(num_list)-1,-1,-1)]
    return reverse_list