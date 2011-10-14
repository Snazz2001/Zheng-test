import urllib2
import re
import pymongo
def findScript(url):
    c=urllib2.urlopen(url)
    contents=c.read()
    pattern = '<script type="text/javascript">.*?_gat._getTrack.*?</script>' #using regular expression to find the track scripts if we know the patten of those scripts, if this is unknown, we can find it using some feature selection to identify the relate feature based on the correlation between the feature and the lable of the document(contain tracking script or not), 
    p = re.compile(pattern)
    m = p.search(contents)                                                 #search the content for the patten
    if m:
        return m.group()                                                   #if found, return it.
    else:
        return None

def sinkMongo(uss)
    from pymongo import Connection    #here we use mongodb to store the data, we can also use xml to store it, but given the data set may be very large, I prefer to store it in NOsql.
    c= Connection()                   #Establish the connection
    db = c.spideio                    #Open the database
    collection = db.urlscripts        #Select the collection 
    for us in uss                     #Insert the urlscript document to the collection
        collection.insert(us)

def main(urls)                        #assume the urls contain the url pool we need  
    urlscripts = {};                  #dictionary to store the url:script pair
    counter = 0;                      #set a counter, whenever we obtain 1000 scripts, we store them into database
    for url in urls
        script = findScript(url)
        if script != None
            urlscripts[url] = script  
            counter++;
        if counter > 1000
            sinkMongo(urlscripts)
            counter = 0;
            urlscripts = {}
            
