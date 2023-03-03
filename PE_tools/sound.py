import pygame


def sound(sound: pygame.mixer.Sound, vol=1, fade_out=0, fade_in=0, one_time=False):
    """play pygame sound with his whole parameters in only one line!"""
    if one_time:
        if sound.get_num_channels() < 1:
            sound.set_volume(vol)
            sound.fadeout(fade_out)
            sound.play(0, 0, fade_in)
    else:
        sound.set_volume(vol)
        sound.fadeout(fade_out)
        sound.play(0, 0, fade_in)


def music(sound: pygame.mixer.Sound, vol=1, fade_out=0, fade_in=0):
    """play the sound only one time at once"""
    if sound.get_num_channels() < 1:
        sound.set_volume(vol)
        sound.fadeout(fade_out)
        sound.play(0, 0, fade_in)


class MusicList:
    """way to play list of sounds in a loop
    great for background musics in games"""
    i = 0

    def __init__(self, sounds: pygame.mixer.Sound, vol=1, fade_out=0, fade_in=0):
        self.sounds = sounds
        self.vol = vol
        self.fade_out = fade_out
        self.fade_in = fade_in

    def play(self):
        """put in the main loop to use
        its the MusicList tick function"""
        i = self.i
        sounds = self.sounds
        vol = self.vol
        fade_out = self.fade_out
        fade_in = self.fade_in
        sound = sounds[i % len(sounds)]
        if sound.get_num_channels() < 1:
            i += 1
            sound.set_volume(vol)
            sound.fadeout(fade_out)
            sound.play(0, 0, fade_in)
