import requests

url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId'
params ={'serviceKey' : 'nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA==', 'stId' : '112000001' }

response = requests.get(url, params=params)
print(response.content)
"""


	
nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA==
"""