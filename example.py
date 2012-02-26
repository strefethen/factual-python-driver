#!/usr/bin/python

from factual import *

KEY = "YOUR_KEY"
SECRET = "YOUR_SECRET"

def main():
    factual = Factual(KEY, SECRET)
    request = factual.api.execute('')
    print request
    
    # Sample Queries
    # query = factual.table("places").query(search = "sushi", filters = {"category": "Food& Beverage"})
    # or
    # query = factual.table("places").search("sushi").filters({"category" : "Food & Beverage"})
  
if __name__ == '__main__':
  main()
