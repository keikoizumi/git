from ast import Import
import os

#ref https://soundeffect-lab.info/sound/button/
#OS PATH
PATH = os.getcwd()

#caption
CAPTION = 'Snake And Apple Game'

#display
DIP_W = 1000
DIP_H = 600

#image
B_IMG_PATH = os.path.join(PATH,'resources/images/background.jpg')
SNAKE_YELLOW_IMG_PATH = os.path.join(PATH,'resources/images/yellow_block.jpg')
SNAKE_RED_IMG_PATH = os.path.join(PATH,'resources/images/red_block.jpg')
SNAKE_GREEN_IMG_PATH = os.path.join(PATH,'resources/images/green_block.jpg')
SNAKE_BLUE_IMG_PATH = os.path.join(PATH,'resources/images/blue_block.jpg')
SNAKE_YELLOW_FACE_IMG_PATH = os.path.join(PATH,'resources/images/yellow_face.png')
SNAKE_RED_FACE_IMG_PATH = os.path.join(PATH,'resources/images/red_face.png')
SNAKE_GREEN_FACE_IMG_PATH = os.path.join(PATH,'resources/images/green_face.png')
SNAKE_YELLOW_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH,'resources/images/yellow_had_bad_apple_face.png')
SNAKE_RED_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH,'resources/images/red_had_bad_apple_face.png')
SNAKE_GREEN_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH,'resources/images/green_had_bad_apple_face.png')
SNAKE_BLUE_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH,'resources/images/blue_had_bad_apple_face.png')
#SNAKE_YELLOW_TAIL_IMG_PATH = os.path.join(PATH,'resources/images/yellow_tail.png')
APPLE_IMG_PATH = os.path.join(PATH,'resources/images/apple.jpg')
BAD_APPLE_IMG_PATH = os.path.join(PATH,'resources/images/badapple.jpg')
GOLD_APPLE_IMG_PATH = os.path.join(PATH,'resources/images/goldapple.jpg')

#sound
B_MUSIC_PATH = os.path.join(PATH,'resources/sounds/bg_music_1.mp3')
B_RAIN_PATH = os.path.join(PATH, 'resources/sounds/bg_rain.mp3')
B_SUMMER_PATH = os.path.join(PATH,'resources/sounds/bg_summer.mp3')
CRASH_SOUND_PATH = os.path.join(PATH,'resources/sounds/crash.mp3')
DING_SOUND_PATH = os.path.join(PATH,'resources/sounds/eatapple.mp3')
GET_GOLD_SOUND_PATH = os.path.join(PATH,'resources/sounds/gold.mp3')
GET_BAD_SOUND_PATH = os.path.join(PATH,'resources/sounds/bad.mp3')

SOUND = True


#apple snake size
SIZE = 40

#snake
SPEED = .2

#apple


#bad apple


#game over display
G_OVER_FONT_SIZE = 30
G_OVER_FONT = 'arial'
G_BEST = 'Congratulation!! You got best score!! '
G_OVER = 'Game is over! Your score is '
G_OVER_OP = 'To play again press Enter. To exit press Escape!'