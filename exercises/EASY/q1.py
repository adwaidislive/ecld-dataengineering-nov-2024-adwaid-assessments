# Q1 : Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

def dis(price,discount):
    dis_price = price*(discount/100)
    finalprice = price - dis_price
    return finalprice

dis(200,25)