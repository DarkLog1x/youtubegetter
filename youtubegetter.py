import urllib, json
import pafy


foundAll = False
ind = 1
videos = []
end = 200
count =0
while not foundAll:
    inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/playlists/908A8E598C7A0F80?start-index={0}&max-results=50&alt=json&orderby=published&'.format( ind ) )
    try:
        resp = json.load(inp)
        inp.close()
        returnedVideos = resp['feed']['entry']
        #here is where the videos get stored
        for video in returnedVideos: 

            videos.append( video ) 
            count += 1 

        ind += 50
        #print len( videos )
        if ( len( videos ) > end ):
            foundAll = True
    except:
        #catch the case where the number of videos in the channel is a multiple of 50
        print "error"
        foundAll = True

print count
for video in videos:
    #print video['title'] # video title
    #print video['link'][0]['href'] #url

    url = video['link'][0]['href']
    try:
        SingleVideo = pafy.new(url)
        bestaudio = SingleVideo.getbestaudio()
        print SingleVideo.title
        print bestaudio.bitrate
        bestaudio.download()
    except:
        print "youtube Error"
    



