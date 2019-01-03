
#UymsuzmFuAz uE yADq uyBADFmzF Ftmz wzAIxqpsq

Letters_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def Encrypt_Ceasar_Cipher(message):
	text = ""
	key = 2 #input ("Select your Key From 0 to 26 : ")
	mode = "Decrypt" #input("Select your Mode 'Encrypt' or 'Decrypt' : ")
	for symbole in message:
		if symbole in Letters_list:
			num = Letters_list.find(symbole)
			if mode == "Encrypt":
				num += int(key)
			elif mode == "Decrypt":
				num -= int(key)
			if num >= len(Letters_list):
				num = num - len(Letters_list)
			elif num < 0:
				num += len(Letters_list)
			text += Letters_list[num]
		else:
			text += symbole
	return text
print (Encrypt_Ceasar_Cipher("Imagination is more important than knowledge"))

