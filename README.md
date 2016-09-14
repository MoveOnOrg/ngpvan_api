# NGPVAN API

Python wrapper for NGPVAN API.

## Example Use

```
from ngpvan_api.event import NGPVANEventAPI

ngpvan_event_api = NGPVANEventAPI({
    'NGPVAN_BASE_URL': 'https://api.securevan.com/v4/',
    'NGPVAN_API_KEY': 'api-key-example|1',
    'NGPVAN_API_APP': 'api-app',
})

events = ngpvan_event_api.get_events_by_type_name('Canvass').get('events')

for event in events:
    signups = ngpvan_event_api.get_signups_for_event(event.get('eventId'), params={'role':'Participant'}).get('signups')
```
