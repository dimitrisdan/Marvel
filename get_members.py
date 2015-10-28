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