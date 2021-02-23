import requests
from bs4 import BeautifulSoup
url='http://www.sweethome3d.com'
#step1:get html 
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# step2: pasre html
soup=BeautifulSoup(htmlContent,"html.parser")
#print(soup.prettify)

# step 3 :html tree traversal
title=soup.title    
#print(title)            #It gives title of the page

#step 4 :ojects as output like tag,Navigation string,beautifulsoup,comment
print("%%%%%%$$")
paras= soup.find_all('p')
#print(paras)

#print(soup.get_text)   #get all text on page

anchors= soup.find_all('a')  #gives all anchors tags
#print(anchors)
#for link in anchors:  #get all the links on page
    #print(link.get('href'))


all_links=set()
for link in anchors:
    if (link!='#'): 
        link= "https://www.mrftyres.com/"+ link.get("href")
        all_links.add(link)
        print(link)