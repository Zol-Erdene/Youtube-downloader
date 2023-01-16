from pytube import YouTube
import tkinter as tk

window = tk.Tk()
window.title("Youtube downloader")
window.geometry("250x300+10+20")
window.minsize(250, 300)
window.maxsize(250, 300)

SAVE_PATH = ""

def processLink(url):    
    try:
        yt = YouTube(url)
        return yt.streams
    except:
        print("Bad link.")

def downloadAudio():
    url = link.get(1.0, "end")
    audioFiles = processLink(url).filter(type="audio")
    audioFiles.first().download(SAVE_PATH)

def downloadVideo():
    url = link.get(1.0, "end")
    videoFiles = processLink(url).filter(type="video")
    videoFiles.order_by("resolution").desc().first().download(SAVE_PATH)


lbl = tk.Label(window, text="Youtube downloader", font=(20))
lbl.place(x=30, y=10)

intro_text = tk.Label(window, text="Enter your Youtube link:")
intro_text.place(x=10, y= 40)

link = tk.Text(window, height = 5, width = 25)
link.place(x=10, y=70)

downloadButtonAudio = tk.Button(window, text = "Download audio", command = downloadAudio)
downloadButtonAudio.place(x=10, y=160)
downloadButtonVideo = tk.Button(window, text = "Download video", command = downloadVideo)
downloadButtonVideo.place(x=120, y=160)

window.mainloop()

