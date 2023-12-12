"""
CP1404 Wikipedia
"""

import wikipeadia

query = input("Search Wikipedia: ")
while query != "":
    result = wikipeadia.page(query)
    print(result.title)
    print(result.url)
    print(result.summary)
    query = input("Search Wikipedia: ")