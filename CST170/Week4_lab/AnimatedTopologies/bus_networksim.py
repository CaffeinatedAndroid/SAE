#Author: Yeesh 1st June 2026
#Revised by:

import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
BUS_Y = HEIGHT // 2
BUS_WIDTH = 600
DEVICE_WIDTH, DEVICE_HEIGHT = 80, 30

DEVICE_COLOR = (0, 0, 255)
PACKET_COLOR = (0, 200, 0)
STOPPED_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bus Topology - Blocking Collision")

font = pygame.font.Font(None, 20)

# Devices
devices = [
    (100, BUS_Y - DEVICE_HEIGHT - 60),
    (200, BUS_Y - DEVICE_HEIGHT - 60),
    (300, BUS_Y - DEVICE_HEIGHT - 60),
    (400, BUS_Y - DEVICE_HEIGHT - 60),
    (500, BUS_Y - DEVICE_HEIGHT - 60),
    (600, BUS_Y - DEVICE_HEIGHT - 60),
]

# Packet: [x, y, direction, active, sender, receiver]
packets = []

# ✅ Initial scenario
packets.append([devices[0][0] + DEVICE_WIDTH // 2, BUS_Y, 1, True, 0, 4])  # T1 → T5
packets.append([devices[4][0] + DEVICE_WIDTH // 2, BUS_Y, -1, True, 4, 2]) # T5 → T3

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    # Bus limits
    bus_left = WIDTH//2 - BUS_WIDTH//2
    bus_right = WIDTH//2 + BUS_WIDTH//2

    # Draw bus
    pygame.draw.line(screen, (0, 0, 0),
                     (bus_left, BUS_Y),
                     (bus_right, BUS_Y), 6)

    # Draw devices + connection lines
    for i, d in enumerate(devices):
        cx = d[0] + DEVICE_WIDTH // 2

        pygame.draw.rect(screen, DEVICE_COLOR,
                         (d[0], d[1], DEVICE_WIDTH, DEVICE_HEIGHT))

        label = font.render(f"T{i+1}", True, (0, 0, 0))
        screen.blit(label, label.get_rect(center=(cx, d[1] + 15)))

        pygame.draw.line(screen, (0, 0, 0),
                         (cx, d[1] + DEVICE_HEIGHT),
                         (cx, BUS_Y), 2)

    # Draw packets
    for p in packets:
        color = PACKET_COLOR if p[3] else STOPPED_COLOR
        pygame.draw.circle(screen, color, (int(p[0]), BUS_Y), 6)

        if p[3]:
            pygame.draw.line(screen, (0, 0, 0),
                             (p[0], BUS_Y),
                             (p[0] + 12 * p[2], BUS_Y), 2)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            for i, d in enumerate(devices):
                cx = d[0] + DEVICE_WIDTH // 2

                if (d[1] < my < d[1] + DEVICE_HEIGHT and
                        abs(mx - cx) < DEVICE_WIDTH // 2):

                    sender = i
                    receiver = random.choice(
                        [x for x in range(len(devices)) if x != sender]
                    )

                    target_x = devices[receiver][0] + DEVICE_WIDTH // 2
                    direction = 1 if target_x > cx else -1

                    packets.append([cx, BUS_Y, direction, True, sender, receiver])
                    break

    # ✅ Step 1: Collision + Blocking logic
    for i in range(len(packets)):
        p1 = packets[i]

        if not p1[3]:
            continue

        for j in range(len(packets)):
            if i == j:
                continue

            p2 = packets[j]

            if abs(p1[0] - p2[0]) < 12:

                # ✅ Moving vs moving → collision
                if p2[3]:
                    p1[3] = False
                    p2[3] = False

                    offset = 6
                    p1[0] -= offset
                    p2[0] += offset

                # ✅ Moving hits stopped → BLOCK
                else:
                    p1[3] = False

                    if p1[2] == 1:   # moving right
                        p1[0] = p2[0] - 12
                    else:            # moving left
                        p1[0] = p2[0] + 12

    # ✅ Step 2: Move packets
    for p in packets:
        if not p[3]:
            continue

        p[0] += 5 * p[2]

        # Stop at receiver
        target_x = devices[p[5]][0] + DEVICE_WIDTH // 2
        if abs(p[0] - target_x) < 5:
            p[3] = False

        # Stop at ends
        if p[0] < bus_left or p[0] > bus_right:
            p[3] = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()