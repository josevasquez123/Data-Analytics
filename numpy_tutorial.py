import numpy as np

#TRABAJA IGUAL QUE PYTHON LIST

if __name__== "__main__":
    a = np.array([[1,2,3,4], [2,4,3,6]])
    b = np.arange(5)
    b += 100
    print(a[-1][0:2])
    print(a[0,2])
    print(b)
    print(b[b>=101])                        #Se puede hacer comparaciones dentro de los arrays para filtrar mas rapido los datos

    