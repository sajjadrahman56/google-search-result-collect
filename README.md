# Google Search Link Collector 📌  

This **Streamlit app** uses **Selenium** to scrape search results from Google and categorize them into Facebook, YouTube, and Website links.

## 🚀 Features  
- 🔍 **Fetches Google Search Results** based on user input  
- 📌 **Categorizes results** into Facebook, YouTube, and Website  
- 📊 **Displays results in a table** dynamically  
- ⏳ **Spinner loading animation** while fetching results  
- ♻️ **Reset button** to clear results and start a new search  


![pag-11](https://github.com/user-attachments/assets/ab0861e5-a7fb-4356-bedd-655c2d1f6eea)


## 🛠️ Installation  

Before running the app, ensure you have **Python 3.8+** installed.  

### **1️⃣ Clone this repository**
```bash
git clone https://github.com/your-username/google-search-result-collector.git
cd google-search-result-collector
```

### **2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, manually install the required libraries:
```bash
pip install streamlit pandas selenium webdriver-manager
```
## 🎯 Running the App  
After installing the dependencies, run:
```bash
streamlit run app.py
```
Then, open the **local URL** shown in the terminal (e.g., `http://localhost:8501`).

## 🖥️ How to Use  
1. **Enter a search query** in the input box  
2. Click the **"Submit"** button  
3. Wait for the spinner to complete  
4. View the **categorized search results** in a table  
5. Click **"Reset"** to start a new search  

## ⚠️ Wait  
- This script **uses Selenium** to interact with Google, so ensure **Google Chrome** is installed.  
- It runs **headless** (no browser UI) for efficiency.  
- **Google search scraping may be blocked if overused**—use responsibly!
  
_Thank You_
