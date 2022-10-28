import sys
import random
from pico2d import *


class mob:
    image = None

    def handle_events(self, event):
        #능지를... 부여해.. 쥬세요
        pass

    def __init__(self): #렉 안걸리는 법
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        if mob.image == None:
            mob.image = load_image('mob.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)