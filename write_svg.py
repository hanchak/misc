import random
import os
N = 800

with open('test.svg','w') as f:
    
    f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
    
    f.write(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{N}" height="{N}">\n')
    
    # filter (optional):
    filter = 0
    f.write(f'<defs><filter id="f1" x="0" y="0" w="{N}" h="{N}"><feGaussianBlur in="SourceGraphic" stdDeviation="{filter}" /></filter></defs>\n')
    
    for i in range(50):
        
        x = random.randint(1,N/2)
        y = random.randint(1,N/2)
        w = random.randint(1,N/2)
        h = random.randint(1,N/2)
        c = random.choice(["red","blue","green","none"])   
        o = random.random() 
    
        f.write(f'\t<rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill:{c};stroke:black;stroke-width:1;fill-opacity:{o/2:1.2f};stroke-opacity:1" filter="url(#f1)"/>\n')
    
    f.write('</svg>\n')

os.system(r'start chrome "C:\Users\HanchaMS\Documents\Python Scripts\misc\test.svg"')
