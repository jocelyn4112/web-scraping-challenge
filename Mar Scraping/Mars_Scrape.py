from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
#URL 
def scrape_info():
#Mars Image JPL Scrape
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    pic = soup.find("img",)["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
   

#News Headlines HERE
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    news_soup = bs(html,'html.parser')
    element = news_soup.select_one('ul.item_list li.slide')
    news_title = element.find("div", class_='content_title').get_text()
    

#Text
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    news_soup = bs(html,'html.parser')
    element = news_soup.select_one('ul.item_list li.slide')
    news_para = element.find("div", class_='article_teaser_body').get_text()
    

#moons - Moon Names 
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup3 = bs(html, 'html.parser')
    lists = soup3.find_all('div', class_='description')
    new_list=[]
    hemisphere_image_urls=[]
    for ls in lists:
        new_list.append(ls.a.h3.text)
    

#moon images 
    for list2 in new_list:
        browser.click_link_by_partial_text(list2)
        link= browser.find_by_text('Sample')['href']
        dic = {'title': new_list, 'img_url': link}
        hemisphere_image_urls.append(dic)
        browser.visit(url)
    


    # Store data in a dictionary
    mars_data = {
        "featured_image_url": featured_image_url,
        "news_title": news_title,
        "news_para": news_para,
        "Moons":  new_list,
        "Hem URL": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
    print(mars_data)
 

 
#def scrape_info(Headline) 
    # Click the 'Next' button on each page
 #   try:
  #      browser.click_link_by_partial_text('next')
          
   # except:
        #print("Scraping Complete")
      #  return(mars_data)