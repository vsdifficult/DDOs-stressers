


import random, io, requests
from threading import Thread

uA = [
    
]


user_agent = random.choice(uA) 

def send_request(url):
    
    
    headers = {
                'User-Agent': user_agent, 
                
            } 
    
    try:
        
        response = requests.get(url, headers=headers)
        print(f"Request to {url} succeeded with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")

def stress_test(url, num_requests):
    for _ in range(num_requests):
        Thread(target=send_request, args=(url,)).start()

if __name__ == "__main__":
    url = input("URL: ") # Замените на URL вашего сайта
    num_requests = int(input('Treads: ')) # Количество запросов для отправки
    
    stress_test(url, num_requests)
