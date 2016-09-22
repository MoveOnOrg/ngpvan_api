import json
from ngpvan_api import base
from ngpvan_api.signup import NGPVANSignupAPI

class NGPVANEventAPI(base.NGPVANAPI):

    def get_events(self, page_number=False, params={}):
        return self.get_page_or_pages('events', page_number, params, 'events')

    def get_event(self, event_id, params={}):
        result = self.client.get(
            '%s/events/%s' % (self.base_url, event_id),
            params=params
        )
        return {'results': [result], 'events': [result.json()]}

    def create_event(self, event_data={}):
        result = self.client.post(
            '%s/events' % (self.base_url),
            data=json.dumps(event_data)
        )
        return {'results': [result], 'event_id': result.json()}

    def get_signups_for_event(self, event_id, params={}):
        ngpvan_signup_api = NGPVANSignupAPI(self.settings)
        params['eventId'] = event_id
        return ngpvan_signup_api.get_signups(params=params)

    def get_events_by_type_name(self, type_name, page_number=False, params={}):
        params['eventTypeIds'] = self.get_event_type_id_by_name(type_name)
        return self.get_events(page_number, params=params)

    def get_event_type_id_by_name(self, name):
        event_type = self.get_event_type_by_name(name)
        return event_type.get('eventTypeId')

    def get_event_type_by_name(self, name):
        event_types = self.get_event_types().get('types')
        for event_type in event_types:
            if event_type['name'] == name:
                return event_type
        return False

    def get_event_types(self, params={}):
        result = self.client.get(
            '%s%s' % (self.base_url, 'events/types'),
            params=params
        )
        return {'results': [result], 'types': result.json()}
