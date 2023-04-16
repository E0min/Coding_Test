def solution(price, money, count):
    total_price = 0
    for i in range(1, count+1):
        total_price = total_price + i*price
    if money>total_price:
        return 0
    else:
        return total_price - money

    