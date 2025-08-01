#multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time 

def print_number(num):
  time.sleep(1)
  return f"Number : {num}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor :
  results = executor.map(print_number,numbers)
  
for result in results:
  print(result)