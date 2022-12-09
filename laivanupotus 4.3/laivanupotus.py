import random
import time
import pygame


#haetaan ohjelmat
from aliohjelmat.tulostus import tulostus
from aliohjelmat.tulostus import ruudukko
from aliohjelmat.laivat_tarkistus import laivat_tarkistus
from aliohjelmat.lista_tarkistus_tekoaly import lista_tarkistus_tekoaly
from aliohjelmat.uponnut_tarkistus import uponnut_tarkistus
from aliohjelmat.valinta import valinta
from aliohjelmat.lista_tarkistus import lista_tarkistus
from aliohjelmat.alku import alku




'''
Laivanupotus 4.0.3
tarvitsee pygamen toimiakseen


ominaisuudet:
Ohjelman nopeutta rajoitettu joten se kuormittaa prosessoria vähemmän
tietorakenteet toteutettu konstruktorilla

pelaaja valitsee itse laivojensa sijainnit
uponnut laiva piirretään punaisena
ampumistekoäly ei ammu upotetun laivan viereen
laskuri josta näkee kuinka monta laivaa jäljellä
'''

pygame.init() #alustetaan pygame moduuli
naytto = pygame.display.set_mode((900, 700)) #luodaan ikkuna
pygame.display.set_caption("Laivanupotus") #nimetään ikkuna



#tietorakenne joka sisältää ampumistekoälyn tietoja
class tekoaly_ampuminen_tiedot:
    def __init__(self,vaaka,pysty,upottaminen,oikealle,ylos,luku):
        self.vaaka = vaaka #onko laiva vaaka asennossa
        self.pysty = pysty #onko laiva pysty asennossa
        self.upottaminen = upottaminen  #onko laivan upottaminen kesken
        self.oikealle = oikealle #ammutaan oikealle puolelle False = vasemmalle
        self.ylos = ylos #ammutaan ylös False = alas
        #tämä sisältää tiedon mihin osutun kohdan viereen ammutaan
        self.luku = luku #1 = ylös 2 = oikea 3 = alas


    class sijainnit: #sijainnit
        def __init__(self,vaaka,pysty):
            self.vaaka = vaaka
            self.pysty = pysty

#käytetään edellisiä tietorakenteita
tiedot = tekoaly_ampuminen_tiedot(False,False,False,True,True,1) 
sijainti = tekoaly_ampuminen_tiedot.sijainnit(0,0)



