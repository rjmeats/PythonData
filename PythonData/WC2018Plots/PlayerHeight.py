import csv
import matplotlib.pyplot as plt
import numpy as np
import urllib
import io

if __name__ == "__main__" :

    #filename = r'C:\Users\owner\Git\MiscellaneousData\MiscellaneousData\output_data\WorldCup2018Squads\FIFA_tables_from_PDF.csv'
    #with open(url, newline='', encoding='utf-8') as csvfile :
    #    csvreader = csv.reader(csvfile,    delimiter = ',')        
    #    print(csvreader)
    # url = r'https://gist.github.com/rjmeats/a0d7e0154afe43d42a467324a69c19ff#file-fifa_tables_from_pdf-csv'       # Need link to raw file
    url = r'https://gist.githubusercontent.com/rjmeats/a0d7e0154afe43d42a467324a69c19ff/raw/a2789f5c07abe16b8c412dd6baa7d553cec2eb12/FIFA_tables_from_PDF.csv'
    response = urllib.request.urlopen(url)
    csvreader = csv.reader(io.StringIO(response.read().decode('utf-8')), delimiter=',') 

    fieldnames = []
    playerInfo = []
    for row in csvreader :
        if len(fieldnames) == 0 :
            fieldnames = row
        else :
            d = dict(zip(fieldnames, row))
            playerInfo.append(d)
    
    print('Found details of {0} players'.format(len(playerInfo)))

pn = list(range(len(playerInfo)))
pw = list(map(int, [ p['Weight'] for p in playerInfo])) #if p['National Team'] != "XXEngland"]))
ph = list(map(int, [ p['Height'] for p in playerInfo])) #if p['National Team'] != "XXEngland"]))


fig, ax = plt.subplots()
#ax.plot(pw, ph)
ax.scatter(pw, ph)

ax.set(xlabel='Weight (kg)', ylabel='Height (cm)', title='World Cup 2018\nPlayer heights and weights')
# ax.grid()

#fig.savefig("test.png")
plt.show()

