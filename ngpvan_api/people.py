from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_people(self, my_campaigns_id):
        response = self.client.get(
            '%speople/%s?$expand=phones,emails,addresses,customFields' % (self.base_url, van_id)
        )
        return {'results': response, 'items': my_campaigns_id}