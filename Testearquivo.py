a= open("/storage/emulated/0/qpython/curso/salvo.txt","a")
ins=0
nome=input("Nome:")
idade=input("Idade:")
a.write(nome)
a.write("\n")
a.write(idade)
a.write ("\n")
a.write ("1\n")
a.close()


a= open("/storage/emulated/0/qpython/curso/salvo.txt","r")
cont=a.readlines()
co=cont
co=len (cont)
ins=co/3
ins=int (ins)
n=ins*3
n=n-3
no=cont[n]
print (co)
print("Nome:",no,"\nIdade:",cont [1],"\nSua inscrição é:",ins)
a.close()
                                                                
a=open("/storage/emulated/0/qpython/curso/salvo.txt" , "a")
ins=str(ins)
a.write(ins)
a.write("\n")