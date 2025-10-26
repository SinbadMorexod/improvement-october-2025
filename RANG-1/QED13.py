# pomodoro | 
""" 


"""

import httpx

url1 = "https://jsonplaceholder.typicode.com/comments/1"


response = httpx.get(url1,timeout=30.0) 

print(response.status_code)
print(response.json())