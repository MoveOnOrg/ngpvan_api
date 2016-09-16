from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_people(self, van_id):
        return self.client.get(
            '%speople/%s?$expand=phones,emails,addresses,customFields' % (self.base_url, van_id)
        )