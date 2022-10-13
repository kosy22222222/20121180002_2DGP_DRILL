
import pico2d
import game_framework
import logo_state
import play_state

# 위에 치고... 아래에 열심히 임폴트한거 두개 . 붙여서 적어주고...


pico2d.open_canvas()
game_framework.run(logo_state)
pico2d.close_canvas()


"""state.enter()

# game main loop code
while state.running:
    state.handle_events()

#게임 월드 객체를 업데이트 - 게임 로직
    state.update()
    state.draw()
    pico2d.delay(0.05)
state.exit()"""

# finalization code
pico2d.close_canvas()
