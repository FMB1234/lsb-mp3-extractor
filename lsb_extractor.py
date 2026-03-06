import wave
import numpy as np

# Function to extract hidden text using LSB
def extract_hidden_text(mp3_file):
    # Open the MP3 file
    with open(mp3_file, 'rb') as file:
        byte = file.read(1)
        hidden_bits = []
        while byte:
            # Convert byte to integer
            byte_value = ord(byte)
            # Extract LSB
            hidden_bits.append(byte_value & 1)
            byte = file.read(1)

    # Convert bits to text
    hidden_text = ''.join(chr(int(''.join(str(bit) for bit in hidden_bits[i:i+8]), 2)) for i in range(0, len(hidden_bits), 8))
    return hidden_text.strip()  # Return the extracted hidden text

# Test function
if __name__ == '__main__':
    mp3_path = 'path_to_your_mp3_file.mp3'  # Change this to your MP3 file path
    print(extract_hidden_text(mp3_path))