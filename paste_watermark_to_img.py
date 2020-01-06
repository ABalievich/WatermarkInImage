from PIL import Image


def paste_watermarks(path_img_bg, path_watermark_2=None):
    img_bg = Image.open(path_img_bg)
    img_bg_width, img_bg_height = img_bg.size

    watermark_1 = Image.open('watermark_1.png')
    img_bg.paste(watermark_1, (18, 18), watermark_1)

    if path_watermark_2:
        watermark_2 = Image.open(path_watermark_2)
        watermark_2_width, watermark_2_height = watermark_2.size

        if img_bg_width > img_bg_height:
            watermark_2_width_new = int(img_bg_width * 8 / 100)
            scaling_factor = watermark_2_width_new / watermark_2_width
            watermark_2_height_new = int(watermark_2_height * scaling_factor)
        else:
            watermark_2_width_new = int(img_bg_height * 8 / 100)
            scaling_factor = watermark_2_width_new / watermark_2_width
            watermark_2_height_new = int(watermark_2_height * scaling_factor)

        watermark_2_resize = watermark_2.resize(
            (watermark_2_width_new, watermark_2_height_new),
            Image.LANCZOS)

        box_width = img_bg_width - watermark_2_width_new - 18
        box_height = img_bg_height - watermark_2_height_new - 18

        img_bg.paste(watermark_2_resize, (box_width, box_height), watermark_2_resize)

    img_bg.save('img_bg_out.jpg')


paste_watermarks('img_bg.jpg', 'watermark_2.png')
