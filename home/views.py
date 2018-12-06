from django.shortcuts import render_to_response, render, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from authentico.models import User
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
