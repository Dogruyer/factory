from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'home.views.planlar',
                           name='planlarhome'),

                       url(r'^giris$',
                           'home.views.giris',
                           name='giris'),

                       url(r'^patrecete$',
                           'home.views.patrecete',
                           name='patrecete'),

                       url(r'^uretimrecete$',
                           'home.views.uretimrecete',
                           name='uretimrecete'),

                       url(r'^recetedesen$',
                           'home.views.recetedesen',
                           name='recetedesen'),

                       url(r'^girisfiyatlar$',
                           'home.views.girisfiyatlar',
                           name='girisfiyatlar'),

                       url(r'^gmm$',
                           'home.views.gmm',
                           name='gmm'),

                       url(r'^hammadde$',
                           'home.views.hammadde',
                           name='hammadde'),

                       url(r'^malzeme$',
                           'home.views.malzeme',
                           name='malzeme'),

                       url(r'^ops$',
                           'home.views.ops',
                           name='ops'),

                       url(r'^planlar$',
                           'home.views.planlar',
                           name='planlar'),

                       url(r'^prg',
                           'home.views.prg',
                           name='prg'),

                       url(r'^siparisfoyu$',
                           'home.views.siparisfoyu',
                           name='siparisfoyu'),

                       # url(r'^$',
                       #     'home.views.home',
                       #     name='home'),
                       # # url(r'^login$',
                       #     'authentico.views.login',
                       #     name='login'),
                       #
                       # url(r'^register$',
                       #     'authentico.views.register',
                       #     name='register'),
                       #
                       # url(r'^logout$',
                       #     'authentico.views.logout',
                       #     name='logout'),
                       #
                       # url(r'^test$',
                       #     'home.views.test',
                       #     name='test'),
                       #
                       # url(r'^sorgu$',
                       #     'home.views.sorgu',
                       #     name='sorgu'),
                       #
                       # url(r'^proje/ekle$',
                       #     'home.views.projeekle',
                       #     name='projeekle'),
                       #
                       # url(r'^musteri/ekle$',
                       #     'home.views.musteriekle',
                       #     name='musteriekle'),
                       #
                       # url(r'^gorev/ekle$',
                       #     'home.views.gorevekle',
                       #     name='gorevekle'),
                       #
                       # url(r'^duzenle/(?P<username>\w+)',
                       #     'home.views.duzenle_kullanici',
                       #      name='duzenle_kullanici'),

                       )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )