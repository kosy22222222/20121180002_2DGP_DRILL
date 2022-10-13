from pico2d import *
import game_framework
import title_state

#이미지를 넣어주자!
image = None
running = True
logo_time = 0.0

def enter():
    global image, logo_time, running
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    running = True
    pass

def exit():
    global image
    del image
    pass

def update(): #경과시간이 1초를 넘으면 런닝을 폴스로 만들어 준다.
    global running
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        game_framework.change_state(title_state)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





