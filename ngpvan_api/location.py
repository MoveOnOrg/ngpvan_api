import json
from ngpvan_api import base

class NGPVANLocationAPI(base.NGPVANAPI):

    def get_locations(self, page_number=False, params={}):
        return self.get_page_or_pages('locations', page_number, params, 'locations')

    def get_or_create_location(self, location_data={}):
        result = self.client.post(
            '%s/locations/findOrCreate' % (self.base_url),
            data=json.dumps(location_data)
        )
        return {'results': [result], 'location_id': result.json()}
