import os 
from bitrix24 import Bitrix24
bxurl = 'https://easybooking.bitrix24.ru/rest/31387/ha6dao4g69uqbr80/'
print(bxurl)
bx = Bitrix24(bxurl)


class BX_PROMO_STATUS:
    ACTIVE = 7139
    USED = 7141
    EXPIRED = 7143
    NOT_EXISTS = 7151


def BX_SET_DEAL_PROMOSTAT(deal_id, promo_sts : BX_PROMO_STATUS):
    bx.callMethod('crm.deal.update', {
    'id' : deal_id, 
    'fields' : {
            'UF_CRM_1715853973089' :  promo_sts
        }
    })