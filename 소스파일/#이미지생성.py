#이미지생성
# Import modules
import PIL
from PIL import Image, ImageDraw, ImageFont

# Create a blank image
cover = Image.new('RGB', (600, 800), 'blue')

# Create a draw object
draw = ImageDraw.Draw(cover)

# Load fonts
title_font = ImageFont.truetype('Arial.ttf', 60)
author_font = ImageFont.truetype('Arial.ttf', 40)

# Write text
draw.text((50, 200), '시간 관리의 기술', fill='white', font=title_font)
draw.text((50, 300), '한재원', fill='white', font=author_font)

# Save image
cover.save('cover.jpg')