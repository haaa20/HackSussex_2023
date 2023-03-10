import pygame, sys
from settings import *
from player_c import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = STAGE_WIDTH // 28
        self.cell_height = STAGE_HEIGHT // 30
        self.player = Player(self, PLAYER_START_POS)

        self.load()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

        #############INTRO FUNCTIONS###################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLUE)
        self.draw_text('CATastrophe',
                       self.screen, [WIDTH // 2, HEIGHT // 2 - 125],
                       TITLE_SIZE, (0, 0, 0),
                       START_FONT,
                       centered=True)
        self.draw_text('PUSH SPACE BAR',
                       self.screen, [WIDTH // 2, HEIGHT // 2 - 50],
                       START_TEXT_SIZE, (0, 0, 0),
                       START_FONT,
                       centered=True)
        self.draw_text('1 PLAYER ONLY',
                       self.screen, [WIDTH // 2, HEIGHT // 2 + 50],
                       START_TEXT_SIZE, (0, 0, 0),
                       START_FONT,
                       centered=True)
        self.draw_text('HIGH SCORE',
                       self.screen, [60, 10],
                       START_TEXT_SIZE, (0, 0, 0),
                       START_FONT,
                       centered=False)
        pygame.display.update()


##############PLAYING FUNCTIONS################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = 'playing'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        self.player.update()

    def playing_update(self):
        self.player.update()

    def playing_draw(self):
        self.screen.fill(BLUE)
        self.screen.blit(self.background,
                         (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2))
        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score),
                       self.screen, [90, 12], 18, BLACK, START_FONT)
        self.draw_text('HIGH SCORE: 0', self.screen, [WIDTH // 2, 12], 18,
                       BLACK, START_FONT)
        self.player.draw()
        pygame.display.update()

########Helper functions########

    def draw_text(self,
                  words,
                  screen,
                  pos,
                  size,
                  colour,
                  font_name,
                  centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('img.png')
        self.background = pygame.transform.scale(self.background,(STAGE_WIDTH, STAGE_HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                             (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                             (WIDTH, x * self.cell_width))