
A = [1, 2, 3, 4, 5, 6]
wynik=[]
for i in range(1,len(A)+1):
    wynik.append([i])
    for k in range(i+1,len(A)+1):
        wynik.append([i,k])
        for v in range(k+1,len(A)+1):
            wynik.append([i,k,v])
            for z in range(v+1,len(A)+1):
                wynik.append([i,k,v,z])
                for t in range(z+1,len(A)+1):
                    wynik.append([i,k,v,z,t])
                    for g in range(t+1,len(A)+1):
                        wynik.append([i,k,v,z,t,g])
                        
                        
                        

def unique_sum_combinations(numbers, start=0, combo=[]):
    if start == len(numbers):
        return [combo] if combo else []
    
    with_current = combo + [numbers[start]]
    without_current = combo
    
    with_current_combinations = unique_sum_combinations(numbers, start + 1, with_current)
    without_current_combinations = unique_sum_combinations(numbers, start + 1, without_current)
    
    return with_current_combinations + without_current_combinations

A = [1, 2, 3, 4, 5, 6]
result = unique_sum_combinations(A)
print(result)
