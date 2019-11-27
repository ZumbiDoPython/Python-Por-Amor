while (True):
  
  
 operacao=(input("Insira sua operação:"))
 operacao1=operacao.split()
 a=int (operacao1[0])
 op=str(operacao1[1])
 b=int (operacao1[2])
 c=a+b
 c=None
    
   
 if op =='+':
     c=a+b
     print (' {} + {} = {}' .format (a,b,c))
 elif op=='-':
     c=a-b
     print (' {} - {} = {}' .format (a,b,c))
 elif op=='*':
     c=a*b
     print (' {} * {} = {}' .format (a,b,c))
 elif op=='/':
     c=a/b
     print (' {} / {} = {}' .format (a,b,c))
 elif op=='**':
        c=int (input('Insira C: \n'))
        d=b**2-4*(a)*(c)
        for i in range (1,100):
         j=i*i
         if j==d :
             x1=(-b+i)/2*a
             x2=(-b-i)/2*a
        

    
