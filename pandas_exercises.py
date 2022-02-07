import pandas as pd

if __name__=="__main__":

    """ #Create an empty pandas Series
    print(pd.Series()) """

    """ #Given the X python list convert it to an Y pandas Series
    X = ['A','B','C']
    print(X, type(X))

    Y = pd.Series(X)
    print(Y, type(Y)) """

    """ #Given the X pandas Series, name it 'My letters'
    X = pd.Series(['A','B','C'])
    X.name = "my letters"
    print(X.name) """

    """ #Given the X pandas Series, show its values
    X = pd.Series(['A','B','C'])
    print(X.values) """

    """ #Assign index names to the given X pandas Series
    X = pd.Series(['A','B','C'])
    index_names = ['first', 'second', 'third']
    X.index = index_names
    print(X) """

    """ #Given the X pandas Series, show its first element
    X = pd.Series(['A','B','C'], index=['first', 'second', 'third'])
    print(X.loc['first'])
    print(X.iloc[0])
    print(X[0]) """

    """ #Given the X pandas Series, show its last element
    X = pd.Series(['A','B','C'], index=['first', 'second', 'third'])

    print(X.loc['third'])
    print(X.iloc[-1])
    print(X[-1]) """

    """ #Given the X pandas Series, show all middle elements    
    X = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])
    
    print(X[1:-1])
    print(X.loc[['second', 'third', 'forth']])
    print(X.iloc[1:-1])  """

    """ #Given the X pandas Series, show the elements in reverse position
    X = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])
    
    print(X[::-1]) """

    """ #Given the X pandas Series, show the first and last elements
    X = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])
    
    print(X[['first','fifth']])
    print(X.iloc[[0,-1]])
    print(X.loc[['first','fifth']]) """

    """ #Convert the given integer pandas Series to float
    X = pd.Series([1,2,3,4,5],
              index=['first','second','third','forth','fifth'])

    print(pd.Series(X, dtype=float)) """

    """ #Reverse the given pandas Series (first element becomes last)
    X = pd.Series([1,2,3,4,5],
              index=['first','second','third','forth','fifth'])

    print(X[::-1]) """

    """ #Order (sort) the given pandas Series
    X = pd.Series([4,2,5,1,3],
              index=['forth','second','fifth','first','third'])

    print(X.sort_values()) """

    """ #Given the X pandas Series, set the fifth element equal to 10
    X = pd.Series([1,2,3,4,5],
              index=['A','B','C','D','E'])
    
    X.iloc[-1] = 10
    print(X) """

    """ #Given the X pandas Series, change all the middle elements to 0
    X = pd.Series([1,2,3,4,5],
              index=['A','B','C','D','E'])
    
    #X[1:-1] = 0
    #X[['B','C','D']] = 0
    X.iloc[1:-1] = 0

    print(X) """

    """ #Given the X pandas Series, add 5 to every element
    X = pd.Series([1,2,3,4,5])
    print(X+5) """

    """ #Given the X pandas Series, make a mask showing negative elements
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])

    print(X[X<0]) """

    """ #Given the X pandas Series, get numbers higher than 5
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])

    print(X[X>5]) """

    """ #Given the X pandas Series, get numbers higher than the elements mean
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])

    print(X[X>X.mean()]) """

    """ #Given the X pandas Series, get numbers equal to 2 or 10
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
    print(X[(X==2) | (X==10)]) """

    """ #Given the X pandas Series, return True if none of its elements is zero
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])

    print(X.all()) """

    """ #Given the X pandas Series, return True if any of its elements is zero
    X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
    print(X.any()) """

    """ #Given the X pandas Series, show the sum of its elements
    X = pd.Series([3,5,6,7,2,3,4,9,4])

    #np.sum(X)
    print(X.sum()) """

    """ #Given the X pandas Series, show the mean value of its elements
    X = pd.Series([1,2,0,4,5,6,0,0,9,10])

    #np.mean(X)
    print(X.mean()) """

    """ #Given the X pandas Series, show the max value of its elements
    X = pd.Series([1,2,0,4,5,6,0,0,9,10])

    #np.max(X)
    print(X.max()) """