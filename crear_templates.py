#!/usr/bin/env python3
"""
Script para crear automáticamente todos los templates del proyecto Logística Global
Ejecutar desde la raíz del proyecto Django
"""

import os

# Configuración base
BASE_DIR = "transporte/templates"

# Definición de entidades y sus campos
ENTIDADES = {
    'ruta': {
        'nombre_singular': 'Ruta',
        'nombre_plural': 'Rutas',
        'icono': '🗺️',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'origen', 'label': 'Origen'},
            {'nombre': 'destino', 'label': 'Destino'},
            {'nombre': 'tipo_transporte', 'label': 'Tipo Transporte'},
            {'nombre': 'distancia_km', 'label': 'Distancia (km)'},
        ]
    },
    'vehiculo': {
        'nombre_singular': 'Vehículo',
        'nombre_plural': 'Vehículos',
        'icono': '🚚',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'patente', 'label': 'Patente'},
            {'nombre': 'tipo_vehiculo', 'label': 'Tipo'},
            {'nombre': 'capacidad_kg', 'label': 'Capacidad (kg)'},
            {'nombre': 'activo', 'label': 'Estado', 'tipo': 'boolean'},
        ]
    },
    'aeronave': {
        'nombre_singular': 'Aeronave',
        'nombre_plural': 'Aeronaves',
        'icono': '✈️',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'matricula', 'label': 'Matrícula'},
            {'nombre': 'tipo_aeronave', 'label': 'Tipo'},
            {'nombre': 'capacidad_kg', 'label': 'Capacidad (kg)'},
            {'nombre': 'activo', 'label': 'Estado', 'tipo': 'boolean'},
        ]
    },
    'conductor': {
        'nombre_singular': 'Conductor',
        'nombre_plural': 'Conductores',
        'icono': '👨‍✈️',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'nombre', 'label': 'Nombre'},
            {'nombre': 'rut', 'label': 'RUT'},
            {'nombre': 'licencia', 'label': 'Licencia'},
            {'nombre': 'activo', 'label': 'Estado', 'tipo': 'boolean'},
        ]
    },
    'piloto': {
        'nombre_singular': 'Piloto',
        'nombre_plural': 'Pilotos',
        'icono': '👨‍✈️',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'nombre', 'label': 'Nombre'},
            {'nombre': 'rut', 'label': 'RUT'},
            {'nombre': 'certificacion', 'label': 'Certificación'},
            {'nombre': 'activo', 'label': 'Estado', 'tipo': 'boolean'},
        ]
    },
    'cliente': {
        'nombre_singular': 'Cliente',
        'nombre_plural': 'Clientes',
        'icono': '👥',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'nombre', 'label': 'Nombre'},
            {'nombre': 'rut', 'label': 'RUT'},
            {'nombre': 'telefono', 'label': 'Teléfono'},
            {'nombre': 'correo_electronico', 'label': 'Email'},
        ]
    },
    'carga': {
        'nombre_singular': 'Carga',
        'nombre_plural': 'Cargas',
        'icono': '📦',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'descripcion', 'label': 'Descripción'},
            {'nombre': 'peso_kg', 'label': 'Peso (kg)'},
            {'nombre': 'volumen_m3', 'label': 'Volumen (m³)'},
            {'nombre': 'cliente', 'label': 'Cliente'},
        ]
    },
    'despacho': {
        'nombre_singular': 'Despacho',
        'nombre_plural': 'Despachos',
        'icono': '📋',
        'campos_mostrar': [
            {'nombre': 'id', 'label': 'ID'},
            {'nombre': 'fecha_despacho', 'label': 'Fecha'},
            {'nombre': 'estado', 'label': 'Estado'},
            {'nombre': 'costo_envio', 'label': 'Costo'},
            {'nombre': 'ruta', 'label': 'Ruta'},
        ]
    },
}


def crear_directorios():
    """Crea la estructura de directorios"""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    
    for entidad in ENTIDADES.keys():
        dir_path = os.path.join(BASE_DIR, entidad)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"✓ Directorio creado: {dir_path}")


