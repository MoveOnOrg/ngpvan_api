from ngpvan import base
from ngpvan.signup import NGPVANSignupAPI

class NGPVANEventAPI(base.NGPVANAPI):

    def get_events(self, page_number=False, params={}):
        return self.get_page_or_pages('events', page_number, params, 'events')

    def get_signups_for_event(self, event_id, params={}):
        ngpvan_signup_api = NGPVANSignupAPI(self.settings)
        params['eventId'] = event_id
        return ngpvan_signup_api.get_signups(params=params)

    def get_events_by_type_name(self, type_name, page_number=False, params={}):
        params['eventTypeIds'] = self.get_event_type_id_by_name(type_name)
        return self.get_events(page_number, params=params)

    def get_event_type_id_by_name(self, name):
        types = self.get_event_types().get('types')
        types = [i for i in types if i.get('name') == name]
        return types[0].get('eventTypeId')

    def get_event_types(self, params={}):
        result = self.client.get(
            '%s%s' % (self.base_url, 'events/types'),
            params=params
        )
        return {'results': [result], 'types': result.json()}
