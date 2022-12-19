import pygame

def tulostus(pelaajan_laivat,vihollisen_laivat,naytto):
    '''
    Pygamea käyttävä funktio
    käytetään erillisenä tiedostona

    saa parametrinä listan jossa laivojen tiedot sekä "naytto" jota pygame käyttää ja jonne asiat piirretään
    ympyrä vaihdettu "O" kirjaimeen
    
    Piirtää laivat
    1 = ei mitään
    2 = laiva johon osuttu eli X
    3 = tyhjä osuttu kohta eli O
    4 = laiva jota ei näy eli pelaajan kartassa L
    5 = Väliaikainen käytetään laivan sijainnin valitsemiseen
    6 = X uponnut laiva joka piirretään punaisena
    '''
    fontti = pygame.font.Font("fontti/Roboto-Regular.ttf", 32) #ladataan fontti
    fontti2 = pygame.font.Font("fontti/Roboto-Regular.ttf", 45) #ladataan fontti, hieman isompi
    l_kirjain = fontti.render("L", True, (255,255,255)) #luodaan tekstiä vastaava kuva
    x_kirjain = fontti.render("X", True, (255,255,255)) #luodaan tekstiä vastaava kuva
    x_kirjain_2 = fontti.render("X", True, (255,0,0)) #luodaan tekstiä vastaava kuva    puaninen
    o_kirjain = fontti2.render("O", True, (255,255,255)) #luodaan tekstiä vastaava kuva
    
    #kirjainten sijainnit y,x
    sijainti_2 = [0,0] 
    sijainti_3 = [0,0] 
    sijainti_4 = [0,0] 
    
    #piirretään pelaajan laivat
    for i in range(10):
        for j in range(10):
            if pelaajan_laivat[i][j] == 2:
                sijainti_2[1] = (i +1) * 40 #pysty
                sijainti_2[0] = (j +1) * 40 + 10 #vaaka
                naytto.blit(x_kirjain, sijainti_2) #piirtää kirjaimen
                
            if pelaajan_laivat[i][j] == 3:
                sijainti_3[1] = (i +1) * 40 - 6 #pysty
                sijainti_3[0] = (j +1) * 40 + 5 #vaaka
                naytto.blit(o_kirjain, sijainti_3) #piirtää kirjaimen  
                
            if pelaajan_laivat[i][j] == 4 or pelaajan_laivat[i][j] == 5:
                sijainti_4[1] = (i +1) * 40 + 2  #pysty
                sijainti_4[0] = (j +1) * 40 + 13 #vaaka
                naytto.blit(l_kirjain, sijainti_4) #piirtää kirjaimen

            if pelaajan_laivat[i][j] == 6:
                sijainti_3[1] = (i +1) * 40 #pysty
                sijainti_3[0] = (j +1) * 40 + 10 #vaaka
                naytto.blit(x_kirjain_2, sijainti_3) #piirtää kirjaimen 
            
    
    #piirretään tekoälyn laivat
    for i in range(10):
        for j in range(10):
            if vihollisen_laivat[i][j] == 2:
                sijainti_2[1] = (i +1) * 40 + 2 #pysty
                sijainti_2[0] = (j +1) * 40 + 450 #vaaka
                naytto.blit(x_kirjain, (sijainti_2)) #piirtää kirjaimen
                
            if vihollisen_laivat[i][j] == 3:
                sijainti_3[1] = (i +1) * 40 - 6 #pysty
                sijainti_3[0] = (j +1) * 40 + 445 #vaaka
                naytto.blit(o_kirjain, sijainti_3) #piirtää kirjaimen

            if vihollisen_laivat[i][j] == 6:
                sijainti_3[1] = (i +1) * 40 + 2 #pysty
                sijainti_3[0] = (j +1) * 40 + 450 #vaaka
                naytto.blit(x_kirjain_2, sijainti_3) #piirtää kirjaimen 



def ruudukko(naytto,teksti1,teksti2):
    '''
    Pygamea hyödyntävä funktio joka piirtää ruudukon
    ja tekstit 
    Saa parametrinä tekstit
    '''
    
    fontti = pygame.font.Font("fontti/Roboto-Regular.ttf", 28) #ladataan fontti
    kirjaimet = ["a","b","c","d","e","f","g","h","i","j"] 
    karttateksti1 = fontti.render("Pelaajan laivat", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
    karttateksti2 = fontti.render("Vihollisen laivat", True, (0, 0, 0))  #luodaan tekstiä vastaava kuva
    laatikko = 40 #laatikon koko
    for x in range(40, 440, laatikko): #mistä mihin ruudukko pirretään levyssuunnassa
        for y in range(40, 440, laatikko): #pystysuunnassa
            rect = pygame.Rect(x, y, laatikko, laatikko)
            pygame.draw.rect(naytto, (255,255,255), rect, 1)
            
    #piirretään toinen ruudukko
    for x in range(480, 880, laatikko): #mistä mihin ruudukko pirretään levyssuunnassa
        for y in range(40, 440, laatikko): #pystysuunnassa
            rect = pygame.Rect(x, y, laatikko, laatikko)
            pygame.draw.rect(naytto, (255,255,255), rect, 1)
            
    #########################
    #piirtää kordinaatiston
    
    for i in range(1,11): #piirtää numerot
        numero = fontti.render(str(i), True, (0,0,0)) #luodaan tekstiä vastaaava kuva
        kirjain = fontti.render((kirjaimet[i -1]), True, (0,0,0)) #luodaan tekstiä vastaaava kuva
        naytto.blit(numero, (5, i * 40)) #piirtää numerot
        naytto.blit(kirjain, (i * 40 + 5, 0)) #piirtää kirjaimet
        
    #piirretään toisenkin ruudunkon ympärille kirjaimet ja numerot  
    for i in range(1,11): #piirtää numerot
        kirjain = fontti.render((kirjaimet[i -1]), True, (0,0,0)) #luodaan tekstiä vastaaava kuva
        numero = fontti.render(str(i), True, (0,0,0)) #luodaan tekstiä vastaaava kuva
        naytto.blit(numero, (445, i * 40)) #piirtää numerot
        naytto.blit(kirjain, (i * 40 + 445, 0)) #piirtää kirjaimet
    #piirtää tekstit
    naytto.blit(karttateksti1, (50, 450)) 
    naytto.blit(karttateksti2, (480, 450)) 
    naytto.blit(teksti1, (10, 600)) 
    naytto.blit(teksti2, (10, 640)) 
 