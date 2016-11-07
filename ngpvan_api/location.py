"""
ngpvan_api.location
~~~~~~~~~~~~~~~
This module contains location-related API calls.
"""

import json
from ngpvan_api import base

class NGPVANLocationAPI(base.NGPVANAPI):

    def get_locations(self, page_number=False, params={}):
        """Gets all locations matching params."""

        return self.get_page_or_pages('locations', page_number, params, 'locations')

    def get_or_create_location(self, location_data={}):
        """
        Gets existing location_id matching location_data, or creates new
        location from location_data if no match is found.
        """

        result = self.client.post(
            '%s/locations/findOrCreate' % (self.base_url),
            data=json.dumps(location_data)
        )
        return {'results': [result], 'location_id': result.json()}
