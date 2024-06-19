# Importing necessary libraries 
from rembg import remove
from PIL import Image

# Open the image file
image = Image.open("path/to/your/image")

# Remove the background
output = remove(image)

# Save the output image as PNG
output.save("Output.png")
