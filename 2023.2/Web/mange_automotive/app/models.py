from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create Custom User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUser(models.Model):
    TYPES = [
        ('E', 'Employee'), # Funcionário
        ('U', 'User'), # Usuário
        ('M', 'Master') # Dono
    ]

    type = models.CharField(max_length=100, choices=TYPES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_link = models.CharField(max_length=500, null=False, blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)

@receiver(post_save, sender=User)
def create_myuser(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_myuser(sender, instance, created, **kwargs):
    instance.myuser.save()

class Service(models.Model):
    service_type = models.CharField(max_length=50, null=False, blank=False)
    service_price = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(1.00)])

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    quantity_in_stock = models.PositiveIntegerField()
    producer_name = models.CharField(max_length=100, null=False, blank=False)
    producer_key = models.CharField(max_length=100, null=False, blank=False)
    purchase_price = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.01)])
    sale_price = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.01)])

class Automobile(models.Model):
    type = models.CharField(max_length=50, null=False, blank=False)
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    year = models.IntegerField(validators=[MinValueValidator(1885)])

class Availability(models.Model):
    STATUS = [
        ('A', 'Available'),
        ('U', 'Unavailable')
    ]

    status = models.CharField(max_length=100,choices=STATUS, default='A')
    station = models.CharField(max_length=100,choices=[('1', 'Posto 1'), ('2', 'Posto 2')])
    date = models.DateField(null=False)

class Maintenance(models.Model):
    STATUS = [
        ('IP', 'In Progress'),
        ('F', 'Finished'),
        ('C', 'Canceled')
    ]

    user = models.ForeignKey(MyUser, related_name='user_maintenance', on_delete=models.CASCADE)
    automobile = models.ForeignKey(Automobile, related_name='automobile_maintenance', on_delete=models.CASCADE)
    dropoff_date = models.ForeignKey(Availability, related_name='dropoff_date', on_delete=models.CASCADE) 
    pickup_date = models.DateField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='IP')

class MaintenanceService(models.Model):
    service = models.ForeignKey(Service, related_name='service_maintenance_service', on_delete=models.CASCADE)
    employee = models.ForeignKey(MyUser, related_name='user_maintenance_service', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10,decimal_places=2, default = 0)

    def save(self, *args, **kwargs):
        self.total = self.service.service_price
        super(MaintenanceService, self).save(*args, **kwargs)

class MaintenanceProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product_maintenance_product', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total = models.DecimalField(max_digits=10,decimal_places=2, default = 0)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.product.sale_price
        super(MaintenanceProduct, self).save(*args, **kwargs)

class Payment(models.Model):
    TYPES = [
        ('PIX','PIX'),
        ('BS','BANK SLIP'),
        ('CC','CREDIT CARD'),
        ('DC','DEBIT CARD'),
    ]

    STATUS = [
        ('P', 'Pending'),
        ('C', 'Canceled'),
        ('A', 'Approved')
    ]

    type_payment = models.CharField(max_length=100,choices=TYPES)
    maintenance = models.ForeignKey(Maintenance, related_name='payment_maintenance', on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.01), MaxValueValidator(1)])
    total = models.DecimalField(max_digits=10,decimal_places=2, default = 0)
    total_discount = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='P')

    def save(self, *args, **kwargs):
        self.total_discount = self.total-(self.total*self.discount)
        super(Payment, self).save(*args, **kwargs)