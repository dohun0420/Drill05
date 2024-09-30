from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True

def handle_events():

    global running  # global이 없을 시 위의 running과 아래 running은 다른 취급

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False # global 없을 시 running : 지역변수
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    events = get_events
    pass

frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if not running: # loop 제어변수
        break

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
