import random
from aliohjelmat.lista_tarkistus import lista_tarkistus #haetaan lista_tarkistus tiedostosta lista_tarkistus funktio




def alku():
    
    '''
    Arpoo laivat kartalle

    importtaa lista tarkistus funktion
    palauttaa vain yhden listan

    funktio joka arpoo laivojen sijainnit
    1 viisi ruuta pitkää
    2 neljä ruutua pitkää
    2 kolme ruutua pitkää
    1 kaksi ruuta pitkää laivaa
    
    Laivat eivät voi olla vierekkäin mutta voivat olla kulmikkain 
    
    Funktio tarvitsee toimiakseen lista_tarkistus funktion
    joka on tässä samassa tiedostossa
    
    arvottavien laivojen pituutta ja määrää voi muuttaa manuaalisesti
    tutkitaan len käskyllä laivojen määrä eikä sitä kirjoiteta lähdekoodiin
    '''


    def arpomis_funktio(laivat): #funktio sisäinen funktio
        lista =  [5,4,4,3,3,2] #lista määrittää laivojen pituuden ja määrän
        pysty = 0 #pystysijainti
        vaaka = 0 #vaakasijainti
        asento = 0 #laivan suunta 1 = ylös 2 = oikealla 3 = alas 4 = vasemmalle
        tarkistus_pysty = 0
        tarkistus_vaaka = 0
        laskuri = 0 #listan läpikäymiseen, kertoo mikä laiva 
        tarkistus = False #onnistuuko laivan sijoittaminen tähän suuntaan True = onnistuu
        
        while True:
            if laskuri > len(lista) -1: #onko kaikki laivat asetettu kartalle
                return(laivat)
            pysty = random.randint(0,9) #arvotaan kohta
            vaaka = random.randint(0,9)
            tarkistus_pysty = pysty
            tarkistus_vaaka = vaaka
            asento = random.randint(1,2) #arvotaan laivan sunta
            if lista_tarkistus(laivat,pysty,vaaka) == False:
                continue

            #tutkitaan mihin suuntaan laiva on mahdollista sijoittaa
            if asento == 1: #ylöspäin
                if pysty - lista[laskuri] < 0:
                    continue
                else:
                    for i in range(lista[laskuri]): #tarkistetaan ylöspäin
                        tarkistus_pysty -= 1
                        tarkistus = lista_tarkistus(laivat,tarkistus_pysty,tarkistus_vaaka)
                        if tarkistus == False: #jos ei onnistu
                            break
                    if tarkistus == False: #jos laivan sijoittaminen ei onnistu
                        continue
                    else: #jos onnistuu, asetetaan laivat kartalle
                        for i in range(lista[laskuri]):
                            laivat[pysty][vaaka] = 4
                            pysty -= 1
                        laskuri += 1
                        continue
            ###########################
            elif asento == 2: #oikealle
                if vaaka + lista[laskuri] > 9:
                    continue
                else:
                    for i in range(lista[laskuri]): #tarkistetaan oikealle
                        tarkistus_vaaka += 1
                        tarkistus = lista_tarkistus(laivat,tarkistus_pysty,tarkistus_vaaka)
                        if tarkistus == False: #jos ei onnistu
                            break
                    if tarkistus == False: #jos laivan sijoittaminen ei onnistu
                        continue
                    else: #jos onnistuu, asetetaan laivat kartalle
                        for i in range(lista[laskuri]): #ylöspäin
                            laivat[pysty][vaaka] = 4
                            vaaka += 1
                        laskuri += 1
                        continue
        return(laivat)
    
    laivat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


    laivat = arpomis_funktio(laivat)

    return(laivat)

