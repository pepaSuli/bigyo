def menu(lista):
    for i,szoveg in enumerate(lista):
        print("{}: {}".format(i+1,szoveg))

    valasz=-1
    while (valasz<1 or valasz>len(lista)) and  valasz!=999 :
        try:
            valasz=int(input("Válassz: "))
        except:
            pass

    return valasz-1

    

#lista=["előre","hátra","jobbra","balra"]

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

tortenet=[
    [
        1,  #történetszál sorszáma
        "Reggel felkeltem.",    #történetszál szövege
        ["fogmosás", "reggeli", "öltözés"],#választható cselekvések
        [2,3,4]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        2,
        "Megmostam a fogam, mert még van!",
        ["fogmosás", "reggeli", "öltözés"],#választható cselekvések
        [2,3,4]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        3,
        "Éhes vagyok! Eszek valamit.",
        ["fogmosás", "reggeli", "öltözés"],#választható cselekvések
        [2,3,4]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        4,
        "Kellene valami ruha!",
        ["fogmosás", "reggeli", "öltözés", "Legyen vége!"],#választható cselekvések
        [2,3,4,999]  #cselekvés sorszáma, hova ugorjon
    ]
]

tortenet=[
    [
        1,  #történetszál sorszáma
        "Felébredtem.Hol vagyok? Ki kell innen találnom!",    #történetszál szövege
        ["lefelé", "jobbra"],#választható cselekvések
        [4,2]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        12,  #történetszál sorszáma
        "Itt ébredtem! Most másfelé próbálkozzunk!",    #történetszál szövege
        ["lefelé", "jobbra"],#választható cselekvések
        [4,2]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        2,  #történetszál sorszáma
        "Itt nincs kijárat. Keressünk tovább!",    #történetszál szövege
        ["lefelé", "jobbra","balra"],#választható cselekvések
        [5,3,12]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        3,  #történetszál sorszáma
        "Itt sincs kijárat. Keressünk tovább!",    #történetszál szövege
        ["lefelé", "balra"],#választható cselekvések
        [6,2]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        4,  #történetszál sorszáma
        "Ez egy üres szoba. Keressünk tovább!",    #történetszál szövege
        ["felfelé", "jobbra"],#választható cselekvések
        [12,5]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        5,  #történetszál sorszáma
        "Ez valami központi folyosó lehet. De nincs kijárat. Keressünk tovább!",    #történetszál szövege
        ["felfelé", "lefelé","jobbra","balra"],#választható cselekvések
        [2,8,6,4]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        6,  #történetszál sorszáma
        "Friss levegőt érzek! Keressünk tovább!",    #történetszál szövege
        ["felfelé", "lefelé","balra"],#választható cselekvések
        [3,9,5]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        7,  #történetszál sorszáma
        "Ez zsákutca. Menjünk vissza!",    #történetszál szövege
        ["vissza"],#választható cselekvések
        [8]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        8,  #történetszál sorszáma
        "Már unom... Keressünk tovább!",    #történetszál szövege
        ["felfelé","balra"],#választható cselekvések
        [5,7]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        9,  #történetszál sorszáma
        "Már látom a fényt!",    #történetszál szövege
        ["felfelé","lefelé"],#választható cselekvések
        [6,10]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        10,  #történetszál sorszáma
        "Végre kijutottam! Merre tovább?",    #történetszál szövege
        ["vissza","el innen"],#választható cselekvések
        [9,11]  #cselekvés sorszáma, hova ugorjon
    ],
    [
        11,  #történetszál sorszáma
        "Isten véled rossz emlék!",    #történetszál szövege
        [],#választható cselekvések
        []  #cselekvés sorszáma, hova ugorjon
    ],

]
#        ["előre", "lefelé", "jobbra","balra"],#választható cselekvések


szalId=1
while True:
    tempLista=[]
    for elem in tortenet:
        tempLista.append(elem[0])

    keresettIndex=tempLista.index(szalId)

    print("\n"+"-"*50)
    print(tortenet[keresettIndex][1])

    if len(tortenet[keresettIndex][2])==0:
        break
    valasztott=menu(tortenet[keresettIndex][2])
    
    if szalId==999:
        break

    szalId=tortenet[keresettIndex][3][valasztott]
    
print("VÉGE")










