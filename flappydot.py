from tkinter import *
import tkinter as tk
from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5
STARTING_VELOCITY = -30
JUMP_VELOCITY = -20
PILLAR_SPEED = 5


class Dot(Sprite):
    def init_element(self):
        self.is_started = False
        
    def update(self):
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY
    
    def start(self):
        self.is_started = True

    def jump(self):
        self.vy = JUMP_VELOCITY

class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.gif', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.pillar_pair = PillarPair(self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT // 2)
        self.elements.append(self.pillar_pair)
        self.elements.append(self.dot)

    def init_game(self):
        self.create_sprites()
        self.is_started = False

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        self.dot.start()
        self.dot.jump()

class PillarPair(Sprite):
    def update(self):
        self.x -= PILLAR_SPEED


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Flappy game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
