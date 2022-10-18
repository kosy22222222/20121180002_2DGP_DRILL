from pico2d import *
import game_framework



class YUUM:
    global x, y
    global running

    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = 0
        self.image = load_image('yuum.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)

    def run(self):
        global running
        global dir, dirr
        global k
        frame = 0
        dir = 0
        dirr = 0
        k = 3
        x, y = 200, 150

        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    dir += 1
                    k = 2
                elif event.key == SDLK_LEFT:
                    dir -= 1
                    k = 1
                elif event.key == SDLK_UP:
                    dirr += 1
                    k = 3
                elif event.key == SDLK_DOWN:
                    dirr -= 1
                    k = 4
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    dir -= 1
                elif event.key == SDLK_LEFT:
                    dir += 1
                elif event.key == SDLK_UP:
                    dirr -= 1
                elif event.key == SDLK_DOWN:
                    dirr += 1


class KKO:
    def __init__(self):
        self.x, self.y = 200, 100
        self.frame = 0
        self.image = load_image('kko.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        self.image.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def enter():  # 게임 초기화:객체들을 생성
    global kko, yuum, running
    running = True
    kko = KKO()
    yuum = YUUM()


def exit():
    global kko, yuum, running
    del kko
    del yuum


def update():
    kko.update()
    yuum.update()


def draw_world():
    yuum.draw()
    kko.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass




