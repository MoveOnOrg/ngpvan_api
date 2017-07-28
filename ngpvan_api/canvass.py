"""
ngpvan_api.canvass
~~~~~~~~~~~~~~~
This module contains canvass-data-related API calls.
"""

import json
from ngpvan_api import base

class NGPVANCanvassAPI(base.NGPVANAPI):

    def post_noncanvass(self, person_id, result_id, input_type_id = None, contact_type_id = None, date_canvassed = None):
        """We did not actually contact the person - post the Canvass Result code indicating why not"""

        canvass_data = {
            "canvassContext": {
                "contactTypeId": contact_type_id,
                "inputTypeId": input_type_id,
                "dateCanvassed": date_canvassed
            },
            "resultCodeId": result_id,
            "responses": []
        }

        result = self.client.post(
            '%s/people/%d/canvassResponses' % (self.base_url, person_id),
            data=json.dumps(canvass_data)
        )

        return {'results': [result], 'body': result.json()}


    def post_data(self, person_id, activist_codes, survey_question_responses, input_type_id = None, contact_type_id = None, date_canvassed = None):
        """Posts canvass data with the given parameters."""
        """activist_codes should be an array of ints (each one should be an activist code id)"""
        """survey_question_responses should be an array; each element should be a dict with"""
        """indexes question_id and response_id"""

        canvass_data = {
            "canvassContext": {
                "contactTypeId": contact_type_id,
                "inputTypeId": input_type_id,
                "dateCanvassed": date_canvassed
            },
            "responses": []
        }

        for ac in activist_codes:
            canvass_data['responses'].append({
                "activistCodeId": ac,
                "action": "Apply",
                "type": "ActivistCode"
            })

        for sq in survey_question_responses:
            canvass_data['responses'].append({
                "surveyQuestionId": sq['question_id'],
                "surveyResponseId": sq['response_id'],
                "type": "SurveyResponse"
            })

        result = self.client.post(
            '%s/people/%d/canvassResponses' % (self.base_url, person_id),
            data=json.dumps(canvass_data)
        )

        return {'results': [result], 'body': result.json()}
