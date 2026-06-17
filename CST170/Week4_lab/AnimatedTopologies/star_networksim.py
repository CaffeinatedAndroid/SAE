#Author: Yeesh 1st June 2026
#Revised by:


import pygame
import math
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 150
DEVICE_WIDTH, DEVICE_HEIGHT = 60, 30
DEVICE_COLOR = (0, 0, 255)
PACKET_COLOR_REQUEST = (0, 0, 0)
PACKET_COLOR_RESPONSE = (0, 200, 0)
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Topology Simulation")

font = pygame.font.Font(None, 20)
big_font = pygame.font.Font(None, 40)

# Create terminals
num_terminals = 6
devices = []
for i in range(num_terminals):
    angle = 2 * math.pi * i / num_terminals
    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)
    devices.append((x, y))

# Packet: [x, y, state, source, target, type]
packets = []

clock = pygame.time.Clock()
running = True

click_count = 0
hub_failed = False


def move(packet, tx, ty):
    dx = tx - packet[0]
    dy = ty - packet[1]
    dist = math.sqrt(dx**2 + dy**2)

    if dist < 5:
        return True

    if dist > 0:
        dx /= dist
        dy /= dist
        packet[0] += 5 * dx
        packet[1] += 5 * dy

    return False


while running:
    screen.fill(BACKGROUND_COLOR)

    # ✅ STEP 1: Draw connections FIRST (background layer)
    for d in devices:
        pygame.draw.line(screen, DEVICE_COLOR, (CENTER_X, CENTER_Y), d, 2)

    # ✅ STEP 2: Draw hub on top (larger radius so it hides lines)
    hub_color = (255, 0, 0) if hub_failed else DEVICE_COLOR
    pygame.draw.circle(screen, hub_color, (CENTER_X, CENTER_Y), 24)

    hub_label = font.render("Hub", True, (0, 0, 0))
    screen.blit(hub_label, hub_label.get_rect(center=(CENTER_X, CENTER_Y)))

    # ✅ STEP 3: Draw terminals
    for i, d in enumerate(devices):
        pygame.draw.rect(screen, DEVICE_COLOR,
                         (d[0] - DEVICE_WIDTH // 2,
                          d[1] - DEVICE_HEIGHT // 2,
                          DEVICE_WIDTH, DEVICE_HEIGHT))

        label = font.render(f"T{i+1}", True, (0, 0, 0))
        screen.blit(label, label.get_rect(center=(d[0], d[1] + 20)))

    # ✅ STEP 4: Draw packets
    for p in packets:
        color = PACKET_COLOR_REQUEST if p[5] == "request" else PACKET_COLOR_RESPONSE
        pygame.draw.circle(screen, color, (int(p[0]), int(p[1])), 6)

    # ✅ STEP 5: Hub failure message
    if hub_failed:
        text = big_font.render("HUB FAILURE - PACKETS LOST", True, (255, 0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, 30)))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not hub_failed:
                mx, my = event.pos

                for i, d in enumerate(devices):
                    if (d[0] - DEVICE_WIDTH // 2 < mx < d[0] + DEVICE_WIDTH // 2 and
                        d[1] - DEVICE_HEIGHT // 2 < my < d[1] + DEVICE_HEIGHT // 2):

                        click_count += 1

                        # ✅ Trigger hub failure
                        if click_count >= 5:
                            hub_failed = True
                            packets.clear()
                            break

                        # Random target (not itself)
                        target = random.choice([x for x in range(num_terminals) if x != i])

                        packets.append([d[0], d[1], "to_hub", i, target, "request"])
                        break

    # ✅ Update packets (only if hub is active)
    if not hub_failed:
        new_packets = []

        for p in packets:
            x, y, state, source, target, ptype = p

            # Request: source → hub → target
            if state == "to_hub":
                if move(p, CENTER_X, CENTER_Y):
                    p[2] = "to_target"

            elif state == "to_target":
                td = devices[target]
                if move(p, td[0], td[1]):
                    new_packets.append([td[0], td[1], "to_hub", target, source, "response"])
                    continue

            # Response: target → hub → source
            elif ptype == "response" and state == "to_hub":
                if move(p, CENTER_X, CENTER_Y):
                    p[2] = "to_target"

            elif ptype == "response" and state == "to_target":
                td = devices[target]
                if move(p, td[0], td[1]):
                    continue

            new_packets.append(p)

        packets = new_packets

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()