import pygame
import sys

# Configurações
WIDTH, HEIGHT = 1200, 800
BLOCK_SIZE = 20
BACKGROUND_COLOR = (135, 206, 235)

# Cores disponíveis
COLORS = {
    "Marrom": (139, 69, 19),
    "Verde": (0, 128, 0),
    "Areia": (194, 178, 128),
    "Água": (0, 0, 255),
    "Azul": (0, 0, 255),
    "Amarelo": (255, 255, 0),
    "Vermelho": (255, 0, 0),
    "Preto": (0, 0, 0),
    "Branco": (255, 255, 255),
}

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint 2D")

# Grade para os blocos
grid = {}
current_color = COLORS["Marrom"]
    
def draw_grid():
    for (x, y) in grid.keys():
        pygame.draw.rect(screen, grid[(x, y)], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_color_palette():
    for i, (name, color) in enumerate(COLORS.items()):
        pygame.draw.rect(screen, color, (10 + i * (BLOCK_SIZE + 5), 10, BLOCK_SIZE, BLOCK_SIZE))
        font = pygame.font.Font(None, 24)
        text = font.render(name, True, (0, 0, 0))
        screen.blit(text, (10 + i * (BLOCK_SIZE + 5), 10 + BLOCK_SIZE))

def draw_instructions():
    font = pygame.font.Font(None, 24)
    instructions = [
        "Instruções:",
        "1. Selecione uma cor na paleta.",
        "2. Clique e segure o botão esquerdo do mouse para desenhar.",
        "3. Clique e segure o botão direito do mouse para apagar.",
        "4. Pressione 'Esc' para sair."
    ]
    for i, line in enumerate(instructions):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (10, HEIGHT - 100 + i * 30))  # Ajuste a posição na parte inferior

def main():
    global current_color
    left_mouse_pressed = False
    right_mouse_pressed = False

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        draw_color_palette()
        draw_instructions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] <= BLOCK_SIZE + 10:  # Verifica se o clique foi na paleta de cores
                    index = (pos[0] - 10) // (BLOCK_SIZE + 5)
                    if 0 <= index < len(COLORS):
                        current_color = list(COLORS.values())[index]
                else:
                    grid_x = pos[0] // BLOCK_SIZE
                    grid_y = pos[1] // BLOCK_SIZE

                    if event.button == 1:  # Botão esquerdo do mouse
                        left_mouse_pressed = True
                        grid[(grid_x, grid_y)] = current_color
                    elif event.button == 3:  # Botão direito do mouse
                        right_mouse_pressed = True
                        grid.pop((grid_x, grid_y), None)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    left_mouse_pressed = False
                elif event.button == 3:
                    right_mouse_pressed = False

            # Pressionar 'Esc' para sair
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Desenhar blocos enquanto o botão esquerdo do mouse estiver pressionado
        if left_mouse_pressed:
            pos = pygame.mouse.get_pos()
            grid_x = pos[0] // BLOCK_SIZE
            grid_y = pos[1] // BLOCK_SIZE
            grid[(grid_x, grid_y)] = current_color

        # Apagar blocos enquanto o botão direito do mouse estiver pressionado
        if right_mouse_pressed:
            pos = pygame.mouse.get_pos()
            grid_x = pos[0] // BLOCK_SIZE
            grid_y = pos[1] // BLOCK_SIZE
            grid.pop((grid_x, grid_y), None)

        pygame.display.flip()

if __name__ == "__main__":
    main()
