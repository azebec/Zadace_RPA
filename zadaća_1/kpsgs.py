import random #generiranje slucajnog broja
#Odabir 
kps = ['kamen', 'papir', 'skare', 'guster', 'Spock']
#Igra

igraj= "d"
bodovi= int()

while igraj == "d":
    print('='*20)
    Talion= str(input('Talion:'))
    Ork = random.choice(kps)
    print('Ork je odabrao {}'.format(Ork))
    print('='*20)
    if Talion == 'kamen' and Ork == 'papir' :
        print( 'Pobjednik je Ork, papir prekrije kamen')
        bodovi -= 1
    elif Talion== 'papir' and Ork == 'kamen' :
        print ('Pobjednik je Talion, papir prekrije kamen ')
        bodovi += 1
    elif Talion == 'kamen' and Ork == 'skare' :
        print ('Pobjednik je Talion, kamen uništi škare')
        bodovi += 1
    elif Talion == 'kamen' and Ork == 'kamen' :
        print ('Rezultat je nerješen, oba igrača odabrali su isto')
        bodovi +=0 
    elif Talion == 'papir' and Ork == 'papir' :
        print ('Rezultat je nerješen, oba igrača odabrali su isto')
        bodovi += 0
    elif Talion == 'papir' and Ork == 'skare' :
        print ('Pobjednik je Ork, škare prerežu papir')
        bodovi -= 1
    elif Talion == 'skare' and Ork == 'skare' :
        print ('Rezultat je nerješen, oba igrača odabrali su isto')
        bodovi += 0
    elif Talion == 'skare' and Ork == 'kamen' :
        print ('Pobjednik je Ork, kamen uništi škare')
        bodovi -= 1
    elif Talion == 'skare' and Ork == 'papir' :
        print ('Pobjednik je Talion, škare režu papir')
        bodovi += 1
    elif Talion == 'kamen' and Ork == 'guster':
        print ('Pobjednik je Talion, kamen razbije guštera')
        bodovi += 1
    elif Talion == 'guster' and Ork == 'kamen':
        print ('Pobjednik je Ork, kamen razbije guštera')
        bodovi -= 1
    elif Talion == 'guster' and Ork == 'Spock':
        print ('Pobjednik je Talion, gušter otruje Spocka')
        bodovi +=1
    elif Talion == 'Spock' and Ork == 'guster':
        print ('Pobjednik je Ork, gušter otruje Spocka')
        bodovi -= 1
    elif Talion == 'Spock' and Ork == 'skare':
        print ('Pobjednik je Talion, Spock razbije škare')
        bodovi += 1 
    elif Talion =='skare' and Ork == 'Spock':
        print ('Pobjednik je Ork, Spock razbije škare')
        bodovi -= 1
    elif Talion == 'skare' and Ork == 'guster':
        print ('Pobjednik je Talion, škare obrubljuju guštera')
        bodovi += 1
    elif Talion == 'guster' and Ork == 'skare':
        print ('Pobjednik je Ork, škare obrubljuju guštera')
        bodovi -= 1
    elif Talion == 'guster' and Ork == 'papir':
        print ('Pobjednik je Talion , gušter jede papir')
        bodovi += 1
    elif Talion == 'papir' and Ork == 'guster':
        print ('Pobjednik je Ork, gušter jede papir')
        bodovi -= 1
    elif Talion =='papir' and Ork == 'Spock':
        print ('Pobjednik je Talion, papir opovrgava Spocka')
        bodovi += 1
    elif Talion == 'Spock' and Ork == 'papir':
        print ('Pobjednik je Ork, papir opovrgava Spocka')
        bodovi -= 1
    elif Talion == 'Spock' and Ork == 'kamen':
        print ('Pobjednik je Talion, Spock isparava kamen')
        bodovi += 1
    elif Talion == 'kamen' and Ork == 'Spock':
        print ('Pobjednik je Ork, Spock isparava kamen')
        bodovi -= 1
    elif Talion == 'Spock' and Ork == 'Spock':
        print ('Rezultat je nerješen, oba igrača odabrali su isto')
        bodovi += 0
    elif Talion == 'guster' and Ork == 'guster':
        print ('Rezultat je nerješen, oba igrača odabrali su isto')
        bodovi += 0
    else :
        print ('Talion je unio krivu vrijednost')
    print('Talion ima {} bodova.'.format(bodovi))
    igraj=input("Ponovi igru? Da (d)/Ne (n)")