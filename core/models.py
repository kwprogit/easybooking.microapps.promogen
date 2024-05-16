from django.db import models
from datetime import datetime
from shortuuid import ShortUUID

PROMO_LENGTH = 5
def gen_promo():
    return ShortUUID().random(PROMO_LENGTH).upper()

class Promo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    owner_id = models.CharField(blank=True, null=True, max_length=128)
    code  = models.CharField(unique=True, max_length=32)

    def is_active(self):
        curr_time = datetime.now()
        delta = curr_time.date() - self.created.date()
        if delta.days > 365:
            return False
        return not self.used
    
    def __str__(self) -> str:
        return self.code + (' ИСПОЛЬЗОВАН' if self.used else (' ПРОСРОЧЕН' if not self.is_active() else ''))
    