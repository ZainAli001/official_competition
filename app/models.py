from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    subscription_amount = models.DecimalField(max_digits=6, decimal_places=2)
    commission_earned = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class CommissionPayout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commission_amount = models.DecimalField(max_digits=6, decimal_places=2)
    paypal_email = models.EmailField()
    payout_date = models.DateField(auto_now_add=True)


