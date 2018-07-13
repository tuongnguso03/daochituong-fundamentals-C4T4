def get_even_list(old_list):
    new_list=[]
    for i in range(len(old_list)):
        if old_list[i]%2==0:
            new_list.append(old_list[i])
    return(new_list)    
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

