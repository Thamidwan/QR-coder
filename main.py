import qrcode

img = qrcode.make("https://www.youtube.com/")
img.save("youtube.jpg", scale=8)
