from PIL import ImageFont

font_size = 10
font = ImageFont.truetype('Courier New.ttf', font_size)

# Measure the size of a character
(width, height) = font.getsize('A')  # Or use any other character

print(f'Width: {width}, Height: {height}')
