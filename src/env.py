import pygame
from sys import exit

class env():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()

        self.bg = pygame.Surface((1000, 800))
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

        self.player = pygame.Surface((50, 50))
        self.player.fill('orange')
        self.player_rect = self.player.get_rect(topleft = (200, 350))

        self.button = pygame.Surface((100, 100))
        self.button.fill('white')
        self.button_rect = self.button.get_rect(topleft = (450, 350))

        self.exit = pygame.Surface((200, 600))
        self.exit.fill('white')
        self.exit_rect = self.exit.get_rect(topleft = (800, 100))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.screen.blit(self.bg, self.bg_rect)

        self.player_rect.x += 1

        self.screen.blit(self.button, self.button_rect)
        self.screen.blit(self.exit, self.exit_rect)

        if self.player_rect.colliderect(self.button_rect):
            self.button.fill('yellow')
        else:
            self.button.fill('white')

        self.screen.blit(self.player, self.player_rect)

        pygame.display.update()

    def step(self, x, y):
        self.player_rect.x += x
        self.player_rect.y += y

        if self.player_rect.colliderect(self.button_rect):
            reward = 3
        elif self.player_rect.colliderect(self.exit_rect):
            reward = 100
            self.restart()
        elif not self.player_rect.colliderect(self.bg_rect):
            reward = -100
            self.restart()
        else:
            reward = -3

        self.run()

        return reward, self.player_rect.x, self.player_rect.y

    def restart(self):
        self.bg = pygame.Surface((1000, 800))

        self.player = pygame.Surface((50, 50))
        self.player.fill('orange')
        self.player_rect = self.player.get_rect(topleft = (200, 350))

        self.button = pygame.Surface((100, 100))
        self.button.fill('white')
        self.button_rect = self.button.get_rect(topleft = (450, 350))

        self.exit = pygame.Surface((200, 600))
        self.exit.fill('white')
        self.exit_rect = self.exit.get_rect(topleft = (800, 100))

if __name__ == '__main__':
    game = env()
    game.run()