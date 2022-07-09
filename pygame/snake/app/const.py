#Standard module
import os
from xml.dom import INVALID_ACCESS_ERR

#ref https://soundeffect-lab.info/sound/button/

#OS PATH
PATH = os.getcwd()

#score file path
SCORE_FILE_DIR = 'score'
SCORE_FILE_NAME = 'score.txt'
SCORE_FILE_PATH = os.path.join(PATH ,SCORE_FILE_DIR + '/' + SCORE_FILE_NAME)

#caption
CAPTION = 'Snake And Apple Game'

#apple snake size
SIZE = 40

#display
DIP_W = 1200
PLAY_DIP_W = SIZE * 24
DIP_H = 640
START_DIP_W = 1200
START_DIP_H = 640

#image
B_IMG_PATH = os.path.join(PATH, 'resources/images/background2.jpg')
SNAKE_YELLOW_IMG_PATH = os.path.join(PATH, 'resources/images/yellow_block.jpg')
SNAKE_RED_IMG_PATH = os.path.join(PATH, 'resources/images/red_block.jpg')
SNAKE_GREEN_IMG_PATH = os.path.join(PATH, 'resources/images/green_block.jpg')
SNAKE_BLUE_IMG_PATH = os.path.join(PATH, 'resources/images/blue_block.jpg')
SNAKE_YELLOW_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/yellow_face.png')
SNAKE_RED_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/red_face.png')
SNAKE_GREEN_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/green_face.png')
SNAKE_YELLOW_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/yellow_had_bad_apple_face.png')
SNAKE_RED_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/red_had_bad_apple_face.png')
SNAKE_GREEN_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/green_had_bad_apple_face.png')
SNAKE_BLUE_HAD_BAD_APPLE_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/blue_had_bad_apple_face.png')
SNAKE_YELLOW_EATING_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/yellow_eating_face.png')
SNAKE_RED_EATING_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/red_eating_face.png')
SNAKE_GREEN_EATING_FACE_IMG_PATH = os.path.join(PATH, 'resources/images/green_eating_face.png')
SNAKE_POOP_IMG_PATH = os.path.join(PATH, 'resources/images/poop.png')
APPLE_IMG_PATH = os.path.join(PATH, 'resources/images/apple.jpg')
BAD_APPLE_IMG_PATH = os.path.join(PATH, 'resources/images/badapple.jpg')
GOLD_APPLE_IMG_PATH = os.path.join(PATH, 'resources/images/goldapple.jpg')
FROG_IMG_PATH = os.path.join(PATH, 'resources/images/frog.png')
BLOCK_IMG_PATH = os.path.join(PATH, 'resources/images/block.jpg')
GRASS_IMG_PATH = os.path.join(PATH, 'resources/images/grass.jpg')
RAIN_IMG_PATH = os.path.join(PATH, 'resources/images/rain.jpg')
RAIN_IMG_PNG_PATH = os.path.join(PATH, 'resources/images/rain.png')
CICADA_IMG_PATH  = os.path.join(PATH, 'resources/images/cicada.png')
BIRD_IMG_PATH  = os.path.join(PATH, 'resources/images/bird.png')
LIFE_IMG_PATH  = os.path.join(PATH, 'resources/images/life.png')
START_IMG_PATH = os.path.join(PATH, 'resources/images/start.png')
GAME_OVER_IMG_PATH = os.path.join(PATH, 'resources/images/game_over.png')

#sound
SOUND = True
B_MUSIC_PATH = os.path.join(PATH, 'resources/sounds/bg_music_1.mp3')
B_RAIN_PATH = os.path.join(PATH,  'resources/sounds/bg_rain.mp3')
B_SUMMER_PATH = os.path.join(PATH, 'resources/sounds/bg_summer.mp3')
CRASH_SOUND_PATH = os.path.join(PATH, 'resources/sounds/crash.mp3')
DING_SOUND_PATH = os.path.join(PATH, 'resources/sounds/eatapple.mp3')
GET_GOLD_SOUND_PATH = os.path.join(PATH, 'resources/sounds/gold.mp3')
GET_BAD_SOUND_PATH = os.path.join(PATH, 'resources/sounds/bad.mp3')
GET_POOP_SOUND_PATH = os.path.join(PATH, 'resources/sounds/had_poop.mp3')
GET_FROG_SOUND_PATH = os.path.join(PATH, 'resources/sounds/had_frog.mp3')

#snake
MAX_LIFE = 3
NORMAL_SPEED = .15
FAST_SPEED = .05
PANIC_SPEED = .01
SPEED = NORMAL_SPEED
PANIC_TIME_SEC = 5

#game over display
G_OVER_FONT_SIZE = 25
G_OVER_FONT = 'arial'
G_BEST = 'Congratulation!! You got best record!! '
G_OVER = 'Game is over! You had '
G_OVER_OP = 'To play again press Enter. To exit press Escape!'
G_OVER_CAUSE_BAD_APPLE = 'Your snake had a lot of bad apples.'
G_OVER_CAUSE_COLLISION = 'Collision happen.'
G_OVER_CAUSE_POOP = 'Your snake had a poop!!!!.'
G_OVER_UNKNOWN = 'Unknown'
G_YOUR_BEST = 'Best Score: '
G_YOU_HAVE = 'Your snake had '

#RGB LIST
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE_RED = (255,69,0)
GOLD = (255,215,0)
GREEN_YELLOW = (173,255,47)
BLUE = (0,0,255)
HOT_PINK = (255,105,180)

#Exception
G_OVER_CAUSE_BAD_APPLE = 'Your snake had a lot of bad apples.'
G_OVER_CAUSE_POOP = 'Your snake had a poop.'
INVALID_NUM_ERR = 'invalid number'
