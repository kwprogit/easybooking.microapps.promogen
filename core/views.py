from django.shortcuts import render
from core.models import Promo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CreatePromo(APIView):
    def post(self, request):
        code = request.GET.get('promo')
        Promo.objects.create(code=code)

        return Response(status=200)


class ActivatePromo(APIView):
    def post(self, request):
        code = request.GET.get('promo')
        try:
            promo = Promo.objects.get(code=code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if promo.is_active():
            promo.used = True
            promo.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_423_LOCKED)
        
class CheckPromo(APIView):
    def post(self, request):
        code = request.GET.get('promo')
        try:
            promo = Promo.objects.get(code=code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sts = status.HTTP_200_OK if promo.is_active() else status.HTTP_423_LOCKED
        return Response(status=sts)

 