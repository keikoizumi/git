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
B_IMG_PATH = os.path.join(PATH,'resources/background.jpg')
SNAKE_IMG_PATH = os.path.join(PATH,'resources/block.jpg')
SNAKE_FACE_IMG_PATH = os.path.join(PATH,'resources/face.png')
APPLE_IMG_PATH = os.path.join(PATH,'resources/apple.jpg')
BAD_APPLE_IMG_PATH = os.path.join(PATH,'resources/badapple.jpg')
GOLD_APPLE_IMG_PATH = os.path.join(PATH,'resources/goldapple.jpg')

#sound
B_MUSIC_PATH = os.path.join(PATH,'resources/bg_music_1.mp3')
B_RAIN_PATH = os.path.join(PATH, 'resources/bg_rain.mp3')
B_SUMMER_PATH = os.path.join(PATH,'resources/bg_summer.mp3')
CRASH_SOUND_PATH = os.path.join(PATH,'resources/crash.mp3')
DING_SOUND_PATH = os.path.join(PATH,'resources/eatapple.mp3')
GET_GOLD_SOUND_PATH = os.path.join(PATH,'resources/gold.mp3')

#apple snake size
SIZE = 40

#snake
SPEED = .1

#apple


#bad apple


#game over display
G_OVER_FONT_SIZE = 30
G_OVER_FONT = 'arial'
G_BEST = 'Congratulation!! You got best score!! '
G_OVER = 'Game is over! Your score is '
G_OVER_OP = 'To play again press Enter. To exit press Escape!'