import numpy as np

if __name__=="__main__":
    
    '''
    #Create a numpy array of size 10, filled with zeros
    print(np.zeros(10))
    '''

    '''
    #Create a numpy array with values ranging from 10 to 49
    print(np.arange(10,50))
    '''

    '''
    #Create a numpy matrix of 2x2 integers filled with ones
    print(np.ones([2,2]))
    '''

    '''
    #Create a numpy matrix 3x2 float numbers, filled with ones
    print(np.ones([3,2],dtype=np.float))
    '''

    '''
    #Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
    X = np.arange(4, dtype=np.int)
    print(np.ones_like(X))
    '''

    '''
    #Create a numpy matrix of 4*4 integers, filled with fives.
    print(np.ones([4,4],dtype=np.integer)*5)
    '''

    '''
    #Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens
    X = np.array([[2,3], [6,2]], dtype=np.int)
    print(np.ones_like(X)*7)
    '''

    '''
    #Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
    print(np.identity(3))
    '''

    '''
    #Create a numpy array, filled with 3 random integer values between 1 and 10.
    print(np.random.randint(10, size=3))
    '''

    '''
    #Create a 3*3*3 numpy matrix, filled with random float values.
    print(np.random.rand(3,3,3))
    '''

    '''
    #Given the X python list convert it to an Y numpy array
    X = [1, 2, 3]
    print(type(np.array(X)))
    '''

    '''
    #Given the X numpy array, make a copy and store it on Y.
    X = np.array([5,2,3], dtype=np.int)
    print(id(X))
    Y = np.copy(X)
    print(id(Y))
    '''

    '''
    #Create a numpy array with numbers from 1 to 10
    print(np.arange(1,11))
    '''

    '''
    #Create a numpy array with the odd numbers between 1 to 10
    print(np.arange(1,11,2))
    '''

    '''
    #Create a numpy array with numbers from 1 to 10, in descending order.
    print(np.arange(1,11)[::-1])
    '''

    '''
    #Create a 3*3 numpy matrix, filled with values ranging from 0 to 8
    print(np.arange(9).reshape(3,3))
    '''

    '''
    #Show the memory size of the given Z numpy matrix
    Z = np.zeros((10,10))
    print("%d bytes" % (Z.size * Z.itemsize))
    '''

    '''
    #Given the X numpy array, show it's first element
    X = np.array(['A','B','C','D','E'])
    print(X[0])
    '''

    '''
    #Given the X numpy array, show it's last element
    X = np.array(['A','B','C','D','E'])
    print(X[-1])
    '''

    '''
    #Given the X numpy array, show it's first three elements
    X = np.array(['A','B','C','D','E'])
    print(X[:3])
    '''

    '''
    #Given the X numpy array, show all middle elements
    X = np.array(['A','B','C','D','E'])
    print(X[1:-1])
    '''

    '''
    #Given the X numpy array, show the elements in reverse position
    X = np.array(['A','B','C','D','E'])
    print(X[::-1])
    '''

    '''
    #Given the X numpy array, show the elements in an odd position
    X = np.array(['A','B','C','D','E'])
    print(X[::2])
    #X[[0, 2, -1]]
    '''

    '''
    #Given the X numpy matrix, show the first row elements
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[0])
    '''

    '''
    #Given the X numpy matrix, show the last row elements
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[-1])
    '''

    '''
    #Given the X numpy matrix, show the first element on first row
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[0][0])
    '''

    '''
    #Given the X numpy matrix, show the last element on last row
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[-1][-1])
    '''

    '''
    #Given the X numpy matrix, show the middle row elements
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[1:-1, 1:-1])
    '''

    '''
    #Given the X numpy matrix, show the first two elements on the first two rows
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[:2,:2])
    '''

    '''
    #Given the X numpy matrix, show the last two elements on the last two rows
    X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ])

    print(X[-2:,-2:])
    '''

    '''
    #Convert the given integer numpy array to float
    X = [-5, -3, 0, 10, 40]
    print(np.array(X,dtype=float))
    '''

    #Reverse the given numpy array (first element becomes last)
    X = [-5, -3, 0, 10, 40]