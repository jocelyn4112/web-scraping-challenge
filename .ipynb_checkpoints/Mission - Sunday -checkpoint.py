{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import os\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import time \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jocel\\Documents\\GitHub\\web-scraping-challenge\\chromedriver.exe\n"
     ]
    }
   ],
   "source": [
    "!where chromedriver "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "exec_path ={'executable_path': 'C:/Users/jocel/Documents/GitHub/web-scraping-challenge/chromedriver.exe'}\n",
    "browser = Browser('chrome', **exec_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('MOXIE Could Help Future Rockets Launch Off Mars', \"NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.\")\n"
     ]
    }
   ],
   "source": [
    "# URL of page to be scraped - Text\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "news_soup = bs(html,'html.parser')\n",
    "element = news_soup.select_one('ul.item_list li.slide')\n",
    "news_title = element.find(\"div\", class_='content_title').get_text()\n",
    "news_para = element.find(\"div\", class_='article_teaser_body').get_text()\n",
    "print(f\"{news_title, news_para}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve page with the requests module\n",
    "\n",
    "response = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a Beautiful Soup object\n",
    "#soup = bs(response.text,'html.parser')\n",
    "soup = bs(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Examine the results, then determine element that contains sought info\n",
    "#print(soup.prettify())\n",
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# results are returned as an iterable list\n",
    "results = soup.find_all('', class_=\"result-row\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop through returned results\n",
    "for result in results:\n",
    "    # Error handling\n",
    "    try:\n",
    "        # Identify and return title of title - CORRECT HEADINGF NAME \n",
    "        title = result.find('a', class_=\"result-title\").text\n",
    "        # Identify and return price of listing\n",
    "        price = result.a.span.text\n",
    "        # Identify and return link to listing\n",
    "        link = result.a['href']\n",
    "\n",
    "        # Print results only if title, price, and link are available\n",
    "        if (title and price and link):\n",
    "            print('-------------')\n",
    "            print(title)\n",
    "            print(price)\n",
    "            print(link)\n",
    "    except AttributeError as e:\n",
    "        print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = 'mongodb://localhost:27017'\n",
    "client = pymongo.MongoClient(conn)\n",
    "db = client.mars\n",
    "posts = db.posts\n",
    "db\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrap JPL with Splinter\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "#JPL URL \n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jocel\\.conda\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:493: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  FutureWarning,\n"
     ]
    }
   ],
   "source": [
    " #partial text\n",
    "browser.click_link_by_partial_text(\"FULL IMAGE\")\n",
    "time.sleep(3)\n",
    "browser.click_link_by_partial_text(\"more info\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    " # HTML object\n",
    "    html = browser.html\n",
    "    soup_2=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA19964_hires.jpg'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the element \n",
    "sub_img = soup_2.find( \"figure\", class_=\"lede\")\n",
    "name=sub_img.a[\"href\"]\n",
    "featured_image='https://www.jpl.nasa.gov'+ name\n",
    "featured_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#url \n",
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create df for Mars Data\n",
    "mars_df = tables[0]\n",
    "mars_df.columns = ['0', '1']\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Information</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Mars                    Information\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#rename colum\n",
    "mars_df.rename(columns={\"0\": \"Mars\", \"1\": \"Information\"}, inplace = True)\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Information</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Mars                    Information\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#reindex\n",
    "mars_df.reset_index(drop=True, inplace=True)\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#type\n",
    "type(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Information</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#convert DF to table \n",
    "html_table = mars_df.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Mars</th>      <th>Information</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <th>1</th>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <th>2</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>3</th>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>4</th>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>5</th>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>6</th>      <td>Surface Temperature:</td>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>7</th>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>8</th>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#clean up \n",
    "html_table.replace('\\n', '')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#save as HTML file \n",
    "mars_df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\n",
    "url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(url)\n",
    "html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make new soup \n",
    "soup3 = bs(html, 'html.parser')\n",
    "lists = soup3.find_all('div', class_='wide-image')\n",
    "lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Make dics and click through lists\n",
    "\n",
    "new_list=[]\n",
    "hemisphere_image_urls=[]\n",
    "for ls in new_list:\n",
    "    new_list.append(ls.a.h3.text)\n",
    "for list2 in new_list:\n",
    "    browser.click_link_by_partial_text(list2)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    link=soup.find('image').a['href']\n",
    "    dic = {'title': new_list, 'img_url': link}\n",
    "    hemisphere_image_urls.append(dic)\n",
    "    browser.visit(url)\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\"},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\"},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\"},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg\"},\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
