# coding: utf-8

#Imports & Dependencies





#URL
def MarsImage():
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    pic = soup.find("img",)["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    return featured_image_url

# Iterate through all pages
for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('article', class_='product_pod')

    # Iterate through each book
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        h3 = article.find('h3')
        link = h3.find('a')
        href = link['href']
        title = link['title']
        print('-----------')
        print(title)
        print('http://books.toscrape.com/' + href)

    # Click the 'Next' button on each page
    try:
        browser.click_link_by_partial_text('next')
          
    except:
        print("Scraping Complete")