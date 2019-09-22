from PIL import Image
import matplotlib.pyplot as plt

all_photos = ['/home/mayank/Desktop/GitRepos/MyWebsite/images/Audio_Source_Separation.png',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/craft_example.gif',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/HSI.jpg',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/IDRiD.png',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/ping_pong.png',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/Pixel-Link.png',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/RSA.jpeg',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/SocketProgramming.jpg',
'/home/mayank/Desktop/GitRepos/MyWebsite/images/stitch.jpg']

for photo_i in all_photos:

	image = Image.open(photo_i)
	if image.size[0] == 1433 and image.size[1] == 660:
		print('Continue for ', photo_i)
		continue
	print('Resizing ', photo_i)
	image = image.resize((1433, 660))
	image.save(photo_i)