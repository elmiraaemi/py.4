import qrcode
name:input("yor name ? : ")
PhoneNumber=int(input("yor PhoneNumber ? : "))
img=qrcode.make(name+" | "+PhoneNumber)
img.save("yor qrcode.jpg")