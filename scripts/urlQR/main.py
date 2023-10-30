from qrcode import QRCode
def qrcrate(data,fname):
	qr = QRCode(version=1, box_size=10, border=5)
	qr.add_data("http://127.0.0.1:5000/"+data)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	img.save("qr_code"+fname+".png")
data=["bd1a5db05e1420a1d76c47182958a1cd774827b95cead75adca906b201e45d1d","d9458b2fbc48779ab7d55c4975af13df8d994ae073fa5f391cbd5c21f6d7716c","f8e0095506b9988416c331f1a44a063089ff5666c860af3ba16b70896b3d1418","fbbd3295fcc07d79c7861f5e03330406d3d9cec5120ecd4d78eec4f0bcc77c1a","0fb039dfb0a69acbc5747cf352dc31632d78a3c504b6da6cd539f6d9806c5705"]
for i in range(len(data)):
	qrcrate(data[i],str(i)+"_hit")