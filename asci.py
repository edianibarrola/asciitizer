from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Variables
IMAGE_PATH = "test.png"
NEW_WIDTH = 1000
ASPECT_RATIO = 1
FONT_SIZE = 10
ASCII_CHARS = "@%#*+=-:.  "

ASCII_INDEX = np.arange(0, 256, 256 / len(ASCII_CHARS))  # Create index for ASCII_CHARS

def scale_image(image, new_width=NEW_WIDTH, aspect_ratio=ASPECT_RATIO):  # Adjust aspect_ratio as necessary
    (original_width, original_height) = image.size
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    img_array = np.array(image)
    ascii_img = ""
    for row in img_array:
        for pixel_value in row:
            ascii_img += ASCII_CHARS[np.digitize(pixel_value, ASCII_INDEX) - 1]
        ascii_img += "\n"
    return ascii_img

def convert_image_to_ascii(image_path=IMAGE_PATH, new_width=NEW_WIDTH, aspect_ratio=ASPECT_RATIO):  # Adjust aspect_ratio as necessary
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    image = scale_image(image, new_width, aspect_ratio)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    return ascii_str

def get_text_dimensions(text, font):
    mask = font.getmask(text)
    width, height = mask.size
    return width, height

def ascii_to_image(ascii_str, font_size=FONT_SIZE, aspect_ratio=ASPECT_RATIO):  # Adjust the font_size as necessary
    ascii_str_lines = ascii_str.split('\n')
    fnt = ImageFont.truetype('cour.ttf', font_size)
    max_width = 0
    total_height = 0

    # Calculate the maximum width and total height
    for line in ascii_str_lines:
        line_width, line_height = get_text_dimensions(line, fnt)
        max_width = max(max_width, line_width)
        total_height += line_height

    # Add some padding
    max_width += 20
    total_height += 20

    img = Image.new('L', (max_width, total_height), color=255)
    d = ImageDraw.Draw(img)
    current_height = 10

    # Draw each line of the ASCII art
    for line in ascii_str_lines:
        line_width, line_height = get_text_dimensions(line, fnt)
        d.text(((max_width - line_width) // 2, current_height), line, font=fnt, fill=0)
        current_height += line_height

    return img

def main(image_path=IMAGE_PATH, new_width=NEW_WIDTH, aspect_ratio=ASPECT_RATIO):  # Adjust aspect_ratio as necessary
    ascii_img = convert_image_to_ascii(image_path, new_width, aspect_ratio)
    img = ascii_to_image(ascii_img, font_size=FONT_SIZE, aspect_ratio=aspect_ratio)  # Adjust the font_size as necessary
    img.save('ascii_image.png')

if __name__ == "__main__":
    main()
