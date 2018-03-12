"""
Name: Cars Vs Obstacles
Author: Joey Burgee
Date: March 11, 2018
"""

# IMPORT MODULES
import pygame as pg
import random

# INITIALIZE PYGAME SOUND
pg.mixer.init()
# INITIALIZE PYGAME FONT
pg.font.init()

# DEFINE COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# ------MAKE WINDOW CLASS------
class Window (object):

    def __init__(self):
        # DEFINE WINDOW ATTRIBUTES
        self.WIDTH = 800
        self.HEIGHT = 750
        self.background = pg.image.load("raceway.png")
        self.background2 = pg.image.load("raceway2.png")
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.running = False
        self.p1games_won = 0
        self.p2games_won = 0

        # DEFINE FONT ATTRIBUTES
        self.font = pg.font.SysFont("Comic Sans MS", 30)

        self.winner = self.font.render("", False, RED)
        
        self.crash = pg.mixer.Sound("crash.ogg")
        self.engine_rev = pg.mixer.Sound("engine_rev.ogg")
        self.cars_hitting = pg.mixer.Sound("cars_hitting.ogg")
        pg.mixer.music.load("engine.ogg")
        pg.mixer.music.play(-1)

    # ---MAKE A FUNCTION THAT OPENS START MENU AND RESETS VALUES
    def START(self):
        pg.mixer.music.stop()

        self.bx1 = 0
        self.by1 = 0
        self.bx2 = 0
        self.by2 = -745

        # DEFINE PLAYER 1 ATTRIBUTES
        self.player1 = pg.image.load("car1.png")
        self.x1 = self.WIDTH / 2 - 150
        self.y1 = 600
        self.x1v = 0
        self.y1v = 0

        # DEFINE PLAYER 2 ATTRIBUTES
        self.player2 = pg.image.load("car2.png")
        self.x2 = self.WIDTH / 2 + 150
        self.y2 = 600
        self.x2v = 0
        self.y2v = 0

        # LOAD OBSTACLE IMAGES
        self.crate = pg.image.load("crate.png")
        self.trash_can = pg.image.load("trash_can.png")
        self.sign = pg.image.load("sign.png")

        # PUT OBSTACLE IMAGES INTO AN ARRAY
        self.obstacles = [self.crate, self.trash_can, self.sign]

        # DEFINE OBSTACLE 1 ATTRIBUTES
        self.obstacle1 = random.choice(self.obstacles)
        self.ox1 = random.randrange(150, 225)
        self.oy1 = 15
        self.oy1v = random.randrange(5, 8)

        # DEFINE OBSTACLE 2 ATTRIBUTES
        self.obstacle2 = random.choice(self.obstacles)
        self.ox2 = random.randrange(300, 375)
        self.oy2 = 15
        self.oy2v = random.randrange(5, 8)

        # DEFINE OBSTACLE 3 ATTRIBUTES
        self.obstacle3 = random.choice(self.obstacles)
        self.ox3 = random.randrange(450, 525)
        self.oy3 = 15
        self.oy3v = random.randrange(5, 8)

        # DEFINE OBSTACLE 4 ATTRIBUTES
        self.obstacle4 = random.choice(self.obstacles)
        self.ox4 = random.randrange(600, 625)
        self.oy4 = 15
        self.oy4v = random.randrange(5, 8)

        # DEFINE STOP SIGN ATTRIBUTES
        self.stop_sign = pg.image.load("stop_sign.png")
        self.stopx = 115
        self.stopy = 15
        self.stopyv = 5

        # ------ MAKE START MENU ------

        # SET BACKGROUND
        self.screen.blit(self.background, [0, 0])

        # ---INSTRUCTIONS---
        self.start_text = self.font.render("Press Anywhere To Start Game", False, WHITE)
        self.screen.blit(self.start_text, [self.WIDTH / 2 - 225, self.HEIGHT / 2 - 45])

        self.ins_text = self.font.render("For Control Instructions Press H", False, WHITE)
        self.screen.blit(self.ins_text, [self.WIDTH / 2 - 225, self.HEIGHT / 2 + 100])

        self.reset_text = self.font.render("For Game Count Reset Press R", False, WHITE)
        self.screen.blit(self.reset_text, [self.WIDTH / 2 - 200, self.HEIGHT / 2 + 145])

        # PLAYER 1 INSTRUCTIONS
        self.p1ins = self.font.render("Player 1 Instructions:", False, BLUE)
        self.p1w = self.font.render("W = Up", False, WHITE)
        self.p1s = self.font.render("S = Down", False, WHITE)
        self.p1a = self.font.render("A = Left", False, WHITE)
        self.p1d = self.font.render("D = Right", False, WHITE)

        # PLAYER 2 INSTRUCTIONS
        self.p2ins = self.font.render("Player 2 Instructions:", False, RED)
        self.p2up = self.font.render("Up-Arrow = Up", False, WHITE)
        self.p2down = self.font.render("Down-Arrow = Down", False, WHITE)
        self.p2left = self.font.render("Left-Arrow = Left", False, WHITE)
        self.p2right = self.font.render("Right-Arrow = Right", False, WHITE)

        # WINNER
        self.screen.blit(self.winner, [self.WIDTH / 2 - 100, self.HEIGHT / 2])
        

        # ---MAKE GAME COUNTER---

        # PLAYER 1
        self.p1games_text = self.font.render("P1 Games Won: " + str(self.p1games_won), False, BLUE)
        self.screen.blit(self.p1games_text, [self.WIDTH / 2 - 125, self.HEIGHT - 90])

        # PLAYER 2
        self.p2games_text = self.font.render("P2 Games Won: " + str(self.p2games_won), False, RED)
        self.screen.blit(self.p2games_text, [self.WIDTH / 2 - 125, self.HEIGHT - 45])
        

        pg.display.update()

        
        # MAKE USER-CLICK START GAME
        button_pressed = False
        while button_pressed == False:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_h:
                        # PLAYER 1 INSTRUCTIONS
                        self.screen.fill(BLACK, [0, 0, self.WIDTH, self.HEIGHT])
                        self.screen.blit(self.p1ins, [self.WIDTH / 2 - 350, self.HEIGHT / 2 - 45])
                        self.screen.blit(self.p1w, [self.WIDTH / 2 - 275, self.HEIGHT / 2 + 45])
                        self.screen.blit(self.p1s, [self.WIDTH / 2 - 275, self.HEIGHT / 2 + 90])
                        self.screen.blit(self.p1a, [self.WIDTH / 2 - 275, self.HEIGHT / 2 + 135])
                        self.screen.blit(self.p1d, [self.WIDTH / 2 - 275, self.HEIGHT / 2 + 180])

                        # PLAYER 2 INSTRUCTIONS
                        self.screen.blit(self.p2ins, [self.WIDTH / 2 + 75, self.HEIGHT / 2 - 45])
                        self.screen.blit(self.p2up, [self.WIDTH / 2 + 75, self.HEIGHT / 2 + 45])
                        self.screen.blit(self.p2down, [self.WIDTH / 2 + 75, self.HEIGHT / 2 + 90])
                        self.screen.blit(self.p2left, [self.WIDTH / 2 + 75, self.HEIGHT / 2 + 135])
                        self.screen.blit(self.p2right, [self.WIDTH / 2 + 75, self.HEIGHT / 2 + 180])

                        self.screen.blit(self.start_text, [self.WIDTH / 2 - 225, self.HEIGHT / 2 - 100])
                        
                        pg.display.update()
                    if event.key == pg.K_r:
                        self.p1games_won = 0
                        self.p2games_won = 0
                        
                        self.screen.blit(self.background, [0, 0])
                        
                        # PLAYER 1
                        self.p1games_text = self.font.render("P1 Games Won: " + str(self.p1games_won), False, BLUE)
                        self.screen.blit(self.p1games_text, [self.WIDTH / 2 - 125, self.HEIGHT - 90])

                        # PLAYER 2
                        self.p2games_text = self.font.render("P2 Games Won: " + str(self.p2games_won), False, RED)
                        self.screen.blit(self.p2games_text, [self.WIDTH / 2 - 125, self.HEIGHT - 45])

                        # ---INSTRUCTIONS---
                        self.screen.blit(self.start_text, [self.WIDTH / 2 - 225, self.HEIGHT / 2 - 45])

                        self.screen.blit(self.ins_text, [self.WIDTH / 2 - 225, self.HEIGHT / 2 + 100])

                        self.screen.blit(self.reset_text, [self.WIDTH / 2 - 200, self.HEIGHT / 2 + 145])

                        # WINNER
                        self.screen.blit(self.winner, [self.WIDTH / 2 - 100, self.HEIGHT / 2])
                       
                        pg.display.update()
                if event.type == pg.MOUSEBUTTONDOWN:
                        self.running = True
                        return 0

    # ---MAKE A FUNCTION THAT INITIALIZES PYGAME WINDOW---
    def start_window(self):
        pg.init()

    # ---MAKE A FUNCTION THAT PROCESSES EVENTS---
    def event_handling(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                # PLAYER 1 CONTROLS
                if event.key == pg.K_a:
                    self.x1v = -5
                if event.key == pg.K_d:
                    self.x1v = 5
                if event.key == pg.K_w:
                    self.y1v = -5
                    self.engine_rev.play()
                if event.key == pg.K_s:
                    self.y1v = 5
                # PLAYER 2 CONTROLS
                if event.key == pg.K_LEFT:
                    self.x2v = -5
                if event.key == pg.K_RIGHT:
                    self.x2v = 5
                if event.key == pg.K_UP:
                    self.y2v = -5
                    self.engine_rev.play()
                if event.key == pg.K_DOWN:
                    self.y2v = 5

            if event.type == pg.KEYUP:
                # PLAYER 1 CONTROLS
                if event.key == pg.K_a:
                    self.x1v = 0
                if event.key == pg.K_d:
                    self.x1v = 0
                if event.key == pg.K_w:
                    self.y1v = 0
                if event.key == pg.K_s:
                    self.y1v = 0
                # PLAYER 2 CONTROLS
                if event.key == pg.K_LEFT:
                    self.x2v = 0
                if event.key == pg.K_RIGHT:
                    self.x2v = 0
                if event.key == pg.K_UP:
                    self.y2v = 0
                if event.key == pg.K_DOWN:
                    self.y2v = 0

        # ADD VELOCITY TO PLAYER 1 POSITION
        self.x1 += self.x1v
        self.y1 += self.y1v

        # ADD VELOCITY TO PLAYER 2 POSITION
        self.x2 += self.x2v
        self.y2 += self.y2v

        # ADD VELOCITY TO OBSTACLE POSITIONS
        self.oy1 += self.oy1v
        self.oy2 += self.oy2v
        self.oy3 += self.oy3v
        self.oy4 += self.oy4v

        # ADD VELOCITY TO STOP SIGN
        self.stopy += self.stopyv

        self.by1 += 5
        self.by2 += 5

    # ---MAKE A FUNCTION THAT CHECKS FOR OBJECT COLLISIONS---
    def collision(self):
        # ---SET PLAYER 1 COLLISIONS---
        
        # SET HALFWAY-UP BOUNDARY FOR PLAYER 1
        if (self.y1 < self.HEIGHT / 2):
            self.y1 = self.HEIGHT / 2 + 2
        # SET BOTTOM BOUNDARY FOR PLAYER 1
        if (self.y1 > self.HEIGHT - 64):
            self.y1 = self.HEIGHT - 66
        # SET LEFT-ROAD BOUNDARY FOR PLAYER 1
        if (self.x1 < self.WIDTH / 2 - 250):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            self.crash.play()
            self.running = False
            self.p2games_won += 1
        # SET RIGHT-ROAD BOUNDARY FOR PLAYER 1
        if (self.x1 > self.WIDTH / 2 + 205):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            self.crash.play()
            self.running = False
            self.p2games_won += 1


        # ---SET PLAYER 2 COLLISIONS---
        
        # SET HALFWAY-UP BOUNDARY FOR PLAYER 2
        if (self.y2 < self.HEIGHT / 2):
            self.y2 = self.HEIGHT / 2 + 2
        # SET BOTTOM BOUNDARY FOR PLAYER 2
        if (self.y2 > self.HEIGHT - 64):
            self.y2 = self.HEIGHT - 66
        # SET LEFT-ROAD BOUNDARY FOR PLAYER 2
        if (self.x2 < self.WIDTH / 2 - 250):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.running = False
            self.p1games_won += 1
        # SET RIGHT-ROAD BOUNDARY FOR PLAYER 2
        if (self.x2 > self.WIDTH / 2 + 205):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.running = False
            self.p1games_won += 1


        # MAKE CARS BOUNCE OFF EACH OTHER
        if (int(self.x1) + 45 in range(int(self.x2), int(self.x2) + 45) and int(self.y1) in range(int(self.y2 - 64), int(self.y2) + 64)):
            self.cars_hitting.play()
            self.x1 -= 10
            self.x2 += 10

        if (int(self.x2) + 45 in range(int(self.x1), int(self.x1) + 45) and int(self.y1) in range(int(self.y2 - 64), int(self.y2) + 64)):
            self.cars_hitting.play()
            self.x1 += 10
            self.x2 -= 10

        # --- MAKE OBSTACLES RESET WHEN OFF-SCREEN---
        
        # OBSTACLE 1
        if (self.oy1 > self.HEIGHT):
            self.obstacle1 = random.choice(self.obstacles)
            self.ox1 = random.randrange(150, 225)
            self.oy1 = 15
            self.oy1v = random.randrange(5, 8)
        # OBSTACLE 2
        if (self.oy2 > self.HEIGHT):
            self.obstacle2 = random.choice(self.obstacles)
            self.ox2 = random.randrange(300, 375)
            self.oy2 = 15
            self.oy2v = random.randrange(5, 8)
        # OBSTACLE 3
        if (self.oy3 > self.HEIGHT):
            self.obstacle3 = random.choice(self.obstacles)
            self.ox3 = random.randrange(450, 525)
            self.oy3 = 15
            self.oy3v = random.randrange(5, 8)
        # OBSTACLE 4
        if (self.oy4 > self.HEIGHT):
            self.obstacle4 = random.choice(self.obstacles)
            self.ox4 = random.randrange(600, 625)
            self.oy4 = 15
            self.oy4v = random.randrange(5, 8)

        
        # ---MAKE PLAYER 1 DIE WHEN HIT BY OBSTACLE---
        
        # OBSTACLE 1
        if (int(self.ox1) in range(int(self.x1) - 32, int(self.x1) + 45) and int(self.oy1) in range(int(self.y1) - 45, int(self.y1) + 64)):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            pg.mixer.Sound.play(self.crash)
            self.crash.play()
            self.p2games_won += 1
            self.running = False
        # OBSTACLE 2
        if (int(self.ox2) in range(int(self.x1) - 32, int(self.x1) + 45) and int(self.oy2) in range(int(self.y1) -45, int(self.y1) + 64)):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            self.crash.play()
            self.p2games_won += 1
            self.running = False
        # OBSTACLE 3
        if (int(self.ox3) in range(int(self.x1) - 32, int(self.x1) + 45) and int(self.oy3) in range(int(self.y1) - 45, int(self.y1) + 64)):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            self.crash.play()
            self.p2games_won += 1
            self.running = False
        # OBSTACLE 4
        if (int(self.ox4) in range(int(self.x1) - 32, int(self.x1) + 45) and int(self.oy4) in range(int(self.y1) - 45, int(self.y1) + 64)):
            self.winner = self.font.render("Player 2 Wins!", False, RED)
            self.crash.play()
            self.p2games_won += 1
            self.running = False


        # ---MAKE PLAYER 2 DIE WHEN HIT BY OBSTACLE---

        # OBSTACLE 1
        if (int(self.ox1) in range(int(self.x2) - 32, int(self.x2) + 45) and int(self.oy1) in range(int(self.y2) -45, int(self.y2) + 64)):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.p1games_won += 1
            self.running = False
        # OBSTACLE 2
        if (int(self.ox2) in range(int(self.x2) - 32, int(self.x2) + 45) and int(self.oy2) in range(int(self.y2) - 45, int(self.y2) + 64)):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.p1games_won += 1
            self.running = False
        # OBSTACLE 3
        if (int(self.ox3) in range(int(self.x2) - 32, int(self.x2) + 45) and int(self.oy3) in range(int(self.y2) - 45, int(self.y2) + 64)):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.p1games_won += 1
            self.running = False
        # OBSTACLE 4
        if (int(self.ox4) in range(int(self.x2) - 32, int(self.x2) + 45) and int(self.oy4)in range(int(self.y2) - 45, int(self.y2) + 64)):
            self.winner = self.font.render("Player 1 Wins!", False, RED)
            self.crash.play()
            self.p1games_won += 1
            self.running = False
        
        if (self.stopy > self.HEIGHT):
            self.stopy = - 1500

        if (self.by1 > self.HEIGHT):
            self.by1 = -740
        if (self.by2 > self.HEIGHT):
            self.by2 = -740

    # ---MAKE A FUNCTION THAT DRAWS OBJECTS TO SCREEN---
    def draw(self):
        # DRAW BACKGROUND
        self.screen.blit(self.background, [self.bx1, self.by1])
        self.screen.blit(self.background2, [self.bx2, self.by2])

        # DRAW PLAYER 1
        self.screen.blit(self.player1, [self.x1, self.y1])

        # DRAW PLAYER 2
        self.screen.blit(self.player2, [self.x2, self.y2])

        # DRAW OBSTACLE 1
        self.screen.blit(self.obstacle1, [self.ox1, self.oy1])
        # DRAW OBSTACLE 2
        self.screen.blit(self.obstacle2, [self.ox2, self.oy2])
        # DRAW OBSTACLE 3
        self.screen.blit(self.obstacle3, [self.ox3, self.oy3])
        # DRAW OBSTACLE 4
        self.screen.blit(self.obstacle4, [self.ox4, self.oy4])

        # DRAW STOP SIGN
        self.screen.blit(self.stop_sign, [self.stopx, self.stopy])
        

    # ---MAKE A FUNCTION THAT RENDERS DRAWN OBJECTS TO SCREEN---
    def render(self):
        pg.display.update()
        self.clock.tick(self.FPS)


# ASSIGN WINDOW CLASS TO VARIABLE
Game = Window()

# -- MAKE A FUNCTION THAT STARTS RESET
def START_SCREEN():
    if __name__ == '__main__':
        Game.start_window()
        Game.START()
        LOOP()

# --- MAKE A FUNCTION THAT ACTS AS A GAME LOOP ---
def LOOP():
    pg.mixer.music.load("engine.ogg")
    pg.mixer.music.play(-1)
    while Game.running:
        Game.start_window()
        Game.event_handling()
        Game.collision()
        Game.draw()
        Game.render()
    START_SCREEN()

# CALL ON START FUNCTION TO INITIALIZE THE GAME
START_SCREEN()
