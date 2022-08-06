import qrcode       # importing qr module
a = input("Enter something which you want to make qr : ")   # taking user input
b = qrcode.make(a)  # convert the user input into QR code
b.save("photo.jpg") # saving the file int jpg format (you can save also into pdf,jpeg)
