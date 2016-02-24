#!/home/fedwards/anaconda2/bin/python
import pandas as pd
import urllib
import time
import os
pd.set_option("display.max_colwidth",300)
pd.options.display.max_colwidth

def makeJailFiles(csv):
    df = pd.read_csv(csv)
    for i in range(0,len(df['county'])):
        county_pdf = []
        now = time.strftime('%m-%d-%y')
        countyNameDate= df['county'][i]+df['state'][i]+now
        county_pdf = urllib.urlretrieve(df['url'][i], countyNameDate)
  
os.chdir("/home/fedwards/jail-rosters/roster-out")
makeJailFiles("../roster-url-key.csv")