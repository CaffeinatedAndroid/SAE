#Author: Yeesh 1st June 2026
#Revised by:

import pygame
import math
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mesh Network - Failure Visualization")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

font = pygame.font.Font(None, 20)

# Setup
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
NUM_DEVICES = 6

devices = []
for i in range(NUM_DEVICES):
    angle = 2 * math.pi * i / NUM_DEVICES
    x = CENTER[0] + RADIUS * math.cos(angle)
    y = CENTER[1] + RADIUS * math.sin(angle)
    devices.append((x, y))

# Packets
packets = []

failed_node = None

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # ✅ Draw mesh links
    for i in range(NUM_DEVICES):
        for j in range(i + 1, NUM_DEVICES):

            start = devices[i]
            end = devices[j]

            # If connection is broken due to failure
            if failed_node is not None and (i == failed_node or j == failed_node):
                pygame.draw.line(screen, GRAY, start, end, 2)

                # ✅ Draw red cross on broken link
                mid_x = (start[0] + end[0]) / 2
                mid_y = (start[1] + end[1]) / 2

                size = 8
                pygame.draw.line(screen, RED,
                                 (mid_x - size, mid_y - size),
                                 (mid_x + size, mid_y + size), 2)
                pygame.draw.line(screen, RED,
                                 (mid_x - size, mid_y + size),
                                 (mid_x + size, mid_y - size), 2)
            else:
                pygame.draw.line(screen, BLACK, start, end, 1)

    # ✅ Draw nodes + squares
    for i, (x, y) in enumerate(devices):
        color = RED if i == failed_node else BLUE
        pygame.draw.circle(screen, color, (int(x), int(y)), 18)

        label = font.render(f"T{i+1}", True, BLACK)
        screen.blit(label, label.get_rect(center=(x, y)))

        # ✅ Connection squares
        connections = NUM_DEVICES - 1

        for k in range(connections):
            sq_x = x - 25 + (k % 3) * 12
            sq_y = y + 25 + (k // 3) * 12

            pygame.draw.rect(screen, BLACK, (sq_x, sq_y, 8, 8))

            # ✅ Mark one lost connection with red cross
            if failed_node is not None and i != failed_node and k == 0:
                pygame.draw.line(screen, RED,
                                 (sq_x, sq_y),
                                 (sq_x + 8, sq_y + 8), 2)
                pygame.draw.line(screen, RED,
                                 (sq_x, sq_y + 8),
                                 (sq_x + 8, sq_y), 2)

    # ✅ Draw packets
    new_packets = []
    for p in packets:
        start, end, t = p

        if failed_node is not None and (start == failed_node or end == failed_node):
            continue

        x1, y1 = devices[start]
        x2, y2 = devices[end]

        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        pygame.draw.circle(screen, GREEN, (int(x), int(y)), 6)

        t += 0.02
        if t < 1:
            new_packets.append([start, end, t])

    packets = new_packets

    # ✅ Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # ✅ Force T3 to fail
            if event.key == pygame.K_f:
                if failed_node is None:
                    failed_node = 2  # T3 (index starts at 0)
                else:
                    failed_node = None

        elif event.type == pygame.MOUSEBUTTONDOWN:
            s = random.randint(0, NUM_DEVICES - 1)
            d = random.randint(0, NUM_DEVICES - 1)

            while d == s:
                d = random.randint(0, NUM_DEVICES - 1)

            packets.append([s, d, 0.0])

    # Info text
    text = font.render("Press F to fail T3 | Red X = lost connection", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()