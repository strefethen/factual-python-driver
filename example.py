#!/usr/bin/python

from factual import *

KEY = "YOUR_KEY"
SECRET = "YOUR_SECRET"

def main():
    factual = Factual(KEY, SECRET)
    
    # Sample Queries
    # query = factual.table("places").query(search = "sushi", filters = {"category": "Food& Beverage"})
    # or
    # query = factual.table("places").search("sushi").filters({"category" : "Food & Beverage"})

    table = factual.table('places')
    q1 = table.search("sushi Santa Monica")
    q2 = table.filters({'category': "Food & Beverage", 'region': "CA"}).limit(1)
    print q1.rows()[0]
    print q2.rows()
  
if __name__ == '__main__':
  main()
