from graphqlclient import GraphQLClient
import requests
import json

msg = "abc"
a = f'''
mutation{{
    post(url:"UW",description:"{msg}"){{
        id
    }}
}}
'''


class Messager:
    def __init__(self) -> None:
        self.client = GraphQLClient('http://118.193.38.194:4000')

    def sendMessage(self, url, msg):
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
        # token="0z6Hlfml-OflyhnE2W1Dh"
        # url1=f"https://maker.ifttt.com/trigger/notice_phone/with/key/{token}"
        # url2=f"https://maker.ifttt.com/trigger/notice_mobile_v2/with/key/{token}"
        # url3="https://discord.com/api/webhooks/1209835380694712330/-LPw-QHcefNN7IgiKRe7AEhY7e6ypUS3Z5wzoU-m_Ql_dobysragv6ipcG8EyCNrYTWQ"
        url4 = "https://rest.clicksend.com/v3/sms/send"
        # discordData={"content": f"{words}"}
        # payload={"value1": words}
        payload = json.dumps({
            "messages": [
                {
                    "body": words,
                    "to": "+61424710623",
                    "from": "+61424710623"
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic c2Q4OTA2MjNAZ21haWwuY29tOjVFOTcwQzMwLThDMEEtM0EzRS05QTEyLTQ4Nzc5QjcxMDU5MQ=='
        }
        # headers={"Content-Type": "application/json"}

        try:
            # requests.request("POST",url1,data=json.dumps(payload),headers=headers)
            # requests.request("POST",url2,data=json.dumps(payload),headers=headers)
            # requests.post(url3, json=discordData)
            response = requests.request("POST", url4, headers=headers, data=payload)
            print("Successfully sent notification")
            print(response)
        except Exception as e:
            print("Error: unable to send notification")
            print(e)
