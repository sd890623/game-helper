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
        self.client = GraphQLClient('http://127.0.0.1:4000')
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
        url="https://maker.ifttt.com/trigger/notice_phone/with/key/2q-O-9v1gxg-Tp_XLwSR"
        payload={"value1": words}
        headers={"Content-Type": "application/json"}

        try:
            response=requests.request("POST",url,data=json.dumps(payload),headers=headers)
            print(response.text)
            print("Successfully sent notification")
        except Exception as e:
            print("Error: unable to send notification")
            print(e)
