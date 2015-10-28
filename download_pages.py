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
