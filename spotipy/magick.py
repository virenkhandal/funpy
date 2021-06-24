from PIL import Image, ImageDraw, ImageFont

def writetext():

    # Image + Font Setup
    image = Image.open("igstory.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'/System/Library/Fonts/Supplemental/Arial.ttf', 50) 

    # Text to write onto image
    time = "weeks"
    artist_one = "Kid Cudi"
    artist_two = "Lana Del Rey"
    artist_three = "Machine Gun Kelly"
    artist_four = "Sad Alex"
    artist_five = "Migos"

    track_one = "Vibes (feat...)"
    track_two = "Lana Del Rey"
    track_three = "Machine Gu..."
    track_four = "Sad Alex"
    track_five = "Migos"


    artist_three = concat(artist_three, font)

    # Drawing text on image
    draw.text((650, 200), time, fill="black", font=font, align="left")

    draw.text((120, 1180), artist_one, fill="black", font=font, align="left")
    draw.text((120, 1320), artist_two, fill="black", font=font, align="left")

    draw.text((120, 1455), artist_three, fill="black", font=font, align="left")
    draw.text((120, 1595), artist_four, fill="black", font=font, align="left")
    draw.text((120, 1735), artist_five, fill="black", font=font, align="left")

    draw.text((670, 1180), track_one, fill="black", font=font, align="left")
    draw.text((670, 1320), track_two, fill="black", font=font, align="left")
    draw.text((670, 1455), track_three, fill="black", font=font, align="left")
    draw.text((670, 1595), track_four, fill="black", font=font, align="left")
    draw.text((670, 1735), track_five, fill="black", font=font, align="left")


    # Display image
    image.show()

def concat(text, font):
    split = text.split(" ")

    for i in range(len(split) + 1):
        size = font.getsize(' '.join(split[:i]) + " ...")
        if size[0] > 350:
            artist_breakpoint = i
            break
    text = ' '.join(split[:artist_breakpoint]) + " ..."
    return text

if __name__ == "__main__":
    writetext()