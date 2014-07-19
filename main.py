import gdata.youtube
import gdata.youtube.service

import database as db

class VideoObject:
    title, date, url, viewed = '', '', '', False

    def __init__(self, title, date, url):
        self.title = title
        self.date = date
        self.url = url

myKey = 'AI39si5Hoj2If4u1UHi0FuPGJVLEhEvpku1Aox01MSs23PHQObHuLrkhS7qsdJrIDS_cfkT4ZrhOzDbbh_a6377FP8b1Ykcu3A'
lista = {}
yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True

def GetUserUploads(username, index):
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.author = username
    query.orderby = 'published'
    query.max_results = 1
    query.time = 'all_time'
    query.start_index = index
    query.key = myKey
    return yt_service.YouTubeQuery(query).entry

def EntryToVideoObject(entry):
    return VideoObject(entry.media.title.text,
                       entry.published.text,
                       entry.media.player.url)    

def AddToList(channel, video):
    if lista.has_key(channel):
        lista[channel].append(video)
    else:
        lista[channel] = [video]
    db.SaveDB(lista)
   
def VideoExists(url, videos):
    result = false
    for item in videos:
        result = (video.url == url)
        if result: break

def PrintEntryDetails(entry):
    print 'Video title: %s - %s - %s' % entry.media.title.text % entry.published.text % entry.media.player.url

def SaveEntryResults(channel,index=1):
    entries = GetUserUploads(channel, index)
    if entries:
        more = False
        for entry in entries:
            video = EntryToVideoObject(entry)
            if not VideoExists(video.url):
                AddToList(channel, video)           
        if more:
            VideoResults(index+50)
       
lista = db.LoadDB()
for key in lista.keys():
    SaveEntryResults(key)
    


