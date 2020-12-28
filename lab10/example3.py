def recsum(num_list):
    if (not isinstance(num_list,list)):
        return num_list
    else:
        sum_result = 0

        for item in num_list:
            sum_result += recsum(item)
        return sum_result

a_list = [3,12,76,[4,56,43],[2,8],81,75]
