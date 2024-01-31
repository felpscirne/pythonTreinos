l = [2, 4, 6, 2, 3, 2, 4, 3, 5, 4, 3, 4, 5, 6, 4, 5, 6]

for i in range(len(l)):
    j = i+1  
    if i > (len(l) - 1):       break

    for j in range(len(l)):
        if  j > (len(l) - 1):  break
        if (l[i] == l[j]) and (i != j): l.pop(j)
            
print(l)
            
    
        