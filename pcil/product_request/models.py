from django.db import models


class pcil_products(models.Model):
	name = models.CharField(max_length=1000,blank=False,unique=True)

	def __str__(self):
		return self.name


class pcil_cities(models.Model):
	name = models.CharField(max_length=1000,blank=False,unique=True)

	def __str__(self):
		return self.name

#sub-product
class product_requisition(models.Model):

	def get_default():
		return 1

	# customer_name = models.CharField(max_length=250,blank=False)
	# phone_number = models.CharField(max_length=15,unique=True,blank=False)
	# citi_id = models.ForeignKey(pcil_cities,on_delete=models.CASCADE,blank=False)
	# product_ids = models.ManyToManyField(pcil_products,blank=False)
	# SUBPRODUCT_CHOICES = [
	# 	('TERMITE', 'termite'),
	# 	('BAYERGEL', 'bayergel'),
	# 	('BIODEGRADABLE_GARBAGE_BAG', 'biodegradable_garbage_bag'),
	# 	('TRUSTBASKET_CONCENTRATE', 'turstbasket_concentrate'),
	# 	('Termidor Foam Rat Killer','Termidor Foam Rat Killer'),
	# 	('Trustbasket Concentrated Acid','Trustbasket Concentrated Acid'),
	# 	('Bedbug anti-roach gel','Bedbug anti-roach gel'),
	# 	('Catnip cockroach bait','Catnip cockroach bait'),
	# 	('Diatomaceous','Diatomaceous'),
	# ]
	sub_product_name = models.CharField(max_length=1000,blank=False,unique=True,default='Termite')
	super_product_id = models.ForeignKey(pcil_products,on_delete=models.CASCADE,blank=False,default=get_default)
	is_favorite = models.BooleanField(default=False)


	def __str__(self):
		return self.sub_product_name

# class sub_product_requisition(models.Model):
# 	name = models.CharField(max_length=250,blank=False)
# 	phone_number = models.CharField(max_length=15,unique=True,blank=False)
# 	citi_id = models.ForeignKey(pcil_cities,on_delete=models.CASCADE,blank=False)
# 	product_ids = models.ManyToManyField(pcil_products,blank=False)