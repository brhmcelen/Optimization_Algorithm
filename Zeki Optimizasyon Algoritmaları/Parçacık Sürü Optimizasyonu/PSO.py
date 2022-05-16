# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:15:43 2022

@author: admin
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np



def objective_function(v):
	x, y = v
	return 100 * (y - x**2)**2 + (1 + x)**2


bounds = [(-2.048, 2.048), (-2.048, 2.048)]   # Upper and Lower bounds of variables


nv = 2   # number of variables

nm = -1  # if minimization problem , nm = -1; if maximization problem, nm = 1


particle_size = 10          # number of particle

iterations    = 200        # max number of iterations 

w  = 0.75                   # inertia constant

c1 = 1                      # cognative constant

c2 = 2                      # social constant


fig = plt.figure()
ax = fig.add_subplot()
fig.show()


class Particle:
    
    def __init__(self,bounds):
        
        self.particle_position                    = []
        self.particle_velocity                    = []
        self.local_best_particle_position         = []
        self.fitness_local_best_particle_position = initial_fitness
        self.fitness_particle_position            = initial_fitness
        
        
        for i  in range(nv):
            
            self.particle_position.append(
                
                random.uniform(bounds[i][0], bounds[i][1]))
            
            self.particle_velocity.append(random.uniform(-1,1))
            
    def evaluate(self,objective_function):
        
        self.fitness_particle_position = objective_function(self.particle_position)
        
        if nm == -1:
            
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                
                self.local_best_particle_position = self.particle_position
                self.fitness_local_best_particle_position = self.fitness_particle_position
                
        if nm == 1:
            
            if self.fitness_particle_position > self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position
                self.fitness_local_best_particle_position = self.fitness_particle_position
                
    def update_velocity(self,global_best_particle_position):
        
        for i in range(nv):
            
            r1 = random.random()
            r2 = random.random()
            
            
            cognitive_velocity        = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity           = c2 * r2 * (global_best_particle_position[i] - self.particle_position[i])
            self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity 
            
            
    def update_position(self, bounds):
        
        for i in range(nv):
            
            self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]
            
            
            if self.particle_position[i]  > bounds[i][1]:
                
                self.particle_position[i] = bounds[i][1]
                
            if self.particle_position[i] < bounds[i][0]:
                
                self.particle_position[i] = bounds[i][0]
                
                
if nm == -1:
    
    initial_fitness = float("inf") # for minimization problem
    
if nm == 1:
    
    initial_fitness = -float("inf") # for maximization problem
    
fitness_global_best_particle_position = initial_fitness  

global_best_particle_position = []

swarm_particle = []

for i in range(particle_size):
    
    swarm_particle.append(Particle(bounds))
    
A = []

for i in range(iterations):
    
    for j in range(particle_size):
        
        swarm_particle[j].evaluate(objective_function)
        
        if nm == -1:
            
            
            if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                
                global_best_particle_position = list(swarm_particle[j].particle_position)
                fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                
            
        if nm == 1:
            
            if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                
                global_best_particle_position = list(swarm_particle[j].particle_position)
                fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                
    for j in range(particle_size):
        
        swarm_particle[j].update_velocity(global_best_particle_position)
        swarm_particle[j].update_position(bounds)
        
    A.append(fitness_global_best_particle_position)
    
    
    ax.plot(A, color = 'r')
    fig.canvas.draw()
    ax.set_xlim(left = max (0, i - iterations), right = i +3)
    
print('Optimal solution: ', global_best_particle_position)
print(A)

#print('Objective function value: ', fitness_global_best_particle_position)
#print('Objective function value: ', objective_function)
#print('Objective function value: ', fitness_global_best_particle_position)
plt.show()


                
            
            
        
            
            
            
            
            
            
            
        
            
            
    



  

    