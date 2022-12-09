def laivat_tarkistus(laivat,numero,kirjain): 
    #funktio joka tutkii mihin osuttiin ja palauttaa kartan
    #numero = pysty kirjain = vaaka
    #ottaa huomioon myös 6

    osu = False
    osuttu = False
    
    if laivat[numero][kirjain] == 1:  #jos kohdassa ei mitään
        laivat[numero][kirjain] = 3  #merkitään kohta ammutuksi
    elif laivat[numero][kirjain] == 2: #jos kohtaan jo ammuttu
        osuttu = True
    elif laivat[numero][kirjain] == 3: #jos kohtaan jo ammuttu
        osuttu = True
    elif laivat[numero][kirjain] == 4:  #jos kohdassa on vihollisen laiva
        laivat[numero][kirjain] = 2  #merkitään näkyväksi
        osu = True
    elif laivat[numero][kirjain] == 6: #jos upotettu laiva
        osuttu = True
    return(osu,osuttu,laivat)