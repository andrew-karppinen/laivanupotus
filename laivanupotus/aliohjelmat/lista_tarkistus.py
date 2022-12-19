def lista_tarkistus(laivat,pysty,vaaka,muuttuja = 1):
    '''
    Tarkistaa onko kaksiulotteisessa listassa parametreinä annetussa
    kohdassa tai sen sivuilla (mutta ei kulmissa) mikä tahansa muu luku kuin snnettu muuttuja (tai oletuksena 1)
    jos on paluttaa False
    muuten True
    '''

    if laivat[pysty][vaaka] != 1:
        return(False)

    for i in range(4):
        if i == 0:
            if pysty -1 < 0:#ylös
                continue
            tarkistus_pysty = pysty - 1
            tarkistus_vaaka = vaaka

        elif i == 1: #vasemmalle
            if vaaka -1 < 0:
                continue
            tarkistus_vaaka = vaaka -1
            tarkistus_pysty = pysty

        elif i == 2: #alas
            if pysty +1 > 9:
                continue
            tarkistus_pysty = pysty +1
            tarkistus_vaaka = vaaka

        elif i == 3: #oikealle
            if vaaka +1 > 9:
                continue
            tarkistus_vaaka = vaaka +1
            tarkistus_pysty = pysty
        if laivat[tarkistus_pysty][tarkistus_vaaka] != muuttuja:
            return(False)

    return(True) #jos laivoja ei ollu