mysum = 0
for i in range(5, 11, 2):
    print('mysum', mysum)
    mysum += i
    for j in range(1, 10):
        print('j', j)
        mysum += j        
        if mysum == 6:
            break

    print(mysum)