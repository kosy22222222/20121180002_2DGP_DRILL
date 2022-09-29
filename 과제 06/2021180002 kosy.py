from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir, dirr
    global k

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                k = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                k=0
            elif event.key == SDLK_UP:
                dirr += 1
                k += 2
                if k>3:
                    k -= 2
            elif event.key == SDLK_DOWN:
                dirr -= 1
                k += 2
                if k>3:
                    k -= 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dirr -= 1
            elif event.key == SDLK_DOWN:
                dirr += 1

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
dirr = 0

k = 3
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * k, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    x += dir * 5
    y += dirr * 5
    delay(0.01)

close_canvas()

