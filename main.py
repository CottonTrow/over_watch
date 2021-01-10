# Stat analysis for overwatch accounts. A learning opportunity.
import bs4 as bs
import pandas as pd
import urllib.request

source = urllib.request.urlopen('https://www.overbuff.com/players/pc/FiestaWare-11594').read()
soup = bs.BeautifulSoup(source, 'xml')

