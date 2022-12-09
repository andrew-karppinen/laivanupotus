
import pygame
from aliohjelmat.tulostus import ruudukko
from aliohjelmat.alku import alku
from aliohjelmat.tulostus import tulostus
from aliohjelmat.lista_tarkistus import lista_tarkistus
from aliohjelmat.muunnin import muunnin

'''
toimiva

käyttäjä valitsee laivojen sijainnit
Rajoitettu versio, vähentää prossessorin kuormitusta

importtaa itse aliohjelmia
saa parametriksi "naytto" jota pygame käyttää
tarvitsee pygamen toimiakseen
'''


def poisto(pelaajan_laivat):
    #funktio joka poistaa 5 kartalta
    for i in range(10):
        for j in range(10):
            if pelaajan_laivat[i][j] == 5:
                pelaajan_laivat[i][j] = 1
    return(pelaajan_laivat)

def laivan_sijanti(pelaajan_laivat,piste_y,piste_x,sijainti_y,sijainti_x,vaaka,lista,laskuri):
    #asetetaan laiva kartalle
    if vaaka: #vaakaasento
        sijainti_x = piste_x
        sijainti_y = piste_y
        for i in range(lista[laskuri]):
            if pelaajan_laivat[sijainti_y][sijainti_x] != 4: #tutkitaan onko kohtaan jo asetettu laiva
                pelaajan_laivat[sijainti_y][sijainti_x] = 5
                sijainti_x += 1

    if vaaka == False: #pystyasento
        sijainti_x = piste_x
        sijainti_y = piste_y
        for i in range(lista[laskuri]):
            if pelaajan_laivat[sijainti_y][sijainti_x] != 4: #tutkitaan onko kohtaan jo asetettu laiva
                pelaajan_laivat[sijainti_y][sijainti_x] = 5
                sijainti_y += 1
    return(pelaajan_laivat)


