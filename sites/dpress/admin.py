# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin

from .models import Post, Category

## 如果是直接使用下面的这种方式，在一个model中有多个textfield的时候
## 会引发一个bug------只会有第一个textfield调用EpicEditor，剩下的textfield
## 会显示空白。
## 解决方法，安装django-epiceditor后，把epiceditor加入到install_app中
## 然后改为调用 AdminEpicEditorWidget

##from .widgets import EpicEditorWidget

from epiceditor.widgets import AdminEpicEditorWidget


class PostAdmin(admin.ModelAdmin):
    list_display        = ('title', 'slug', 'author', 'status', 'created_at', 'publish', )
    search_fields       = ('title', 'body', )
    #raw_id_fields       = ('author',)
    #list_filter         = ('category',)
   # formfield_overrides = {
    #    models.TextField: {'widget': EpicEditorWidget},
    #}
    formfield_overrides = {
        models.TextField:{'widget':AdminEpicEditorWidget},
        }

class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('title', 'slug', )
    search_fields       = ('title', 'slug', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
