# Escreva o seu código aqui :-)
import pygame
import random

nuvem = Actor("nuvem")
rato = Actor("rato")
points = 0

# TELA
playing_area_width = 400
playing_area_height = 400

# TUBO
pipe_width = 30
pipe_space_height = 100

pipe_space_y = 150
pipe_space_y_2 = 250
pipe_x = playing_area_width - pipe_width

pipe2_space_y = 150
pipe2_space_y_2 = 250
pipe_x2 = playing_area_width - pipe_width + 300

# NUVENS
cloud_x_1 = 15
cloud_x_2 = 315

# RATO
rato_x_1 = 60
rato_x_2 = 200
rato_y_speed = 0

game_over = False
color = (35, 92, 118)


def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect((0, 0), (playing_area_width, playing_area_height)), color=(35, 92, 118)
    )

    nuvem.pos = (cloud_x_1, 50)
    nuvem.draw()

    nuvem.pos = (cloud_x_2, 150)
    nuvem.draw()

    rato.pos = (rato_x_1, rato_x_2)
    rato.draw()

    draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height)
    draw_pipe(pipe_x2, pipe_width, pipe2_space_y, pipe_space_height)

    screen.draw.text(f"PONTOS: {points}", (15, 15))

    if game_over is True:
        screen.draw.filled_rect(
            Rect((0, 0), (playing_area_width, playing_area_height)), color=(0, 0, 0)
        )
        screen.draw.text("YOU LOSE!", (155, 175))


def draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height):
    screen.draw.filled_rect(
        Rect((pipe_x, 0), (pipe_width, pipe_space_y)), color=(94, 201, 72)
    )

    screen.draw.filled_rect(
        Rect((pipe_x, pipe_space_y + pipe_space_height), (pipe_width, pipe_space_y_2)),
        color=(94, 201, 72),
    )


def on_key_down():
    global rato_y_speed
    if rato_y_speed > 0:
        rato_y_speed -= 250


def update(dt):
    global pipe_x, pipe_space_y, pipe_x2, pipe2_space_y, pipe_width
    global cloud_x_1, cloud_x_2, cloud_x_3
    global rato_y_speed, rato_x_2
    global game_over
    global points

    rato_y_speed += 400 * dt
    rato_x_2 += rato_y_speed * dt

    # TUBO
    if pipe_x > -30:
        pipe_x -= int(165 * dt)
    else:
        pipe_x = playing_area_width - pipe_width + 300
        pipe_space_y = random.randint(50, 250)
    if pipe_x2 > -30:
        pipe_x2 -= int(165 * dt)
    else:
        pipe_x2 = playing_area_width - pipe_width + 300
        pipe2_space_y = random.randint(50, 250)
    # NUVENS
    if cloud_x_1 > -100:
        cloud_x_1 -= 40 * dt
    else:
        cloud_x_1 = 488
        
    if cloud_x_2 > -100:
        cloud_x_2 -= 50 * dt
    else:
        cloud_x_2 = 488
    
    #RATO
    if rato_x_2 > 430:
        game_over = True
    elif rato_x_2 < -30:
        game_over = True
    elif pipe_x == rato_x_1:
        if round(rato_x_2) <= pipe_space_y or round(rato_x_2) >= pipe_space_y + 100:
            game_over = True
        else:
            points += 1
    elif pipe_x2 == rato_x_1:
        if round(rato_x_2) <= pipe2_space_y or round(rato_x_2) >= pipe2_space_y + 100:
            game_over = True
        else:
            points += 1


def draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height):
    screen.draw.filled_rect(
        Rect((pipe_x, 0), (pipe_width, pipe_space_y)), color=(94, 201, 72)
    )

    screen.draw.filled_rect(
        Rect((pipe_x, pipe_space_y + pipe_space_height), (pipe_width, pipe_space_y_2)),
        color=(94, 201, 72),
    )


WIDTH = playing_area_width
HEIGHT = playing_area_height
