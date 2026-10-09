def shuffle_sentence(sentence, order):
    a = sentence.split()
    returning = 0
    result_list =[]
    for i in a :
        order_of_returning = order[returning] 
        result_list.append(a[order_of_returning])
        returning += 1
    return " ".join(result_list)





print(shuffle_sentence('cat dog mouse', (2, 0, 1)))
