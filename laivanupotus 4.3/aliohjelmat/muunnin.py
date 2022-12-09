def muunnin(laivat):
    #funktio joka muuttaa 5 --> 4
    #ja 7 --> 2
    for i in range(10):
        for j in range(10):
            if laivat[i][j] == 5:
                laivat[i][j] = 4
            elif laivat[i][j] == 7:
                laivat[i][j] = 2
    return(laivat)