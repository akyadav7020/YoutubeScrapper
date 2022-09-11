from pytube import YouTube

def youtubescraper(id):
    link = "https://www.youtube.com/watch?v="+id
    video = YouTube(link)
    title = video.title
    videos = video.streams.filter(only_video=True,res="144p",mime_type="video/mp4")
    thumbnail_url = video.thumbnail_url
    return(link,title,thumbnail_url)








