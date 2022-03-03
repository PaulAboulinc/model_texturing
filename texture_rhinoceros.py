import shutil

from pygltflib import *
import main
from PIL import Image


def color_rhinoceros(build_folder):
    screenshot_image = Image.open(build_folder + '/screenshot.jpg')
    width, height = screenshot_image.size
    screenshot_image.crop((0, int(height/8), width, int(height - height/8))).convert('RGB').save(build_folder + '/screenshot_bis.jpg')

    rhinoceros_image = main.get_sub_image(build_folder + '/screenshot_bis.jpg', 'models/rhinoceros/rhinoceros.jpg', 'cv.TM_CCOEFF_NORMED')
    rhinoceros_image.convert('RGB').save(build_folder + "/rhinoceros.jpg")

    head1_image = main.get_sub_image(build_folder + '/rhinoceros.jpg', 'models/rhinoceros/head1.jpg', 'cv.TM_CCOEFF_NORMED')
    head1_image.save(build_folder + "/head1.jpg")

    head2_image = main.get_sub_image(build_folder + '/head1.jpg', 'models/rhinoceros/head2.jpg', 'cv.TM_CCOEFF_NORMED')
    head2_image.save(build_folder + "/head2.jpg")

    head3_image = main.get_sub_image(build_folder + '/head2.jpg', 'models/rhinoceros/head3.jpg', 'cv.TM_CCOEFF_NORMED')
    head3_image.save(build_folder + "/head3.jpg")

    horn1_image = main.get_sub_image(build_folder + '/head2.jpg', 'models/rhinoceros/horn1.jpg', 'cv.TM_CCOEFF_NORMED')
    horn1_image.save(build_folder + "/horn1.jpg")

    horn2_image = main.get_sub_image(build_folder + '/horn1.jpg', 'models/rhinoceros/horn2.jpg', 'cv.TM_CCOEFF_NORMED')
    horn2_image.save(build_folder + "/horn2.jpg")

    body_image1 = main.get_sub_image(build_folder + '/rhinoceros.jpg', 'models/rhinoceros/body1.jpg', 'cv.TM_CCOEFF_NORMED')
    body_image1.save(build_folder + "/body1.jpg")

    body_image2 = main.get_sub_image(build_folder + '/body1.jpg', 'models/rhinoceros/body2.jpg', 'cv.TM_CCOEFF_NORMED')
    body_image2.save(build_folder + "/body2.jpg")

    gltf = GLTF2().load("models/rhinoceros/rhinoceros.gltf")

    head = main.get_dominant_color(head3_image)
    horn = main.get_dominant_color(horn2_image)
    body = main.get_dominant_color(body_image2)

    black = [0.0, 0.0, 0.0, 1.0]
    gltf.materials[8].pbrMetallicRoughness.baseColorFactor = black  # eyes

    gltf.materials[0].pbrMetallicRoughness.baseColorFactor = horn  # horn

    gltf.materials[1].pbrMetallicRoughness.baseColorFactor = head  # head
    gltf.materials[4].pbrMetallicRoughness.baseColorFactor = head  # nose
    gltf.materials[7].pbrMetallicRoughness.baseColorFactor = head  # left ear
    gltf.materials[3].pbrMetallicRoughness.baseColorFactor = head  # right ear

    gltf.materials[2].pbrMetallicRoughness.baseColorFactor = body  # tail
    gltf.materials[5].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[6].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[9].pbrMetallicRoughness.baseColorFactor = body  # body
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
    gltf.materials[21].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[22].pbrMetallicRoughness.baseColorFactor = body  # body
    gltf.materials[23].pbrMetallicRoughness.baseColorFactor = body  # body

    shutil.copyfile("models/rhinoceros/rhinoceros.bin", build_folder + "/rhinoceros.bin")
    gltf.save(build_folder + "/rhinoceros.glb")

    return build_folder + "/rhinoceros.glb"
