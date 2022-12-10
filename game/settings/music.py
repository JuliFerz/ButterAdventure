from constantes import *


class Music:
    def __init__(self, obj_music, volume = 1):
        '''
        This class represents the game music. It can play, play in loop, stop, or change volume music

        :param obj_music: obj
        :param volume: int
        '''
        self.obj_music = obj_music
        self.volume = volume
    
    def change_volume(self, music, value):
        self.volume += value
        if self.volume <= 0: self.volume = 0
        if self.volume >= 1: self.volume = 1

        if DEBUG: print(self.volume)
        self.Volume(music, self.volume)

    def Volume(self, music, value):
        return music.set_volume(value)
    
    def Play(self, music):
        return music.play()
    
    def PlayInLoop(self, music):
        return music.play(-1)

    def Stop(self, music):
        return music.stop()
