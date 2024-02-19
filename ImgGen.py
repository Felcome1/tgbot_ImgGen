from PIL import Image, ImageDraw, ImageFont


WHITE = (255, 255, 255)
GREY = (232, 239, 247)
DARK_GREY = (131, 138, 148)


def font(font, size):
    """Fonts: Arial, DIN2014-Bold, DIN2014-Regular, DIN2014-DemiBold, SFCartoonistHand"""
    return ImageFont.truetype(f'fonts/{font}.ttf', size=size)


def generate(*args):
    r_img1 = Image.open('templates/img1.jpg')
    r_img2 = Image.open('templates/img2.jpg')

    comp_draw = ImageDraw.Draw(r_img1)
    x = (r_img1.width - comp_draw.textlength(args[1], font('DIN2014-Bold', 40))) // 2
    comp_draw.text((44, 23), args[0], font=font('Arial', 23), fill=WHITE)
    comp_draw.text((x, 170), args[1], font=font('DIN2014-Bold', 40), fill=WHITE)
    comp_draw.text((r_img1.width / 2, 253), f'{args[1]}', font=font('DIN2014-DemiBold', 20), fill=DARK_GREY, anchor='ma')
    comp_draw.text((547, 380), f'{args[2]}', font=font('DIN2014-DemiBold', 20), fill=GREY, anchor='ra')
    comp_draw.text((547, 429), f'{args[3]}', font=font('DIN2014-DemiBold', 20), fill=GREY, anchor='ra')
    comp_draw.text((547, 478), args[1], font=font('DIN2014-DemiBold', 20), fill=GREY, anchor='ra')
    comp_draw.text((516, 551), args[4], font=font('DIN2014-DemiBold', 20), fill=DARK_GREY, anchor='ra')
    comp_draw.text((547, 600), args[5], font=font('DIN2014-DemiBold', 20), fill=DARK_GREY, anchor='ra')
    comp_draw.text((519, 651), args[6], font=font('DIN2014-Regular', size=20), fill=GREY, anchor='ra')
    comp_draw.line([(521, 668), (519 - comp_draw.textlength(args[6], font('DIN2014-Regular', size=20)), 668)], fill=GREY, width=1)
    comp_draw.text((554, 796), args[7], font=font('DIN2014-Regular', size=20), fill=GREY, anchor='ra')

    ord_draw = ImageDraw.Draw(r_img2)
    ord_draw.text((20, 15), args[0], font=font('SFCartoonistHand', 20), fill=GREY)
    ord_draw.text((r_img2.width / 2, 149), args[1], font=font('DIN2014-Bold', 40), fill=WHITE, anchor='ma')
    ord_draw.text((r_img2.width / 2, 244), f'{args[1]}', font=font('DIN2014-Regular', 18), fill=DARK_GREY, anchor='ma')
    ord_draw.text((531, 387), f'{args[2]}', font=font('DIN2014-DemiBold', 30), fill=GREY, anchor='ra')
    ord_draw.text((530, 452), f'{args[3]}', font=font('DIN2014-DemiBold', 20), fill=GREY, anchor='ra')
    ord_draw.text((530, 515), args[1], font=font('DIN2014-DemiBold', 20), fill=GREY, anchor='ra')
    ord_draw.text((498, 602), args[4], font=font('DIN2014-Regular', 20), fill=DARK_GREY, anchor='ra')
    ord_draw.text((530, 652), args[5], font=font('DIN2014-Regular', 20), fill=DARK_GREY, anchor='ra')
    ord_draw.text((527, 703), args[6], font=font('DIN2014-Regular', 20), fill=DARK_GREY, anchor='ra')
    ord_draw.line([(528, 726), (527 - comp_draw.textlength(args[6], font('DIN2014-Regular', size=20)), 726)], fill=DARK_GREY, width=1)
    ord_draw.text((542, 807), args[7], font=font('DIN2014-Regular', 18), fill=DARK_GREY, anchor='ra')

    if __name__ == '__main__':
        r_img1.save(f'templates/r_img1.jpg')
        r_img2.save(f'templates/r_img2.jpg')

    else:
        return r_img1, r_img2

