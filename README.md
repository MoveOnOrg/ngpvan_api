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
## Conventions

Every API request returns a dict with two properties:

* `results` is a list of all HTTP requests and responses made to fulfill the request.
* The name of the second property changes depending on the request type. For get requests, it will be the type of thing being requested, e.g. `get_events()` returns a dict with an `events` property, a list of events. For create (POST) requests, the ID of the created object is returned, e.g. `create_event()` returns a dict with an `event_id` property, a single ID value.

Requests that return paged results take an optional `page_number` parameter. If provided, only the given page number of results will be returned. By default, if no `page_number` is provided, all available pages will be requested and returned.
