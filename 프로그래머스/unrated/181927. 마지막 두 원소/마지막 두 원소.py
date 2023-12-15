def solution(num_list):
    for i in num_list:
        if num_list[-1] > num_list[-2]:
            new = num_list[-1] - num_list[-2]
            num_list.append(new)
            return num_list
        else:
            new = num_list[-1]*2
            num_list.append(new)
            return num_list