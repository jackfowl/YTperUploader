import gdata.youtube
import gdata.youtube.service

class MyYouTubeService(object):
    def __init__(self, key):
        self.key = key
        self.service = gdata.youtube.service.YouTubeService()
        self.service.ssl = True
    
    def getUserUploads(self, username, index=1):
        """Pega os videos do usuario"""
        
        query = gdata.youtube.service.YouTubeVideoQuery()
        query.author = username
        query.orderby = 'published'
        query.max_results = 50
        query.time = 'all_time'
        query.start_index = index
        query.key = self.key
        return self.service.YouTubeQuery(query).entry
    
