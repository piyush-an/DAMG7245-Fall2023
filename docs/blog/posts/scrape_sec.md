---
draft: false 
date: 2023-10-11
authors:
  - piyush
categories:
  - SEC Form
  - Web Scraping
---

# How to Scrape SEC Form Data Using BeautifulSoup in Python

## Getting Started with SEC Form Data Scraping

In the ever-evolving world of finance, access to timely and accurate data is a critical asset for investors, analysts, and researchers. The U.S. Securities and Exchange Commission (SEC) is a treasure trove of such data, with companies filing various financial reports and disclosures through SEC forms. Extracting and analyzing this data can provide valuable insights for decision-making and research.

In this section, we'll embark on a journey to explore the process of scraping SEC form data using Python and the BeautifulSoup library. Whether you're a financial analyst seeking the latest corporate filings, a student conducting research, or just a curious data enthusiast, this guide will walk you through the fundamentals of web scraping and data extraction from the SEC's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) database.

By the end of this section, you'll have a solid foundation to navigate SEC form pages, retrieve financial information, and be well on your way to harnessing the power of web scraping for financial analysis.


## Installing BeautifulSoup

Before we dive into the world of web scraping and SEC form data extraction, we need to ensure that we have the necessary tools at our disposal. One of the key libraries we'll be using for this task is BeautifulSoup (often abbreviated as BS4).

BeautifulSoup is a Python library that makes it easy to parse and navigate HTML and XML documents. It's particularly useful for web scraping because it allows you to search and extract specific data from web pages with ease.

To get started with BeautifulSoup, we first need to install it. You can do this using pip, the Python package manager. If you're using a virtual environment for your project (which is recommended for managing dependencies), make sure you activate the environment before running the installation command.

To install BeautifulSoup, open your command line or terminal and run the following command:

```bash
pip install beautifulsoup4
```
This command will download and install BeautifulSoup and its dependencies. Once the installation is complete, you're ready to start working with BeautifulSoup to scrape SEC form data.

## Making HTTP Requests to SEC Forms Page

Now that we have BeautifulSoup installed, we're ready to begin the web scraping process. The first step in scraping SEC form data is to access the webpage containing the information we need. To do this, we'll use the `requests` library in Python.

In the code snippet below, we start by importing the necessary libraries: `requests` for making HTTP requests, `pandas` for data manipulation, and `BeautifulSoup` for parsing HTML. These libraries are crucial tools in our web scraping toolkit.

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

Next, we define the URL of the SEC Forms webpage that we want to scrape. In this example, we'll use the following URL:

```python
url = 'https://www.sec.gov/forms'
```

Now, it's time to send an HTTP GET request to this URL. The requests.get() method is used for this purpose, as shown in the code snippet below:

```python
# Send an HTTP GET request to the URL
response = requests.get(url)
```

Here, the requests.get(url) line sends an HTTP GET request to the specified URL, and the response from the server is stored in the response variable. This response object contains the content of the webpage, which we will later parse using BeautifulSoup.


## Parsing HTML Content and Locating the HTML Table

With the HTTP GET request successfully made to the SEC Forms webpage, we can now proceed to parse the HTML content of the page. To do this, we'll use BeautifulSoup, the Python library designed for precisely this purpose.

In the code snippet below, we initiate the parsing process:

```python
soup = BeautifulSoup(response.text, 'html.parser')
```

Here, we create a BeautifulSoup object named soup by passing two arguments. The first argument, response.text, is the content of the HTTP response that we received from the SEC Forms webpage. The second argument, `html.parser`, specifies the parser we want to use for parsing the HTML content.

With the HTML content successfully parsed, the next step is to locate the HTML table that contains the SEC form data. This table is where the form data is organized in a structured manner.

In the following code snippet, we search for the first `table` element within the parsed HTML:

```python
table_element = soup.find('table')
```
 
The `soup.find('table')` line utilizes BeautifulSoup's find() method to search for the first `table` element within the parsed HTML. This element corresponds to the table that holds the SEC form data.

Once we have located the table, the subsequent task is to find and retrieve the individual rows within the table. Each row corresponds to a different SEC form entry.

In the code below, we use BeautifulSoup to find all the `tr` (table row) elements within the table:

```python
rows = table_element.find_all('tr')
```
The `table_element.find_all('tr')` line uses the `find_all()` method to collect all the `tr` elements, effectively creating a list of rows that we can iterate through and extract data from.


## Extracting Data and Creating a DataFrame

Now that we've successfully parsed the HTML content of the SEC Forms webpage and located the table, the next step is to extract relevant data from the individual SEC form entries. In this section, we'll explore how the provided code accomplishes this task.

