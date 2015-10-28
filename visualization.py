from operator import itemgetter
from statsmodels.distributions import ECDF

from collections import Counter
from collections import OrderedDict


# Visualization of Marvel heroes

heroes = read_data("heroes/")
heroes_length = {}
for key, value in heroes.iteritems() :
    heroes_length[key] = len(value)

heroes_keys,heroes_values = zip(*heroes_length.items())
numBins = 50
plt.figure(figsize=(17,8))
plt.hist(heroes_values,numBins,color='red')
plt.xlabel('Number of Characters')
plt.ylabel('Number of Pages')
plt.show()

ecdf = ECDF(heroes_values)
plt.figure(figsize=(17,8))
plt.plot(ecdf.x, ecdf.y, linewidth=3)
plt.grid(True)
plt.xlabel('Characters')
plt.ylabel('Cumulative probability')

# 10 superheroes with longest pages
sorted_heroes = sorted(heroes_length.items(), key=itemgetter(1), reverse=True)
heroes_keys,heroes_values = zip(*sorted_heroes)
plt.figure(figsize=(17,8))
plt.bar(np.arange(1,11),heroes_values[:10], color='yellow')

plt.xlabel('Superheroes')
plt.ylabel('Characters')
plt.xticks( np.arange(1,11), heroes_keys[:10], rotation=45 )
plt.show()

# For each superhero, extract the debut year from the infobox
infobox_reg = re.compile(ur'{{(Superherobox|Infobox comics character)(.+?)}}', re.DOTALL)
debut_reg = re.compile(ur'^\|\s*?debut\s*?=(.+?)\n', re.MULTILINE)
year_reg = re.compile(ur'(\d{4})')

#infobox_reg = re.compile(ur'{{Superherobox(.+?)}}', re.DOTALL)
#debut_reg = re.compile(ur'^\|debut=(.+?)\n', re.MULTILINE)
#year_reg = re.compile(ur'(\d{4})')

debut_list = []

for hero in heroes.iteritems():
    
    reg = re.search(infobox_reg, hero[1])
    
    if reg is not None:
        infobox = reg.group()
        
        debut = re.search(debut_reg, infobox)
        if debut is not None:
            year = re.findall(year_reg, debut.group())
            
            if year:
                debut_list.append(int(min(year)))
				
# Visualize the number of superheroes that were introduced by year.
counter_debut = Counter(debut_list)

timex = np.arange(min(counter_debut), max(counter_debut)+1)
timey = []

for year in timex:
    timey.append(counter_debut[year])
      
years = sorted(Counter(debut_list).iteritems(),key=itemgetter(0))

plt.figure(figsize=(17,8))
plt.bar(timex,timey, color='orange')
plt.grid(True)
plt.xlabel('Timeline - Year')
plt.ylabel('Number of Heroes Introduced')
plt.show()

# Plot the timeline of Villain creations
debut_list2 = []

for villain in villains.iteritems():
    
    reg = re.search(infobox_reg, villain[1])
    
    if reg is not None:
        infobox = reg.group()
        
        debut = re.search(debut_reg, infobox)
        if debut is not None:
            year = re.findall(year_reg, debut.group())
            
            if year:
                debut_list2.append(min(year))

                k2= Counter(debut_list2)
				
plt.figure(figsize=(17,8))

timex2= np.arange(1939,2013)
timey2=[]
for year in timex2:
    timey2.append(k2[str(year)])
    
plt.bar(timex2, timey2)
plt.xlabel("Year of appearance")
plt.ylabel("Number of Villains introduced")
plt.show()

# Cumulative distributions:
plt.figure(figsize=(17,8))
plt.plot(timex2, np.cumsum(timey2),color='red',label="villains",linewidth=5)  # From 0 to the number of data points-1
plt.plot(timex, np.cumsum(timey),color='blue',label="heroes",linewidth=5)  # From 0 to the number of data points-1
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('Timeline - Year')
plt.ylabel('Number of Heroes')
#plt.step(sorted_data[::-1], np.arange(sorted_data.size))  # From the number of data points-1 to 0

plt.show()

# Extract the teams that each superhero belong to
import re
infobox_reg = re.compile(ur'{{(Superherobox|Infobox comics character)(.+?)}}', re.DOTALL)
alliances_reg = re.compile(ur'^\|\s*?alliances\s*?=(.+?)\n', re.MULTILINE)
alliance_reg = re.compile(ur'\[\[(.+?)(?:\|(?:.+?))?]]')

alliance_counter = Counter()

for hero in heroes.iteritems():

    reg = re.search(infobox_reg, hero[1])
    
    if reg is not None:
        infobox = reg.group()
        
        alliances = re.search(alliances_reg, infobox)
        if alliances is not None:
            year = re.findall(alliance_reg, alliances.group())
            
            if year:
                #print hero[0]
                #print year
                alliance_counter.update(year)
				
# Count the number of members for each team
bars = 10

heroes_keys,heroes_values = zip(*alliance_counter.most_common()[:bars])

plt.figure(figsize=(17,8))
plt.bar(np.arange(1,bars+1),heroes_values, color='yellow')

plt.xlabel('Alliance')
plt.ylabel('Number of Characters')
plt.xticks( np.arange(1,bars+1), heroes_keys, rotation=45 )
plt.show()