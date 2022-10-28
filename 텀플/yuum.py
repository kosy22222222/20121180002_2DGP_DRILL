from pico2d import *

# 이벤트 정의
RD, LD, UD, DD, RU, LU, UU, DU = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU
}


class IDLE:  # 클래스를 이용해 상태를 만듦
    @staticmethod
    def enter():
        print('ENTER RUN')
        pass

    @staticmethod
    def exit():
        print('EXIT RUN')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class Yuum:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter()

        '''if event.type == event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_LEFT:
                    self.dir -= 1
                case pico2d.SDLK_RIGHT:
                    self.dir += 1
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    self.dir += 1
                    self.face_dir = -1
                case pico2d.SDLK_RIGHT:
                    self.dir -= 1
                    self.face_dir = 1'''
        pass

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('yuum.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()
        '''self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)'''

    def draw(self):
        self.cur_state.draw()
        '''if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)'''


class RUN:

    def enter():
        pass

    def do():
        pass

    def exit():
        pass

    def draw():
        pass


next_state = {
    IDLE: {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN},
    RUN: {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE}  # 이해 안가므로 녹강 볼 것..
}

