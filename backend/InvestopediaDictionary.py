import requests
from bs4 import BeautifulSoup

# Send a GET request to the Investopedia website
url = "https://www.investopedia.com/financial-term-dictionary-4769738"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="dictionary-top24-list__list_1-0")

urldict = {}

job_elements = results.find_all("a", class_="dictionary-top24-list__sublist mntl-text-link")

for job_element in job_elements:
    url = job_element["href"]
    # print(url)
    text = job_element.text
    # print(text)
    print()
    urldict[text] = url

print(urldict)

for i in range(13):
    string = "dictionary-top24-list__list_1-0-" + str(i + 1)
    results = soup.find(id=string)
    # print(string)
    job_elements = results.find_all("a", class_="dictionary-top24-list__sublist mntl-text-link")
    for job_element in job_elements:
        url = job_element["href"]
        # print(url)
        text = job_element.text
        # print(text)
        # print()
        urldict[text] = url

for i in range(12):
    string = "dictionary-top24-list__list_2-0-" + str(i + 1)
    results = soup.find(id=string)
    # print(string)
    job_elements = results.find_all("a", class_="dictionary-top24-list__sublist mntl-text-link")
    for job_element in job_elements:
        url = job_element["href"]
        # print(url)
        text = job_element.text
        # print(text)
        # print()
        urldict[text] = url

print(urldict)


# import re
#
# def hyperlink_terms(text, terms_dict):
#     """
#     Replaces all occurrences of financial terms in text with hyperlinks to their respective URLs.
#
#     Parameters:
#     text (str): The text to be processed.
#     terms_dict (dict): A dictionary mapping financial terms to their corresponding URLs.
#
#     Returns:
#     str: The processed text with hyperlinks added.
#     """
#     # Compile a regular expression pattern that matches any of the financial terms
#     pattern = re.compile(r'\b(' + '|'.join(re.escape(term) for term in terms_dict.keys()) + r')\b')
#
#     # Replace each occurrence of a financial term with a hyperlink to its corresponding URL
#     def replace(match):
#         term = match.group(1)
#         url = terms_dict.get(term)
#         return f'<a href="{url}">{term}</a>'
#
#     return pattern.sub(replace, text)

# text = "I invested in some stocks and bonds yesterday. What's the difference between the two?"
# processed_text = hyperlink_terms(text, terms_dict)
# print(processed_text)