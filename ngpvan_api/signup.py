"""
ngpvan_api.signup
~~~~~~~~~~~~~~~
This module contains signup-related API calls.
"""

import json
from ngpvan_api import base

class NGPVANSignupAPI(base.NGPVANAPI):

    def get_signups(self, page_number=False, params={}):
        """Gets all signups matching params."""

        if params.get('role', False):
            # Filter by fake role param after request
            role = params.get('role', '')
            del params['role']
            signups = self.get_signups(page_number, params)
            signups['signups'] = [
                i for i in signups.get('signups', [])
                if i.get('role', {}).get('name', '') == role
            ]
            return signups
        else:
            return self.get_page_or_pages('signups', page_number, params, 'signups')

    def create_signup(self, person_id, event_id, shift_id, role_id, status_id, location_id=False):
        """Creates new signup with the given parameters."""

        signup_data = {
            "person": {
                "vanId": person_id,
            },
            "event": {
                "eventId": event_id,
            },
            "shift": {
                "eventShiftId": shift_id,
            },
            "role": {
                "roleId": role_id
            },
            "status": {
                "statusId": status_id
            }
        }

        if location_id:
            signup_data['location'] = {
                "locationId": location_id
            }

        result = self.client.post(
            '%s/signups' % (self.base_url),
            data=json.dumps(signup_data)
        )
        return {'results': [result], 'signup_id': result.json()}

    def get_statuses(self, event_id=False, event_type_id=False, params={}):
        """
        Gets available signup statuses for given event_id and/or event_type_id.
        """

        if event_id:
            params['eventId'] = event_id
        if event_type_id:
            params['eventTypeId'] = event_type_id
        result = self.client.get(
            '%s/signups/statuses' % (self.base_url),
            params=params
        )
        return {'results': [result], 'statuses': result.json()}
