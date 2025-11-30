# list_in = [2,0,5,6,6]
# list_in =[12,8,10]
list_in = [-5,1,12,17,0,13,8,3,8]
list_result =[]

for i in range(len(list_in)):
    target = list_in[i]
    mini_num = float('inf')
    specific_num = None
    for l in range(len(list_in)):
        compare_num = list_in[l]
        may_it = abs(target - compare_num)
        if l != i and may_it < mini_num:
            mini_num = may_it
            specific_num = compare_num
        elif l != i and may_it == mini_num:
            if compare_num < specific_num:
                specific_num = compare_num
            else:
                pass
    list_result.append(specific_num)
print(list_result)