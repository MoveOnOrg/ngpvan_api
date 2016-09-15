import requests

class NGPVANAPI(object):

    def __init__(self, settings):
        self.settings = settings
        self.client = requests.Session()
        self.client.auth = (settings.get('NGPVAN_API_APP'), settings.get('NGPVAN_API_KEY'))
        self.client.headers.update({'content-type': 'application/json',
                                    'accepts': 'application/json'})
        self.base_url = settings.get('NGPVAN_BASE_URL')

    def get_page(self, path, page_number=0, per_page=50, params={}):
        params['$top'] = per_page
        params['$skip'] = page_number * per_page
        return self.client.get(
            '%s%s' % (self.base_url, path),
            params=params
        )

    def get_all_pages(self, path, per_page=50, params={}):
        complete = False
        page_number = 0
        results = []
        items = []
        while not complete:
            result = self.get_page(path, page_number, per_page, params)
            results.append(result)
            if result.ok:
                json = result.json()
                items.extend(json.get('items', []))
                if json.get('nextPageLink', None) is None:
                    complete = True
                else:
                    page_number += 1
            else:
                complete = True
        return {'results': results, 'items': items}

    def get_page_or_pages(self, path, page_number, params, items_name='items'):
        if page_number:
            page_result = self.get_page(path, page_number=page_number, params=params)
            return {'results': [page_result], items_name: page_result.get('items', [])}
        else:
            page_results = self.get_all_pages(path, params=params)
            return {'results': page_results.get('results', []), items_name: page_results.get('items', [])}
