#!/usr/bin/env python
# coding: utf-8

# In[16]:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep
from parsel import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
options = Options()
#options.add_argument("--headless")


job = input("Please enter JOB here :")
location = input("Please enter location here :")

x = str(job+location).replace(' ','+')

url = 'https://www.google.com/search?q={}&rlz=1C1CHBF_enUS861US861&oq=google+jobs&aqs=chrome.0.69i59l4j0i433i512j69i60l3.1588j0j4&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwjIz7L03pz4AhWfZjABHaurCUAQutcGKAF6BAgGEAY&sxsrf=ALiCzsZK3TLhnR3l8Z_yQR8A2ZGWSoI6Bw:1654653037889&google_abuse=GOOGLE_ABUSE_EXEMPTION%3DID%3D6094fef751fe6e67:TM%3D1654721324:C%3Dr:IP%3D23.105.140.58-:S%3DwJUenVtdBP_M-3CNrpARNrQ%3B+path%3D/%3B+domain%3Dgoogle.com%3B+expires%3DWed,+08-Jun-2022+23:48:44+GMT#fpstate=tldetail&htivrt=jobs&htidocid=t8gvYkzjEioAAAAAAAAAAA%3D%3D'.format(x)

driver = webdriver.Chrome(options=options)
driver.maximize_window()



driver.get(url)
sleep(2)

try:
    driver.find_elements(By.XPATH , '//ul/li').click()
except:
    pass

def scroll_down():
    html = driver.find_element(By.TAG_NAME,'html')
    sleep(3)
    html.send_keys(Keys.END)
    
    
for i in range(10):
    scroll_down()
    
    
def scroll_down():
    html = driver.find_element(By.TAG_NAME,'html')
    sleep(1)
    html.send_keys(Keys.END)
    
    
for i in range(15):
    scroll_down()
    

sleep(1)

def get_data():
    try :
        apply_link = driver.find_elements(By.XPATH ,'//span[@class="DaDV9e"]/a')[-1].get_attribute("href")
    except:
        apply_link = 'none'
    
    try:
        Company = driver.find_elements(By.XPATH ,'//div[@class="nJlQNd sMzDkb"]')[-1].text
    except:
        company = 'none'

    try:
        State = driver.find_elements(By.XPATH ,'//div[@class="sMzDkb"]')[-1].text
    except :
        State = 'none'

    try:
        title = driver.find_elements(By.XPATH ,'//h2')[-1].text

    except:
        title= 'none'
        
    try:
        quali = []
        links = driver.find_element(By.XPATH ,'//div[@class="whazf bD1FPe"]')
        q = links.find_elements(By.XPATH ,'.//div[contains(text(),"Qualifications")]/parent::div/div/div[2]/div')
        for a in q :
            quali.append(a.text)
        
    except:
        quali = 'none'
        
    try:
        respo = []
        links = driver.find_element(By.XPATH ,'//div[@class="whazf bD1FPe"]')
        q = links.find_elements(By.XPATH ,'.//div[contains(text(),"Responsibilities")]/parent::div/div/div[2]/div')
        for a in q :
            respo.append(a.text)
    except:
        respo = 'none'

    try:
        links = driver.find_element(By.XPATH ,'//div[@class="whazf bD1FPe"]')
        desc = links.find_element(By.XPATH ,'/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[4]').text
        #desc = driver.find_elements(By.XPATH ,'//span[@class="HBvzbc"]')[-1].text
    except:
        desc = 'none'
    try:
        
        job_highlight=[]
        #job_highlights.append(quali , respo)
        for q in quali:
            job_highlight.append(q)
        for r in respo :
            job_highlight.append(r)

        job_highlights =[]
        for i in job_highlight :
            if i != '' :
                job_highlights.append(i)
    except:
        job_highlights = ''
    try: 
        image_urls = driver.find_elements(By.XPATH , '//*[@id="_bjmpYvXSKMHn5NoP1fiR0Ao4"]').text
    except: 
        image_urls = 'none'    


    try:
        time = driver.find_elements(By.XPATH ,'//span[@class="LL4CDc"]')[-1].text
    except:
        time = 'none'
        
        
    mean = driver.find_element(By.XPATH ,'//div[@class="whazf bD1FPe"]')
        
    try:
        salary = driver.find_elements(By.XPATH ,'/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[3]/div[2]')[-1].text
    except:
        salary = 'none'
    if '$' in salary:
        salary = salary
    else:
        salary = 'none'  
    try:
        days_ago = mean.find_element(By.XPATH ,'.//span[contains(text(),"days ago")]').text
    except:
        days_ago = ''
        
        
    data.append({'apply_link':apply_link ,'days_ago':days_ago,'job_highlights':job_highlights,'Company':Company ,'State':State , 'title':title ,'desc':desc ,'time':time ,'salary':salary , 'apply_link':apply_link , 'image urls':image_urls })
    print(Company)
    
data = []

linkes = driver.find_elements(By.XPATH , '//ul/li')
nums=[]
for i in range(1,len(linkes)):
    nums.append(int(-i))
for i in nums :
    linkes[i].click()
    sleep(1)
    get_data()
    print(len(data))
    
def scroll_down():
    html = driver.find_element(By.TAG_NAME,'html')
    sleep(1)
    html.send_keys(Keys.END)
    
    
for i in range(20):
    scroll_down()
    
linkes = driver.find_elements(By.XPATH , '//ul/li')
nums=[]
for i in range(1,len(linkes)):
    nums.append(int(-i))
for i in nums :
    linkes[i].click()
    sleep(1)
    get_data()
    print(len(data))   
    

    
df = pd.DataFrame(data,columns = ['title','apply_link','Company','State' , 'desc','time','days_ago','salary','job_highlights', 'image urls'])
df.to_csv('test_8.csv',index=False)


# In[ ]:




