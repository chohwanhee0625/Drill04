from pico2d import *

open_canvas()

TUK_WHIDTH, TUK_HEIGHT = 1280, 860
open_canvas(TUK_WHIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('cat.png')

def handle_events():
    global running, dir, vert

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            if event.key == SDLK_UP:
                vert += 1
            elif event.key == SDLK_DOWN:
                vert -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_UP:
                vert -= 1
            elif event.key == SDLK_DOWN:
                vert += 1

running = True
x, y = TUK_WHIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir, vert = 0, 0

while (running):
    clear_canvas()

    tuk_ground.draw(TUK_WHIDTH // 2, TUK_HEIGHT // 2)

    if (dir == -1):
        character.clip_draw(frame * 84, 0, 84, 56, x, y)
    else:
        character.clip_draw(frame * 84, 57, 84, 56, x, y)
    update_canvas()

    handle_events()

    if (dir > 0):
        frame = (frame + 1) % 8
    else:
        frame = (frame - 1) % 8

    if (x <= TUK_WHIDTH and x >= 0 and y <= TUK_HEIGHT and y >= 0):
        x += dir * 10
        y += vert * 10
    else:
        x -= dir * 50
        y -= vert * 50

    delay(0.05)

close_canvas()

# code complete