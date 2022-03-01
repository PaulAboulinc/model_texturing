import os
import shutil

from pygltflib import *
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


def color_monkey():
    build_path = 'build'
    if os.path.exists(build_path) and os.path.isdir(build_path):
        shutil.rmtree(build_path)

    os.mkdir(build_path)

    monkey_image = get_sub_image('screenshot.jpg', 'models/monkey.jpg', 'cv.TM_CCOEFF_NORMED')
    monkey_image.save("build/monkey.jpg")

    head_image = get_sub_image('build/monkey.jpg', 'models/head.jpg', 'cv.TM_CCOEFF_NORMED')
    head_image.save("build/head.jpg")

    top_head_image = get_sub_image('build/head.jpg', 'models/top_head.jpg', 'cv.TM_CCOEFF_NORMED')
    top_head_image.save("build/top_head.jpg")

    face_image = get_sub_image('build/head.jpg', 'models/face.jpg', 'cv.TM_CCOEFF_NORMED')
    face_image.save("build/face.jpg")

    mouth_image = get_sub_image('build/head.jpg', 'models/mouth.jpg', 'cv.TM_CCOEFF_NORMED')
    mouth_image.save("build/mouth.jpg")

    body_image = get_sub_image('build/monkey.jpg', 'models/body.jpg', 'cv.TM_CCOEFF_NORMED')
    body_image.save("build/body.jpg")

    gltf = GLTF2().load("models/monkey.gltf")

    head = get_dominant_color(top_head_image)
    face = get_dominant_color(face_image)
    mouth = get_dominant_color(mouth_image)
    body = get_dominant_color(body_image)

    black = [0.0, 0.0, 0.0, 1.0]
    gltf.materials[8].pbrMetallicRoughness.baseColorFactor = black  # eye
    gltf.materials[9].pbrMetallicRoughness.baseColorFactor = black  # eye
    gltf.materials[11].pbrMetallicRoughness.baseColorFactor = black  # mouth

    gltf.materials[5].pbrMetallicRoughness.baseColorFactor = head  # head
    gltf.materials[13].pbrMetallicRoughness.baseColorFactor = head  # left ear
    gltf.materials[14].pbrMetallicRoughness.baseColorFactor = head  # right ear

    gltf.materials[6].pbrMetallicRoughness.baseColorFactor = face  # face

    gltf.materials[7].pbrMetallicRoughness.baseColorFactor = mouth  # mouth surface
    gltf.materials[10].pbrMetallicRoughness.baseColorFactor = mouth  # nose

    gltf.materials[1].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[2].pbrMetallicRoughness.baseColorFactor = body  # right arm
    gltf.materials[0].pbrMetallicRoughness.baseColorFactor = body  # left arm
    gltf.materials[3].pbrMetallicRoughness.baseColorFactor = body  # right leg
    gltf.materials[4].pbrMetallicRoughness.baseColorFactor = body  # left leg
    gltf.materials[12].pbrMetallicRoughness.baseColorFactor = body  # tail

    gltf.save("build/monkey.gltf")


color_monkey()
