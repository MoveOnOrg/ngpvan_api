from ngpvan_api import base

class NGPVANSignupAPI(base.NGPVANAPI):

    def get_signups(self, page_number=False, params={}):
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
