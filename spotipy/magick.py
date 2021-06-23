from PIL import Image, ImageDraw, ImageFont

def writetext():
    image = Image.open("igstory.png")
    draw = ImageDraw.Draw(image)
    text = "Kid Cudi"
    font = ImageFont.truetype(r'/System/Library/Fonts/Supplemental/Arial.ttf', 20) 
    # font = ImageFont.load_default()

    draw.text((100, 100), text, fill="black", font=font, align="left")
    image.show()

if __name__ == "__main__":
    writetext()