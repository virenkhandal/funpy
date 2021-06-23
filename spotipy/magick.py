from PIL import Image, ImageDraw, ImageFont

def writetext():
    image = Image.open("igstory.png")
    draw = ImageDraw.Draw(image)
    time = "weeks"
    one = "Kid Cudi"
    two = "Lana Del Rey"
    three = "Machine Gun K..."
    four = "Sad Alex"
    five = "Migos"
    font = ImageFont.truetype(r'/System/Library/Fonts/Supplemental/Arial.ttf', 60) 
    # font = ImageFont.load_default()

    draw.text((120, 110), time, fill="black", font=font, align="left")

    draw.text((120, 1180), one, fill="black", font=font, align="left")
    draw.text((120, 1320), two, fill="black", font=font, align="left")
    draw.text((120, 1455), three, fill="black", font=font, align="left")
    draw.text((120, 1595), four, fill="black", font=font, align="left")
    draw.text((120, 1735), five, fill="black", font=font, align="left")
    image.show()

if __name__ == "__main__":
    writetext()