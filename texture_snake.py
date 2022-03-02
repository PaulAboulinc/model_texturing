import shutil

from pygltflib import *
import main
from PIL import Image


def color_snake(build_folder):
    screenshot_image = Image.open(build_folder + '/screenshot.jpg')
    width, height = screenshot_image.size
    screenshot_image.crop((0, int(height/8), width, int(height - height/8))).convert('RGB').save(build_folder + '/screenshot_bis.jpg')

    snake_image = main.get_sub_image(build_folder + '/screenshot_bis.jpg', 'models/snake/snake.jpg', 'cv.TM_CCOEFF_NORMED')
    snake_image.convert('RGB').save(build_folder + "/snake.jpg")

    head_image = main.get_sub_image(build_folder + '/snake.jpg', 'models/snake/head.jpg', 'cv.TM_CCOEFF_NORMED')
    head_image.save(build_folder + "/head.jpg")

    top_head_image = main.get_sub_image(build_folder + '/head.jpg', 'models/snake/top_head.jpg', 'cv.TM_CCOEFF_NORMED')
    top_head_image.save(build_folder + "/top_head.jpg")

    bottom_head = main.get_sub_image(build_folder + '/head.jpg', 'models/snake/bottom_head.jpg', 'cv.TM_CCOEFF_NORMED')
    bottom_head.save(build_folder + "/bottom_head.jpg")

    body_image = main.get_sub_image(build_folder + '/snake.jpg', 'models/snake/body.jpg', 'cv.TM_CCOEFF_NORMED')
    body_image.save(build_folder + "/body.jpg")

    gltf = GLTF2().load("models/snake/snake.gltf")

    top_head = main.get_dominant_color(top_head_image)
    bottom_head = main.get_dominant_color(bottom_head)
    body = main.get_dominant_color(body_image)
    #
    black = [0.0, 0.0, 0.0, 1.0]
    gltf.materials[4].pbrMetallicRoughness.baseColorFactor = black  # right eye
    gltf.materials[5].pbrMetallicRoughness.baseColorFactor = black  # left eye

    gltf.materials[1].pbrMetallicRoughness.baseColorFactor = top_head  # top head
    gltf.materials[3].pbrMetallicRoughness.baseColorFactor = top_head  # very top head

    gltf.materials[2].pbrMetallicRoughness.baseColorFactor = bottom_head  # bottom head
    gltf.materials[0].pbrMetallicRoughness.baseColorFactor = bottom_head  # right nose
    gltf.materials[6].pbrMetallicRoughness.baseColorFactor = bottom_head  # left nose
    gltf.materials[7].pbrMetallicRoughness.baseColorFactor = bottom_head  # tongue

    gltf.materials[8].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[9].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[10].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[11].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[12].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[13].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[14].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[15].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[16].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[17].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[18].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[19].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[20].pbrMetallicRoughness.baseColorFactor = body  # body

    shutil.copyfile("models/snake/snake.bin", build_folder + "/snake.bin")
    gltf.save(build_folder + "/snake.glb")

    return build_folder + "/snake.glb"
