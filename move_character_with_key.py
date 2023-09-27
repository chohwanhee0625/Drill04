from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('cat.png')

def handle_events():
    global running, dir
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
        # fill here


running = True
x = 800 // 2
frame = 0
dir = 0

while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 85, 57, 85, 57, x, 0)
    update_canvas()

    handle_events()

    frame = (frame + 1) % 8
    x += dir * 10
    delay(0.05)

# fill here


close_canvas()

