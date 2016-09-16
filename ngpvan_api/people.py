from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_people(self, van_id):
        return self.client.get(
            '%speople/%s' % (self.base_url, van_id)
        )