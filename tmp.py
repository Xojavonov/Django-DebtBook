import datetime
import os
import django
from django.db.models import Q, OuterRef, F, Count, Sum, Min, Max
from django.db.models.functions import Substr

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTodo.settings')
django.setup()

from apps.models import Category, Product, User, Order, OrderItem, DebtBook

# ========================================ORM=======================
# u=User.objects.filter(created_at__lt=datetime.datetime.today())
# print(u)
# ========================================================
# p=Product.objects.filter(price__gt=500)
# print(p)
# ========================================================
# p2=Product.objects.filter(category__name='Elektronika').aggregate(Min('price'),Max('price'))
# print(p2)
# ========================================================
# c=Category.objects.annotate(product_count=Count('products'))
# print(c)
# ==============================================================
# last_day=datetime.datetime.today()-datetime.timedelta(days=30)
# o=Order.objects.filter(created_at__gte=last_day,created_at__lte=datetime.datetime.today())
# print(o)
# ==================================================================
# u2=User.objects.annotate(order_count=Count('orders'))
# print(u2)
# ==================================================================
# o2=OrderItem.objects.filter(order_id=1).aggregate(total=Sum(F('product__price')*F('quantity')))
# print(o2)
# =================================================================
# o3=Order.objects.select_related('user').filter(status='yangi')
# print(o3)
# =======================================================================
# p3=Product.objects.filter(name__icontains='phone')
# print(p3)
# =========================================================================
# u3=User.objects.prefetch_related('orders')
# print(u3)
#========================================================================
# p4=Product.objects.filter(category__name='uy').all()
# print(p4)
#=======================================================================
# o4=Order.objects.annotate(orders=Count(F('items'))).filter(orders__gt=5)
# print(o4)
# dupl=Category.objects.values('name').annotate(category=Count('name')).filter(category__gt=1)
# print(dupl)
# ==========================================================================
# p5=Product.objects.filter(created_at__lte=datetime.datetime.today())
# print(p5)
# ====================================================================
# u5=(User.objects.filter(orders__created_at__gt=datetime.datetime.today()).
#     values('orders__status','orders__created_at'))
# print(u5)
# ====================================================================
# upg=Order.objects.filter(id=1).update(status='yetkazildi')
# print(upg)
# =====================================================================
# add=Product.objects.bulk_create(
#     [
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#         Product(name='Apple',price=11,description='zor',category_id=2,created_at='2025-04-01'),
#      ]
# )
# ==================================================================================
# p6=Product.objects.annotate(name2=F('name'))
# print(p6)
# ====================================================================================
# c3=Category.objects.annotate(category_count=Count(F('products'))).filter(category_count__lte=1)
# print(c3)

# ====================================ORM==============================

#==============================================================================
# u5=User.objects.filter(created_at__lt=datetime.datetime.today()).order_by().values('created_at')
# print(u5)
# =============================================================================
# c4=Category.objects.filter(name__exact='Elektronika').all()
# print(c4)
# =============================================================================
# u6=User.objects.prefetch_related('orders__items')
# print(u6)
# ============================================================================
# o4=Order.objects.prefetch_related('items__product')
# print(o4)
# ============================================================================
# p5=Product.objects.aggregate(Sum('price'),Sum('orderitem__quantity'))
# print(p5)
# ============================================================================
# u6=User.objects.order_by('orders__items').aggregate(Sum('orders__items__quantity'))
# print(u6)
# ===========================================================================
# o5=Order.objects.prefetch_related('items')
# print(o5)
# ==========================================================================
# p6=Product.objects.all().order_by('price')
# print(p6)
# =========================================================================
# o7=Order.objects.filter(status='yangi')
# print(o7)
# =========================================================================
# u8=User.objects.aggregate(Sum(F('orders__items')))
# print(u8)