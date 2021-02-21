from bs4 import BeautifulSoup as bs
import requests,json
import pandas as pd
import sqlite3
link="https://www.flipkart.com/sqr-running-shoes-men/product-reviews/itm174a40422e23b?pid=SHOFYGGRB84JBYCW&lid=LSTSHOFYGGRB84JBYCWRYXSCG&marketplace=FLIPKART"
# link=input("enter link:")
if link[-8:] == 'FLIPKART':
    page = requests.get(link)
    soup = bs(page.content,'html.parser')
    commentClass = soup.find_all(class_='_6K-7Co')
    comments=[commentClass[comments].get_text() for comments in range(len(commentClass))]
    print(comments)

    # DATABASE - WORDS
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    query = "SELECT * FROM Flipkart"
    cursor.execute(query)
    print(cursor.fetchall())

    for i in range(len(comments)): 
        print(comments[i])   
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO Flipkart(data) VALUES (?)", comments[i])       
        conn.commit()
        conn.close()
    
    def cat():
        return comments

else:
    pass
