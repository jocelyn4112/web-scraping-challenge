coding: utf-8

#Imports & Dependencies





#URL 
def scrape_info():
#Mars Image JPL Scrape
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    pic = soup.find("img",)["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    return featured_image_url

#News Headlines HERE
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    news_soup = bs(html,'html.parser')
    element = news_soup.select_one('ul.item_list li.slide')
    news_title = element.find("div", class_='content_title').get_text()
    return news_title

#Text
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    news_soup = bs(html,'html.parser')
    element = news_soup.select_one('ul.item_list li.slide')
    news_para = element.find("div", class_='article_teaser_body').get_text()
    return (f"{news_para}")

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
    return {{new_list}}

#moon images 
    for list2 in new_list:
        browser.click_link_by_partial_text(list2)
        link= browser.find_by_text('Sample')['href']
        dic = {'title': new_list, 'img_url': link}
        hemisphere_image_urls.append(dic)
        browser.visit(url)
    return hemisphere_image_urls

def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    avg_temps = soup.find('div', id='weather')

    # Get the min avg temp
    min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
 

 
def scrape_info(Headline) 
    # Click the 'Next' button on each page
    try:
        browser.click_link_by_partial_text('next')
          
    except:
        print("Scraping Complete")
        return(SEE COSTA AND MAKE A DIC )