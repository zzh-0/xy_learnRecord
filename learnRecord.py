import requests

url = 'https://ccnu.ai-augmented.com/api/jx-iresource/learnLength/learnRecord'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

if __name__ == '__main__':
    group_id = input('group_id: ')
    resourceId = input('resourceId: ')
    user_id = input('user_id: ')
    data = {
    "clientType": 1,
    "group_id": group_id,
    "resourceId": resourceId,
    "roleType": 1,
    "user_id": user_id,
    }
    response = requests.post(url,headers=headers,json=data)
    if response.status_code == 200:    
        print('Request successful: ', response.text)  
    else:  
        print('Request failed: ', response.status_code, response.text)