try:
    
    import pygame
    import pendulum_movement as pm
    from math import pi, radians
    from random import randint

except Exception:
    
    print("You are either missing one or more files or they are not in same directory")

pygame.init()
p_c = dict()
flag = 0
a1, a2 = 1440, 1280                     #PROVIDE THE DISPLAY CONFIGURATION HERE
running = True
x_offset, y_offset = a1 // 2, a2 // 2


def run(p, *theme_col1):
    
    pygame.draw.line(screen, theme_col1, (x_offset, y_offset), (x_offset + (x1:=p.movement()[0]), y_offset - (y1:=p.movement()[1])))
    pygame.draw.circle(screen, theme_col1, (x_offset + x1, y_offset - y1), p.mass * 3)

try:
        
    n = int(input("Number of pendulums: "))

    for i in range(n):

        print(f"\nFor pendulum {i + 1}\n")
        theta = radians(float(input("Enter start angle[in degrees]: ")))
        mass = float(input("Enter mass[in kg]: "))
        length = float(input("Enter length[in m]: ")) * 100
        p_c[i] = pm.pendulum(length, mass, theta)

    theme_col = input("Enter Theme[Dark, Light, RGB]:")
    
    if theme_col.lower() == 'dark':
            
            col = [0, 0, 0]
        
    elif theme_col.lower() == 'light':
        
            col = [255, 255, 255]
    
    elif theme_col.lower() == 'rgb':
            
            col = [randint(0, 255), randint(0, 255), randint(0, 255)]
            flag = 1
            count = [0, 0, 0]
        
    print("To quit just close the window or press ESC.")

    screen = pygame.display.set_mode([a1, a2])
    pygame.display.set_caption('Simple Pendulum')
    
    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.display.quit()
                pygame.quit()
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    
                    pygame.display.quit()
                    pygame.quit()
                    running = False
        
        screen.fill(tuple(col))
        
        if flag:
            
            for i in range(3):    
                col[i] += randint(1, 3) * ((-1) ** count[i])
                
                if col[i] > 255:
                    
                    col[i] = 255
                    count[i] += 1
                
                if col[i] < 0:
                    
                    col[i] = 0
                    count[i] -= 1

        for i in p_c:
            run(p_c[i], 255 - col[0], 255 - col[1], 255 - col[2])
        
        pygame.display.update()
        pygame.time.delay(13)

    print("Thank You for trying out my Simple Pendulum project... Will upload double pendulum too so stay tuned")

except Exception as e:
    
        print(e)
        pygame.display.quit()
        pygame.quit()
        running = False    

