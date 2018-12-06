from django.shortcuts import render_to_response, render, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from authentico.models import User
from .forms import GorevEkle, MusteriEkle, ProjeEkle
from .models import Gorev, Musteri, Proje
import feedparser
# import xlrd, unicodedata'
# import pandas as pd


# done 30.11.2018 - 11:45 Cuma
def planlar(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")
        query = feedparser.parse("http://demo.7houseburger.com/Planlar/SipNo/" + str(siparisno))

        result_array = query["entries"]

        # siparis_no = query["entries"][1].values()[0]
        # siparis_no = siparis_no.replace("/", "-")
        #
        # son_query = feedparser.parse("http://demo.7houseburger.com/Planlar/SipNo/" + str(siparis_no))
        # result_array = son_query["entries"]

        c = {"request": request,
             "result_array": result_array}

        c.update(csrf(request))

        return render(request, "sonuc/planlar.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/planlar.html", c)


# done 30.11.2018 - 11:45 Cuma
def gmm(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/GMMTablo/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/gmm.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/gmm.html", c)


# done 30.11.2018 - 11:45 Cuma
def hammadde(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")
        partinoogren = feedparser.parse("http://demo.7houseburger.com/SiparisFoyu/SipNo/" + siparisno)

        partino = partinoogren["entries"][6].values()[0]
        metraj = partinoogren["entries"][4].values()[0]

        partino_yeni = partino.replace("/", "-")
        girisfiyatlar = feedparser.parse("http://demo.7houseburger.com/GirisFiyatlar/PartiNo/" + partino_yeni)

        if girisfiyatlar["entries"]:
            if girisfiyatlar["entries"][1].values()[0] and girisfiyatlar["entries"][1].values()[0] != 0:
                # tl
                alim_fiyati = girisfiyatlar["entries"][1].values()[0]

            elif girisfiyatlar["entries"][2].values()[0] and girisfiyatlar["entries"][2].values()[0] != 0:
                # euro
                alim_fiyati = girisfiyatlar["entries"][2].values()[0]

            elif girisfiyatlar["entries"][3].values()[0] and girisfiyatlar["entries"][3].values()[0] != 0:
                #tl
                alim_fiyati = girisfiyatlar["entries"][3].values()[0]

            elif girisfiyatlar["entries"][4].values()[0] and girisfiyatlar["entries"][4].values()[0] != 0:
                # euro
                alim_fiyati = girisfiyatlar["entries"][4].values()[0]
            else:
                alim_fiyati = 0
        else:
            alim_fiyati = 0

        if alim_fiyati != 0:
            a = int(alim_fiyati.split(',')[0])
        else:
            a = 0

        b = int(metraj.split(',')[0])

        toplam_ham_maliyet = a * b

        c = {"request": request,
             "siparisno": siparisno,
             "toplam_ham_maliyet": toplam_ham_maliyet,
             "alim_fiyati": alim_fiyati,
             "metraj": metraj,
             "partino": partino,
             }

        c.update(csrf(request))

        return render(request, "sonuc/hammadde.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/hammadde.html", c)


# done 30.11.2018 - 11:45 Cuma
def ops(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/Ops/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/ops.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/ops.html", c)


# tamamlanmadi
def malzeme(request):
    if request.POST:
        malzeme_adi = request.POST["malzeme"]
        encoded_malzeme_adi = malzeme_adi.encode('utf-8')
        base64_malzeme_adi = base64.b64encode(encoded_malzeme_adi)

        query = feedparser.parse("http://demo.7houseburger.com/MalzemeHareketi/Adi/" + base64_malzeme_adi)
        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/malzeme.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/malzeme.html", c)


# done 30.11.2018 - 11:45 Cuma
def giris(request):
    if request.POST:
        partino = request.POST["partino"]
        partino = partino.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/Giris/PartiNo/" + str(partino))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/giris.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/giris.html", c)


# done 30.11.2018 - 11:45 Cuma
def prg(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/Prg/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/prg.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/prg.html", c)


# done 30.11.2018 - 11:45 Cuma
def siparisfoyu(request):
    if request.POST:
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/SiparisFoyu/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}
        c.update(csrf(request))

        return render(request, "sonuc/siparisfoyu.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/siparisfoyu.html", c)


# done 30.11.2018 - 11:45 Cuma
def patrecete(request):
    if request.POST:
        patrecete = request.POST["patrecete"]
        encoded_patrecete = base64.b64encode(patrecete)

        query = feedparser.parse("http://demo.7houseburger.com/PatRecete/Pat/" + str(encoded_patrecete))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/patrecete.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/patrecete.html", c)


def uretimrecete(request):
    if request.POST:
        # siparis_no = sipno["entries"][5].values()[0]
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/UretimRecete/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/uretimrecete.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/uretimrecete.html", c)


def recetedesen(request):
    if request.POST:
        # siparis_no = sipno["entries"][2].values()[0]
        sipno = request.POST["sipno"]
        siparisno = sipno.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/ReceteDesen/SipNo/" + str(siparisno))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/recetedesen.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/recetedesen.html", c)


def girisfiyatlar(request):
    if request.POST:
        partino = request.POST["partino"]
        partino = partino.replace("/", "-")

        query = feedparser.parse("http://demo.7houseburger.com/GirisFiyatlar/PartiNo/" + str(partino))

        result_array = query["entries"]

        c = {"request": request,
             "result_array": result_array,
             "counter": functools.partial(next, itertools.count())}

        c.update(csrf(request))

        return render(request, "sonuc/girisfiyatlar.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "factory/girisfiyatlar.html", c)


# def senaryo(request):
#     if request.POST:
#
#         senaryo_sipno = request.POST["senaryo"]
#         # encoded = base64.b64encode(gelen)
#         ilksorgu = feedparser.parse("http://demo.7houseburger.com/ReceteDesen/SipNo/" + senaryo_sipno)
#
#         desen_no = ilksorgu["entries"][3].values()[0]
#         varyant = ilksorgu["entries"][4].values()[0]
#
#         recetesorgu = feedparser.parse("http://demo.7houseburger.com/Recete/DesenVaryant/" + desen_no + "-" + varyant)
#         kac_tane_ad_geldi = len(recetesorgu["entries"])
#
#         for i in range(0,kac_tane_ad_geldi):
#             if not "Pat" in recetesorgu["entries"][i].values()[i]:
#                 encodelanmis_ad = base64.b64encode(recetesorgu["entries"][i].values()[i])
#
#                 malzemesorgu = feedparser.parse("http://demo.7houseburger.com/MalzemeHareketi/Adi/" + encodelanmis_ad)
#
#                 kactanegeldi = len(malzemesorgu["entries"])
#                 kac_satir = kactanegeldi / 20
#
#                 toplam_depoya_giren = 0
#                 toplam_cekilen_miktar = 0
#
#                 for j in range(0, int(kac_satir)):
#                     toplam_depoya_giren = toplam_depoya_giren + malzemesorgu["entries"][6].values()[0]
#                     toplam_cekilen_miktar = toplam_cekilen_miktar + malzemesorgu["entries"][7].values()[0]
#
#                 fark = toplam_depoya_giren - toplam_cekilen_miktar
#
#
#         result_array = query["entries"]
#         kontrol = 0
#         c = {"request": request,
#              "kontrol": kontrol,
#              "result_array": result_array,
#              "counter": functools.partial(next, itertools.count())}
#
#         c.update(csrf(request))
#
#         return render(request, "sonuc/malzeme.html", c)
#
#     c = {"request": request}
#     c.update(csrf(request))
#
#     return render(request, "factory/malzeme.html", c)
#
#
# def blank(request):
#     return render_to_response("blank.html")
#
#
# def home(request):
#     tum_gorevler = Gorev.objects.all()
#     tum_projeler = Proje.objects.all()
#     tum_musteriler = Musteri.objects.all()
#     tum_kullanicilar = User.objects.all()
#
#     c = {"request": request,
#          "tum_gorevler": tum_gorevler,
#          "tum_kullanicilar": tum_kullanicilar,
#          "tum_musteriler": tum_musteriler,
#          "tum_projeler": tum_projeler}
#
#     c.update(csrf(request))
#
#     return render_to_response("home/home.html", c)
#
#
# def duzenle_kullanici(request, username):
#     getirilen_kullanici = User.objects.get(username=username)
#
#     return HttpResponse(getirilen_kullanici.email)
#
#
# def musteri_duzenle(request, id):
#     duzenlenecek_musteri = Musteri.objects.get(username=id)
#
#     c = {"request": request,
#          "duzenlenecek_musteri": duzenlenecek_musteri}
#
#     c.update(csrf(request))
#
#     return render_to_response("add/musteri-ekle.html", c)
#
#
# def musteriekle(request):
#     if request.POST:
#         yeni_musteri = MusteriEkle()
#
#         # yeni_musteri.title = request.POST["title"]
#         # yeni_musteri.content = request.POST["content"]
#         # yeni_musteri.active = request.POST["aktif-select"]
#
#         yeni_musteri.save()
#
#         c = {"request": request}
#         c.update(csrf(request))
#
#         return render_to_response("home/home.html", c)
#
#     form = MusteriEkle()
#
#     c = {"form": form,
#          "request": request}
#
#     c.update(csrf(request))
#
#     return render(request, "add/musteri-ekle.html", c)
#
#
# def gorevekle(request):
#     if request.POST:
#         user = request.POST["user-select"]
#         proje = request.POST["proje-select"]
#         musteri = request.POST["musteri-select"]
#
#         current_user = User.objects.filter(username=user)
#         current_proje = Proje.objects.filter(title=proje)
#         current_musteri = Musteri.objects.filter(title=musteri)
#
#         yeni_gorev = Gorev()
#
#         yeni_gorev.title = request.POST["title"]
#         yeni_gorev.which_musteri = current_musteri[0]
#         yeni_gorev.which_user = current_user[0]
#         yeni_gorev.which_proje = current_proje[0]
#
#         yeni_gorev.save()
#
#         c = {"request":request}
#         c.update(csrf(request))
#
#         return render_to_response("home/home.html", c)
#
#     form = GorevEkle()
#     tum_kullanicilar = User.objects.all()
#     tum_projeler = Proje.objects.all()
#     tum_musteriler = Musteri.objects.all()
#
#     c = {"form": form,
#          "tum_kullanicilar": tum_kullanicilar,
#          "tum_projeler": tum_projeler,
#          "tum_musteriler": tum_musteriler,
#          "request": request}
#
#     c.update(csrf(request))
#
#     return render(request, "add/gorev-ekle.html", c)
#
#
# def projeekle(request):
#     if request.POST:
#         yeni_proje = Proje()
#
#         yeni_proje.title = request.POST["title"]
#         yeni_proje.content = request.POST["content"]
#         yeni_proje.active = request.POST["aktif-select"]
#         yeni_proje.deadline = request.POST["deadline"]
#
#         yeni_proje.save()
#
#         c = {"request": request}
#         c.update(csrf(request))
#
#         return render_to_response("home/home.html", c)
#
#     form = ProjeEkle()
#
#     c = {"form": form,
#          "request": request}
#
#     c.update(csrf(request))
#
#     return render(request, "add/proje-ekle.html", c)
#
#
# def musteriduzenle(request):
#     return HttpResponse("musteri duzenle")
#
#
# def gorevduzenle(request):
#     return HttpResponse("musteri duzenle")
#
#
# def projeduzenle(request):
#     return HttpResponse("proje duzenle")



# def test(request):
#     book = xlrd.open_workbook('1.xlsx')
#     dizi = []
#
#     # for sheet in book.sheets():
#     #     print sheet.name
#
#     sheet = book.sheet_by_name('offene EK-Positionen F01')
#     toplam_girdi = sheet.nrows
#
#     # for i in range(sheet.nrows):
#     #     dizi.append(sheet.row_values(i))
#
#     # for i in xrange(sheet.nrows):
#     #     row = sheet.row_values(i)
#     #     for cell in row:
#     #         dizi.append(cell)
#
#     # count = 0
#     # for i in xrange(sheet.nrows):
#     #     if count < 10:
#     #         row = sheet.row_values(i)
#     #         dizi.append(row)
#     #
#     #     count += 1
#
#     # count = 0
#     # for i in xrange(sheet.nrows):
#     #     if count < 1:
#     #         if i >= 0:
#     #             row = sheet.row_values(i)
#     #             dizi.append(row)
#     #         count += 1
#
#
#     c = {"toplam_girdi": toplam_girdi,
#          "dizi": dizi,
#          "request": request}
#
#     c.update(csrf(request))
#
#     return render(request, "test.html", c)


# def sorgu(request):
#
#     c = {"request": request}
#     c.update(csrf(request))
#
#     return render(request, "factory/sorgu-calistir.html", c)