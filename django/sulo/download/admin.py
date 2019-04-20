from django.contrib import admin
from download.models import product
from download.models import downloadlink
# Register your models here.
admin.site.site_title="Sulo-Support"
admin.site.site_header="商品资料维护"
admin.site.index_title="商品"

class productList(admin.ModelAdmin):
    list_display = ('id','name', 'desc', 'create_time', 'update_time', 'remark') # list
admin.site.register(product, productList)

class downloadlinkList(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'product_link')
admin.site.register(downloadlink, downloadlinkList)

# Create your models here.
