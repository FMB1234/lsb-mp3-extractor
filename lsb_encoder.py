import wave
import struct
import sys

def encode_lsb(mp3_file, secret_message):
    # Open the MP3 file
    with open(mp3_file, 'rb') as audio:
        audio_bytes = bytearray(audio.read())
    
    # Prepare the message with a delimiter
    secret_message += '\0'  # Null character as a delimiter
    message_index = 0
    message_length = len(secret_message)
    
    # Encode the message into the audio bytes
    for i in range(len(audio_bytes)):
        if message_index < message_length:
            # Set the LSB of the byte to the next bit of the message
            audio_bytes[i] = (audio_bytes[i] & ~1) | (ord(secret_message[message_index]) & 1)
            if audio_bytes[i] & 1 == 0:  # Move to the next character if LSB was set to zero
                message_index += 1
        else:
            break
    
    # Write the modified audio bytes back to a new MP3 file
    with open('encoded_' + mp3_file, 'wb') as encoded_audio:
        encoded_audio.write(audio_bytes)
    
    print('Encoding complete. Hidden message encoded into:', 'encoded_' + mp3_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python lsb_encoder.py <mp3_file> <secret_message>')
        sys.exit(1)
    encode_lsb(sys.argv[1], sys.argv[2])