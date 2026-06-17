# Author: Yeesh 1st June 2026
# Revised: Ring Topology Version

import pygame
import math
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ring Network - Failure Visualization")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

font = pygame.font.Font(None, 22)

# Network setup
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
NUM_DEVICES = 6

devices = []
for i in range(NUM_DEVICES):
    angle = 2 * math.pi * i / NUM_DEVICES
    x = CENTER[0] + RADIUS * math.cos(angle)
    y = CENTER[1] + RADIUS * math.sin(angle)
    devices.append((x, y))

# Packet list
packets = []

failed_node = None

clock = pygame.time.Clock()
running = True

# Helper functions
def next_node(i):
    return (i + 1) % NUM_DEVICES

def prev_node(i):
    return (i - 1) % NUM_DEVICES

while running:
    screen.fill(WHITE)

    # ✅ Draw ring connections (only neighbours)
    for i in range(NUM_DEVICES):
        j = next_node(i)

        start = devices[i]
        end = devices[j]

        if failed_node is not None and (i == failed_node or j == failed_node):
            pygame.draw.line(screen, GRAY, start, end, 3)

            # Draw red X on broken link
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2

            size = 10
            pygame.draw.line(screen, RED,
                             (mid_x - size, mid_y - size),
                             (mid_x + size, mid_y + size), 2)
            pygame.draw.line(screen, RED,
                             (mid_x - size, mid_y + size),
                             (mid_x + size, mid_y - size), 2)
        else:
            pygame.draw.line(screen, BLACK, start, end, 3)

    # ✅ Draw nodes
    for i, (x, y) in enumerate(devices):
        color = RED if i == failed_node else BLUE
        pygame.draw.circle(screen, color, (int(x), int(y)), 18)

        label = font.render(f"T{i+1}", True, BLACK)
        screen.blit(label, label.get_rect(center=(x, y)))

    # ✅ Move packets (clockwise around ring)
    new_packets = []
    for packet in packets:
        current, destination, t = packet

        nxt = next_node(current)

        # Stop if failed node is involved
        if failed_node is not None and (current == failed_node or nxt == failed_node):
            continue

        x1, y1 = devices[current]
        x2, y2 = devices[nxt]

        # Interpolate movement
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        pygame.draw.circle(screen, GREEN, (int(x), int(y)), 6)

        t += 0.03

        if t < 1:
            new_packets.append([current, destination, t])
        else:
            # Move to next hop
            if nxt != destination:
                new_packets.append([nxt, destination, 0.0])

    packets = new_packets

    # ✅ Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Toggle failure on node T3
            if event.key == pygame.K_f:
                if failed_node is None:
                    failed_node = 2  # T3
                else:
                    failed_node = None

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Send random packet
            s = random.randint(0, NUM_DEVICES - 1)
            d = random.randint(0, NUM_DEVICES - 1)

            while d == s:
                d = random.randint(0, NUM_DEVICES - 1)

            packets.append([s, d, 0.0])

    # ✅ Info text
    text = font.render("Ring Topology | Click = send packet | Press F to fail T3", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()