import pygame
import random

nuvem = Actor("nuvem")
rato = Actor("rato")
points = 0

# BIRD
bird_x = 62
bird_y = 200
bird_width = 30
bird_heigth = 25
bird_y_speed = 0

# TELA
playing_area_width = 400
playing_area_height = 400

#TUBO
pipe_width = 30
pipe_space_height = 100

pipe_space_y = 150
pipe_space_y_2 = 250
pipe_x = playing_area_width - pipe_width

pipe2_space_y = 150
pipe2_space_y_2 = 250
pipe_x2 = playing_area_width - pipe_width + 300

#NUVENS
cloud_x_1 = 15
cloud_x_2 = 315

#RATO
rato_x_1 = 60
rato_x_2 = 200

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(Rect((0, 0), (playing_area_width, playing_area_height)), color=(35, 92, 118))

    nuvem.pos = ((cloud_x_1, 50))
    nuvem.draw()

    nuvem.pos = ((cloud_x_2, 150))
    nuvem.draw()

    rato.pos = ((rato_x_1, rato_x_2))
    rato.draw()

    draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height)
    draw_pipe(pipe_x2, pipe_width, pipe2_space_y, pipe_space_height)


def draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height):
    screen.draw.filled_rect(Rect((pipe_x, 0), (pipe_width, pipe_space_y)), color=(94, 201, 72))

    screen.draw.filled_rect(Rect((pipe_x, pipe_space_y + pipe_space_height), (pipe_width, pipe_space_y_2)),color=(94, 201, 72))

def update(dt):
    global pipe_x, pipe_space_y, pipe_x2, pipe2_space_y, pipe_width
    
    #TUBO
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


def draw_pipe(pipe_x, pipe_width, pipe_space_y, pipe_space_height):
    screen.draw.filled_rect(Rect((pipe_x, 0), (pipe_width, pipe_space_y)), color=(94, 201, 72))

    screen.draw.filled_rect(Rect((pipe_x, pipe_space_y + pipe_space_height), (pipe_width, pipe_space_y_2)),color=(94, 201, 72))

WIDTH = playing_area_width
HEIGHT = playing_area_height

