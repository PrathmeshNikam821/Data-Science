from logger import logging

def add(a,b):
  
  logging.debug("The addition operation is taking place   ")
  return a+b

logging.debug("addtion function is called")

print(add(10,15))