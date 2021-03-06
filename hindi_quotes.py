import urllib, requests
from bs4 import BeautifulSoup

def get_hindi_quotes(text):
    print("fetching_q_hindi....")
    text = text.strip().replace(" ", "+")
    query_url = "https://www.shayarism.com/?s={}".format(text)
    
    try:
        html = requests.get(query_url)
        soup = BeautifulSoup(html.text, "html.parser")
        results = soup.select("div[class='post-entry']")

        if len(results) == 0:
            return "No results found :(\nSearch for something else :)"

        response = ""
        count = 0

        for result in results:
            response += result.getText()
            count += 1
            if count == 5:
                break
            response += "\n........\n"
        
        response = urllib.parse.quote_plus(response)
        return response
    except Exception as _:
        return "Error Occurred!"