import freetype
import os
from PIL import Image, ImageDraw
from pathlib import Path
from io import BytesIO

# Function to render a character set as a texture atlas
def render_atlas(face, atlas_width=512, atlas_height=512, font_size=48, padding=4, margin=2, character_padding=4):
    pen_x, pen_y = padding, padding
    max_row_height = 0

    # Set the font size
    face.set_char_size(font_size * 64)  # 64 is FreeType's fixed-point format

    # Calculate the maximum height of all characters (ascender + descender)
    ascender = face.size.ascender >> 6  # Convert from 1/64th pixels to pixels
    descender = abs(face.size.descender >> 6)  # Negative descender, so take absolute value
    max_height = ascender + descender  # Total height from ascender to descender

    # Create a blank image for the atlas (RGBA format)
    img = Image.new("RGBA", (atlas_width, atlas_height), (0, 0, 0, 0))

    # Prepare to store character positions
    char_positions = {}

    print(f"Generating font atlas with size {font_size}px and {character_padding}px padding between characters")

    for char_code in range(32, 127):  # ASCII characters
        char = chr(char_code)
        face.load_char(char)
        glyph = face.glyph
        bitmap = glyph.bitmap

        # Handle the space character separately
        if char_code == 32:  # ASCII 32 is the space character
            char_width = glyph.advance.x >> 6  # Use the advance width for space
            char_height = max_height
        else:
            char_width = glyph.advance.x >> 6  # Use the advance width for logical space
            char_height = max_height  # All characters occupy the same vertical space, max height

        # Check if the current character fits in the current row
        if pen_x + char_width + margin > atlas_width:
            # Move to the next row
            pen_x = padding
            pen_y += max_row_height + margin + character_padding  # Add padding between rows
            max_row_height = char_height  # Reset the row height for the new row

        # Ensure the texture atlas doesn't overflow vertically
        if pen_y + char_height + margin > atlas_height:
            raise ValueError(f"Atlas size exceeded {atlas_width}x{atlas_height}. Try reducing the font size.")

        # Calculate the vertical position within the box to align glyph as if rendered in text
        y_offset = pen_y + ascender - glyph.bitmap_top  # Aligns the character with the baseline

        # Render glyph onto the image (skip the space character as it has no bitmap)
        if char_code != 32:  # Don't render the space character (no visible glyph)
            glyph_img = Image.frombytes('L', (bitmap.width, bitmap.rows), bytes(bitmap.buffer))
            img.paste(glyph_img, (pen_x + glyph.bitmap_left, y_offset), glyph_img)

        # Store character position and size in the correct format
        char_positions[char_code] = (pen_x, pen_y, char_width, char_height)

        # Move pen for the next character
        pen_x += char_width + margin + character_padding  # Add padding between characters
        max_row_height = max(max_row_height, char_height)  # Keep track of the tallest character in the row

    return img, char_positions

# Function to generate the atlas and ini file
def generate_atlas(font_path, atlas_width=512, atlas_height=512, font_size=48, character_padding=4):
    # Load the font
    face = freetype.Face(str(font_path))
    
    # Render the ASCII characters as a texture atlas
    text_image, char_positions = render_atlas(face, atlas_width, atlas_height, font_size, character_padding=character_padding)

    # Create a blank texture atlas (RGBA format, fully transparent)
    atlas_image = Image.new("RGBA", (atlas_width, atlas_height), (0, 0, 0, 0))

    # Paste the rendered characters onto the atlas
    atlas_image.paste(text_image, (0, 0), text_image)

    # Save the texture atlas to memory
    atlas_output = BytesIO()
    atlas_image.save(atlas_output, format="PNG")
    atlas_output.seek(0)
    
    
    # Generate the character mapping file (ini format) to memory
    mapping_output = BytesIO()
    for char_code, (x, y, width, height) in char_positions.items():
        mapping_output.write(f"{char_code}={x},{y},{width},{height}\n".encode())
    mapping_output.seek(0)
    
    return atlas_output, mapping_output

# Main function to process all font files in the current directory
def process_fonts(font_files, atlas_width=512, atlas_height=512, font_size=48, character_padding=4):
    
    # Process each font files in the directory
    for font_file in font_files:
        print(f"Processing font: {font_file}")
        try:
            atlas_output, mapping_output = generate_atlas(font_file, atlas_width, atlas_height, font_size, character_padding)
            return atlas_output, mapping_output
        except Exception as e:
            print(f"Error processing {font_file}: {e}")
        if atlas_output:
            atlas_output.close()
        if mapping_output:
            mapping_output.close()
    return None, None