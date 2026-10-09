def extract_middle_elements(lst:list):
    """
    Extracts the middle element(s) from a list of integers.

    Args:
        lst (list): The list of integers.

    Returns:
        list: A list containing either the middle element (if odd length) or 
        the two middle elements (if even length).
    """
    ...
    
    no_of_element_in_list = len(lst) -1
    if no_of_element_in_list % 2 == 0:
        middle_elements = int(no_of_element_in_list/2)
        a = lst[middle_elements]
    return [a]
a = extract_middle_elements([7, 8, 9, 10, 11, 12, 13])
print(a)