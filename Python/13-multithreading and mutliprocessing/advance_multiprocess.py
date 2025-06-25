#Multiprocessing with ProcessPoolExecutor 

from concurrent.futures import ProcessPoolExecutor
import time 

def print_number(num):
  time.sleep(1)
  return f"Number : {num*num}"

numbers=[1,2,3,4,5,4,5,6,7,8,9,101,1,1,1,11,22233,434]

if __name__ == "__main__":

  with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    
  for result in results:
    print(result)
