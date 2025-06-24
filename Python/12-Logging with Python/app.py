import logging

#logging settings 

logging.basicConfig(
       level=logging.DEBUG,
       format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
       datefmt='%Y-%m-%d %H:%M:%S',
       handlers=[
         logging.FileHandler("app1.log"),
         logging.StreamHandler() 
       ]
)

logger = logging.getLogger("Arithmetic App")

def add(a,b):
  result = a+b
  logger.debug(f"Adding {a} and {b} : {result}")
  return result



def sub(a,b):
  result = a-b
  logger.debug(f"Subtracting {a} and {b} : {result}")
  return result

def mul(a,b):
  result = a*b
  logger.debug(f"Multiplying {a} and {b} : {result}")
  return result

def divide(a,b):
  try:
    result=a/b
    logger.debug(f"Dividing {a} by {b} : {result}")
    return result
  except ZeroDivisionError:
    logger.error("Division by zero error")
    return None
  
  
print(add(10,15))
print(sub(10,15))
print(mul(10,15))
divide(10,0)
divide(10,2)