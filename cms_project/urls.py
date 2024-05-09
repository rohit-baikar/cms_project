from django.contrib import admin
from django.urls import path
from cmsapp.views import ulogin, usignup, urnp, uhome, ulogout, showdept, adddept, removedept, showstudent, addstudent, removestudent, updatestudent
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", uhome, name="uhome"),
    path("ulogin", ulogin, name="ulogin"),
    path("usignup", usignup, name="usignup"),
    path("ulogout", ulogout, name="ulogout"),
    path("urnp", urnp, name="urnp"),
    path("showdept", showdept, name="showdept"),
    path("adddept", adddept, name="adddept"),
    path("removedept/<int:id>", removedept, name="removedept"),
    path("showstudent", showstudent, name="showstudent"),
    path("addstudent", addstudent, name="addstudent"),
    path("removestudent/<int:id>", removestudent, name="removestudent"),
    path("updatestudent/<int:id>", updatestudent, name="updatestudent"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

