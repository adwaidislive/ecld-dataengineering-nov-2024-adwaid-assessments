def after_n_days(days, n):
    week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    n = n % 7
    outputdays = []
    for day in days:
        initial_val = week.index(day)
        final = week[(initial_val + n) % 7]
        outputdays.append(final)
    
    return outputdays
    
print(after_n_days(["Thursday", "Monday"], 4))