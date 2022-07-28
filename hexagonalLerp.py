import pygame

# declare variables

# a 2d array representing the hexagonal grid
ao = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# the pixel coordinates of the camera
cameraX = 0
cameraY = 0

# axial positions to draw line between
player = (9, 0)
target = (3, 4)

# converts cubic coordinates to axial coordinates by dropping the y value
def cubeToAxial(cube):
    q = cube[0]
    r = cube[2]
    return (q, r)

# converts axial coordinates to cubic coordinates by adding a y value such that the point satisfies the homogenous linear system x + y + z = 0
def axialToCube(hexagon):
    x = hexagon[0]
    z = hexagon[1]
    y = -x-z
    return (x, y, z)

def cubeDistance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

def cubeRound(cube):
    rx = round(cube[0])
    ry = round(cube[1])
    rz = round(cube[2])

    xDiff = abs(rx - cube[0])
    yDiff = abs(ry - cube[1])
    zDiff = abs(rz - cube[2])

    if xDiff > yDiff and xDiff > zDiff:
        rx = -ry-rz
    elif yDiff > zDiff:
        ry = -rx-rz
    else:
        rz = -rx-ry

    return (rx, ry, rz)

def lerp(a, b, t): # for floats
    return a + (b - a) * t

def cubeLerp(a, b, t): # for hexes
    return (lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t))

def cubeLineDraw(a, b):

    n = cubeDistance(a, b)
    results = []
    
    for i in range(n + 1):
        print("lerping" + str(i))
        results.append(cubeRound(cubeLerp(a, b, 1.0 / n * i)))
    
    return results

#main function
def main():
    # initialize the pygame module
    pygame.init()
    
    #create a surface on screen that has the size of 1920 x 1080
    screen = pygame.display.set_mode((1280, 720))
    
    #define a variable to control the main loop
    running = True
    
    #main loop
    while running:
        screen.fill((255, 255, 255))
        for row in range(len(ao)):
            column = 0
            for column in range(len(ao[row])):
                pygame.draw.polygon(screen, (0, 0, 0), [(3 ** 0.5 * 40 * (column + (row * 0.5)) + cameraX, row * 60 + 60 + cameraY), (3 ** 0.5 * 40 * (column + (row * 0.5)) + cameraX, row * 60 + 20 + cameraY), (3 ** 0.5 * 40 * (column + (row * 0.5) + 0.5) + cameraX, row * 60 + cameraY), (3 ** 0.5 * 40 * (column + (row * 0.5) + 1) + cameraX, row * 60 + 20 + cameraY), (3 ** 0.5 * 40 * (column + (row * 0.5) + 1) + cameraX, row * 60 + 60 + cameraY), (3 ** 0.5 * 40 * (column + (row * 0.5) + 0.5) + cameraX, row * 60 + 80 + cameraY)], 2)
        
        pygame.draw.line(screen, (255, 0, 0), (3 ** 0.5 * 40 * (player[0] + (player[1] * 0.5) + 0.5) + cameraX, player[1] * 60 + 40 + cameraY), (3 ** 0.5 * 40 * (target[0] + (target[1] * 0.5) + 0.5) + cameraX, target[1] * 60 + 40 + cameraY), 3)
        
        results = cubeLineDraw(axialToCube(player), axialToCube(target))
        
        for result in results:
            result = cubeToAxial(result)
            pygame.draw.polygon(screen, (0, 0, 255), [(3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5)) + cameraX, result[1] * 60 + 60 + cameraY), (3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5)) + cameraX, result[1] * 60 + 20 + cameraY), (3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5) + 0.5) + cameraX, result[1] * 60 + cameraY), (3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5) + 1) + cameraX, result[1] * 60 + 20 + cameraY), (3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5) + 1) + cameraX, result[1] * 60 + 60 + cameraY), (3 ** 0.5 * 40 * (result[0] + (result[1] * 0.5) + 0.5) + cameraX, result[1] * 60 + 80 + cameraY)], 3)
        
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # exit the main loop
                running = False
            # call quit event if escape is pressed
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()