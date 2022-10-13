import pico2d
from pico2d import *
import game_framework
import item_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 500:
            self.dir = -1
            self.x = 500
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.item == '+':
            self.image.draw(self.x + 20, self.y)
        elif self.item == '-':
            self.image.draw(self.x + 10, self.y + 50)
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)


boy = None
grass = None
running = True


def enter():  # 게임 초기화:객체들을 생성
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True


def exit():
    global boy, grass, running
    del boy
    del grass


def update():
    boy.update()


def draw_world():
    grass.draw()
    boy.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


# 아래를 다 주석처리한후 실행시키면 당연히 구동 안됨. 실행문이 없으므로....


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

