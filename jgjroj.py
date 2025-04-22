'''        *
          * *
         * * *
          * *
           *


           
i=0     0,1,2,3,4,5,6
i=1and 5    0,1,5,6
i=3      0,3,6
i=2and 4    0,2,4,6  
i=6     0,1,2,3,4,5,6  '''

n=7
def printhallow():
    for i in range(n):
        for j in range(n):
             if(i==0 or i==n-1):
                 print("*",end="")
             
             if(i==1 or i==5):
                if j in (0, 1, 5, 6):
                     print("*",end="")
                else:
                    print(" ",end="")
             if(i==3):
                 if j in (0,3,6):
                     print("*",end="")
                 else:
                     print(" ",end='')
             if i in (2,4):
                 if j in (0,2,4,6):
                     print("*",end='')
                 else:
                     print(" ",end="")
        print()


         
     


printhallow()