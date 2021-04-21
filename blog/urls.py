from django.urls import path, include
from blog.views import IletisimFormView, anasayfa, KategoriListView, yazilarim, DetayView, YaziEkleCreateView, YaziGuncelleUpdateView, \
    YaziSilDeleteView, yorum_sil
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim/', IletisimFormView.as_view(), name='iletisim'),
    path('yonlendir/', RedirectView.as_view(url='https://www.getbootstrap.com/'), name='yonlendir'),
    path('hakkimda/', TemplateView.as_view(template_name='pages/hakkimda.html'), name='hakkimda'),
    path('kategori/<slug:kategoriSlug>', KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi-sil'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name='yazi-ekle'),
    path('yorum-sil/<int:id>', yorum_sil, name='yorum-sil'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),

]
