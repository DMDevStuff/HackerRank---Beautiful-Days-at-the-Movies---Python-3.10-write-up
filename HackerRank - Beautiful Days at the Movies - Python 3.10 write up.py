##    https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
##
##    Visit above link for official problem description

##### ##### ##### #####

#   O(n)
#   n is the end_day - start_day
#   Algo:
#       iterate, check condition, increment based on condition

def beautifulDays(start_day, end_day, divisor):
    
    beautiful_days_found = 0
    
    for day in range(start_day, end_day + 1):
        
        if abs(day - int(str(day)[::-1])) % divisor == 0:
            
            beautiful_days_found += 1
            
    return beautiful_days_found
