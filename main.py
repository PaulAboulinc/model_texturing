import cv2 as cv
from PIL import Image


def get_dominant_color(pil_img):
    img_copy = pil_img.copy()
    img_copy.convert("RGB")
    img_copy = img_copy.resize((1, 1), resample=0)
    rgb = img_copy.getpixel((0, 0))

    return [
        pow(float(rgb[0]) / 255, 2.2),
        pow(float(rgb[1]) / 255, 2.2),
        pow(float(rgb[2]) / 255, 2.2),
        1.0
    ]


def get_sub_image(image, sub_image, meth):
    img = cv.imread(image, 0)
    img2 = img.copy()
    template = cv.imread(sub_image, 0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    # meth = 'cv.TM_CCOEFF_NORMED'

    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    top = top_left[1]
    left = top_left[0]
    bottom = top + h
    right = left + w

    img = Image.open(image)

    return img.crop((left, top, right, bottom))
