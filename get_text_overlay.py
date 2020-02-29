# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure"
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
#
# Note that you don't need to extract the text, the output is an image with only
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np


def getTextOverlay(input_image):
    # Write your code here for output

    img_in_copy = input_image.copy()
    lower_black_threshold = np.array((20, 20, 20))
    upper_black_threshold = np.array((255, 255, 255))
    #
    mask = cv2.inRange(img_in_copy, lower_black_threshold, upper_black_threshold)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
    output = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    output_rgb = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    return output_rgb


if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpsons_text.png', output)

#####################
