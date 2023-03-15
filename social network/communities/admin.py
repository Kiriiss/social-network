from django.contrib import admin
from communities.models import Community
from users.models import AbstrapUser


admin.site.register(Community)
admin.site.register(AbstrapUser)