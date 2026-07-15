#!/usr/bin/env python3
"""Generate PWA icons for DL25 using Pillow"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded rectangle background
    radius = int(size * 0.156)
    draw.rounded_rectangle([0, 0, size, size], radius=radius, fill='#1a3a5c')
    
    # Text
    try:
        # Try to use a bold font
        font_size = int(size * 0.55)
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    text = "DL25"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) / 2
    y = (size - text_h) / 2 + size * 0.02
    
    draw.text((x, y), text, font=font, fill='white')
    
    img.save(output_path)
    print(f"Created {output_path} ({size}x{size})")

if __name__ == '__main__':
    out_dir = r'C:\Users\amirhosein\Desktop\drive test\dl25_deploy'
    create_icon(512, os.path.join(out_dir, 'icon-512.png'))
    create_icon(192, os.path.join(out_dir, 'icon-192.png'))
    print("Done!")