import pygame, random
from pygame import MOUSEBUTTONDOWN



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((640, 512))
        m_x, m_y = 0, 0


        clock = pygame.time.Clock()

        def draw_lines():
            for x_line in range(0, 33):
                pygame.draw.line(screen, "black",(x_line*32, 0), (x_line*32, 512))
            for y_line in range(0, 33):
                pygame.draw.line(screen, "black", (0, y_line*32), (640, y_line*32))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x = x//32 * 32
                    y = y//32 * 32
                    if m_x == x and m_y == y:
                        M_x = random.randrange(0, 20)
                        M_y = random.randrange(0, 16)
                        m_x = M_x*32
                        m_y = M_y*32


            screen.fill("gold")
            mole_image = pygame.image.load("mole.png")
            screen.blit(mole_image, mole_image.get_rect(topleft=(m_x, m_y)))
            draw_lines()
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()




if __name__ == "__main__":
    main()
