import pygame as pg
from math import sqrt
from colorsys import hsv_to_rgb
import time
pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()
B=1
itr=50
fac=100
X,Y=250,250
def draw():
    for y in range(-Y,Y):
            for x in range(-X,X):
                a=x/fac
                b=y/fac
                ca,cb=a,b
                for n in range(itr):
                    aa=a**2-b**2
                    bb=2*a*b
                    a=aa+ca
                    b=bb+cb
                    if a**2+b**2>16:break
                
                if n==itr-1:
                    c=(0,0,0)
                else:
                    n=sqrt(n/itr)
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
                fac+=10
            elif event.button==5:
                fac-=10
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
            
                    
