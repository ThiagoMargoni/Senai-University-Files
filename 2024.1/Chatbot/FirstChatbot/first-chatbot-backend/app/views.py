from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests
import json

mock_enabled = True
mocked_answer = '{"content": "gg boys", "contentId": "343284nsadjs"}'

token1 = 'g.a000fwgYv3-khSLt0-7lNoXlD_FjQIOfk1v_YUmQyTS-aoZOyb9gLrggPeVU_v75LbDfHzrgnAACgYKAbcSAQASFQHGX2Mi9ziZUskqzIyCRxosG9FKORoVAUF8yKp2IZycqm4eSPNvBPc7bq7d0076'
token2 = 'sidts-CjIBPVxjSnW40l9XicGsBe2ucC-gJJg5LL-qgcScEAWV509NlREsccfzjfSUKqUgCosMARAA'
token3 = 'ABTWhQGdCSDYCRCgmOoyzQYkOhOkmBHi12xUTxvgfd2f3sISTv5cFxjgywk4wQ2p3_vOhN8DQw'

tokenCookies = {
    '__Secure-1PSID': token1,
    '__Secure-1PSIDTS': token2,
    '__Secure-1PSIDCC': token3
}

class ChatBotView(APIView):
    def post(self, request):
        
        if mock_enabled:
            return Response(status=201, data=json.loads(mocked_answer))

        bard = BardCookies(cookie_dict=tokenCookies)
        
        data = request.data

        conversationId = data.get('conversationId')

        if conversationId is not None:
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None

        answer = bard.get_answer(data['question'])

        return Response(status=201, data=answer)