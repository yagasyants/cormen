def calc(num_people):
    return 1 - calc_diff(num_people)
    
def calc_diff(num_people):
    if(num_people==1):
        return 1.0
    else:
        return ((365.0 - num_people + 1) / 365.0) * calc_diff(num_people - 1)
    