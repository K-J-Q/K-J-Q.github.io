# Import the libraries
from PIL import Image
import sys
import glob

# Check if there are enough arguments
if len(sys.argv) == 0:
    print("Usage: python script.py pattern1 pattern2 ...")
    exit()

# Create an empty list to store image filenames
image_names = []

# Loop through the command-line arguments
for arg in sys.argv[1:]:
    # Use glob to find all the files that match the pattern
    matches = glob.glob(arg + "*")

    # Check if there are any matches
    if len(matches) == 0:
        # Print a warning message and skip the argument
        print("No images found for pattern:", arg)
    else:
        # Add the matches to the list
        image_names.extend(matches)

# Check if there are any images found
if len(image_names) == 0:
    print("No images found")
    exit()

# Open all the images and store them in a list
images = [Image.open(image_name) for image_name in image_names]

# Get the size of the first image
image_width, image_height = images[0].size

# Loop through the images and resize them if necessary
for i in range(len(images)):
    if images[i].size != (image_width, image_height):
        images[i] = images[i].resize((image_width, image_height))

# Get the size of the images
image_width, image_height = images[0].size

# Define the maximum number of pictures per row in the collage
max_images_per_row = 4

# Calculate the number of pictures per row based on the number of images
if len(images) % 2 == 0:
    images_per_row = len(images) // 2
else:
    images_per_row = min(len(images), max_images_per_row)

# Calculate the number of rows required for the collage
num_rows = (len(image_names) - 1) // images_per_row + 1

# Calculate the size of the collage
collage_width = image_width * images_per_row
collage_height = image_height * num_rows

# Create a new image for the collage
collage = Image.new("RGBA", (collage_width, collage_height), (0, 0, 0, 0))

# Loop through the images and paste them onto the collage
for i in range(len(images)):
    x = (i % images_per_row) * image_width
    y = (i // images_per_row) * image_height
    collage.paste(images[i], (x, y))

# Save the collage as output.png
collage.save("output.png")
