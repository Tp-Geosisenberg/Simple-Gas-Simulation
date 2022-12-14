import renderer as gui
import particles as prt
import pygame


pool = prt.pool(e=.96, g= 0.01)
pool.setdomain(((400,200),(800, -200)))

pool2 = prt.pool(e = 1,g =.001)
pool2.setdomain(((-800, 200), (-400, -200)))

pool.random(60, 1, 15)
pool2.random(60, 20, 15)

pools = [pool, pool2]

i = 0

while True:
    i += 1
    pygame.time.Clock().tick(144)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if i ==300000:
            pool.merge(pool2)
            pool.setdomain(((-800, 400), (800, -400)))
            pools.remove(pool2)

    for p in pools:
        p.update()
        print("pool temp : ",p.getmediantemp())
        gui.drawpool(p)

    gui.update()


