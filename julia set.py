import pygame as pg
from math import sqrt
from colorsys import hsv_to_rgb
import time
pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()
B=1
itr=1000

r=10 # choose R > 0 such that R**2 - R >= sqrt(cx**2 + cy**2)
X,Y=250,250
def draw():
    for y in range(-Y,Y,10):
            for x in range(-X,X,10):
                zx=x/(X*2)
                zy=y/(Y*2)
                n=0
                while zx**2+zy**2<r**2 and n<itr:
                    xtemp = zx * zx - zy * zy
                    zy = 2 * zx * zy 
                    zx = xtemp 
                    n+=1
                
                if n==itr:
                    c=(0,0,0)
                else:
                    n=n/itr
                    c=hsv_to_rgb(1-n,1,255)
                f.set_at((x+X,y+Y),c)
   
    pg.display.flip()
while B:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            B=0
        elif event.type==pg.MOUSEBUTTONUP:
            if event.button==4:
                r+=0.1
            elif event.button==5:
                r-=0.1
        elif event.type==pg.KEYUP:
            if event.key==pg.K_s:
                pg.image.save(f,'mandelbrot.png')
            else:
                t=time.time()
                draw()
                print('done',round(time.time()-t,2),'sec')
        elif event.type==pg.VIDEORESIZE:
            X=int(event.w/2)
            Y=int(event.h/2)
            draw()
            
                    