def tekoaly_ampuminen(pelaajan_laivat,tiedot,sijainti,vuoro_teksti_2,teksti1,teksti2):

    '''
    Funktio joka arpoo mihin tekoäly ampuu
    jos se osuu laivaan se ampuu uudestaan
    ampuu älykkäästi osutun kohdan viereen
    käyttää uponnut_tarkistus funktiota joka tarkistaa onko laiva uponnut

    Tarvitsee toimiakseen tekoaly_ampuminen_tiedot luokasta tietoja
    vahvasti sidoksissa muun ohjelman toimintaan
    '''
    upposi = False #upposiko laiva

    while True:
        if tiedot.upottaminen == False: #jos minkää laivan upottaminen ei ole kesken
            sijainti.pysty =  random.randint(0,9) #arvotaan kohta
            sijainti.vaaka = random.randint(0,9)
            if lista_tarkistus_tekoaly(pelaajan_laivat,sijainti.pysty,sijainti.vaaka) == False: #tarkistaa onko kohdan vieressä upotettu laiva
                continue #jos on ei ammuta siihen

            osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka) #funktio joka tarkistaa mitä ammutussa kohdassa on
            if osuttu: #jos kohtaan jo osuttu
                continue
            if osu: #jos osuttiin
                #alustetaan muuttujat upottamista varten
                tiedot.luku = 1
                tiedot.oikealle = True
                tiedot.ylos = True
                tiedot.upottaminen = True
                tiedot.vaaka = False
                tiedot.pysty = False
            else:
                break

        if tiedot.upottaminen: #jos laivan upottaminen kesken
            #piirretään näytölle jutut
            naytto.fill((77,136,255)) #asetetaan taustan väri
            ruudukko(naytto,teksti1,teksti2)
            tulostus(pelaajan_laivat,vihollisen_laivat,naytto) #laivat
            naytto.blit(vuoro_teksti_2, (480, 500)) #piirtää tekstin
            pygame.display.flip() #päivittää näytön
            time.sleep(0.2) #viive
            pelaajan_laivat,upposi = uponnut_tarkistus(pelaajan_laivat, sijainti.pysty, sijainti.vaaka) #tutkii onko laiva uponnut
            if upposi: #jos laiva upposi
                tiedot.upottaminen = False
                continue
            #onko tiedossa missä asennossa laiva on
            if tiedot.vaaka: #vaaka-asennossa
                if tiedot.oikealle: #oikealle
                    if sijainti.vaaka +1 <= 9: #tutkitaan loppuuko kartta
                        sijainti.vaaka += 1
                        if pelaajan_laivat[sijainti.pysty][sijainti.vaaka] == 3: #tarkistetaan onko kohtaan ammuttu ja tyhjä
                            tiedot.oikealle = False #vasemmalle
                        elif pelaajan_laivat[sijainti.pysty][sijainti.vaaka] != 2:
                            osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka) #ammutaan kohtaan
                            if osu == False: #jos ei osuttu
                                tiedot.oikealle = False #vasemmalle
                                break

                    else: #jos kartta loppuu
                        tiedot.oikealle = False #vasemmalle

                if tiedot.oikealle == False: #vasemmalle
                    sijainti.vaaka -= 1
                    if pelaajan_laivat[sijainti.pysty][sijainti.vaaka] != 2:
                        osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka) #ammutaan kohtaan



            ###########################################
            elif tiedot.pysty: #pysty asennossa
                if tiedot.ylos: #ylös
                    if sijainti.pysty -1 >= 0: #tutkitaan loppuuko kartta
                        sijainti.pysty -= 1
                        if pelaajan_laivat[sijainti.pysty][sijainti.vaaka] == 3: #tarkistetaan onko kohtaan ammuttu ja tyhjä
                            tiedot.ylos = False #alas
                        elif pelaajan_laivat[sijainti.pysty][sijainti.vaaka] != 2:
                            osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka)
                            if osu == False: #jos ei osuttu
                                tiedot.ylos = False #alas
                                break
                    else: #jos kartta loppuu
                         tiedot.ylos = False #alas

                if tiedot.ylos == False: #alas
                    sijainti.pysty += 1
                    if pelaajan_laivat[sijainti.pysty][sijainti.vaaka] != 2:
                        osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka) #ammutaan kohtaan



            ###################################################
            #jos ei tutkitaan mitä osutun kohdan ympärillä on
            elif tiedot.luku == 1: #tässä tutkitaan mitä ylhäällä on
                if sijainti.pysty -1 < 0: #jos kartta loppuu
                    tiedot.luku = 2
                elif pelaajan_laivat[sijainti.pysty -1][sijainti.vaaka] == 1 or pelaajan_laivat[sijainti.pysty -1][sijainti.vaaka] == 4: #jos kohdan yläpuolella ampumaton kohta ammutaan siihen
                    osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat, sijainti.pysty -1,sijainti.vaaka) #funktio joka tarkistaa mitä ammutussa kohdassa on
                    if osu: #jos osuttiin
                        tiedot.pysty = True
                    else: #jos ei osuttu
                        tiedot.luku = 2
                        break
                else: #jos kohdan yläpuolella on jo ammuttu
                    tiedot.luku = 2

            elif tiedot.luku == 2: #tässä tutkitaan mitä oikealla on
                if sijainti.vaaka +1 > 9: #jos kartta loppu
                    tiedot.luku = 3
                elif pelaajan_laivat[sijainti.pysty][sijainti.vaaka +1] == 1 or pelaajan_laivat[sijainti.pysty][sijainti.vaaka +1] == 4: #jos kohdan oikealla puolella ampumaton kohta ammutaan siihen
                    osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty,sijainti.vaaka +1,) #funktio joka tarkistaa mitä ammutussa kohdassa on
                    if osu: #jos osuttiin
                        tiedot.vaaka = True
                    else: #jos ei osuttu
                        tiedot.luku = 3
                        break
                else: #jos kohdan oikealle puolelle on jo ammuttu
                    tiedot.luku = 3

            elif tiedot.luku == 3: #tässä tutkitaan mitä alapuolella on
                if sijainti.pysty +1 > 9: #jos kartta loppu
                    tiedot.vaaka = True
                    tiedot.luku = 1
                elif pelaajan_laivat[sijainti.pysty +1][sijainti.vaaka] == 1 or pelaajan_laivat[sijainti.pysty +1][sijainti.vaaka] == 4: #jos kohdan alapuolella ampumaton kohta ammutaan siihen
                    osu,osuttu,pelaajan_laivat = laivat_tarkistus(pelaajan_laivat,sijainti.pysty +1,sijainti.vaaka) #funktio joka tarkistaa mitä ammutussa kohdassa on
                    if osu: #jos osuttiin
                        tiedot.pysty = True
                    else: #jos ei osuttu
                        tiedot.vaaka = True
                        break
                else: #jos kohdan alapuolelle on jo ammuttu
                    tiedot.vaaka = True
    return(pelaajan_laivat)



