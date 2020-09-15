N = input()
N1 = N
i = 0
while True :
    try :
        X = N[1]
    except :
        N = "0" + N[0]

    R = int(N[0]) + int(N[1])
    R1 = str(R)
    try :
        X = R1[1]
    except :
        R1 = "0" + R1[0]

    N = N[1] + R1[1]
    i +=1
    if int(N) == int(N1) :
        print(i)
        break



