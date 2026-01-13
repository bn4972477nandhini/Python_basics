def enter_amount(m):
    price=0
    if m>=1000:
        price=m*0.90
    elif m>500 and m <1000:
        price=m*0.95
    else:
        print("invalid")
    print(price)
    

enter_amount(800)
enter_amount(1400)
enter_amount(400)