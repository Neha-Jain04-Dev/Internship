#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-1
# WEB SCRAPING
# 

# 
# In all the following questions, you have to use BeautifulSoup to scrape different websites and collect data as per
# the requirement of the question.
# Every answer to the question should be in form of a python function which should take URL as the parameter.
# Use Jupyter Notebooks to program, upload it on your GitHub and send the link of the Jupyter notebook to
# your SME.
# 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year of release) and make data frame.
# 2) Write a python program to scrape product name, price and discounts from
# https://peachmode.com/search?q=bags
# 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.
# 4) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.
# 5) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji Nagar.
# 6) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[34]:


from bs4 import BeautifulSoup
import requests

import pandas as pd


# Solution 1

# In[127]:


def displaytopMovies(url):
    Page=requests.get(url)
    
    if Page.status_code==200:
        soup=BeautifulSoup(Page.content)
        name=[]
        rating=[]
        yearOfRelease=[]
        
        for i in soup.find_all("h3",class_="lister-item-header"):
            name.append(i.text.replace("\n",""))
        #print(name)
        for i in soup.find_all('div',class_="ipl-rating-star small"):
            rating.append(i.text.replace("\n","")) 
        #print(rating)
        for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
            yearOfRelease.append(i.text.strip('()'))
        #print(yearOfRelease)
        df=pd.DataFrame({'Movie name':name,'Rating':rating,'Year_Of_Release':yearOfRelease})
        print(df) 
        print(df.shape)
        #print(df.head(100))
    
        
    
    else:
        print("Page is not allowed to access:",Page.status_code)
    

Url="https://www.imdb.com/list/ls056092300/"
displaytopMovies(Url)


# Solution 2

# In[ ]:


from bs4 import BeautifulSoup
import requests

import pandas as pd

Page=requests.get("https://peachmode.com/search?q=bags")
soup=BeautifulSoup(Page.content)
Productname=[]
Price=[]

        
for i in soup.find_all('div',class_="product-title"):
    Productname.append(i.text.strip())
            
for i in soup.find_all('span',class_="discounted_price st-money money done"):
    Price.append(i.text.strip()) 
   
       
       
df=pd.DataFrame({'Product name':Productname,'PriceOfProduct':Price})
print(df) 
print(df.shape)
#print(df.head(100))
         

    



# Solution 3 (a)

# In[ ]:


import pandas as pd
       
Page=requests.get("https://www.icc-cricket.com/rankings/team-rankings/mens/odi")
Page
soup=BeautifulSoup(Page.content)
matches_points_ratings=[]

for i in soup.find_all('div',class_='si-table-body'):
    matches_points_ratings.append(i.text.replace('\n',' '))

matches_points_ratings[:10]


# Solution 3(b)

# In[ ]:


Page=requests.get("https://www.icc-cricket.com/rankings/batting/mens/odi")
Page
soup=BeautifulSoup(Page.content)
team_batsman_ratings=[]

for i in soup.find_all('div',class_='si-table-body'):
    team_batsman_ratings.append(i.text)

team_batsman_ratings[:10]


# Solution 3(c)

# In[ ]:


Page=requests.get("https://www.icc-cricket.com/rankings/bowling/mens/odi")
Page
soup=BeautifulSoup(Page.content)
team_bowler_ratings=[]

for i in soup.find_all('div',class_='si-table-row'):
    team_bowler_ratings.append(i.text.replace('\n',' '))

team_bowler_ratings[:10]


# Solution 4

# In[ ]:


Page=requests.get("https://www.patreon.com/coreyms")
Page
soup=BeautifulSoup(Page.content)
heading=[]
date=[]
content=[]
likes=[]
for i in soup.find_all("span",class_="sc-1hmaiaw-0"):
    heading.append(i.text)
      
for i in soup.find_all('a',class_="sc-jQrDum bMyBFw"):
    date.append(i.text.replace("\n","")) 
        
for i in soup.find_all('div',class_="sc-1ye87qi-0 bCBphS"):
    content.append(i.text.replace("\n",""))
        
for i in soup.find_all('span',class_="sc-fotOHu dFvBhM"):
    likes.append(i.text) 
        

        
df=pd.DataFrame({'heading':heading,'date':date,'content':content,'likes':likes})
print(df) 
print(df.shape)



# Solution 5

# In[ ]:


Page=requests.get("https://www.nobroker.in/")
Page
soup=BeautifulSoup(Page.content)
house_title=[]
location=[]
area=[]
EMI=[]
price=[] 
for i in soup.find_all("h2",class_="heading-6 flex items-center font-semi-bold m-0"):
    house_title.append(i.text.replace("\n",""))
      
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text.replace("\n","")) 
        
for i in soup.find_all('span',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-"):
    area.append(i.text.replace("\n",""))
        
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r border-r-solid border-card-overview-border-color last:border-r-1 "):
    EMI.append(i.text.replace("\n","")) 
        
for i in soup.find_all('div',id="minDeposit"):
    price.append(i.text.replace("\n",""))
        
df=pd.DataFrame({'house title':house_title,'location':location,'area':area,'EMI':EMI,'price':price})
print(df) 
print(df.shape)


# Solution 6

# In[170]:


Page=requests.get("https://www.bewakoof.com/bestseller?sort=popular")
Page
soup=BeautifulSoup(Page.content)
product_name=[]
price=[]
Image_URL=[]

for i in soup.find_all("h2",class_="clr-shade4"):
    product_name.append(i.text.replace("\n",""))
      
for i in soup.find_all('div',class_="discountedPriceText"):
    price.append(i.text.replace("\n","")) 
        
for i in soup.find_all('img',class_="wishlist-icon-animate"):
    Image_URL.append(i['src'])
    
df=pd.DataFrame({'product_name':product_name,'price':price,'Image_URL':Image_URL})
print(df) 
print(df.shape)


# In[ ]:




