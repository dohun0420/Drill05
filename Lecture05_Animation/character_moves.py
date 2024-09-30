from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

for x in range(0, 800, 5):
    clear_canvas()  # 백버퍼를 지운다
    grass.draw(400, 30) # 백버퍼에 그린다
    character.draw(x, 90)
    update_canvas() # 두개의 버퍼를 교환
    delay(0.01)

close_canvas()

