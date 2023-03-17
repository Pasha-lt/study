# Declare a class named MediaPlayer with two methods:
#
# open(file) - for opening a media file with the name file
# (creates a local property filename with the value of the file argument in the MediaPlayer class object)
# play() - for playing the media file (prints the string "Playing <media file name>")
#
# Create two instances of this class with the names: media1 and media2. Call the open()
# method with the argument "filemedia1" for the media1 object and "filemedia2" for the media2 object. After that, call the play() method through the objects. As a result, two lines should be displayed on the screen (without quotes):
#
# "Playing filemedia1"
# "Playing filemedia2"


class MediaPlayer:
    def open(self, filename):
        self.filename = filename

    def play(self):
        print(f"Playing {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()
