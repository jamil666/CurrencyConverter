from bs4 import BeautifulSoup
import urllib.request

class valyuta(object):

    url = 'http://en.cbar.az/other/azn-rates'

    def get_html(url):  # This function connects to web site

        response = urllib.request.urlopen(url)
        return response.read()

    soup = BeautifulSoup(get_html(url), 'html5lib')  # Create variable for soup

    table1 = soup.find_all("td", class_ = "rate")   # Select table with currency

    usd = table1[0].text    # Find USD field in table
    usd = float(usd)

    euro = table1[1].text   # Find Euro field in table
    euro = float(euro)

    gbp = table1[16].text   # Find GBP field in table
    gbp = float(gbp)

    rub = table1[34].text   # Find RUB field in table
    rub = float(rub)