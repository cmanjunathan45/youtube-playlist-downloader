from pytube import *
import pafy  
url =input("Enter the playlist URL : ")
playlist = pafy.get_playlist(url) 
items = playlist["items"] 
for i in range (0,2000000000000000000):
	try:
		item = items[i] 
		i_pafy = item['pafy'] 
		y_url = i_pafy.watchv_url 
		print(y_url) 
		
		yt=YouTube(y_url)
		y = yt.streams.get_highest_resolution()
		y.download('videos')
		
	except:
		print("done")
		print(f"totally {i} videos")
		break


