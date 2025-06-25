#processes that run in parallel 

## cpu - bound tasks 
##parallel execution 


import multiprocessing
import time 

def sq_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"square of {i} is {i*i}")


def cube_numbers():
  for i in range(5):
    time.sleep(1.4)
    print(f"cube of {i} is {i*i*i}")
    
    
if __name__ == "__main__":
    
  #create two process 

  p1 = multiprocessing.Process(target=sq_numbers)
  p2 = multiprocessing.Process(target=cube_numbers)


  t=time.time()
  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print(time.time()-t)
