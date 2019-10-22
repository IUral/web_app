from django.shortcuts import render
from django.contrib import auth
from .models import Product


def products(request):
	if request.user.is_authenticated:
		username = auth.get_user(request).username
		products_name = Product.objects.values_list('name')
		products_cost = Product.objects.values_list('cost')
		print(products_name)
		products_1 = products_name[0][0] + ', ' + str(products_cost[0][0]) #+ ' руб.'
		products_2 = products_name[1][0] + ', ' + str(products_cost[1][0]) #+ ' руб.'
		products_3 = products_name[2][0] + ', ' + str(products_cost[2][0]) #+ ' руб.'
		return render(
			request, 'products.html',
			context={'username':username,
				'products_1':products_1,
				'products_1_cost':products_cost[0][0],
				'products_2':products_2,
				'products_2_cost':products_cost[1][0],
				'products_3':products_3,
				'products_3_cost':products_cost[2][0]
			}
		)



def order(request):
	if request.user.is_authenticated:
		username = auth.get_user(request).username
		if request.method == "POST":
			user_amount = request.POST.get('out')
			return render(request, 'order.html', {'username':username, 'user_amount':user_amount})



