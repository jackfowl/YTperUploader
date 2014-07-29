import database as db
import youtube as yt
import Tkinter as tk
import ttk
import webbrowser

YT_KEY = 'AI39si5Hoj2If4u1UHi0FuPGJVLEhEvpku1Aox01MSs23PHQObHuLrkhS7qsdJrIDS_cfkT4ZrhOzDbbh_a6377FP8b1Ykcu3A'

class VideoObject:
    title, date, url, viewed = '', '', '', False

    def __init__(self, title, date, url):
        self.title = title
        self.date = date
        self.url = url

class VideoControl(tk.Frame):
    
    def __init__(self, video, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.W)
        self.see = tk.Button(self, text=video.title)
        self.see.grid(row=0,column=0,sticky=tk.W)

class ChannelTab(ttk.Frame):
    text, videos, controls, pages = '', [], [], 1
    
    def __init__(self, channel, videos, master=None):
        ttk.Frame.__init__(self, master)
        self.text = channel
        self.videos = videos
        self.grid(row=0,column=0,sticky=tk.W)
        self.draw(2)

    def draw(self, page=1):
        for video in self.videos[((page-1)*25):page*25]:
            self.controls.append(VideoControl(video))


class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
        
    def createWidgets(self):
        top=self.winfo_toplevel()
        #Adding channels panel
        self.channel = tk.Entry(self)
        self.channel.grid(row=0, column=0, stick=tk.W)
        self.add = tk.Button(self, text='Add', command=self.addChannel)
        self.add.grid(row=0, column=1, stick=tk.W)
        self.quit = tk.Button(self, text='Close', command=top.destroy)
        self.quit.grid(row=0, column=2, stick=tk.E)
        #Show added channels panel
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row=1, column=0, stick=tk.W)
        self.frames = []
        for key in lista.keys():
            print(key)
            self.frames.append(ChannelTab(key, lista[key], self.tabs))
            self.tabs.add(self.frames[-1], text=key)

    def addChannel(self):
        print(self.channel.get())
        saveEntryResults(self.channel.get(), yt_service)
        self.channel.delete(0, tk.END)

#------------------------------------------------------------------------        

def entryToVideoObject(entry):
    return VideoObject(entry.media.title.text,
                       entry.published.text,
                       entry.media.player.url)    

def addToList(channel, video):
    result = True
    if lista.has_key(channel):
        result = videoExists(video, lista[channel])
        if not result:
            lista[channel].append(video)
    else:
        lista[channel] = [video]
   
def videoExists(video, videos):
    result = False
    for item in videos:
        result = (video.url == item.url)
        if result: break

def printEntryDetails(entry):
    print 'Video title: %s - %s - %s' % entry.media.title.text % entry.published.text % entry.media.player.url

def saveEntryResults(channel, yt_service, index=1):
    entries = yt_service.getUserUploads(channel, index)
    if entries:
        for entry in entries:
            if not addToList(channel, entryToVideoObject(entry)):
                more = False
                break
        if more:
            saveEntryResults(channel, yt_service, index+50)
    db.saveDB(lista)

if __name__ == '__main__':
    yt_service = yt.MyYouTubeService(YT_KEY)
    
    lista = db.loadDB()
    for key in lista.keys():
        saveEntryResults(key, yt_service)
    
    app = Application()
    app.master.title('YTperUploader')    
    app.mainloop()
