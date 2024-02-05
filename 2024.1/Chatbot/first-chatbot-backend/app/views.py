from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

token1 = 'g.a000fwgYv3-khSLt0-7lNoXlD_FjQIOfk1v_YUmQyTS-aoZOyb9gLrggPeVU_v75LbDfHzrgnAACgYKAbcSAQASFQHGX2Mi9ziZUskqzIyCRxosG9FKORoVAUF8yKp2IZycqm4eSPNvBPc7bq7d0076'
token2 = 'sidts-CjIBPVxjSkj-VrxVJvukX4GOsp3V9_vov51XrBAIV9S8_m6z-mmP0UUW23oQSrrCukR7YBAA'
token3 = 'ABTWhQHqndUAzAibRdcs17tWa8P6uKeecdxagZYuE1WBjrz0RDUTJSxmKPHk9L5bex0UIvaa6Q'

tokenCookies = {
    '__Secure-1PSID': token1,
    '__Secure-1PSIDTS': token2,
    '__Secure-1PSIDCC': token3
}

bard = BardCookies(cookie_dict=tokenCookies)

class ChatBotView(APIView):
    def post(self, request):
        data = request.data

        conversationId = data.get('conversationId')

        if conversationId is not None:
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None

        answer = bard.get_answer(data['question'])

        return Response(status=201, data=answer)