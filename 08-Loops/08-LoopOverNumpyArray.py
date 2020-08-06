# Import numpy as np
import numpy as np

# For loop over np_height
for key in np_height:
    print(str(key)+" inches")

# For loop over np_baseball
for element in np.nditer(np_baseball):
    print(str(element))