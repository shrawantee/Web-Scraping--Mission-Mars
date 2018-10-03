
# coding: utf-8
# ### ASK
# Define a function `scrape` that will execute all of your scraping code from above (the notebook) 
# and return one Python dictionary containing all of the scraped data.



# Import dependencies
import os
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq
from urllib.parse import urlsplit
import requests
from splinter import Browser
from selenium import webdriver
import time

# Set Path for the Chromedriver
def init_browser():
    executable_path = {'executable_path':'/Users/DoraB/Downloads/chromedriver'}
    return browser = Browser("chrome", **executable_path, headless=False)
    
    def scrape():
    #Declare the python dictionary
    newslistings = {}
    
    #Scrape Nasa.gov
    url ="https://mars.nasa.gov/news/"
    browser.visit(url)

    html1 = browser.html
    soup = BeautifulSoup(html1, 'html.parser')

    #Store the scraped data in the dictionary created above 
    newslistings["news_title"] = soup.find("div", class_="content_title").find("a").get_text()
    newslistings["news_p"] = soup.find("div", class_="article_teaser_body").get_text()

    #Scrape Nasa.gov for the images
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    html2 = browser.html
    soup = BeautifulSoup(html2, 'html.parser')
    extension = soup.find("article").find("figure", class_="lede").a["href"]
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    #Store the scraped data in the dictionary created above 
    newslistings["featured_image_url"]

    #Scrape Twitter for Mars Weather
    url2 ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url2)

    html3 = browser.html
    soup = BeautifulSoup(html3, 'html.parser')

    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text
    #Store the scraped data in the dictionary created above 
    newslistings["mars_weather"]

    # Scrape Mars Facts for facts about the planet including Diameter, Mass, etc.
    url3 ="http://space-facts.com/mars/"
    browser.visit(url3)
    response = requests.get(url3)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_profile = soup.find("table", class_="tablepress tablepress-id-mars").text
    print(mars_profile)
    table = pd.read_html(url3)
    print(table[0])

    #convert table to dataframe
    #reset index
    df_mars_facts = table[0]
    df_mars_facts.columns=["Description", "Value"]
    df_mars_facts.set_index(["Description"])

    #Use Pandas to convert the data to a HTML table string.
    html_table=df_mars_facts.to_html()
    print(html_table)

    # Scrape USGS site for high resolution images for each of Mar's hemispheres.

    #Visit URL
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Scrape for Cerberus Hemisphere Enhanced
    browser.visit(url4)
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)
    html4 = browser.html
    soup = BeautifulSoup(html4, 'html.parser')

    cerberus_link = soup.find("div", class_="downloads").a["href"]
    print(cerberus_link)
    # Declare an empty list to collect the image URLS
    hemisphere_image_urls = []

    # Create a dictionary
    cerberus = {
        "title": "Cerberus Hemisphere Enhanced",
        "img_url": cerberus_link
    }
    # Append the dictionary to the list
    hemisphere_image_urls.append(cerberus)

    #Schiaparelli Hemisphere Enhanced
    #Visit URL
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Scrape for Cerberus Hemisphere Enhanced
    browser.visit(url5)
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)
    html5 = browser.html
    soup = BeautifulSoup(html5, 'html.parser')

    schiaparelli_link = soup.find("div", class_="downloads").a["href"]
    print(schiaparelli_link)

    # Create a dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere Enhanced",
        "img_url": schiaparelli_link
    }
    # Append the dictionary to the list
    hemisphere_image_urls.append(schiaparelli)

    #Syrtis Major Hemisphere Enhanced
    #Visit URL
    url6 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Scrape for Cerberus Hemisphere Enhanced
    browser.visit(url6)
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)
    html6 = browser.html
    soup = BeautifulSoup(html6, 'html.parser')

    syrtis_link = soup.find("div", class_="downloads").a["href"]
    print(syrtis_link)

    # Create a dictionary
    syrtis = {
        "title": "Syrtis Major Hemisphere Enhanced",
        "img_url": syrtis_link
    }
    # Append the dictionary to the list
    hemisphere_image_urls.append(syrtis)

    #Valles Marineris Hemisphere Enhanced
    #Visit URL
    url7 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Scrape for Cerberus Hemisphere Enhanced
    browser.visit(url7)
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)
    html7 = browser.html
    soup = BeautifulSoup(html7, 'html.parser')

    valles_marineris_link = soup.find("div", class_="downloads").a["href"]
    print(valles_marineris_link)

    # Create a dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere Enhanced",
        "img_url": valles_marineris_link
    }
    # Append the dictionary to the list
    hemisphere_image_urls.append(valles_marineris)

