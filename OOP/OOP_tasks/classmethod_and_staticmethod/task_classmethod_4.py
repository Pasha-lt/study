# Declare a class Video in your program with two methods:
#
# create(self, name) - to set the name of the current video
# (the method stores the name in the local attribute name of the Video class object);
# play(self) - to play the video (the method prints the string "playing video <name>" to the screen).
#
# Declare another class named YouTube with two methods (with the @classmethod decorator):
#
# add_video(cls, video) - to add a new video (the method puts the Video class object video into a list);
# play(cls, video_indx) - to play a video from the list by the specified index (zero-based indexing).
#
# (here cls is a reference to the YouTube class). And a list (also inside the YouTube class):
#
# videos - to store the added Video class objects (initially the list is empty).
#
# The play() method of the YouTube class should refer to the Video class object by the index of the videos list,
# and then call the play() method of the Video class.
#
# Call the add_video and play methods directly from the YouTube class. No need to create an instance of this class.
#
# Create two Video class objects v1 and v2, then, using the create() method,
# give them the names "Python" and "Python OOP". After that, using the add_video method of the YouTube class,
# add these two videos to it and play (using the play method of the YouTube class) first the first video,
# and then the second video.
#
# Sample Input:
#
# Sample Output:
# playing video Python
# playing video Python OOP

class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"playing video {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python OOP")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
