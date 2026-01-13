def remove_characters(input):
    result=""
    letter="ABCDEFGHIJKLMNOPQURSTVWXYZqwertyuiopasdfghjklzxcvbnm"
    number="0123456789"
    under = "_"
    l = input.lower()
    # print(l)
    for j in l:
        if j in letter or j in number or j in under:
            result+=j.
    print(result)
            
remove_characters("Ram!_Kumar@2024")
