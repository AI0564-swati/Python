# import re

# txt = input("Enter text: ")
# word = input("Enter a word : ")
# pattern = re.compile(r'\b'+re.escape(word) + r'\b',re.IGNORECASE)
# pattern = r'#\w+' # To print only #tags
# pattern = r'https?://\S+'  # To print the website
# pattern = r'\b\w*\d\w*\b'  
# pattern = r'\b\d{2}/\d{2}/\d{4}\b' # To find date
# len = 5
# pattern = r'\b\w{'+ str(len)+r'}\b' # Return a particular length word
# pattern = r'\b[A-Z][.?!]*[.?]'

# ms = re.findall(pattern,txt)
# for m in ms:
#   print("Found")
#   print(m)

# al = []
# while True:
#   word = input("Enter a word : ")
#   if word == "":
#     break
#   al.append(word)

# pattern = r'\b(?:'+'|'.join(al)+r')\b'
# matches = re.findall(pattern, txt)
# print("Found")
# for m in matches:
#   print(m)

# prefix = input("Enter prefix: ")
# suffix = input("Enter suffix: ")

# pattern = '\b'+ prefix + r'\w*' + suffix + r'\b'
# matches = re.findall(pattern, txt)
# print("Found")
# for m in matches:
#   print(m)

# import cowsay

# help('cowsay')
# cowsay.daemon("Sample")
# cowsay.kitty("Sample")
# cowsay.beavis("Sample")
# cowsay.octopus("Sample")

# Works on windows
# import winsound
# winsound.Beep(2500,5000)

# import pywhatkit
# pywhatkit.playonty("Python") # youtube search
# pywhatkit.search("Python") # google search
# pywhatkit.info("Monty Python") # wiki search
# pywhatkit.sendwhatmsg("+91987654321", "your_msg",9,9) # send message
# pywhatkit.show_history() 
# pywhatkit.shutdown(300) # Shut down the system
# pywhatkit.image_to_ascii_art(r'b1.jpg',r'b1.txt')

# Creating QR Code
# import pyqrcode
# from pyqrcode import QRCode
# s = 'Swati Tanu'
# url = pyqrcode.create(s)
# url.svg("aggqr.svg", scale = 10)

# Create audio file
# from gtts import gTTS
# obj = gTTS(text='Hello...how are you', lang='en', slow=False)
# obj.save('agg1.mp3')
# print("Done")

# Saving insta dp
# import instaloader
# ig = instaloader.Instaloader()
# ig.download_profile('i_am_yeagar', profile_pic_only=True)
# print("Done")

# Opening website page using url
# import webbrowser 
# url = input("Enter the website: ")
# webbrowser.open(url)
# print("Done")

