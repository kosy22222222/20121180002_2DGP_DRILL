from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#이거 아래쪽(런닝 위)으로 옮겨야 함. 옮긴후 엔터 추가
open_canvas()

#def 추가. 이후 전역 변수로 바꿔줘야 함.
#그전에 보이와 그래스를 분리해야함... 고로 none
boy = Boy()
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()
#잘모르겠는데 여기서 업데이트 드래그 하고 우클릭 해서 리팩터 누르고 메소드 한다음 업데이트라 해주면 뭐가 된대...
    boy.update()

#위의 네줄도 리팩터... 드로우로 명명
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
