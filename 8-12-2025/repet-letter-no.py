def repet_letter_no(n):
    result=""
    for i in n:
        if i not in result:
            result+=i
    print(result)
    
   
repet_letter_no("heeelloooo")