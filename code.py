import qrcode

features = qrcode.QRCode(version = 1, box_size = 40, border = 3)
link = input("Please give the link of which you want to make a QR code")
features.add_data(link)
features.make(fit = True)
generate_image = features.make_image(fill_colour = "olive green", back_color = "white")
generate_image.save("image3.png")

