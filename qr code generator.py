import pyqrcode
url=input("Enter the URL:")
x=pyqrcode.create(url)
x.svg('qr.svg',scale=8)

