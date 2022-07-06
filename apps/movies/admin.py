
from .models import Movie, MovieImage
from django.contrib import admin
from django.utils.safestring import mark_safe


class InlineMovieImage(admin.TabularInline):
    model = MovieImage
    extra = 1
    fields = ('image',)


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('title', 'slug', 'year', 'genre', 'country', 'image', )
    prepopulated_fields = {'slug': ('title', )}
    inlines = [InlineMovieImage, ]
    list_filter = ('genre', 'country', 'year', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f"<img scr='{img.image.url}' width='80' height='80' style='object-fit: contain'/>")
        else:
            return ""


admin.site.register(Movie, MovieAdmin)