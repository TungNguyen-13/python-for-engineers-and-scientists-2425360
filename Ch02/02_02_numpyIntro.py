import numpy as np
import matplotlib.pyplot as pp

# Load a simple image to generate the array
array = np.load("image.npy")

# Check some parameters of the array
print(type(array))  # Variable type

print(array.ndim)   # Dimension

print(array.shape)  # Shape

print(array.dtype)  # Array tyep

# Size, i.e. the muptiplication of the three dimension
print(array.size, 599 * 402 * 3)

pp.imshow(array)    # Plot the array

# Access a single index of array and change its value
print(array[100, 200, 0])

array[100, 200, 0] = 225

print(array[100, 200, 0])

print(array[10, 0])

# Access a subsec of the array using slicing
# Note that the subsec of the array creating using slicing will still refer
# or point too the original array.  Therefore, any changes to the subsec will
# also affect the original array.
subarray = array[0:150, 75:275, :]

pp.imshow(subarray)

subarray[80:100, :, :] = 0

pp.imshow(subarray)

pp.imshow(array)

# Slicing of the array can be done with a step
downscaled = array[0:599:20, 0:402:20, :]

pp.imshow(downscaled)

print(array.strides)

print(downscaled.strides)

# Simple statistical operation such as mean can be performed on the array
grayscale = np.mean(array, axis=2)

pp.imshow(grayscale, cmap='gray')

# Indexing elements on the array can be done using boolean
grayscale[grayscale < 100] = 0

grayscale[grayscale > 0] = 255

pp.imshow(grayscale, cmap='gray')

# Array can also be reshape, using reshape method
print(downscaled.shape)

reshaped = downscaled.reshape((30 // 2, 21 * 2, 3))

pp.imshow(reshaped)

pp.show()
