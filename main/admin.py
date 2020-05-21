from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries

from tinymce import TinyMCE
from django.db import models
#these two imports are there to add widget to the textfield


#customize adminn site below
class TutorialAdmin(admin.ModelAdmin):
    fields = [  "tutorials_title",
                "tutorials_published",
                "tutorials_content",
                "tutorials_slug",
                "tutorialseries",
                ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)

