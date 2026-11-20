isim=input("adiniz nedir?")
print(f"tanistiğiğima memnun oldum, {isim}")
print()
print(f"{isim},şu anda pek bir bilgim yok ama bana soru sormak için şu kelimeleri dene,uzay,minecraft,araba,bilgisayar,ders dalları")
kelime=input("hadi bir kelime gir:")
if kelime == "uzay":
	print("Uzay, Dünya'nın atmosferi dışında kalan sonsuz genişlikteki boşluktur.")
	print()
	print(f"bitti teşekkûrler,{isim}")
if kelime == "minecraft":
	print("Minecraft, oyuncuların bloklardan oluşan bir dünyayı keşfedebildiği, inşa edebildiği ve hayatta kalmaya çalıştığı bir sandbox oyunudur.")
	print()
	print(f"bitti teşekkûrler,{isim}")
if kelime == "araba":
	print("Araba, insanları ve yükleri bir yerden başka bir yere taşımak için kullanılan motorlu kara taşıtıdır.")
	print()
	print(f"bitti teşekkûrler,{isim}")
if kelime == "bilgisayar":
	print("Bilgisayar, verileri işleyerek bilgi üreten ve çeşitli işlemleri gerçekleştiren elektronik bir cihazdır.")
	print()
	print(f"bitti teşekkûrler,{isim}")
if kelime == "ders dalları":
	print("Ders dalları, farklı bilgi ve becerileri öğreten eğitim alanlarıdır. Örneğin matematik sayıları, fizik doğa olaylarını, kimya maddeleri, biyoloji canlıları, tarih geçmişteki olayları, coğrafya ise Dünya'yı inceler")
	print()
	print(f"bitti teşekkûrler,{isim}")
kelime = int(input("ônceki kelimelere devam etmek istiyorsan 1 devam etmek istemiyorsan 2 update yapmak istiyorsan 3 yaz"))
if kelime == 1:
	kelime=input("hadi bir kelime gir:")
if kelime == "uzay":
	print("Uzay, Dünya'nın atmosferi dışında kalan sonsuz genişlikteki boşluktur.")
	print()
	print(f"bitti teşekkûrler,{isim}")
	exit()
if kelime == "minecraft":
	print("Minecraft, oyuncuların bloklardan oluşan bir dünyayı keşfedebildiği, inşa edebildiği ve hayatta kalmaya çalıştığı bir sandbox oyunudur.")
	print()
	print(f"bitti teşekkûrler,{isim}")
	exit()
if kelime == "araba":
	print("Araba, insanları ve yükleri bir yerden başka bir yere taşımak için kullanılan motorlu kara taşıtıdır.")
	print()
	print(f"bitti teşekkûrler,{isim}")
	exit()
if kelime == "bilgisayar":
	print("Bilgisayar, verileri işleyerek bilgi üreten ve çeşitli işlemleri gerçekleştiren elektronik bir cihazdır.")
	print()
	print(f"bitti teşekkûrler,{isim}")
	exit()
if kelime == "ders dalları":
	print("Ders dalları, farklı bilgi ve becerileri öğreten eğitim alanlarıdır. Örneğin matematik sayıları, fizik doğa olaylarını, kimya maddeleri, biyoloji canlıları, tarih geçmişteki olayları, coğrafya ise Dünya'yı inceler")
	print()
	print(f"bitti teşekkûrler,{isim}")
	exit()
if kelime == 2:
	print()
	print(f"tekrardan görüşmek üzere,{isim}")
	exit()
if kelime == 3:
	print(f"anlasıldı,{isim},yükleniyor---->")
	print()
	print("\033[1;32mYükleme tamamlandı\033[0m")
	print("yeni kelime listeniz şunlardır:tarih,aile,müzik,oyun,dil,python")
kelime = input("yeni update olan kelimelerden birini giriniz:")
if kelime == "tarih":
	print("Tarih, geçmişte yaşamış insanların faaliyetlerini, toplumları ve meydana gelen olayları inceleyen bilim dalıdır")
	print()
	print(f"bitti teşekkürler,{isim}")
if kelime == "müzik":
	print("Müzik, duygu ve düşünceleri ses, ritim ve melodiler aracılığıyla ifade eden sanat dalıdır.")
	print()
	print(f"bitti teşekkürler,{isim}")
if kelime == "aile":
	print("Aile, sevgi, güven ve dayanışma bağlarıyla birbirine bağlı olan, birlikte yaşayan veya birbirini destekleyen insanlardan oluşan topluluktur.")
	print()
	print(f"bitti teşekkürler,{isim}")
if kelime == "oyun":
	print("Oyun, insanların eğlenmek, vakit geçirmek veya becerilerini geliştirmek amacıyla katıldığı etkinliktir.")
	print()
	print(f"bitti tesekkürler,{isim}")
if kelime == "dil":
	print("Dil, insanların duygu, düşünce ve bilgilerini konuşarak, yazarak veya işaretlerle birbirine aktarmasını sağlayan iletişim sistemidi")
	print()
	print(f"bitti teşekkürler,{isim}")
if kelime == "python":
	print("Python, çeşitli programlar, oyunlar ve yazılımlar geliştirmek için kullanılan, öğrenmesi kolay ve çok amaçlı bir programlama dilidir.")
	print()
	print(f"bitti teşekkürler,{isim}")
