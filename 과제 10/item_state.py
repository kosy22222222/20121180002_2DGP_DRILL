from pico2d import *
import pico2d
import game_framework
import play_state

image = None


def enter():
    global image
    global boy
    image = load_image('add_delete_boy.png')
    boy = load_image('animation_sheet.png')
    pass


def exit():
    global image
    del image
    pass


def update(): #경과시간이 1초를 넘으면 런닝을 폴스로 만들어 준다.
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_PLUS:
                    boy.draw()
                case pico2d.SDLK_MINUS:
                    boy.draw()








def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
