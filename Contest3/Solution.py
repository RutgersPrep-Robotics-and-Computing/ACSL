def countUniqueValues(fibNumber):
    count = 1
    i = 1
    j = 1
    
    while i != fibNumber:
        i += j
        j = i - j
        count += 1
        
    print(count)
    
    PT = [
        [1],
        [1, 1]
    ]
    
    for i in range(1, count):
        Row = [1]
        
        for i in range(len(PT[-1]) - 1):
            Row.append(PT[-1][i] + PT[-1][i + 1])
        
        Row.append(1)
        PT.append(Row)