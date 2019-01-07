import base64
import feedparser

sipno = "18-33438"

get_recete_no = feedparser.parse("http://demo.7houseburger.com/UretimRecete/SipNo/" + sipno)

if get_recete_no['entries'][0].values()[0]:
    recete_no = get_recete_no['entries'][0].values()[0]
    tarih = get_recete_no['entries'][1].values()[0]

    yil = tarih.split('.')[2].split(' ')[0]
    ay = tarih.split('.')[1]
    gun = tarih.split('.')[0]

print "recete no: ", recete_no
print "tarih: ", tarih
print "ay: ", ay
print "yil: ", yil
print "gun: ", gun

base64recete_no = base64.b64encode(recete_no)

get_recete_icerik = feedparser.parse("http://demo.7houseburger.com/Recete/ReceteNo/" + base64recete_no)

for i in range(0, len(get_recete_icerik['entries'])):
    if i % 2 == 0:
        malzeme_adi = get_recete_icerik['entries'][i].values()[0]
        base64_malzeme_adi = base64.b64encode(malzeme_adi)
        recetedeki_deger = get_recete_icerik['entries'][i + 1].values()[0]

        go_to_malzeme = feedparser.parse("http://demo.7houseburger.com/Stok/Adi/"
                                         + base64_malzeme_adi + '/'
                                         + str(ay) + '-' + str(gun) + '-' + str(yil))

        stok = go_to_malzeme['entries'][0].values()[0]
        print "\nmalzeme adi: ", malzeme_adi
        print "stok: ", stok

        toplam_giren = feedparser.parse("http://demo.7houseburger.com/StokToplamGiren/Adi/" + base64_malzeme_adi
                                        + '/'
                                        + str(ay)
                                        + '-'
                                        + str(gun)
                                        + '-'
                                        + str(yil))

        total_depo = toplam_giren['entries'][0].values()[0]

        if ',' in total_depo:
            float_total_depo = float((str(total_depo)).replace(',', '.'))
        else:
            float_total_depo = float(total_depo)
        if ',' in stok:
            float_stok = float((str(stok)).replace(',', '.'))
        else:
            float_stok = float(stok)

        fark = float_total_depo - float_stok
        toplam = 0

        print "fark: ", fark
        print "float stok: ", float_stok
        print "float total depo: ", float_total_depo

        for j in range(1, 1000):
            step_counter = feedparser.parse("http://demo.7houseburger.com/StokGiren/Adi/" + str(j)
                                            + '/'
                                            + base64_malzeme_adi
                                            + '/'
                                            + str(ay)
                                            + '-'
                                            + str(gun)
                                            + '-'
                                            + str(yil))
            if j == 1:
                toplam = toplam + float(step_counter['entries'][0].values()[0])
            else:
                toplam = toplam + float(step_counter['entries'][(len(step_counter['entries']) - 1)].values()[0])

            if toplam > float_stok:
                sorgu_adimi = j
                print "toplam: ", toplam, " stok: ", float_stok, " sorgu adimi: ", j
                break

            print "toplam: ", toplam, " stok: ", float_stok, " sorgu adimi: ", j

        bartex_tarih_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokTarih/" + str(sorgu_adimi)
                                                + '/'
                                                + base64_malzeme_adi
                                                + '/'
                                                + str(ay)
                                                + '-'
                                                + str(gun)
                                                + '-'
                                                + str(yil))
        if sorgu_adimi == 1:
            bartex_tarih = bartex_tarih_sorgusu['entries'][0].values()[0]
            print "bartex tarih: ", bartex_tarih, " sorgu adimi: ", sorgu_adimi
        else:
            bartex_tarih = bartex_tarih_sorgusu['entries'][(len(bartex_tarih_sorgusu['entries']) - 1)].values()[0]
            print "bartex tarih: ", bartex_tarih, " sorgu adimi: ", sorgu_adimi

        bartex_dovizcinsi_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokDoviz/" + str(sorgu_adimi)
                                                     + '/'
                                                     + base64_malzeme_adi
                                                     + '/'
                                                     + str(ay)
                                                     + '-'
                                                     + str(gun)
                                                     + '-'
                                                     + str(yil))

        if sorgu_adimi == 1:
            bartex_doviz = bartex_dovizcinsi_sorgusu['entries'][0].values()[0]
            print "bartex doviz: ", bartex_doviz, " sorgu adimi: ", sorgu_adimi
        else:
            bartex_doviz = bartex_dovizcinsi_sorgusu['entries'][(len(bartex_dovizcinsi_sorgusu['entries']) - 1)].values()[0]
            print "bartex doviz: ", bartex_doviz, " sorgu adimi: ", sorgu_adimi

        bartex_birim_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokBirimFiyat/" + str(sorgu_adimi)
                                                + '/'
                                                + base64_malzeme_adi
                                                + '/'
                                                + str(ay)
                                                + '-'
                                                + str(gun)
                                                + '-'
                                                + str(yil))

        if sorgu_adimi == 1:
            bartex_birim = bartex_birim_sorgusu['entries'][0].values()[0]
            print "bartex_birim: ", bartex_birim, " sorgu adimi: ", sorgu_adimi
        else:
            bartex_birim = bartex_birim_sorgusu['entries'][(len(bartex_birim_sorgusu['entries']) - 1)].values()[0]
            print "bartex_birim: ", bartex_birim, " sorgu adimi: ", sorgu_adimi

        malzeme_kodu_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokAdKod/" + base64_malzeme_adi)
        malzeme_kodu = malzeme_kodu_sorgusu['entries'][0].values()[0]
        base64malzeme_kodu = base64.b64encode(malzeme_kodu)

        print "malzeme adi: ", malzeme_adi
        print "malzeme kodu: ", malzeme_kodu
        print "base64 malzeme kodu: ", base64malzeme_kodu

        tiger_yil = bartex_tarih.split('.')[2].split(' ')[0]
        tiger_ay = bartex_tarih.split('.')[1]
        tiger_gun = bartex_tarih.split('.')[0]

        print "tiger_yil: " ,tiger_yil
        print "tiger gun: ", tiger_gun

        if int(tiger_ay) < 10:
            print "tiger ay: 0", tiger_ay
            tiger_sorgusu = feedparser.parse("http://demo.7houseburger.com/Tiger/" + base64malzeme_kodu
                                                      + '/'
                                                      + str(tiger_yil)
                                                      + '-0'
                                                      + str(tiger_ay)
                                                      + '-'
                                                      + str(tiger_gun))
        else:
            print "tiger_ay: ", tiger_ay
            tiger_sorgusu = feedparser.parse("http://demo.7houseburger.com/Tiger/" + base64malzeme_kodu
                                             + '/'
                                             + str(tiger_yil)
                                             + '-'
                                             + str(tiger_ay)
                                             + '-'
                                             + str(tiger_gun))

        tiger_sorgu_sonucu = tiger_sorgusu['entries']
        print "\n---tiger_sorgusu sonucu---\n"
        print tiger_sorgu_sonucu

