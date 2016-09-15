from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_people(self, path, vanid):
        return self.client.get(
            '%s%s/%s' % (self.base_url, path, vanid)
        )