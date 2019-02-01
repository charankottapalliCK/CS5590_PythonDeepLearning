n = int(input("How many  numbers  do you have? "))

s = 0
obs = map(int, raw_input().split())
if len(obs) != n:
    print("Did not enter "+str(n)+" values")
else:
    for i in range(0,len(obs)):
        s = s+obs[i]
    avg = s / float(n)
    print (avg)

