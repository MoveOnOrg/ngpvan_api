from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_people(self, mycampaign_id):
        response = self.client.get(
            '%speople/%s?$expand=phones,emails,addresses,customFields' % (self.base_url, mycampaign_id)
        )
        return {'results': response, 'items': mycampaign_id}