def remove_spc_chars(num):
    result=""
    l="!;.,';:*"
    for i in num:
        if i not in l:
            result+=i
    print(result)
    
remove_spc_chars("Best-Selling! Laptop, 2024 Edition.")