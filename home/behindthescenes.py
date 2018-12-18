for i in range(0, len(get_recete_icerik['entries'])):
    ...:     if i % 2 == 0:
    ...:         base64_malzeme_adi = base64.b64encode(get_recete_icerik['entries'][i].values()[0])
    ...:         recetedeki_deger = base64.b64encode(get_recete_icerik['entries'][i+1].values()[0])
    ...:         go_to_malzeme = feedparser.parse("http://demo.7houseburger.com/Stok/Adi/"+ base64_malzeme_adi + '/'+ str(ay) + '-' + s
    ...: tr(gun) + '-' + str(yil))
    ...:         stok = go_to_malzeme['entries'][0].values()[0]
    ...:         toplam_giren = feedparser.parse("http://demo.7houseburger.com/StokToplamGiren/Adi/" + base64_malzeme_adi + '/'+ str(ay
    ...: ) + '-' + str(gun) + '-' + str(yil))
    ...:         toplam_giren_sayisi = toplam_giren['entries'][0].values()[0]
    ...:         print "toplamgiren - stok : " + toplam_giren_sayisi + " - " + stok

    for j in range(1, 1000):
        hangi_alim = feedparser.parse("http://demo.7houseburger.com/StokGiren/Adi/" + j + "/" + base64_malzeme_adi + '/' +
                                  ...: str(ay) + '-' + str(gun) + '-' + str(yil))


for i in range(0, len(get_recete_icerik['entries'])):
    ...:     if i % 2 == 0:
    ...:         base64_malzeme_adi = base64.b64encode(get_recete_icerik['entries'][i].values()[0])
    ...:         recetedeki_deger = base64.b64encode(get_recete_icerik['entries'][i+1].values()[0])
    ...:         go_to_malzeme = feedparser.parse("http://demo.7houseburger.com/Stok/Adi/"+ base64_malzeme_adi + '/'+ str(ay) + '-' + s
    ...: tr(gun) + '-' + str(yil))
    ...:         stok = go_to_malzeme['entries'][0].values()[0]
    ...:         toplam_giren = feedparser.parse("http://demo.7houseburger.com/StokToplamGiren/Adi/" + base64_malzeme_adi + '/'+ str(ay
    ...: ) + '-' + str(gun) + '-' + str(yil))
    ...:         toplam_giren_sayisi = str(toplam_giren['entries'][0].values()[0])
    ...:         integer_toplam_giren = float(toplam_giren_sayisi)
    ...:         if "," in stok:
    ...:             str_stok = str(stok)
    ...:             str_stok.replace(",",".")
    ...:             integer_stok = float(str_stok)
    ...:         else:
    ...:             integer_stok = float(stok)
    ...:         fark = integer_toplam_giren - integer_stok
    ...:         print fark


for i in range(0, len(get_recete_icerik['entries'])):
    ...:     if i % 2 == 0:
    ...:         base64_malzeme_adi = base64.b64encode(get_recete_icerik['entries'][i].values()[0])
    ...:         recetedeki_deger = base64.b64encode(get_recete_icerik['entries'][i+1].values()[0])
    ...:         go_to_malzeme = feedparser.parse("http://demo.7houseburger.com/Stok/Adi/"+ base64_malzeme_adi + '/'+ str(ay) + '-' + s
    ...: tr(gun) + '-' + str(yil))
    ...:         stok = go_to_malzeme['entries'][0].values()[0]
    ...:         toplam_giren = feedparser.parse("http://demo.7houseburger.com/StokToplamGiren/Adi/" + base64_malzeme_adi + '/'+ str(ay
    ...: ) + '-' + str(gun) + '-' + str(yil))
    ...:         toplam_giren_sayisi = toplam_giren['entries'][0].values()[0]
    ...:         string_giren = str(toplam_giren_sayisi)
    ...:         #print "string giren: " + string_giren
    ...:         #print "float giren: " + float(string_giren)
    ...:         #print "int giren: " + int(string_giren)
    ...:         #print "string stok: " + string_stok
    ...:         #print "float stok: " + float(string_stok)
    ...:         if ',' in string_giren:
    ...:             string_giren = string_giren.replace(',', '.')
    ...:         print string_giren