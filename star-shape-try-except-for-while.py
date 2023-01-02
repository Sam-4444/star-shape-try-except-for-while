try:

    p= input("Enter a digit between 5 and 10 and press enter  :) ")
    p= int(p)
    if (p<5 or p>10):
        print(f" {p} is not in specified range !")
        exit()
    else:
        for z in range (p,0,-1):
            print(z*"*")

        print(p*"<->")        
        for z in range (1,p):
            print(z*"*")

        while p>0:
            print(p*"*")
            p-=1
except ValueError:
    print(f"The input is not a number ! {p}")
