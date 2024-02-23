from django.apps import AppConfig


class BagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'

self.coupon_id = self.session.get('coupon_id')