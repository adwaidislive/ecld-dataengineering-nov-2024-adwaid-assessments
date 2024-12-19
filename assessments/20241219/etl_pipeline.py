# Exercise 3: ETL Pipeline for E-commerce Analytics

def total_transaction_values(jsonfile):
    total_price = 0
    for i in range(len(json_file)):
        for j in range(len(json_file[i]['items'])):
            total_price = total_price + json_file[i]['items'][j]['price']


    return total_price

def unique_categories(jsonfile):
    categories = []
    for i in range(len(json_file)):
        for j in range(len(json_file[i]['items'])):
            categories.append(json_file[i]['items'][j]['category'])


    return set(categories)