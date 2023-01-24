from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def calculate_commission(subscription_amount):
    direct_referral_commission = subscription_amount * 0.1
    return direct_referral_commission

def calculate_multi_level_commission(referrer, level):
    commission = 0
    if level == 1:
        commission = referrer.subscription_amount * 0.05
        commission = referrer * 0.05
    elif level == 2:
        # commission = referrer.subscription_amount * 0.03
        commission = referrer * 0.03
    elif level == 3:
        # commission = referrer.subscription_amount * 0.02
        commission = referrer* 0.02
    return commission

def pay_commission(user, commission_amount):
    paypal_email = user.email
    payout = CommissionPayout.objects.create(user=user, commission_amount=commission_amount, paypal_email=paypal_email)
    payout.save()

def handle_referral(referrer, referral):
    direct_referral_commission = calculate_commission(float(referral.subscription_amount))
    print('pppppppppppppppppppppppppppppppppppppp')
    print('okkokokokokokoko',referrer.commission_earned)
    sav = float(referrer.commission_earned)
    sav += direct_referral_commission
    print('ok2oko2oko2kok2o',sav)
    # referrer.commission_earned += direct_referral_commission
    # referrer.save()
    pay_commission(referrer, direct_referral_commission)
    level = 1
    while referrer.referred_by:
        referrer = referrer.referred_by
        multi_level_commission = calculate_multi_level_commission(referrer, level)
        referrer.commission_earned += multi_level_commission
        # referrer.save()
        pay_commission(referrer, multi_level_commission)
        level += 1




# referre = User.objects.get(pk=4)
# referrer = float(referre.subscription_amount)
# print('hhhhhhhhhhhh...',referrer)

# referrl = User.objects.get(pk=3)
# referral = float(referrl.subscription_amount)
# print('lllllllll...',referral)


# print('Calculate Commission..........',calculate_commission(referrer))
# print('Calculate_multi_level_commission............',calculate_multi_level_commission(referrer,3))
# print('Handle referral............',handle_referral(referre,referrl))

