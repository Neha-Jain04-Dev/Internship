#!/usr/bin/env python
# coding: utf-8

# # Assignment 1- Web Scraping with BeautifulSoup

# In[72]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[73]:


from bs4 import BeautifulSoup
import requests


# In all the following questions, you have to use BeautifulSoup to scrape different websites and collect data as per the requirement of the question. 
# 
# Every answer to the question should be in form of a python function which should take URL as the parameter. Use Jupyter Notebooks to program, upload it on your GitHub and send the link of the Jupyter notebook to your SME.
# 
# Question 1) Write a python program to display all the header tags from wikipedia.org.
# Question 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of 
#             release) and make data frame.
# Question 3) Write a python program to scrape mentioned details from dineout.co.in : i) Restaurant name ii) Cuisine             iii) Location iv) Ratings v) Image URL.
# Question 4) Write s python program to display list of respected former finance minister of India(i.e. Name , Term 
#             of office) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# # Solution 1

# In[52]:


def displayHeaderTags(url):
    Page= requests.get (url)
    soup=BeautifulSoup(Page.content)
    headertags=soup.find_all(['h1','h2','h3','h4','h5','h6'])
    for i in headertags:
        print(i.text)
    
            

        
url="https://www.wikipedia.org"
displayHeaderTags(url)


# # Solution2

# In[99]:


def displayTopMovies(url):
    Page=requests.get(url)
    
    if Page.status_code==200:
        soup=BeautifulSoup(Page.content)
        name=[]
        rating=[]
        yearOfRelease=[]
        for i in soup.find_all('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title"):
            name.append(i.text)
        #print(name)
        for i in soup.find_all('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"):
            rating.append(i.text) 
        #print(rating)
        for i in soup.find_all('span',class_="sc-be6f1408-8 fcCUPU cli-title-metadata-item"):
            yearOfRelease.append(i.text)
        #print(yearOfRelease)
        df=pd.DataFrame({'Movie name':name,'Rating':rating,'Year_Of_Release':yearOfRelease})
        print(df) 
        print(df.shape)
        print(df.head(100))
    
    else:
        print("Page is not allowed to access:",Page.status_code)
    

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
displayTopMovies(Url)


# # Solution 3

# In[10]:


from bs4 import BeautifulSoup
import requests


# In[48]:


import pandas as pd

def detailsDineOut(url):
    Page=requests.get(url)
    soup=BeautifulSoup(Page.content)
    titles=[]
    location=[]
    cuisine=[]
    ratings=[]
    imageurl=[]
    for i in soup.find_all('a',class_="restnt-name ellipsis"):
        titles.append(i.text)
    print(len(titles))
    for i in soup.find_all('div',class_="restnt-loc ellipsis"):
        location.append(i.text) 
    #print(len(location))
    for i in soup.find_all('span',class_="double-line-ellipsis"):
        cuisine.append(i.text)
    #print(len(cuisine))
    for i in soup.find_all('div',class_="restnt-rating-widget pull-right text-right"):
        ratings.append(i.text.replace("votes", " "))
    #print(len(ratings))
    for i in soup.find_all('img',class_="no-img"):
        imageurl.append(i['data-src'])
    #print(len(imageurl))
    df=pd.DataFrame({'Restaurant name':titles,'cuisine':cuisine,'Location':location,'Ratings':ratings,'ImagesUrl':imageurl})
    print(df)
    print(df.shape)
               
Url="https://www.dineout.co.in/delhi-restaurants?loc=Noida"
detailsDineOut(Url)


# # Solution4
#     
#                
# 

# Question -4 Write s python program to display list of respected former finance minister of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# Solution: There is not any kind of list of respected former finance minister of India at this link https://presidentofindia.nic.in/former-presidents.htm

# In[ ]:




