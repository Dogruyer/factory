from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

'''
    Url List:
    
    * planlar 
        - /planlar -> url: Planlar/SipNo/{id}
    * giris
        - /giris -> url: Giris/PartiNo/{id}
    * patrecete
        - /patrecete -> url: PatRecete/Pat/{pat-adi}
    * uretimrecete
        - /uretimrecete -> url: UretimRecete/SipNo/{id}
    * recetedesen
        - /recetedesen -> url: ReceteDesen/SipNo/{id}
    * girisfiyatlar
        - /girisfiyatlar -> url: /GirisFiyatlar/PartiNo/BAL-306605
    * gmm
        - /gmm-> url: GMMTablo/SipNo/{id}
    * hammadde
        - /hammadde -> url:
                        - SiparisFoyu/SipNo/
                        - GirisFiyatlar/PartiNo/
    * malzeme
        - /malzeme -> url: MalzemeHareketi/Adi/
    * ops
        - /ops -> url: Ops/SipNo/
    * prg
        - /prg -> url: Prg/SipNo/
    * siparisfoyu
        - /siparisfoyu -> SiparisFoyu/SipNo/
'''

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

                       url(r'^test$',
                           'home.views.test',
                           name='test'),

                       url(r'^login$',
                           'authentico.views.login',
                           name='login'),

                       url(r'^register$',
                           'authentico.views.register',
                           name='register'),

                       url(r'^logout$',
                           'authentico.views.logout',
                           name='logout'),

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