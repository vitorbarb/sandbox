def romanToInt():
    s = input("Type a number in roman letters: ").upper()
    string = []
    values = []
    for x in s:
        string.append(x)
        
        
    for i in range(len(string)):
        match string[i]:
            case "I":
               values.append(1)
            case "V":
                values.append(5)
            case "X":
                values.append(10)
            case "L":
                values.append(50)
            case "C":
                values.append(100)
            case "D":
                values.append(500)
            case "M":
                values.append(100)
    print(values)
    
    counter = 0
    for x in range(len(values)):
        if values[x] == values[x +1 ]: # Fix this logic somehow to make list index inside the range but still observe the next one in the list
            if
            counter = values[x] + values[x+1]
            
    print(counter)
        


romanToInt()
    
    
