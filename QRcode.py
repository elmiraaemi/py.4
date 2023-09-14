import qrcode
name=input("yor name ? : ")
number=int(input("yor PhoneNumber ? : "))
QR=[]
QR.append(name)
QR.append(number)
img=qrcode.make(QR)
img.save("qrcode.jpg")
