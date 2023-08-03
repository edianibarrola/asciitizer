from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Path to the input image
INPUT_IMAGE_PATH = "test.png"

# Number of ASCII characters in each row of the output image
ASCII_CHARACTERS_IN_ROW = 400

# Adjusts the height of the ASCII art relative to its width
HEIGHT_WIDTH_ADJUSTMENT = 1.3

# Size of the font for ASCII characters
ASCII_FONT_SIZE = 10

# ASCII characters used for the ASCII art
ASCII_CHARACTERS = "@%#;:*+=-.  "

# Creates an index for ASCII_CHARACTERS
ASCII_CHAR_INDEX = np.arange(0, 256, 256 / len(ASCII_CHARACTERS)) 

def adjust_image_size(image, characters_per_row=ASCII_CHARACTERS_IN_ROW, height_width_ratio=HEIGHT_WIDTH_ADJUSTMENT):
    (original_width, original_height) = image.size
    new_width = characters_per_row
    character_aspect_ratio = 1.67
    new_height = int(height_width_ratio * new_width * original_height / original_width / character_aspect_ratio)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_image_to_grayscale(image):
    return image.convert("L")

def convert_pixels_to_ascii(image):
    img_array = np.array(image)
    ascii_img = ""
    for row in img_array:
        for pixel_value in row:
            ascii_img += ASCII_CHARACTERS[np.digitize(pixel_value, ASCII_CHAR_INDEX) - 1]
        ascii_img += "\n"
    return ascii_img

def convert_pixels_to_ascii_with_color(image, black_canvas=False):
    img_array = np.array(image)
    ascii_img = ""
    for row in img_array:
        for pixel_value in row:
            char_index = np.digitize(pixel_value[0], ASCII_CHAR_INDEX) - 1
            if black_canvas:
                char_index = len(ASCII_CHARACTERS) - 1 - char_index
            ascii_img += ASCII_CHARACTERS[char_index] 
        ascii_img += "\n"
    return ascii_img

def transform_image_to_ascii(image_path=INPUT_IMAGE_PATH, characters_per_row=ASCII_CHARACTERS_IN_ROW, height_width_ratio=HEIGHT_WIDTH_ADJUSTMENT, color_enabled=False, black_canvas=False):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = image.convert("RGB")
    image = adjust_image_size(image, characters_per_row, height_width_ratio)
    
    if color_enabled:  
        ascii_str = convert_pixels_to_ascii_with_color(image, black_canvas)
    else:
        image = convert_image_to_grayscale(image)
        ascii_str = convert_pixels_to_ascii(image)
    
    return ascii_str

def calculate_text_dimensions(text, font):
    mask = font.getmask(text)
    width, height = mask.size
    return width, height

def transform_ascii_to_image(ascii_text, font_size=ASCII_FONT_SIZE, height_width_ratio=HEIGHT_WIDTH_ADJUSTMENT, color_enabled=False, black_canvas=False):
    ascii_str_lines = ascii_text.split('\n')
    fnt = ImageFont.truetype('cour.ttf', font_size)
    max_width = 0
    total_height = 0

    for line in ascii_str_lines:
        line_width, line_height = calculate_text_dimensions(line, fnt)
        max_width = max(max_width, line_width)
        total_height += line_height

    max_width += 20
    total_height += 20

    if color_enabled:
        img = Image.new('RGB', (max_width, total_height), color=(0, 0, 0) if black_canvas else (255, 255, 255))
    else:
        img = Image.new('L', (max_width, total_height), color=0 if black_canvas else 255)

    d = ImageDraw.Draw(img)
    current_height = 10

    for line in ascii_str_lines:
        line_width, line_height = calculate_text_dimensions(line, fnt)
        if color_enabled:
            d.text(((max_width - line_width) // 2, current_height), line, font=fnt, fill=(255, 255, 255) if black_canvas else (0, 0, 0))
        else:
            d.text(((max_width - line_width) // 2, current_height), line, font=fnt, fill=255 if black_canvas else 0)
        current_height += line_height

    return img

def main(image_path=INPUT_IMAGE_PATH, characters_per_row=ASCII_CHARACTERS_IN_ROW, height_width_ratio=HEIGHT_WIDTH_ADJUSTMENT):
    render_option = input("Please choose your desired ASCII art format: Enter 'color' for color, 'grayscale' for black and white: ").strip().lower()
    
    if render_option == 'color':
        color_enabled = True
        black_canvas = False
    elif render_option == 'grayscale':
        color_enabled = False
        black_canvas = False
    else:
        print("Invalid input. Defaulting to grayscale rendering.")
        color_enabled = False
        black_canvas = False

    black_canvas_option = input("Do you want a black canvas with white text? (yes/no): ").strip().lower()
    if black_canvas_option == 'yes':
        black_canvas = True
    elif black_canvas_option == 'no':
        black_canvas = False
    else:
        print("Invalid input. Defaulting to white canvas with black text.")
        black_canvas = False

    ascii_img = transform_image_to_ascii(image_path, characters_per_row, height_width_ratio, color_enabled, black_canvas)
    img = transform_ascii_to_image(ascii_img, font_size=ASCII_FONT_SIZE, height_width_ratio=height_width_ratio, color_enabled=color_enabled, black_canvas=black_canvas)
    img.save('ascii_image.png')

if __name__ == "__main__":
    main()
