# -*- coding: latin-1 -*-
from pylab import *
import pygame

def ens_mandelbrot(L,H,xmin,xmax,ymin,ymax,kmax):
  # Parcour de la fenêtre pixel par pixel :
  for y in range(0,H):
    for x in range(0,L):
      # Point C :
      cx = (x*(xmax - xmin)/L + xmin)
      cy = (y*(ymin - ymax)/H + ymax)
      # Initialisation de la suite :
      xk = 0
      yk = 0
      k = 0
      test = 0
      # Test si la suite diverge, càd distance OM inférieure ou égale à 2 :
      while test < 2 and k < kmax:
        # Nouveau point M :
        xk_aux = xk
        yk_aux = yk
        xk = xk_aux**2 - yk_aux**2 + cx
        yk = 2*xk_aux*yk_aux + cy
        k = k + 1
        test = sqrt(xk**2 + yk**2)
      # Si la suite converge :
      if k == kmax:
        # Coloration du pixel en noir :
        screen.set_at((x,y), (0,0,0))
      # Si la suite ne converge pas :
      else:
        # Coloration du pixel en couleur :
        screen.set_at((x,y), ((3*k)%256,(1*k)%255,(10*k)%255))

if __name__ == "__main__":
  
  # Définition des constantes :
  kmax =200 # Nombre d'itération maximum
  xmin, xmax, ymin, ymax = -2, 0.5, -1.25, 1.25 #Bornes du repère
  L = 1000 # Largeur de la fenêtre en pixel
  H = 1000 # Hauteur de la fenêtre en pixel
  
  # Création de la fenêtre :
  pygame.init()
  screen = pygame.display.set_mode((L,H))
  pygame.display.set_caption("Fractale de Mandelbrot")
  
  # Création de l'ensemble de Mandelbrot
  ens_mandelbrot(L,H,xmin,xmax,ymin,ymax,kmax)
  
  # Rafréchissement de la fenêtre :
  pygame.display.flip()
  
  # Affichage de la fenêtre :
  loop = True
  while loop:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        loop = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        p = pygame.mouse.get_pos()
        px = (p[0]*(xmax - xmin)/L + xmin)
        py = (p[1]*(ymin - ymax)/H + ymax)
        print("({};{})".format(px,py))
  
  pygame.quit()
