from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule

def search_youtube(query):
    driver = webdriver.Chrome()  # You can use other web drivers as needed

    try:
        # Open YouTube
        driver.get("https://www.youtube.com/")

        # Wait for the page to load (you might need to adjust the sleep time)
        time.sleep(5)

        # Type the query in the search bar
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for two hours (adjust the sleep time accordingly)
        time.sleep(2 * 60 * 60)

    finally:
        # Close the browser window
        driver.quit()

# Define your search queries with the correct time format
queries = {
    '07:30': 'Advanced JavaScript',
    '09:30': 'Mobile Development',
    '11:30': 'C#',
}

# Schedule the searches
for time_str, query in queries.items():
    schedule.every().day.at(time_str).do(search_youtube, query)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)