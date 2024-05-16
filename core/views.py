from core.models import Promo
from django.http import HttpResponse , HttpRequest
from django.views.decorators.csrf import csrf_exempt

from .bxactions import BX_PROMO_STATUS, BX_SET_DEAL_PROMOSTAT


@csrf_exempt
def webhook(request : HttpRequest):
    if request.method == 'POST':        
        data = request.body.decode()
        code = request.GET.get('promo')
        deal = None 
        for key in request.POST:
            # document_id[2] DEAL_239117
            value = request.POST[key]
            if key.startswith('document_id') and value.startswith('DEAL_'):
                deal = value.split('_')[1]
                break 
        
        
        return HttpResponse("Webhook received!")

@csrf_exempt
def createPromo(request : HttpRequest):
    if request.method == 'POST':
        data = request.body.decode()
        code = request.GET.get('promo')
        Promo.objects.create(code=code)
        return HttpResponse(status=200)


@csrf_exempt
def activatePromo(request : HttpRequest):
    print('activate method')
    if request.method == 'POST':
        data = request.body.decode()

        code = request.GET.get('promo')
        deal = None 
        for key in request.POST:
            # document_id[2] DEAL_239117
            value = request.POST[key]
            if key.startswith('document_id') and value.startswith('DEAL_'):
                deal = value.split('_')[1]
                break 
        try:
            promo = Promo.objects.get(code=code)
        except:
            BX_SET_DEAL_PROMOSTAT(deal, BX_PROMO_STATUS.NOT_EXISTS)
            return HttpResponse(status=404)
        if promo.is_active():
            promo.used = True
            promo.save()
            BX_SET_DEAL_PROMOSTAT(deal, BX_PROMO_STATUS.ACTIVE)
            return HttpResponse(status=200)
        else:
            if promo.used:
                BX_SET_DEAL_PROMOSTAT(deal, BX_PROMO_STATUS.USED)
            else:
                BX_SET_DEAL_PROMOSTAT(deal, BX_PROMO_STATUS.EXPIRED)
            return HttpResponse(status=423)


# class CheckPromo(APIView):
#     def post(self, request):
#         code = request.GET.get('promo')
#         try:
#             promo = Promo.objects.get(code=code)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         sts = status.HTTP_200_OK if promo.is_active() else status.HTTP_423_LOCKED
#         return Response(status=sts)

 