def generar_list_html(entidad, config):
    """Genera el HTML de lista"""
    entidad_plural = f"{entidad}s" if entidad != 'carga' else 'cargas'
    
    # Generar headers
    headers = ""
    for campo in config['campos_mostrar']:
        headers += f"                    <th>{campo['label']}</th>\n"
    
    # Generar columnas
    columns = ""
    for campo in config['campos_mostrar']:
        nombre_campo = campo['nombre']
        tipo_campo = campo.get('tipo', 'text')
        
        if tipo_campo == 'boolean':
            columns += f"""                    <td>
                        {{% if {entidad}.{nombre_campo} %}}
                            <span style="background-color: #10b981; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">Activo</span>
                        {{% else %}}
                            <span style="background-color: #ef4444; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">Inactivo</span>
                        {{% endif %}}
                    </td>
"""
        elif nombre_campo == 'id':
            columns += f"                    <td>{{{{ {entidad}.{nombre_campo} }}}}</td>\n"
        else:
            columns += f"                    <td><strong>{{{{ {entidad}.{nombre_campo}|default:'No especificado' }}}}</strong></td>\n"
    
    template = f"""{{% extends 'base.html' %}}

{{% block title %}}Lista de {config['nombre_plural']} - Logística Global{{% endblock %}}

{{% block content %}}
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
        <h1 class="card-title" style="margin-bottom: 0;">{config['nombre_plural']}</h1>
        <a href="{{% url '{entidad}-create' %}}" class="btn btn-primary">{config['icono']} Nuevo/a {config['nombre_singular']}</a>
    </div>

    {{% if {entidad_plural} %}}
    <div style="overflow-x: auto;">
        <table class="table">
            <thead>
                <tr>
{headers}                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {{% for {entidad} in {entidad_plural} %}}
                <tr>
{columns}                    <td>
                        <a href="{{% url '{entidad}-update' {entidad}.pk %}}" class="btn btn-secondary" style="padding: 0.5rem 1rem; margin-right: 0.5rem;">✏️ Editar</a>
                        <a href="{{% url '{entidad}-delete' {entidad}.pk %}}" class="btn btn-danger" style="padding: 0.5rem 1rem;">🗑️ Eliminar</a>
                    </td>
                </tr>
                {{% endfor %}}
            </tbody>
        </table>
    </div>

    {{% if is_paginated %}}
    <div style="display: flex; justify-content: center; gap: 0.5rem; margin-top: 2rem;">
        {{% if page_obj.has_previous %}}
            <a href="?page=1" class="btn btn-secondary">Primera</a>
            <a href="?page={{{{ page_obj.previous_page_number }}}}" class="btn btn-secondary">Anterior</a>
        {{% endif %}}

        <span style="padding: 0.75rem 1.5rem; background-color: var(--primary-color); color: white; border-radius: 5px;">
            Página {{{{ page_obj.number }}}} de {{{{ page_obj.paginator.num_pages }}}}
        </span>

        {{% if page_obj.has_next %}}
            <a href="?page={{{{ page_obj.next_page_number }}}}" class="btn btn-secondary">Siguiente</a>
            <a href="?page={{{{ page_obj.paginator.num_pages }}}}" class="btn btn-secondary">Última</a>
        {{% endif %}}
    </div>
    {{% endif %}}

    {{% else %}}
    <div style="text-align: center; padding: 3rem; background-color: var(--bg-light); border-radius: 8px;">
        <p style="font-size: 1.2rem; color: var(--text-light);">No hay {config['nombre_plural'].lower()} registrados</p>
        <a href="{{% url '{entidad}-create' %}}" class="btn btn-primary" style="margin-top: 1rem;">Crear primer/a {config['nombre_singular'].lower()}</a>
    </div>
    {{% endif %}}
</div>
{{% endblock %}}
"""
    return template


def generar_form_html(entidad, config):
    """Genera el HTML de formulario - versión simplificada usando form.as_p"""
    template = f"""{{% extends 'base.html' %}}

{{% block title %}}
    {{% if form.instance.pk %}}Editar {config['nombre_singular']}{{% else %}}Nuevo/a {config['nombre_singular']}{{% endif %}} - Logística Global
{{% endblock %}}

{{% block content %}}
<div class="card">
    <h1 class="card-title">
        {{% if form.instance.pk %}}
            ✏️ Editar {config['nombre_singular']}
        {{% else %}}
            {config['icono']} Nuevo/a {config['nombre_singular']}
        {{% endif %}}
    </h1>

    <form method="post" style="max-width: 600px;">
        {{% csrf_token %}}
        
        {{{{ form.as_p }}}}

        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
            <button type="submit" class="btn btn-primary">
                {{% if form.instance.pk %}}💾 Guardar Cambios{{% else %}}{config['icono']} Crear {config['nombre_singular']}{{% endif %}}
            </button>
            <a href="{{% url '{entidad}-list' %}}" class="btn btn-secondary">❌ Cancelar</a>
        </div>
    </form>
</div>

<style>
    form p {{
        margin-bottom: 1.5rem;
    }}
    form p label {{
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 500;
        color: var(--text-dark);
    }}
    form p input, form p select, form p textarea {{
        width: 100%;
        padding: 0.75rem;
        border: 2px solid #e5e7eb;
        border-radius: 5px;
        font-size: 1rem;
    }}
    form p input[type="checkbox"] {{
        width: auto;
    }}
</style>
{{% endblock %}}
"""
    return template


