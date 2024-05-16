import os 
from bitrix24 import Bitrix24
bxurl = os.getenv('BITRIX24_URLKEY')
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