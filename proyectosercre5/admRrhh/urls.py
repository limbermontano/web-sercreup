
from django.urls import path
from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from . import views
from .views import user_login
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.iniciar, name='iniciar' ),
    path('base/',views.base, name='base' ),
    path('grafana_etapas',views.grafana_etapas, name='grafana_etapas' ),
    # path('login_view',views.login_view, name='login_view' ),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('login/', user_login, name='login'),
    # path('loginus', views.loginus, name='loginus'),
    #/////AREA
    path('areLista',views.areLista, name='areLista'),
    path('areCrear',views.areCrear, name='areCrear'),
    path('areGuardar',views.areGuardar, name='areGuardar'),
    path('areEditar/<int:id>',views.areEditar, name='areEditar'),
    path('areActualizar/<int:id>',views.areActualizar, name='areActualizar'),
    path('areEliminar/<int:id>',views.areEliminar, name='areEliminar'),
    #/////Cargo
    path('cargLista',views.cargLista, name='cargLista'),
    path('cargCrear',views.cargCrear, name='cargCrear'),
    path('cargGuardar',views.cargGuardar, name='cargGuardar'),
    path('cargEditar/<int:id>',views.cargEditar, name='cargEditar'),
    path('cargActualizar/<int:id>',views.cargActualizar, name='cargActualizar'),
    path('cargEliminar/<int:id>',views.cargEliminar, name='cargEliminar'),
        #/////DOCUMENTO
    path('docLista',views.docLista, name='docLista'),
    path('docCrear',views.docCrear, name='docCrear'),
    path('docGuardar',views.docGuardar, name='docGuardar'),
    path('docEditar/<int:id>',views.docEditar, name='docEditar'),
    path('docActualizar/<int:id>',views.docActualizar, name='docActualizar'),
    path('docEliminar/<int:id>',views.docEliminar, name='docEliminar'),
        #/////ESTUDIO
    path('estLista',views.estLista, name='estLista'),
    path('estCrear',views.estCrear, name='estCrear'),
    path('estGuardar',views.estGuardar, name='estGuardar'),
    path('estEditar/<int:id>',views.estEditar, name='estEditar'),
    path('estActualizar/<int:id>',views.estActualizar, name='estActualizar'),
    path('estEliminar/<int:id>',views.estEliminar, name='estEliminar'),
        #/////PROFESION
    path('profLista',views.profLista, name='profLista'),
    path('profCrear',views.profCrear, name='profCrear'),
    path('profGuardar',views.profGuardar, name='profGuardar'),
    path('profEditar/<int:id>',views.profEditar, name='profEditar'),
    path('profActualizar/<int:id>',views.profActualizar, name='profActualizar'),
    path('profEliminar/<int:id>',views.profEliminar, name='profEliminar'),
        #/////PERSONA
    path('perLista',views.perLista, name='perLista'),
    path('perCrear',views.perCrear, name='perCrear'),
    path('perGuardar',views.perGuardar, name='perGuardar'),
    path('perEditar/<int:id>',views.perEditar, name='perEditar'),
    path('perActualizar/<int:id>',views.perActualizar, name='perActualizar'),
    path('perEliminar/<int:id>',views.perEliminar, name='perEliminar'),
    path('perTarjeta/<int:id>',views.perTarjeta, name='perTarjeta'),
         #/////PERSONAL
    path('perlLista',views.perlLista, name='perlLista'),
    path('perlCrear',views.perlCrear, name='perlCrear'),
    path('perlGuardar',views.perlGuardar, name='perlGuardar'),
    path('perlEditar/<int:id>',views.perlEditar, name='perlEditar'),
    path('perlActualizar/<int:id>',views.perlActualizar, name='perlActualizar'),
    path('perlEliminar/<int:id>',views.perlEliminar, name='perlEliminar'),
         #/////ZONA
    path('zonLista',views.zonLista, name='zonLista'),
    path('zonCrear',views.zonCrear, name='zonCrear'),
    path('zonGuardar',views.zonGuardar, name='zonGuardar'),
    path('zonEditar/<int:id>',views.zonEditar, name='zonEditar'),
    path('zonActualizar/<int:id>',views.zonActualizar, name='zonActualizar'),
    path('zonEliminar/<int:id>',views.zonEliminar, name='zonEliminar'),
        #/////FISCAL
    path('fisLista',views.fisLista, name='fisLista'),
    path('fisCrear',views.fisCrear, name='fisCrear'),
    path('fisGuardar',views.fisGuardar, name='fisGuardar'),
    path('fisEditar/<int:id>',views.fisEditar, name='fisEditar'),
    path('fisActualizar/<int:id>',views.fisActualizar, name='fisActualizar'),
    path('fisEliminar/<int:id>',views.fisEliminar, name='fisEliminar'),
        #/////PROYECTO
    path('proyLista',views.proyLista, name='proyLista'),
    path('proyCrear',views.proyCrear, name='proyCrear'),
    path('proyGuardar',views.proyGuardar, name='proyGuardar'),
    path('proyEditar/<int:id>',views.proyEditar, name='proyEditar'),
    path('proyActualizar/<int:id>',views.proyActualizar, name='proyActualizar'),
    path('proyEliminar/<int:id>',views.proyEliminar, name='proyEliminar'),
        #/////MAESTRO
    path('proyEditarDetall/<int:id>',views.proyEditarDetall, name='proyEditarDetall'),
    path('proyDetalleM/<int:id>',views.proyDetalleM, name='proyDetalleM'),
    path('asigGuardetalle',views.asigGuardetalle, name='asigGuardetalle'),
    path('asigEliminarD/<int:id>',views.asigEliminarD, name='asigEliminarD'),
        #/////ASIGNACION
    path('asigLista',views.asigLista, name='asigLista'),
    path('asigCrear',views.asigCrear, name='asigCrear'),
    path('asigGuardar',views.asigGuardar, name='asigGuardar'),
    path('asigEditar/<int:id>',views.asigEditar, name='asigEditar'),
    path('asigActualizar/<int:id>',views.asigActualizar, name='asigActualizar'),
    path('asigEliminar/<int:id>',views.asigEliminar, name='asigEliminar'),
        #/////PARENTESCO
    path('parLista',views.parLista, name='parLista'),
    path('parCrear',views.parCrear, name='parCrear'),
    path('parGuardar',views.parGuardar, name='parGuardar'),
    path('parEditar/<int:id>',views.parEditar, name='parEditar'),
    path('parActualizar/<int:id>',views.parActualizar, name='parActualizar'),
    path('parEliminar/<int:id>',views.parEliminar, name='parEliminar'),
        #/////FAMILIAR
    path('famLista',views.famLista, name='famLista'),
    path('famCrear',views.famCrear, name='famCrear'),
    path('famGuardar',views.famGuardar, name='famGuardar'),
    path('famEditar/<int:id>',views.famEditar, name='famEditar'),
    path('famActualizar/<int:id>',views.famActualizar, name='famActualizar'),
    path('famEliminar/<int:id>',views.famEliminar, name='famEliminar'),
        #/////ENVIO
    path('envLista',views.envLista, name='envLista'),
    path('envCrear',views.envCrear, name='envCrear'),
    path('envGuardar',views.envGuardar, name='envGuardar'),
    path('envEditar/<int:id>',views.envEditar, name='envEditar'),
    path('envActualizar/<int:id>',views.envActualizar, name='envActualizar'),
    path('envEliminar/<int:id>',views.envEliminar, name='envEliminar'),
        #/////ORDEN DE TRABAJO
    path('ordLista',views.ordLista, name='ordLista'),

    path('ordCrear',views.ordCrear, name='ordCrear'),
    path('ordGuardar',views.ordGuardar, name='ordGuardar'),
    path('ordEditar/<int:id>',views.ordEditar, name='ordEditar'),
    path('ordActualizar/<int:id>',views.ordActualizar, name='ordActualizar'),
    path('ordEliminar/<int:id>',views.ordEliminar, name='ordEliminar'),
        #/////// USUARIO
    path('permDetalleM/<int:id>',views.permDetalleM, name='permDetalleM'),
    path('permEditarDetall/<int:id>',views.permEditarDetall, name='permEditarDetall'),
    path('userPermLista',views.userPermLista, name='userPermLista'),
    path('usuLista',views.usuLista, name='usuLista'),
    path('usuCrear',views.usuCrear, name='usuCrear'),
    path('usuGuardar',views.usuGuardar, name='usuGuardar'),
    path('usuEditar/<int:id>',views.usuEditar, name='usuEditar'),
    path('usuActualizar/<int:id>',views.usuActualizar, name='usuActualizar'),
    path('usuEliminar/<int:id>',views.usuEliminar, name='usuEliminar'),
    
    #///////////PERMISOS
    path('permLista',views.permLista, name='permLista'),
    path('permCrear',views.permCrear, name='permCrear'),
    path('permGuardar',views.permGuardar, name='permGuardar'),
    path('permEditar/<int:id>',views.permEditar, name='permEditar'),
    path('permActualizar/<int:id>',views.permActualizar, name='permActualizar'),
        #///////////USER-PERMISOS
    path('rolPermGuardar',views.rolPermGuardar, name='rolPermGuardar'),
    path('userRolGuardar',views.userRolGuardar, name='userRolGuardar'),
    path('userRolEliminar/<int:usuario_id>/<int:grupo_id>/', views.userRolEliminar, name='userRolEliminar'),
        #/////ROLES
    path('rolLista',views.rolLista, name='rolLista'),
    path('rolCrear',views.rolCrear, name='rolCrear'),
    path('rolGuardar',views.rolGuardar, name='rolGuardar'),
    path('rolEditar/<int:id>',views.rolEditar, name='rolEditar'),
    path('rolActualizar/<int:id>',views.rolActualizar, name='rolActualizar'),
    path('rolEliminar/<int:id>',views.rolEliminar, name='rolEliminar'),
    path('permDetalle/<int:id>',views.permDetalle, name='permDetalle'),
    path('rolPermEliminar/<int:grupo_id>/<int:permiso_id>/>',views.rolPermEliminar, name='rolPermEliminar'),
        #////////////////REPORTES
    path('reproyLista',views.reproyLista, name='reproyLista'),
    path('repListapdf',views.repListapdf, name='repListapdf'),
    path('export_pdf2', views.export_pdf2, name="export_pdf2" ),
    path('repinicio',views.repinicio, name='repinicio'),
    path('repestacado',views.repestacado, name='repestacado'),
    path('repdigitacion',views.repdigitacion, name='repdigitacion'),
    path('repplano',views.repplano, name='repplano'),
    path('repenvio',views.repenvio, name='repenvio'),
    path('repersonal',views.repersonal, name='repersonal'),
        #///REPORTES PDF
    path('repestacado_pdf2', views.repestacado_pdf2, name="repestacado_pdf2" ),
    path('repenvio_pdf2', views.repenvio_pdf2, name="repenvio_pdf2" ),
    path('export-pdf1/<int:id>', views.export_pdf1, name="export-pdf1" ),
    path('proyListapdf/<int:id>',views.proyListapdf, name='proyListapdf'),
    #/////MODALES
    path('areGuardarM',views.areGuardarM, name='areGuardarM'),
    path('cargGuardarM',views.cargGuardarM, name='cargGuardarM'),
    path('profGuardarM',views.profGuardarM, name='profGuardarM'),
    #OTROS
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)