#tarkistaa onko enää laivoja jäljellä ja jos on palautta False muuten True
def tarkistus(laivat):
    for i in range(len(laivat)):
        for j in range(len(laivat[i])):
            if laivat[i][j] == 4:
                return (False)
    return(True)


#kutsutaan funktiota jossa valitaan omien laivojen sijainnit
pelaajan_laivat,vihollisen_laivat = valinta(naytto)



#esitellään muuttujia
pelaajan_vuoro = True
hiiren_sijainti = [0,0]
klik = False #hiiren klikkausta varten
klik2 = True
numero = 0 #pysty
kirjain = 0 #vaaka
upposi = False
laskuri = 6 #monta laivaa jäljellä

kello = pygame.time.Clock() #kello jolla rajoitetaan pelin nopeutta
#Luodaan tekstejä
fontti = pygame.font.Font("fontti/Roboto-Regular.ttf", 28 ) #ladataan fontti
pelaaja_voitti = fontti.render("Pelaaja voitti", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
Vihollinen_voitti = fontti.render("Vihollinen voitti", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
osuttu_teksti = fontti.render("Tähän jo osuttu!", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
uppotettu_teksti = fontti.render("Laiva upotettu!", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
vuoro_teksti = fontti.render("Pelaajan vuoro", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
vuoro_teksti_2 = fontti.render("Vihollisen vuoro", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva

teksti1 = fontti.render("X = laiva johon osuttu, O = ammuttu kohta", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
teksti2 = fontti.render("pelaajan kartassa L = laiva", True, (0,0,0))
laivat_teksti = fontti.render("Laivoja jäljellä: ", True, (0,0,0))

while True: #pääsilmukka
    naytto.fill((77,136,255)) #asetetaan taustan väri
    ruudukko(naytto,teksti1,teksti2) #piirretään ruudukko
    tulostus(pelaajan_laivat,vihollisen_laivat,naytto) #piirtää laivat
    laivojen_maara = fontti.render(str(laskuri), True, (0,0,0)) #luodaan tekstiä vastaava kuva
    naytto.blit(laivat_teksti, (50, 550)) #piirtää tekstin
    naytto.blit(laivojen_maara, (250, 552)) #piirtää tekstin

    #tapahtumasilmukka
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT: #jos ohjelma suljetaan
            exit() #lopetetaan ohjelma

        if pelaajan_vuoro: #tutkitaan hiiren näppäimen painalluksia
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN: #tutkitaan painettiinko hiiren nappia ikkunan alueella
                klik = True
                hiiren_sijainti = tapahtuma.pos #missä kohtaa hiiren näppäintä painettiin

            if klik:
                if tapahtuma.type == pygame.MOUSEBUTTONUP: #tutkitaan päästettiinkö hiiren nappi ylös ikkunan alueella
                    klik2 = True


    if pelaajan_vuoro: #jos pelaajan vuoro
        naytto.blit(vuoro_teksti, (50, 500)) #piirtää tekstin
        pygame.display.flip() #päivittää näytön

        #painettiinko hiiren näpäintä
        if klik and klik2:
            klik2 = False
            klik = False
            #tutkiaan tapahtuiko klikki ruudukon alueella
            if hiiren_sijainti[0] > 480 and hiiren_sijainti[0] <880 and hiiren_sijainti[1] > 40 and hiiren_sijainti[1] < 440:
                #lasketaan minkä ruudun kohdalla hiirtä painettiin
                numero = (hiiren_sijainti[1] // 40) -1 #pysty
                kirjain = (hiiren_sijainti[0] -480) // 40 #vaaka

                osu, osuttu,vihollisen_laivat = laivat_tarkistus(vihollisen_laivat,numero,kirjain)

                if osuttu: #jos kohtaan jo osuttu
                    naytto.blit(osuttu_teksti, (300, 500)) #piirtää tekstin
                    pygame.display.flip() #päivittää näytön
                    time.sleep(1) #viive
                    continue

                if osu:
                    vihollisen_laivat,upposi = uponnut_tarkistus(vihollisen_laivat,numero,kirjain)
                    if upposi:
                        laskuri -= 1
                        if tarkistus(vihollisen_laivat): #funktio joka tarkistaa onko laivoja jäljellä
                            #piirretään asiat näytölle

                            laivojen_maara = fontti.render(str(laskuri), True, (0,0,0)) #luodaan tekstiä vastaava kuva
                            naytto.fill((77,136,255)) #asetetaan taustan väri
                            ruudukko(naytto,teksti1,teksti2) #piirretään ruudukko
                            naytto.blit(laivat_teksti, (50, 550)) #piirtää tekstin
                            naytto.blit(laivojen_maara, (250, 552)) #piirtää tekstin
                            naytto.blit(pelaaja_voitti, (270, 500)) #piirtää tekstin
                            tulostus(pelaajan_laivat, vihollisen_laivat,naytto) #piirtää laivat
                            pygame.display.flip() #päivittää näytön
                            time.sleep(3) #viive
                            exit()
                        else:
                            naytto.blit(uppotettu_teksti, (300, 500)) #piirtää tekstin
                            pygame.display.flip() #päivittää näytön
                            time.sleep(1) #viive
                            continue

                if osu: #jos osui saa ampua uudestaan
                    pelaajan_vuoro = True
                else:
                    pelaajan_vuoro = False
                    continue

    ###############################################
    #tekoälyn vuoro
    if pelaajan_vuoro == False:
        naytto.blit(vuoro_teksti_2, (480, 500)) #piirtää tekstin
        pygame.display.flip() #päivittää näytön
        #tekoälyn toiminnot
        pelaajan_laivat = tekoaly_ampuminen(pelaajan_laivat,tiedot,sijainti,vuoro_teksti_2,teksti1,teksti2) #funktio joka hoitaa sen mihin tekoäly ampuu
        if tarkistus(pelaajan_laivat):  #funktio joka tarkistaa onko laivoja enää jäljellä
            naytto.blit(Vihollinen_voitti, (270, 500)) #piirtää tekstin
            tulostus(pelaajan_laivat,vihollisen_laivat,naytto) #tulostus
            pygame.display.flip() #päivittää näytön
            time.sleep(3) #viive
            exit()
        else:
            tulostus(pelaajan_laivat,vihollisen_laivat,naytto) #tulostus
            time.sleep(0.2) #viive

        pelaajan_vuoro = True #tekoälyn vuoron jälkeen pelaajan vuoro

    kello.tick(30) #rajoittaa pelin nopeutta vähentäen tietokoneen kuormitusta
