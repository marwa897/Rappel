tab=[]
somme=0
for i in range(5) :
    tab[i].append(int(input('donner une valeur')))
    somme=somme+tab[i]
    print(" la somme des elements est" , somme )