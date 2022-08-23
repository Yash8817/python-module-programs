import pyqrcode
from pyqrcode import QRCode

s = "https://yash8817.github.io/portfolio.github.io/"

qr = pyqrcode.create(s)
qr.svg("mycode.pdf",scale=8)
