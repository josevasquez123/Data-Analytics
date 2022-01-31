import pandas as pd
import numpy as np

#Los series tienen index, ademas estos se pueden cambiar
#Series tiene sus datos ordenados de forma ascendente o alfabetica
#Cuando usas el [:] para obtener data de un lugar a otro, en pandas agarra hasta el extremo que le dices, en una list
#normal agarra hasta una posición anterior al limite
#Tambien se puede realizar operaciones booleanas 
#Se puede  modificar la data de pandas series 

if __name__ == "__main__":
    seriesData = pd.Series([35,25,45,25])
    seriesData.index = ['Peru', 'Canada', 'Bolivia', 'UK']              #Cambio de index
    print(seriesData)
    print(seriesData.dtype)
    print(seriesData[0])

    #Con el index, se puede llamar la data mediante su nombre
    print("Population of UK: " + str(seriesData['UK']))

    #Operaciones booleanas
    print(seriesData[seriesData>25])

    #Modificaciones
    seriesData[0] = 120
    print(seriesData)