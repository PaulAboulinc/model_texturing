import shutil

from pygltflib import *
import main
from PIL import Image


def color_monkey(build_folder):
    screenshot_image = Image.open(build_folder + '/screenshot.jpg')
    width, height = screenshot_image.size
    screenshot_image.crop((0, int(height/8), width, int(height - height/8))).convert('RGB').save(build_folder + '/screenshot_bis.jpg')

    monkey_image = main.get_sub_image(build_folder + '/screenshot_bis.jpg', 'models/monkey/monkey.jpg', 'cv.TM_CCOEFF_NORMED')
    monkey_image.convert('RGB').save(build_folder + "/monkey.jpg")

    head_image = main.get_sub_image(build_folder + '/monkey.jpg', 'models/monkey/head.jpg', 'cv.TM_CCOEFF_NORMED')
    head_image.save(build_folder + "/head.jpg")

    top_head_image = main.get_sub_image(build_folder + '/head.jpg', 'models/monkey/top_head.jpg', 'cv.TM_CCOEFF_NORMED')
    top_head_image.save(build_folder + "/top_head.jpg")

    face_image = main.get_sub_image(build_folder + '/head.jpg', 'models/monkey/face.jpg', 'cv.TM_CCOEFF_NORMED')
    face_image.save(build_folder + "/face.jpg")

    mouth_image = main.get_sub_image(build_folder + '/head.jpg', 'models/monkey/mouth.jpg', 'cv.TM_CCOEFF_NORMED')
    mouth_image.save(build_folder + "/mouth.jpg")

    body_image = main.get_sub_image(build_folder + '/monkey.jpg', 'models/monkey/body.jpg', 'cv.TM_CCOEFF_NORMED')
    body_image.save(build_folder + "/body.jpg")

    body2_image = main.get_sub_image(build_folder + "/body.jpg", 'models/monkey/body2.jpg', 'cv.TM_CCOEFF_NORMED')
    body2_image.save(build_folder + "/body2.jpg")

    gltf = GLTF2().load("models/monkey/monkey.gltf")

    head = main.get_dominant_color(top_head_image)
    face = main.get_dominant_color(face_image)
    mouth = main.get_dominant_color(mouth_image)
    body = main.get_dominant_color(body2_image)

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

    shutil.copyfile("models/monkey/monkey.bin", build_folder + "/monkey.bin")
    gltf.save(build_folder + "/monkey.glb")

    return build_folder + "/monkey.glb"
