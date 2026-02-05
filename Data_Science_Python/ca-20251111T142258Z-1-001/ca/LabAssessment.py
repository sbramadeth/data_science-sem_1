import matplotlib.pyplot as plt

class DimensionError(Exception):
    pass

def print3d(randomWalk:dict):
    """
    Function to create a 3d representation of the 3d Random walk.
    
    Args:
        randomWalk: A dictionary containing the coordinates for the
        dimensions X, Y and Z.

    Raises:
        TypeError: If the input is not a dictionary.
        
    """
    if isinstance(randomWalk, dict)==False:
        raise TypeError("The expected input is a dictionary")
    elif isinstance(randomWalk, dict) ==True and len(randomWalk) >3:
        raise DimensionError("We are working with only 3 dimensions")
    else:
        fig = plt.figure()
        ax = plt.axes(projection='3d')

    
        x = randomWalk["X"]
        y = randomWalk["Y"]
        z = randomWalk["Z"]

        ax.plot3D(x, y, z)
        ax.plot3D(x[0], y[0], z[0], marker='o',
                  markerfacecolor='r', label="Start")
        ax.plot3D(x[-1], y[-1], z[-1], marker='o',
                  markerfacecolor='purple', label="Finish")
        ax.legend(loc="best")
        ax.set_title('3D Scatter Plot')
        plt.show()