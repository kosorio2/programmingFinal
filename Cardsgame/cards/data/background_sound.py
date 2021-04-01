import arcade
import time

MUSIC_VOLUME = 0.5

class MySound(arcade.Window):
    """ Main application class. """

    def __init__(self):


        # Variables used to manage our music. See setup() for giving them
        # values.
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        self.sound_list = []
        self.sound = None
    

    def advance_song(self):
        """ Advance our pointer to the next song. This does NOT start the song. """
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
        print(f"Advancing song to {self.current_song_index}.")

    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop()

        # Play the next song
        #print(f"Playing {self.music_list[self.current_song_index]}")
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of music
        self.music_list = [":resources:music/funkyrobot.mp3", ":resources:music/1918.mp3"]
        # Array index of what to play
        self.current_song_index = 0
        # Play the song
        self.play_song()


    def play_sound(self):

        self.music = arcade.Sound(self.sound_list, streaming=True)
        self.current_player = self.sound.play(MUSIC_VOLUME*2)


    def card_sound(self):

        self.sound_list = [":resources:sounds/upgrade3.wav"]

        self.play_sound()