from graphqlclient import GraphQLClient

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
        result = self.client.execute(f'''
        mutation{{
            post(url:"{url}",description:"{msg}"){{
                id
            }}
        }}
        ''')
        print(result)

