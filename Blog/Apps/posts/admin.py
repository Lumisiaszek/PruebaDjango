from django.contrib import admin
from .models import Posts, Categorias, Comentarios, CustomUser
from unidecode import unidecode
from django.db.models import Q

class PostsAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_publicacion", "categoria")
    search_fields = ("titulo", "categoria__nombre")
    list_filter = ("fecha_publicacion",)

    def get_search_results(self, request, queryset, search_term):

        search_term_normalized = unidecode(search_term).strip().lower()


        queryset, use_distinct = super().get_search_results(request, queryset, search_term)


        queryset |= self.model.objects.filter(
            Q(titulo__icontains=search_term) |
            Q(categoria__nombre__icontains=search_term)
        )

        # filtra resultados sin acentos
        queryset |= self.model.objects.filter(
            Q(titulo__icontains=search_term_normalized) |
            Q(categoria__nombre__icontains=search_term_normalized)
        ).exclude(id__in=queryset.values_list('id', flat=True))

        return queryset, use_distinct

# Registra tus modelos aquí.
admin.site.register(Posts, PostsAdmin)
admin.site.register(Categorias)
admin.site.register(Comentarios)
admin.site.register(CustomUser)
