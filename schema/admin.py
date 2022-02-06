from django.contrib import admin
from schema.models import Schema, Column

admin.site.register([Schema, Column])