We've initiated an empty list named `data` to store the extracted data:

```python
# Initialize an empty list to store extracted data
data = []

# Loop through each row in the table, skipping the header row (index 0)
for row in rows[1:]:
  
  # Extract the form number from the row
  form_no = row.find('span', class_='show-for-small').find_next_sibling(string=True).strip()
  
  # Extract the form title from the row
  form_title = row.find('td', class_='display-title-content views-field views-field-field-display-title').find('a').get_text()
  
  # Construct the full form URL by appending the base URL to the 'href' attribute
  form_url = f"https://www.sec.gov{row.find('td', class_='display-title-content views-field views-field-field-display-title').find('a')['href']}"
  
  # Extract the last updated date from the 'datetime' attribute
  last_updated = row.find('time')['datetime']
  
  # Send an HTTP GET request to check if the form URL is valid
  response = requests.get(form_url)
  
  # Check the HTTP response status code to determine if the link is valid
  if response.status_code == 200:
    link_valid = 'Y'  # Valid link
  else:
    link_valid = 'N'  # Invalid link
  
  # Append the extracted data as a list to the 'data' list
  data.append([form_no, form_title, form_url, last_updated, link_valid])

# Create a DataFrame from the list of extracted values with defined column names
df = pd.DataFrame(data, columns=['Form No', 'Form Title', 'Form URL', 'Last Updated', 'Link Valid'])

# Print the DataFrame to display the extracted SEC form data
df
```

Within this loop, we extract various pieces of information from each SEC form entry. Here's what we extract and how we do it:

- **form_no:** We find the form number by locating a `<span>` element with the class 'show-for-small' and then navigating to the next sibling containing the form number text.

- **form_title:** We locate the form title by finding a `<td>` element with the class 'display-title-content' and a nested `<a>` element, from which we extract the text.

- **form_url:** We construct the form's URL by combining the SEC's base URL with the 'href' attribute of the anchor element.

- **last_updated:** We extract the 'datetime' attribute of the 'time' element, which provides the last update date of the form.

- **link_valid:** We check the validity of the form's URL by sending another HTTP GET request to the form's URL and verifying if the response status code is 200 (indicating a successful request). We store 'Y' if the link is valid and 'N' if it's not.

We append these extracted values as lists to the `data` list.

After extracting the data, we use the `pandas` library to create a DataFrame named `df`. This DataFrame stores the extracted values and has the following columns: 'Form No', 'Form Title', 'Form URL', 'Last Updated', and 'Link Valid'.

Finally, we print the DataFrame to display the extracted SEC form data in a structured and tabular format.

|index|Form No|Form Title|Form URL|Last Updated|Link Valid|
|---|---|---|---|---|---|
|0||Examination Brochure: Information about Examinations \(PDF\)|https://www\.sec\.gov/files/exam-brochure\.pdf|2023-01-31|Y|
|1||Transferred Federal Employees|https://www\.sec\.gov/ohr/transferred-federal-employees-page-link|2016-05-24|Y|
|2||Term Employees|https://www\.sec\.gov/ohr/term-employees-page-link|2016-05-24|Y|
|3|1|Application for registration or exemption from registration as a national securities exchange \(PDF\)|https://www\.sec\.gov/files/form1\.pdf|1999-02-01|Y|
|4|1-A|Regulation A Offering Statement \(PDF\)|https://www\.sec\.gov/files/form1-a\.pdf|2021-09-27|Y|

## Conclusion

Congratulations! You've learned how to scrape SEC form data using Python and BeautifulSoup. The code provided in this blog post extracts valuable information from the SEC Forms webpage, including form numbers, titles, URLs, last updated dates, and link validity.

Now, if you're eager to put this knowledge into practice and run the code yourself, I invite you to refer to our accompanying Python notebook. You can access the notebook at [Github](https://github.com/piyush-an/DAMG7245-Fall2023/blob/main/notebooks/Scrape_SEC_forms.ipynb).

In the Python notebook, you'll find the complete code and be able to execute it step by step. Feel free to modify and adapt it to your specific needs, whether you're a financial analyst seeking data for analysis, a student conducting research, or anyone interested in exploring the world of web scraping.

Remember to stay mindful of ethical web scraping practices, respect the website's terms of use, and always handle data with care. Happy scraping, and may your exploration of SEC form data be insightful and productive!

[Scrape_SEC_forms.ipynb](https://github.com/piyush-an/DAMG7245-Fall2023/blob/main/notebooks/Scrape_SEC_forms.ipynb)
