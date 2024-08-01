def pattern():
    a=1
    for i in range(10):
        for j in range(i+1):
            print(a,end=' ')
        a+=1
        print()
pattern()

