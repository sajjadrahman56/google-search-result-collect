import time
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

st.title("Link collect from Google Search")

search_query = st.text_input("Enter your search query:")
placeholder = st.empty() 

if "results_data" not in st.session_state:
    st.session_state.results_data = []

if st.button("Submit") and search_query:
    placeholder.empty() 
    
    with st.spinner("Fetching search results... Please wait."):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run without UI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # ✅ Fix: Use the latest compatible ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.google.com/")
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span/a/h3'))
        )

        results_data = []
        for _ in range(5):  
            try:
                results = driver.find_elements(By.XPATH, '//span/a')
                for result in results:
                    try:
                        title_element = result.find_element(By.TAG_NAME, 'h3')
                        url = result.get_attribute('href')  

                        if "facebook.com" in url:
                            category = "Facebook"
                        elif "youtube.com" in url:
                            category = "YouTube"
                        else:
                            category = "Website"

                        if url and "google.com" not in url:
                            results_data.append({"Title": title_element.text, "URL": url, "Category": category})
                    except:
                        continue 

            except Exception as e:
                print(f"Error fetching results: {e}")
                break

            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#pnnext > span.oeN89d"))
                )
                next_button.click()
                time.sleep(2)
            except:
                print("Next button not found, stopping search.")
                break

        driver.quit()
        
        st.session_state.results_data = results_data

with placeholder.container():
    if st.session_state.results_data:
        df = pd.DataFrame(st.session_state.results_data)
        st.success("Search complete!")  
        st.write("### Search Results  in Category - FB, YT & Website  ")
        st.dataframe(df)

if st.button("Reset"):
    st.session_state.results_data = []
    placeholder.empty()  
    st.rerun()  
