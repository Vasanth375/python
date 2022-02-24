import qrcode
try:
    data="123456789"
    qr=qrcode.make(data)
    qr.save('C:\\Users\\VASANTH\\ECET')
except Exception as e:
    print(e)