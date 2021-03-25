# opens several tabs on Google search results
# accepts one argument in command line

import sys, requests, webbrowser, bs4, re

# downloading the Google Page
search = ' '.join(sys.argv[1:])
results = 10 # valid options 10, 20, 30, 40, 50, and 100
res = requests.get(f"https://www.google.com/search?q={search}&num={results}")
res.raise_for_status()

# retrieve top search results links
soup = bs4.BeautifulSoup(res.content, "lxml")
links = soup.findAll("a") # get all the links
results = [] # store the filtered links
for link in links : # filter each link in links
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        link = link.get('href').split("?q=")[1].split("&sa=U")[0]
        results.append(link)

minResults = min(5, len(results)) # 5 results only
for i in range(minResults):
  webbrowser.open(results[i])  # open top 5 results in browser
