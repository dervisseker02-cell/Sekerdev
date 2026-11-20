import random
print("===///KELİME OYUNUNA HOSGELDİNİZ///===")
print()
print("kurallar basit ben sana sectigin zorluga gore kelimeler vericem ve sende ona göre tahmin ettiğim kelimeyi bulmaya calisicaksin")
print()
print("zorluklara göre can degerleron sunlardir:  ")
print("kolay mod---->3 can")
print("orta mod----->5 can")
print("zor mod------>6 can")
zorluk=input("simdi bir zorluk sec bakalim (kolay,orta,zor):   ").lower().strip()
if zorluk=="kolay":
	can=3
	print("kelimelerin sunlardir: ")
	print()
	print("elma,erik,armut,çilek,karpuz,muz,portakal,limon,domates,nektari")
	kelime=random.choice(["elma","erik","armut","çilek","karpuz","muz","portakal","limon","domates","nektari"])
	while can>0:
		tahmin=input("şimdi tahmin et bakalım:  ").lower().strip()
		if tahmin == kelime:
			print("===tebrikler doğru bildin tekrardan oynamak icin kod dosyasini yeniden baslat====")
			break
		else:
			can-=1
			print("¡!yanlış bildin!¡")
			print(f"can degeriniz:   {can}")
		if can ==0:
			print("***canın bitti kaybettin***")
			break
if zorluk=="orta":
		can=5
		print("kelimeler şunlardır")
		print()
		print("araba,avakado,bilgisayar,kalemlik,lamba,kitap,mühendis,python,biyoloji,fosfor,kırmızı,mürekkep,yay,pencere,kapı")
		kelime=random.choice(["araba","avakado","kalemlik","lamba","kitap","mühendis","python","biyoloji","fosfor","kırmızı","mürekkep","yay","pencere","kapı","bilgisayar"])
		while can>0:
					tahmin=input("şimdi tahmin et bakalım:    ").lower().strip()
					if tahmin==kelime:
						print("===aferin kazandın,tekrardan oynamak istiyorsan kod dosyasini yeniden başlat===")
						break
					else:
						can-=1
						print("¡!yanlış bildin!¡")
						print(f"can degeriniz:   {can}")
					if can == 0:
						print("***canın bitti kaybettin***")
						break
if zorluk == "zor":
						can=6
						print("demek zor modu seçtin tabikide her zorlukta kelime sayisi arttirmicağım o yüzden bu sefer kelime sayısını sabit tutup belirsiz kelimeler vereceğim yap yapabiliyorsan: ")
						print()
						print("kelimeler şunlardır:  ")
						print()
						print("p?r?a?a?,m?s?a?a, k?t?p?a?e, t?l?f?n, ç?k?l?t?, y?ld?z, m?h?nd?s, b?l?g?s?y?r, k?r?d?z, ş?m??y?, s?n?m?, d?n?z?lt?, m?c?r?, m?tf?k, k?l?m?l?k")
						kelime=random.choice(["portakal","masabaşı","kütüphane","telefon","çikolata","yıldız","mühendis","bilgisayar","karpuz","şemsiye","sinema","denizaltı","macera","mutfak","kalemlik"])
						while can>0:
							tahmin =input("şimdi tahmin et bakalın:  ").lower().strip()
							if tahmin==kelime:
								print("===kutluyorum,gercekten tahmin oyunlarinda çok iyisin,tekrardan oynamak istersen kod dosyasını yeniden başlat===")
								break
							else:
								can-=1
								print("¡!yanlış bildin!¡")
								print(f"can değeriniz:   {can}")
							if can ==0:
								print("***kaybettin tekrardan denemeni öneririm***")
								break
				
