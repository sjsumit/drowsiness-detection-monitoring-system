URL = 'https://www.sms4india.com/api/v1/sendCampaign'


def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


response = sendPostRequest(URL, 'XIZ70FFYYTTJM890C6NAZPCQSWU21256', 'K1KI3ZGJ8PC6WQVY', 'stage', '9873771901', 'sumitjain1472@gmail.com', 'Hi Sumit be alert!' )


#print(response.text)



  '''url = "https://www.fast2sms.com/dev/bulk"
        {
            "return": true,
            "request_id": "lwdtp7cjyqxvfe9",
            "message": [
                "Message sent successfully"
            ]
        }
        
        querystring = {"authorization":"nexEU7y9vTJlfHu4aISgGYQN1BqVmoRAcK5ibDsZXPj6zrOWFMzohEQfFqlwW9cO704tZiHm52AvRKyC","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"9873771901"}
        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)'''
      
        '''response = sendPostRequest(URL, 'PLA6N06GQDNLEHWLLXCGFLTN80TOX97J', 'HJL8MDNX5L9RT3IA', 'stage', '9873771901', 'sumitjain1472@gmail.com', 'Hi Sumit be alert!')
        print(response.text)  '''
