def upper_case_letter(num):
    result=""
    number="0123456789"
    letter="ABCDEFGHIJKLMNOPQURSTVWXYZqwertyuiopasdfghjklzxcvbnm"
    for i in num:
        if i in number or i in letter:
            result+=i.upper()
           
    print(result)
upper_case_letter("ab#12!cd@EF3")