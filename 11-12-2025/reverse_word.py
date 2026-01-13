def reverse_word(num):
    word=""
    result=""
    for i in num:
        if i !=" ":
            word=i+word
        else:
            result+=word+" "
            word=" "
    print(result+word)
reverse_word("I love python")








def reverse_word(n):
    new=""
    res=""
    for i in range(len(n)):
        if n[i]!=" ":
            res=n[i]+res
        else:
            new=new+res+" "
            res=" "
   

    print(new+res)
reverse_word("hello word")