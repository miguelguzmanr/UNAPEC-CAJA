from django.shortcuts import render
from django.contrib import messages
from . import models
from . import forms

# Create your views here.

def index(request):
  return render(request, 'index.html', {})

# Tipos de Cliente

def tipos_cliente(request):
  return render(request, 'tipos_cliente/index.html', {'tipos_cliente': models.TipoCliente.objects.all(), 'messages': messages.get_messages(request)})


def tipo_cliente_create(request):
  if request.method == 'POST':
    form = forms.TipoClienteForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_cliente/create.html', {})


def tipo_cliente_update(request, tipo_cliente_id):
  tipo_cliente = models.TipoCliente.objects.get(pk=tipo_cliente_id)

  if request.method == 'POST':
    form = forms.TipoClienteForm(request.POST or None, instance=tipo_cliente)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_cliente(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_cliente/update.html', {'tipo_cliente': tipo_cliente})


def tipo_cliente_delete(request, tipo_cliente_id):
  models.TipoCliente.objects.get(pk=tipo_cliente_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return tipos_cliente(request)

# Carreras

def carreras(request):
  return render(request, 'carreras/index.html', {'carreras': models.Carrera.objects.all(), 'messages': messages.get_messages(request)})


def carrera_create(request):
  if request.method == 'POST':
    form = forms.CarreraForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'carreras/create.html', {})


def carrera_update(request, carrera_id):
  carrera = models.Carrera.objects.get(pk=carrera_id)

  if request.method == 'POST':
    form = forms.CarreraForm(request.POST or None, instance=carrera)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return carreras(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'carreras/update.html', {'carrera': carrera})


def carrera_delete(request, carrera_id):
  models.Carrera.objects.get(pk=carrera_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return carreras(request)

# Productos

def productos(request):
  return render(request, 'productos/index.html', {'productos': models.Producto.objects.all(), 'messages': messages.get_messages(request)})


def producto_create(request):
  if request.method == 'POST':
    form = forms.ProductoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'productos/create.html', {})


def producto_update(request, producto_id):
  producto = models.Producto.objects.get(pk=producto_id)

  if request.method == 'POST':
    form = forms.ProductoForm(request.POST or None, instance=producto)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return productos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'productos/update.html', {'producto': producto})


def producto_delete(request, producto_id):
  models.Producto.objects.get(pk=producto_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return productos(request)

# Horarios

def horarios(request):
  return render(request, 'horarios/index.html', {'horarios': models.Horario.objects.all(), 'messages': messages.get_messages(request)})


def horario_create(request):
  if request.method == 'POST':
    form = forms.HorarioForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/create.html', {})


def horario_update(request, horario_id):
  horario = models.Horario.objects.get(pk=horario_id)

  if request.method == 'POST':
    form = forms.HorarioForm(request.POST or None, instance=horario)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return horarios(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/update.html', {'horario': horario})


def horario_delete(request, horario_id):
  models.Horario.objects.get(pk=horario_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return horarios(request)

# Formas de Pago

def formas_pago(request):
  return render(request, 'formas_pago/index.html', {'formas_pago': models.FormaPago.objects.all(), 'messages': messages.get_messages(request)})


def forma_pago_create(request):
  if request.method == 'POST':
    form = forms.FormaPagoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'formas_pago/create.html', {})


def forma_pago_update(request, forma_pago_id):
  forma_pago = models.FormaPago.objects.get(pk=forma_pago_id)

  if request.method == 'POST':
    form = forms.FormaPagoForm(request.POST or None, instance=forma_pago)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return formas_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'formas_pago/update.html', {'forma_pago': forma_pago})


def forma_pago_delete(request, forma_pago_id):
  models.FormaPago.objects.get(pk=forma_pago_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return formas_pago(request)

# Modalidades de Pago

def modos_pago(request):
  return render(request, 'modos_pago/index.html', {'modos_pago': models.ModoPago.objects.all(), 'messages': messages.get_messages(request)})


def modo_pago_create(request):
  if request.method == 'POST':
    form = forms.ModoPagoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'modos_pago/create.html', {})


def modo_pago_update(request, modo_pago_id):
  modo_pago = models.ModoPago.objects.get(pk=modo_pago_id)

  if request.method == 'POST':
    form = forms.ModoPagoForm(request.POST or None, instance=modo_pago)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return modos_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'modos_pago/update.html', {'modo_pago': modo_pago})


def modo_pago_delete(request, modo_pago_id):
  models.ModoPago.objects.get(pk=modo_pago_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return modos_pago(request)

# Tipos de Documento

def tipos_documento(request):
  return render(request, 'tipos_documento/index.html', {'tipos_documento': models.TipoDocumento.objects.all(), 'messages': messages.get_messages(request)})


def tipo_documento_create(request):
  if request.method == 'POST':
    form = forms.TipoDocumentoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_documento/create.html', {})


def tipo_documento_update(request, tipo_documento_id):
  tipo_documento = models.TipoDocumento.objects.get(pk=tipo_documento_id)

  if request.method == 'POST':
    form = forms.TipoDocumentoForm(request.POST or None, instance=tipo_documento)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_documento(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_documento/update.html', {'tipo_documento': tipo_documento})


def tipo_documento_delete(request, tipo_documento_id):
  models.TipoDocumento.objects.get(pk=tipo_documento_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return tipos_documento(request)
