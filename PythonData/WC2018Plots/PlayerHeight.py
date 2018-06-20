import csv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__" :

    filename = r'C:\Users\owner\Git\MiscellaneousData\MiscellaneousData\output_data\WorldCup2018Squads\FIFA_tables_from_PDF.csv'
    with open(filename, newline='', encoding='utf-8') as csvfile :
        csvreader = csv.reader(csvfile, delimiter = ',')
        print(csvreader)
        fieldnames = []
        playerInfo = []
        for row in csvreader :
            if len(fieldnames) == 0 :
                fieldnames = row
            else :
                d = dict(zip(fieldnames, row))
                playerInfo.append(d)
        
        print(len(playerInfo))

pn = list(range(len(playerInfo)))
pw = list(map(int, [ p['Weight'] for p in playerInfo])) #if p['National Team'] != "XXEngland"]))
ph = list(map(int, [ p['Height'] for p in playerInfo])) #if p['National Team'] != "XXEngland"]))

print(ph)

# Data for plotting
#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
#ax.plot(pw, ph)
ax.scatter(pw, ph)

#ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#       title='About as simple as it gets, folks')
#ax.grid()

#fig.savefig("test.png")
plt.show()