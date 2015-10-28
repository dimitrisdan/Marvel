def get_members(category,con=" "):
    """ Return a list from wikipedia with the members in the given category """

    members = []
    none = []
    url = 'http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{}&cmprop=title&cmlimit=500&format=json&continue=&cmcontinue={}'.format

    while con:
        
        response = urllib2.urlopen(url(category,con)) 
        json_dict = json.loads(response.read())
        
        members.extend([member['title'] for member in json_dict['query']['categorymembers'] if member['ns'] == 0])
        none.extend([member['title'] for member in json_dict['query']['categorymembers'] if member['ns'] != 0])

        if json_dict.has_key('continue'):
            con = json_dict['continue']['cmcontinue']
        else:
            con = False
    
    return members
	

def download_pages(pages,folder):
    """ Download the wiki pages from a list in the given folder """
    
    link = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles={}&prop=revisions&rvprop=content'.format
    
    if not os.path.isdir(folder):
            os.makedirs(folder)
            print "Folder" + folder + " has been created."
    
    for page in pages:
        url_title = urllib2.quote(page.encode('utf8'))
        response = urllib2.urlopen(link(url_title))
        html = response.read().decode('utf-8')
        if page != u'Se\xf1or Muerte / Se\xf1or Suerte' :
            f = codecs.open(folder +'/'+ page + '.json','w','utf-8')
            f.write(html)
            f.close
        else :
             f = codecs.open(folder +'/'+ 'Senor Muerte_Senor Suerte'+ '.json','w','utf-8')
             f.write(html)
             f.close


 def read_data(folder):
    filelist = os.listdir(folder)
    data = {}

    for file in filelist:
        
        file = codecs.open(folder + file,'r','utf-8')
        source = json.loads(file.read())
        file.close()
        
        title = source['query']['pages'].itervalues().next()['title']
        content = source['query']['pages'].itervalues().next()['revisions'][0]['*']

        data[title] = content
    
    return data
	

heroes_list = get_members("Marvel_Comics_superheroes")
print "Number of Heroes mined: "
print len(heroes_list)
#download_pages(heroes_list,"heroes") # Uncomment to download the pages		

villains_list = get_members("Marvel_Comics_supervillains")
print "Number of Villains mined: "
print len(villains_list)
#download_pages(villains_list,"villains") # Uncomment to download the pages

ambigous_list = set(heroes_list).intersection(villains_list)
print "Number of Ambiguous: "
print len(ambigous_list)
#download_pages(ambigous_list,"ambigous/") # Uncomment to download the pages 

villains = read_data("villains/")
heroes = read_data("heroes/")
ambigous = read_data("ambigous/")

print len(villains)
print len(heroes)
print len(ambigous) 