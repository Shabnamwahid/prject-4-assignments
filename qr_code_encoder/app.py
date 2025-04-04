import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Function to generate a QR code for a given string
def generate_qr_code(data, filename='qrcode.png'):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated QR code image
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

# Function to decode a QR code from an image file
def decode_qr_code(image_file):
    # Open the image containing the QR code
    img = Image.open(image_file)

    # Decode the QR code
    decoded_objects = decode(img)
    for obj in decoded_objects:
        # Extract the data from the QR code and print it
        data = obj.data.decode('utf-8')
        print(f"Decoded Data: {data}")
        return data

# Main function to test the QR Code encoding and decoding
def main():
    # Get input from user to generate a QR code
    data = input("Enter data to encode into a QR code: ")
    generate_qr_code(data)
    
    # Ask the user for a QR code image to decode
    image_file = input("Enter the path of the QR code image to decode: ")
    decoded_data = decode_qr_code(image_file)

if __name__ == "__main__":
    main()
