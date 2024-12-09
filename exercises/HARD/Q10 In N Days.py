def after_n_days(days, n):
    weekdays = {
        "Sunday" : 1,
        "Monday" : 2,
        "Tuesday" : 3,
        "Wednesday" : 4,
        "Thursday" : 5,
        "Friday" : 6,
        "Saturday" : 7
    }
    outputdays = []
    
    n = n % 7
    for i in days:
        initial_val = weekdays[i]
        target = initial_val + n
        if target>7:
            target = target % 7
            for key,value in weekdays.items():
                if value == target:
                    outputdays.append(key)
        else:
            for key,value in weekdays.items():
                if value == target:
                    outputdays.append(key)
        
    return outputdays
            
print(after_n_days(["Thursday", "Monday"], 4))
print(after_n_days(["Saturday"], 1))
    
		