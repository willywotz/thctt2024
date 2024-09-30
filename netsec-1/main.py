from PIL import Image

def reverse_lsb_to_text(image_path):
    """Reverses the least significant bit of each pixel in the given image and converts the resulting data to text.

    Args:
        image_path: The path to the image file.

    Returns:
        The extracted text.
    """

    with Image.open(image_path) as img:
        pixels = img.load()

        extracted_bits = []
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                extracted_bits.append(str(r & 1))  # Convert to string before joining
                # extracted_bits.append(str((g & 1) >> 1))  # Convert to string before joining
                # extracted_bits.append(str(b & 1))  # Convert to string before joining

        # Convert extracted bits to bytes
        extracted_bytes = [int(''.join(extracted_bits[i:i+8]), 2) for i in range(0, len(extracted_bits), 8)]

        # Convert bytes to text
        extracted_text = ''.join(chr(byte) for byte in extracted_bytes)

        return extracted_text

# Example usage:
image_path = "image.png"
extracted_text = reverse_lsb_to_text(image_path)
print(extracted_text)
