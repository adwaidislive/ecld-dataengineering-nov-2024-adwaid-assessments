def after_n_days(days, n):
    week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    n = n % 7 # If n is greater than 7 it reduced here
    outputdays = []
    for day in days:
        initial_val = week.index(day) # We find out the index of the input day
        final = week[(initial_val + n) % 7]
        outputdays.append(final)
    
    return outputdays
    
print(after_n_days(["Thursday", "Monday"], 4))