from django.shortcuts import render


def static_home(request):
    items = [
        {
            "title": "Landing en Vercel",
            "description": "Pagina de prueba sin base de datos.",
            "updated_at": "Hoy",
        },
        {
            "title": "Checklist",
            "description": "Verificar que el despliegue responde en produccion.",
            "updated_at": "Hace 1 minuto",
        },
    ]
    return render(request, "items/item_list.html", {"items": items})