# sipno = "18-33438"
# get_recete_no = feedparser.parse("http://demo.7houseburger.com/UretimRecete/SipNo/" + sipno)
#
#
# if get_recete_no['entries'][0].values()[0]:
#     recete_no = get_recete_no['entries'][0].values()[0]
#     tarih = get_recete_no['entries'][1].values()[0]
#
#     yil = tarih.split('.')[2].split(' ')[0]
#     ay = tarih.split('.')[1]
#     gun = tarih.split('.')[0]
#
# print "recete no: ", recete_no
# print "tarih: ", tarih
# print "ay: ", ay
# print "yil: ", yil
# print "gun: ", gun
#
# get_recete_icerik = feedparser.parse("http://demo.7houseburger.com/Recete/ReceteNo/" + recete_no)
#
# for i in range(0, len(get_recete_icerik['entries'])):
#     if i % 2 == 0:
#         base64_malzeme_adi = base64.b64encode(get_recete_icerik['entries'][i].values()[0])
#         recetedeki_deger = get_recete_icerik['entries'][i + 1].values()[0]
#
#         go_to_malzeme = feedparser.parse("http://demo.7houseburger.com/Stok/Adi/"
#                                          + base64_malzeme_adi + '/'
#                                          + str(ay) + '-' + str(gun) + '-' + str(yil))
#
#         stok = go_to_malzeme['entries'][0].values()[0]
#
#         print "stok: ", stok
#
#         toplam_giren = feedparser.parse("http://demo.7houseburger.com/StokToplamGiren/Adi/" + base64_malzeme_adi
#                                         + '/'
#                                         + str(ay)
#                                         + '-'
#                                         + str(gun)
#                                         + '-'
#                                         + str(yil))
#
#         total_depo = toplam_giren['entries'][0].values()[0]
#
#         if ',' in total_depo:
#             float_total_depo = float((str(total_depo)).replace(',', '.'))
#         else:
#             float_total_depo = float(total_depo)
#         if ',' in stok:
#             float_stok = float((str(stok)).replace(',', '.'))
#         else:
#             float_stok = float(stok)
#
#         fark = float_total_depo - float_stok
#         toplam = 0.0
#
#         print "fark: ", fark
#         print "float stok: ", float_stok
#         print "float total depo: ", float_total_depo
#
#         for j in range(1, 1000):
#             get_step_count = feedparser.parse("http://demo.7houseburger.com/StokGiren/Adi/" + str(j)
#                                                  + '/'
#                                                  + base64_malzeme_adi
#                                                  + '/'
#                                                  + str(ay)
#                                                  + '-'
#                                                  + str(gun)
#                                                  + '-'
#                                                  + str(yil))
#             print "Adim Sayisi: ", j
#
#             if j == 1:
#                 toplam = toplam + float(get_step_count['entries'][0].values()[0])
#                 print "gelen deger: ", str(get_step_count['entries'][0].values()[0])
#             else:
#                 toplam = toplam + float(get_step_count['entries'][(len(get_step_count['entries']) - 1)].values()[0])
#                 print "gelen deger: ", str(get_step_count['entries'][(len(get_step_count['entries']) - 1)].values()[0])
#
#             print "toplam: ", toplam, " stok: ", stok
#
#
#             if toplam > float_stok:
#                 print toplam, " <- toplam buyuk stok -> " , stok
#                 sorgu_adimi = j
#                 break
#
#         tarih_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokTarih/" + sorgu_adimi
#                                          + '/'
#                                          + base64_malzeme_adi
#                                          + '/'
#                                          + str(ay)
#                                          + '-'
#                                          + str(gun)
#                                          + '-'
#                                          + str(yil))
#
#         if sorgu_adimi == 1:
#             bartex_tarih = get_recete_icerik['entries'][0].values()[0]
#         else:
#             bartex_tarih = get_recete_icerik['entries'][(len(get_recete_icerik['entries']) - 1)].values()[0]
#
#         """
#             gelecegim
#         """
#
#
#
#         tiger_sorgusu = feedparser.parse("http://demo.7houseburger.com/Tiger/" + base64_malzeme_adi
#                                               + '/'
#                                               + base64_malzeme_adi
#                                               + '/'
#                                               + str(yil)
#                                               + '-'
#                                               + str(ay)
#                                               + '-'
#                                               + str(gun))
#
#         """
#         """
#         bartex_dovizcinsi_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokDoviz/" + sorgu_adimi
#                                               + '/'
#                                               + base64_malzeme_adi
#                                               + '/'
#                                               + str(ay)
#                                               + '-'
#                                               + str(gun)
#                                               + '-'
#                                               + str(yil))
#
#         if sorgu_adimi == 1:
#             bartex_doviz = bartex_dovizcinsi_sorgusu['entries'][0].values()[0]
#         else:
#             bartex_doviz = bartex_dovizcinsi_sorgusu['entries'][(len(get_recete_icerik['entries']) - 1)].values()[0]
#
#         bartex_birim_sorgusu = feedparser.parse("http://demo.7houseburger.com/StokBirimFiyat/" + sorgu_adimi
#                                          + '/'
#                                          + base64_malzeme_adi
#                                          + '/'
#                                          + str(ay)
#                                          + '-'
#                                          + str(gun)
#                                          + '-'
#                                          + str(yil))
#
#         if sorgu_adimi == 1:
#             bartex_birim = bartex_birim_sorgusu['entries'][0].values()[0]
#         else:
#             bartex_birim = bartex_birim_sorgusu['entries'][(len(get_recete_icerik['entries']) - 1)].values()[0]
