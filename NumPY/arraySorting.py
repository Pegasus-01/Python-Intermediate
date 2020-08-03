import numpy as np


np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

light = bmi<21             #light = lightweight basketball players


print(light)

print(bmi[light])