def valinta(naytto):
    '''
    Funktio jossa pelaaja voi valita laivojensa sijainnit 
    ja hakee alku tiedostosta myös vihollisen laivat
    Tarvitsee laivat funktion joka tulostaa myös 5
    '''
    kello = pygame.time.Clock() #kello jolla rajoitetaan pelin nopeutta
    
    pelaajan_laivat = [
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

    vihollisen_laivat = alku()

    #Muuttujat
    vasemmalle = False #näppäimet
    oikealle = False
    ylos = False
    alas = False
    space = False
    t_kirjain = False #t-näppäin

    piste_x = 2 #sijainti
    piste_y = 2
    sijainti_x = 0
    sijainti_y = 0

    tarkistus_y = 0
    tarkistus_x = 0
    onnistuuko = True

    vaaka = True #laivan asento False = pysty
    lista =  [5,4,4,3,3,2] #lista määrittää laivojen pituuden ja määrän
    laskuri = 0

    fontti = pygame.font.Font("fontti/Roboto-Regular.ttf", 28) #ladataan fontti
    teksti = fontti.render("Liikuta laivaa nuolinäppäimillä, käännä laivaa painamalla välilyöntiä,", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
    teksti2 = fontti.render("ja aseta laiva paikoilleen painamalla t-kirjainta", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva

    while True: #funktion pääsilmukka
        #tapahtumasilmukka
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP: #tutkitaan painetaanko ylintä nuolinäppäintä
                    ylos = True #asetetaan muuttuja ylos arvoon True
                    oikealle = False #muut false
                    vasemmalle = False
                    alas = False
                    
                if tapahtuma.key == pygame.K_DOWN: #tutkitaan painetaanko alinta nuolinäppäintä
                    alas = True #asetetaan muuttuja alas arvoon True
                    ylos = False #muut false
                    oikealle = False
                    vasemmalle = False
            
                if tapahtuma.key == pygame.K_LEFT: #tutkitaan painetaanko vasenta nuoinäppäintä
                    vasemmalle = True #asetetaan muuttuja vasemmalle arvoon True
                    oikealle = False #muut False
                    alas = False
                    ylos = False
                    
                if tapahtuma.key == pygame.K_RIGHT: #tutkitaan painetaanko oikeaa nuolinäppäintä
                    oikealle = True #asetetaan muuttuja oikealle arvoon True
                    vasemmalle = False #muut False
                    ylos = False
                    alas = False
        
                if tapahtuma.key == pygame.K_SPACE: #tutkitaan painetaanko välilyöntiä
                    space = True #asetetaan muuttuja space arvoon True
                
                if tapahtuma.key == pygame.K_t: #tutkitaan painetaanko t kirjainta
                    t_kirjain = True #asetetaan muuttuja t arvoon True           

            if tapahtuma.type == pygame.QUIT: #jos ohjelma suljetaan
                exit() #lopetetaan ohjelma
        
        #Liikutetaan laivaa 
        if oikealle: #oikealle
            oikealle = False 
            if vaaka and piste_x + lista[laskuri] <= 9: #vaakaasennossa
                piste_x += 1
            elif vaaka == False and piste_x +1 <= 9: #pystyasennossa
                piste_x += 1 

        if vasemmalle: #vasemmalle
            vasemmalle = False
            if piste_x -1 >= 0:
                piste_x -= 1
                
        if alas: #alas
            alas = False
            if vaaka == False and piste_y + lista[laskuri] <= 9:#pystyasennossa
                piste_y += 1
            elif vaaka and piste_y +1 <= 9: #vaakaasennossa
                piste_y += 1
        if ylos: #ylös
            ylos = False
            if piste_y - 1 >= 0:
                piste_y -= 1

        poisto(pelaajan_laivat) #funktio joka poistaa liikuteltavan laivan
        if pelaajan_laivat[piste_y][piste_x] != 4: #tutkitaan onko kohtaan jo asetettu laiva
            pelaajan_laivat[piste_y][piste_x] = 5 #laitetaan piste kartalle

        #sijoittaa laivan kartalle
        pelaajan_laivat = laivan_sijanti(pelaajan_laivat,piste_y,piste_x,sijainti_y,sijainti_x,vaaka,lista,laskuri)


        if space: #muuttaa laivan asentoa
            pelaajan_laivat = poisto(pelaajan_laivat)#funktio joka poistaa liikuteltavan laivan
            space = False
            if vaaka: 
                if piste_y + lista[laskuri] -1 <= 9: #lasketaan pysyykö laiva kartalla
                    vaaka = False #muutetaan laiva pystyasentoon
            else:
                if piste_x + lista[laskuri] -1 <= 9: #lasketaan pysyykö laiva kartalla
                    vaaka = True #muutetaan vaakaasentoon
        
            
        if t_kirjain: #jos käyttäjä painoi t-näppäintä sijoitetaan laiva siihen ja siirrytään seuraavaan laivaan
            t_kirjain = False
            poisto(pelaajan_laivat) #poistetetaan liikuteltavat laivat
            tarkistus_y = piste_y
            tarkistus_x = piste_x
            #tarkistetaan voiko laivaa asettaa tähän
            for i in range(lista[laskuri]):
                #funktio tutkii onko kohdan ympärillä laivoja
                onnistuuko = lista_tarkistus(pelaajan_laivat,tarkistus_y,tarkistus_x)
                if onnistuuko == False:
                    break
                
                if vaaka: #jos vaakaasennossa
                    tarkistus_x += 1
                else: #jos pystyasennossa
                    tarkistus_y += 1

            if onnistuuko:
                pelaajan_laivat = laivan_sijanti(pelaajan_laivat,piste_y,piste_x,sijainti_y,sijainti_x,vaaka,lista,laskuri)
                laskuri += 1 #seuraava laiva
                pelaajan_laivat = muunnin(pelaajan_laivat) 

        if laskuri == 6: #jos kaikkien laivojen sijainnit valittu
            return(pelaajan_laivat,vihollisen_laivat)

        #piirretään asiat!!!
        naytto.fill((77,136,255)) #asetetaan taustan väri
        ruudukko(naytto,teksti,teksti2) #piirtää ruudukon
        tulostus(pelaajan_laivat,vihollisen_laivat,naytto) #piirtää laivat
        pygame.display.flip() #päivittää näytön
        kello.tick(30) #rajoittaa pelin nopeutta vähentäen tietokoneen kuormitusta
