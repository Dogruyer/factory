# siparis_no = query["entries"][1].values()[0]
# siparis_no = siparis_no.replace("/", "-")
#
# son_query = feedparser.parse("http://demo.7houseburger.com/Planlar/SipNo/" + str(siparis_no))
# result_array = son_query["entries"]


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
