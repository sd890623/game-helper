from graphqlclient import GraphQLClient
import requests
import json

msg="abc"
a=f'''
mutation{{
    post(url:"UW",description:"{msg}"){{
        id
    }}
}}
'''

class Messager:
    def __init__(self) -> None:
        self.client = GraphQLClient('http://118.193.38.194:4000')
    def sendMessage(self,url,msg):
        try:
            result = self.client.execute(f'''
            mutation{{
                post(url:"{url}",description:"{msg}"){{
                    id
                }}
            }}
            ''')
            print(result)
        except Exception as e:
            print(e)

    def sendNotification(self, words):
        token="0z6Hlfml-OflyhnE2W1Dh"
        url1=f"https://maker.ifttt.com/trigger/notice_phone/with/key/{token}"
        url2=f"https://maker.ifttt.com/trigger/notice_mobile_v2/with/key/{token}"
        payload={"value1": words}
        headers={"Content-Type": "application/json"}

        try:
            requests.request("POST",url1,data=json.dumps(payload),headers=headers)
            requests.request("POST",url2,data=json.dumps(payload),headers=headers)
            print("Successfully sent notification")
        except Exception as e:
            print("Error: unable to send notification")
            print(e)