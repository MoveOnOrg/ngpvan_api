from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_person(self, mycampaign_id, expand='', params={}):
        params['$expand'] = expand
        response = self.client.get(
            '%speople/%s' % (self.base_url, mycampaign_id),
            params = params
        )
        return {'results': [response], 'person': response.json()}
