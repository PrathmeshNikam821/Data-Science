#web scrapping using multithreading 


'''
https://python.langchain.com/docs/introduction/


https://docs.smith.langchain.com/


https://langchain-ai.github.io/langgraph/

'''


import threading
import requests
from bs4 import BeautifulSoup

urls =[ 
       
      ' https://python.langchain.com/docs/introduction/',
       'https://docs.smith.langchain.com/',
       'https://langchain-ai.github.io/langgraph/'
]


def fetech_content(url):
  response=requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser')
  print(f'Fetched : {len(soup.text)} characters from {url}')  
  
threads = []

for url in urls :
  thread = threading.Thread(target=fetech_content,args=(url,))
  threads.append(thread)
  thread.start()
  
for thread in threads:
  thread.join()
  
  
print("all webpages are fetched.")
  