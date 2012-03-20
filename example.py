#!/usr/bin/python

from factual import *

KEY = "YOUR_KEY"
SECRET = "YOUR_SECRET"

def main():
    factual = Factual(KEY, SECRET)
    
    table = factual.table('places')
    
    q1 = table.search("sushi Santa Monica")
    print q1.rows()[0]

    q2 = table.filters({'category': "Food & Beverage", 'region': "CA"}).limit(1)
    print q2.rows()
  
if __name__ == '__main__':
  main()