def generar_delete_html(entidad, config):
    """Genera el HTML de eliminación"""
    # Generar filas de detalles
    detail_rows = ""
    toggle = False
    
    for campo in config['campos_mostrar']:
        nombre_campo = campo['nombre']
        label = campo['label']
        tipo_campo = campo.get('tipo', 'text')
        bg = ' style="background-color: white;"' if toggle else ''
        toggle = not toggle
        
        if tipo_campo == 'boolean':
            detail_rows += f"""            <tr{bg}>
                <td style="padding: 0.75rem; font-weight: bold; width: 200px;">{label}:</td>
                <td style="padding: 0.75rem;">
                    {{% if object.{nombre_campo} %}}
                        <span style="color: var(--success);">✓ Activo</span>
                    {{% else %}}
                        <span style="color: var(--danger);">✗ Inactivo</span>
                    {{% endif %}}
                </td>
            </tr>
"""
        else:
            detail_rows += f"""            <tr{bg}>
                <td style="padding: 0.75rem; font-weight: bold; width: 200px;">{label}:</td>
                <td style="padding: 0.75rem;">{{{{ object.{nombre_campo}|default:"No especificado" }}}}</td>
            </tr>
"""
    
    template = f"""{{% extends 'base.html' %}}

{{% block title %}}Eliminar {config['nombre_singular']} - Logística Global{{% endblock %}}

{{% block content %}}
<div class="card">
    <h1 class="card-title" style="color: var(--danger);">🗑️ Confirmar Eliminación</h1>

    <div style="background-color: #fee2e2; border-left: 4px solid #ef4444; padding: 1.5rem; border-radius: 5px; margin: 2rem 0;">
        <h3 style="color: #991b1b; margin-bottom: 1rem;">⚠️ Advertencia</h3>
        <p style="color: #7f1d1d; font-size: 1.1rem;">
            ¿Está seguro que desea eliminar el/la siguiente {config['nombre_singular'].lower()}?
        </p>
    </div>

    <div style="background-color: var(--bg-light); padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">
        <table style="width: 100%;">
{detail_rows}        </table>
    </div>

    <p style="color: var(--text-light); margin: 1.5rem 0;">
        Esta acción no se puede deshacer. Todos los datos relacionados se eliminarán permanentemente.
    </p>

    <form method="post" style="display: inline;">
        {{% csrf_token %}}
        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
            <button type="submit" class="btn btn-danger">🗑️ Sí, Eliminar</button>
            <a href="{{% url '{entidad}-list' %}}" class="btn btn-secondary">❌ Cancelar</a>
        </div>
    </form>
</div>
{{% endblock %}}
"""
    return template


def crear_templates():
    """Crea todos los templates"""
    crear_directorios()
    
    for entidad, config in ENTIDADES.items():
        # Crear directorio
        dir_path = os.path.join(BASE_DIR, entidad)
        
        # Generar list
        list_html = generar_list_html(entidad, config)
        with open(os.path.join(dir_path, f"{entidad}_list.html"), 'w', encoding='utf-8') as f:
            f.write(list_html)
        print(f"✓ Creado: {entidad}_list.html")
        
        # Generar form
        form_html = generar_form_html(entidad, config)
        with open(os.path.join(dir_path, f"{entidad}_form.html"), 'w', encoding='utf-8') as f:
            f.write(form_html)
        print(f"✓ Creado: {entidad}_form.html")
        
        # Generar delete
        delete_html = generar_delete_html(entidad, config)
        with open(os.path.join(dir_path, f"{entidad}_confirm_delete.html"), 'w', encoding='utf-8') as f:
            f.write(delete_html)
        print(f"✓ Creado: {entidad}_confirm_delete.html")
    
    print("\n✅ Todos los templates han sido creados exitosamente!")
    print("\n📝 IMPORTANTE: No olvides crear también:")
    print("   - transporte/templates/base.html")
    print("   - transporte/templates/home.html")
    print("\n   (Copia el contenido de los artifacts que te proporcioné)")


if __name__ == "__main__":
    crear_templates()