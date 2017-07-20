"""
ngpvan_api.canvass
~~~~~~~~~~~~~~~
This module contains canvass-data-related API calls.
"""

import json
from ngpvan_api import base

class NGPVANCanvassAPI(base.NGPVANAPI):

    def create_canvass(self, person_id, result_id, activist_codes, survey_question_responses, contact_type_id = null, input_type_id = null, date_canvassed=null):
        """Posts signup data with the given parameters."""

        canvass_data = {
            "canvassContext": {
                "contactTypeId": contact_type,
                "inputTypeId": input_type,
                "dateCanvassed": date_canvassed
            },
            "resultCodeId": result_id,
            "responses": []
        }

        for ac in activist_codes:
            canvass_data.responses.append({
                "activistCodeId": ac,
                "action": "Apply",
                "type": "ActivistCode"
            })

        for sq in survey_question_responses:
            canvass_data.responses.append({
                "surveyQuestionId": sq.question_id,
                "surveyResponseId": sq.response_id,
                "type": "SurveyResponse"
            })

        result = self.client.post(
            '%s/people/%d/canvassResponses' % (self.base_url, person_id),
            data=json.dumps(canvass_data)
        )
        return {'results': [result]}
