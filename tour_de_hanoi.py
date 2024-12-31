Pile1=[1,3,5,13]
Pile2=[13]
Pile3=[13]
choix=1
choix2=1
def afficher():
    print('tour 1 : ' + str(Pile1))
    print('tour 2 : ' + str(Pile2))
    print('tour 3 : ' + str(Pile3))
afficher()

while(Pile3!=[1,3,5,13]):
    choix=input(' Sur quelle tour doit ont prendre la première valeur ')
    afficher()

    if choix== '1':
        choix2 = input("sur quelle tour souhaitez vous déplacer la valeur ")
        if choix2 == '2' and Pile1[0]<Pile2[0]:
            Pile2.insert(0,Pile1[0])
            Pile1.pop(0)
            afficher()
        elif choix2 == '3' and Pile1[0]<Pile3[0]:            
            Pile3.insert(0,Pile1[0])
            Pile1.pop(0)
            afficher()
        else :
            print('La valeur est incorrecte')


    if choix == '2':
        choix2 = input("sur quelle tour souhaitez vous déplacer la valeur ")
        if choix2 == '1' and Pile2[0]<Pile1[0]:
            Pile1.insert(0,Pile2[0])
            Pile2.pop(0)
            afficher()
        elif choix2 == '3' and Pile2[0]<Pile3[0]:            
            Pile3.insert(0,Pile2[0])
            Pile2.pop(0)
            afficher()
        else :
            print('La valeur est incorrecte ')


    if choix == '3':
        choix2 = input("sur quelle tour souhaitez vous déplacer la valeur ")
        if choix2 == '2' and Pile3[0]<Pile2[0]:
            Pile2.insert(0,Pile3[0])
            Pile3.pop(0)
            afficher()
        elif choix2 == '1' and Pile3[0]<Pile1[0]:            
            Pile1.insert(0,Pile3[0])
            Pile3.pop(0)
            afficher()
        else :
            print('La valeur est incorrecte')
print('Bravo!!!'+"\U0001F44D")

