# def print_ing_word(num):
#     # res=[]
#     for i in num:
#         print(i)
#         if i in "ing":
#             print(i)
#     #         res.append(i)
#     # print(res)
        
            
# print_ing_word(["playing", "run", "walking", "see", "coding"])


def find_max(m):
    res=""
    for i in m:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            # print(i+"")
            res+=i+"  "
    print(res)
find_max("HeLLoWoRlD")