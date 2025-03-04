"""
This module provides functionality for web scraping using BeautifulSoup
and handling HTTP requests.
It includes:
a function to scrape the raw HTML content of a given URL,
and a function to scrape and prettify HTML content from a given URL.
"""

import os
import requests
import time
from flask import jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scrape_with_requests(url: str):
    """
    Scrapes the content of the given URL and returns the raw HTML.

    Parameters:
      url (str): The URL of the website to scrape.

    Returns:
      str: The raw HTML content of the page, or an error message.
    """
    try:
        # send an http get request to the url
        response = requests.get(url, timeout=10)
        print("Scraping URL with requests...")

        # Check if the response was successful (status code 200).
        if response.status_code != 200:
            return (
                jsonify(
                    {"status": "failure", "error": "Failed to retrieve URL content"}
                ),
                400,
            )

        # Return the entire HTML content.
        return response.text

    except Exception as e:
        # If an error occurs, return a message with the error details.
        return {"status": "failure", "error": f"An error occurred: {e}"}


def scrape_with_bs4(url: str):
    """
    Scrapes the content of the given URL and returns the prettified HTML.

    Parameters:
      url (str): The URL of the website to scrape.

    Returns:
      str: The prettified HTML content of the page, or an error message.
    """
    try:
        # send an http get request to the url
        response = requests.get(url, timeout=10)
        print("Scraping URL with bs4...")

        # Check if the response was successful (status code 200).
        if response.status_code != 200:
            return (
                jsonify(
                    {"status": "failure", "error": "Failed to retrieve URL content"}
                ),
                400,
            )

        # parse the html content using beautifullsp
        soup = BeautifulSoup(response.text, "html.parser")

        # Return the entire HTML content, formatted with indentation.
        pretified_html = soup.prettify()
        return pretified_html

    except Exception as e:
        # If an error occurs, return a message with the error details.
        return {"status": "failure", "error": f"An error occurred: {e}"}


def scrape_with_selenium(url: str):
    """
    Scrapes dynamic web pages using Selenium.

    Parameters:
      url (str): The URL of the website to scrape.

    Returns:
      str: The scraped HTML content after JavaScript execution.
    """
    chrome_path = os.getenv("CHROME_PATH")

    try:
        # Set up Chrome options (headless for better performance)
        chrome_options = Options()
        chrome_options.headless = False
        # chrome_options.add_argument("--headless") # if
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(url)

        # Wait for elements to load (optional, for sites with AJAX)
        # driver.implicitly_wait(5)
        # time.sleep(5)

        search_field_id = 'ybar-sbq'
        element_search_field = driver.find_element(By.ID, search_field_id)
        element_search_field.clear()
        element_search_field.send_keys('TSLA')
        element_search_field.send_keys(Keys.ENTER)

        # Get the page source after JavaScript execution
        page_source = driver.page_source

        # Close the browser
        driver.quit()

        # Parse with BeautifulSoup for structured output
        soup = BeautifulSoup(page_source, "html.parser")
        return soup.prettify()

    except Exception as e:
        return {"status": "failure", "error": f"An error occurred: {e}"}


# store the raw scraped data to the database as a BLOB
# def scrape_result_to_db(pretofied_data):
#     raw_scraped_data = Scraped_raw(scraped_raw_data=pretofied_data)
#     try:
#         db.session.add(raw_scraped_data)
#         db.session.commit()
#         print("Raw Scraped data saved to database")
#     except Exception as e:
#         print(f"Error saving to database: {str(e)}")


# send the raw scraped data to AI for cleaning
