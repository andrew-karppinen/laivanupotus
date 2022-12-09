
'''

toimiva
Funktio joka tarkistaa onko laiva uponnut
jos on palauttaa True muuten False
saa parametriksi sijainnin
palauttaa laivat
käyttää muunnin funktiota
Muuttaa laivan 7
ja 6 jos kokonaan uponnut
'''


def muunnin(laivat):
    #funktio joka muuttaa 7 --> 2
    for i in range(10):
        for j in range(10):
            if laivat[i][j] == 5:
                laivat[i][j] = 4
            elif laivat[i][j] == 7:
                laivat[i][j] = 2
    return(laivat)
 
def muunnin_2(laivat):
    #muuntaa 7 --> 6
    for i in range(10):
        for j in range(10):
            if laivat[i][j] == 5:
                laivat[i][j] = 4
            elif laivat[i][j] == 7:
                laivat[i][j] = 6
    return(laivat)

def uponnut_tarkistus(laivat,pysty,vaaka):

    vaaka_asennossa = False #laiva vaakaasennossa
    pysty_asennossa = False #laiva pystyasennossa
    oikealle = True #mihin suuntaan liikutaan
    ylos = True

    if laivat[pysty][vaaka] == 2:
        laivat[pysty][vaaka] = 7

    #tutkitaan missä asennossa laiva
    if vaaka +1 <= 9: #tarkistetaan loppuuko kartta
        if laivat[pysty][vaaka +1] == 4 or laivat[pysty][vaaka +1] == 2: #onko kohdan oikealla puolella laiva
            vaaka_asennossa = True #laiva on vaakasennossa
    
    if vaaka -1 >= 0: #tarkistetaan loppuuko kartta  
        if laivat[pysty][vaaka -1] == 4 or laivat[pysty][vaaka -1] == 2: #onko kohdan vasemmalla puolella laiva
            vaaka_asennossa = True #laiva on vaaka asennossa

    if pysty +1 <= 9: #tarkistetaan loppuuko kartta  
        if laivat[pysty +1][vaaka] == 4 or laivat[pysty +1][vaaka] == 2: #onko kohdan alapuolella laivaa
            pysty_asennossa = True #laiva pystyasennossa

    if pysty -1 >= 0: #tarkistetaan loppuuko kartta  
        if laivat[pysty -1][vaaka] == 4 or laivat[pysty -1][vaaka] == 2: #onko kohdan yläpuolella laivaa
            pysty_asennossa = True #laiva on pystyasennossa



    while vaaka_asennossa: #jos laiva vaakaasennossa
        if oikealle: #oikealle
            if laivat[pysty][vaaka] == 1 or laivat[pysty][vaaka] == 3: #jos ei laivaa
                vaaka -= 1 #takaisinpäin kordinaatistossa
                oikealle = False #vasemmalle
            elif laivat[pysty][vaaka] == 4: #jos upottamaton laiva
                laivat = muunnin(laivat) #funktio joka muuntaa 7 takaisin 2
                return(laivat, False) 
            elif laivat[pysty][vaaka] == 2 or laivat[pysty][vaaka] == 7: #jos kohdassaa 2 tai 7
                if vaaka +1 <= 9: #jos kartta ei lopu
                    laivat[pysty][vaaka] = 7 #muutetan kohta 7
                    vaaka += 1
                else: #jos kartta loppuu
                    oikealle = False #vasemmalle
        #########################
        if oikealle == False: #vasemmalle
            if laivat[pysty][vaaka] == 4: #jos upottamaton laiva
                laivat = muunnin(laivat) #funktio joka muuntaa 7 takaisin 2
                return(laivat, False)
            elif laivat[pysty][vaaka] == 1 or laivat[pysty][vaaka] == 3: #jos ei laivaa
                laivat = muunnin_2(laivat) #muutetaan 7 --> 6
                return(laivat, True)
            elif laivat[pysty][vaaka] == 2 or laivat[pysty][vaaka] == 7: #jos kohdassaa 2 tai 7
                if vaaka -1 >= 0: #jos kartta ei lopu
                    laivat[pysty][vaaka] = 7 #muutetan kohta  7
                    vaaka -= 1
                else: #jos kartta loppuu
                    laivat[pysty][vaaka] = 7
                    laivat = muunnin_2(laivat)
                    return(laivat, True)

    ################################################
    while pysty_asennossa: #pysty asennossa
        if ylos: #ylös
            if laivat[pysty][vaaka] == 1 or laivat[pysty][vaaka] == 3: #jos ei laivaaä")
                pysty += 1 #takaisinpäin kordinaatistossa
                ylos = False #alas
            elif laivat[pysty][vaaka] == 4: #jos upottamaton laiva
                laivat = muunnin(laivat) #funktio joka muuntaa 7 takaisin 2
                return(laivat, False) 
            elif laivat[pysty][vaaka] == 2 or laivat[pysty][vaaka] == 7: #jos kohdassaa 2 tai 7
                if pysty -1 >= 0: #jos kartta ei lopu
                    laivat[pysty][vaaka] = 7 #muutetaan kohta 7
                    pysty -= 1
                else: #jos kartta loppuu
                    ylos = False #alas
        #############################
        if ylos == False: #alas
            if laivat[pysty][vaaka] == 4: #jos upottamaton laiva
                laivat = muunnin(laivat) #funktio joka muuntaa 7 takaisin 2
                return(laivat, False)
            elif laivat[pysty][vaaka] == 1 or laivat[pysty][vaaka] == 3: #jos ei laivaa
                laivat = muunnin_2(laivat) #muutetaan 7 --> 6
                return(laivat, True)
            elif laivat[pysty][vaaka] == 2 or laivat[pysty][vaaka] == 7: #jos kohdassaa 2 tai 7
                if pysty +1 <= 9: #jos kartta ei lopu
                    laivat[pysty][vaaka] = 7 #muutetan kohta 7
                    pysty += 1
                else: #jos kartta loppuu
                    laivat[pysty][vaaka] = 7
                    laivat = muunnin_2(laivat) #muutetaan 7 --> 6
                    return(laivat, True)