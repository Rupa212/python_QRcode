# import qrcode

# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# qr.add_data("Hello, world!")
# qr.make(fit=True)
# qr_code = qr.make_image(fill_color="black", back_color="white")
# qr_code.save("qrcodes.png")



import pyqrcode

input_text = input("Enter the text or URL for the QR code: ")

qr_code = pyqrcode.create(input_text)

file_name = "qrcode.png"
qr_code.png(file_name, scale=8)
print("QR code image saved as:", file_name)
print("QR code generated successfully!")