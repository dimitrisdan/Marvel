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