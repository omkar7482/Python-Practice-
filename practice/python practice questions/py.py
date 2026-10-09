def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    '''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
    '''
    middle_no_of_tuuple = int(((len(t)-1)/2))
    before_middle_no = t[0:middle_no_of_tuuple]
    list_of_before_middle_no = list(before_middle_no)
    after_middle_no = t[middle_no_of_tuuple + 1 :]
    list_of_after_middle_no = list(after_middle_no)
    a = t[middle_no_of_tuuple]
    n_times_middle =[]
    count = 0
    while count < n :
        n_times_middle.append(a)
        count += 1
    return tuple(list_of_before_middle_no+n_times_middle+list_of_after_middle_no)
        
             
    
    
a = replace_middle_with_n_times_middle((1, 2, 3, 4, 5), 5)
print(a)
    
    
    
