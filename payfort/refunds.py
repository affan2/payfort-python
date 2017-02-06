import requests

from . import api_base
from .payfort import PayFortObject

__all__ = ("Refund",)


class Refund(PayFortObject):
    url = api_base + "/charges"

    def create(self, charge_id, data):
        return self.handle_response(requests.post(
            "%s/%s/refunds" % (self.url, charge_id), data=data,
            auth=self.auth
        ))

    def get_all(self, charge_id):
        return self.handle_response(
            requests.get("%s/%s/refunds" % (self.url, charge_id),
                         auth=self.auth))
