from PIL import Image
from get_noice import get_noice

# Image.ROTATE_90


def create_holst():
    frames_w = 4
    size_w = 16*frames_w+16*(frames_w-1)
    frames_w = 5
    size_h = 16*frames_w+16*(frames_w-1)
    holst = Image.new("RGB", size=(size_w, size_h), color=0)
    return holst


def create_frames():
    holst = create_holst()

    noice1 = get_noice()
    noice2 = get_noice()

    mask_half = Image.open("16x16_half.png").convert('L')
    mask_angle = Image.open("16x16_angle.png").convert('L')
    mask_solo = Image.open("16x16_solo.png").convert('L')

    holst.paste(noice1, (0, 0))
    holst.paste(noice2, (32, 0))

    holst.paste(noice2, (64, 0))
    holst.paste(noice1, (64, 0), mask_solo)
    holst.paste(noice1, (96, 0))
    holst.paste(noice2, (96, 0), mask_solo)

    weight = 0
    height = 32

    for i in range(4):
        holst.paste(noice1, (weight, height))
        holst.paste(noice2, (weight, height), mask_half)
        mask_half = mask_half.rotate(90)
        weight += 32
    height += 32
    weight = 0

    for i in range(4):
        holst.paste(noice1, (weight, height))
        holst.paste(noice2, (weight, height), mask_angle)
        mask_angle = mask_angle.rotate(90)
        weight += 32
    height += 32
    weight = 0

    for i in range(4):
        holst.paste(noice2, (weight, height))
        holst.paste(noice1, (weight, height), mask_half)
        mask_half = mask_half.rotate(90)
        weight += 32
    height += 32
    weight = 0

    for i in range(4):
        holst.paste(noice2, (weight, height))
        holst.paste(noice1, (weight, height), mask_angle)
        mask_angle = mask_angle.rotate(90)
        weight += 32
    height += 32

    holst.show()


create_frames()
