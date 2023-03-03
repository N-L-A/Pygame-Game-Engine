import pygame
import random
import time
from PE_tools import Label


spawn_rate_sens = 100
delta_time = 0


def rand_spread(spread_range: int, rot: int):
    """pick random rotation in a range (used by the particle emitter)"""
    spread_range = int(spread_range/2)
    return random.randint(rot-spread_range, spread_range+rot)


class Particle:
    """Used by the emitter. useless by itself"""
    def __init__(self, texture:pygame.Surface, pos: pygame.Vector2, size:float, direction:int):
        self.pos = pos
        self.size = size
        self.direct = direction
        self.texture = texture
        self.spawned = time.time()
        self.rot = 0

    def show(self, workspace: pygame.Surface):
        """put the particle on a surface"""
        Label.fast_image(workspace, self.texture, [self.size]*2, self.pos, rot=self.rot)


class Emitter:
    """Emits particles."""
    def __init__(self, texture: pygame.Surface, pos: pygame.Vector2, size=10, speed=1, life_time=1, spawn_rate=1,
                 max_particles=20, spread_range=360, rotation=0, rot_speed=0):
        self.texture = texture
        self.pos = pos
        self.size = size
        self.speed = speed
        self.life_time = life_time
        self.max_spawn = max_particles
        self.particles = []
        self.rate = spawn_rate
        self.spread = spread_range
        self.rot = rotation
        self.rot_speed = rot_speed

    def show(self, workspace: pygame.Surface):
        """put the emitter on a surface"""
        for x in self.particles:
            x.show(workspace)

    def frame(self):
        """tick update for the simulation. put in the main loop."""
        if isinstance(self.rate, int):
            for i in range(self.rate):
                if len(self.particles) < self.max_spawn:
                    self.particles.append(Particle(self.texture, self.pos, self.size, rand_spread(self.spread, self.rot)))
        else:
            for i in range(int(self.rate)):
                if len(self.particles) < self.max_spawn:
                    self.particles.append(Particle(self.texture, self.pos, self.size, rand_spread(self.spread, self.rot)))
            if random.randint(0, spawn_rate_sens) <= (self.rate%1)*spawn_rate_sens:
                self.particles.append(Particle(self.texture, self.pos, self.size, rand_spread(self.spread, self.rot)))

        for x in self.particles:
            if time.time()-x.spawned > self.life_time:
                self.particles.remove(x)
            else:
                speed = self.speed*delta_time
                vec = pygame.math.Vector2(0, 1).rotate(x.direct)
                x.pos = (x.pos[0]+(vec.x*speed), x.pos[1]+(vec.y*speed))
                x.rot += self.rot_speed*delta_time

    def change_variables(self, texture=None, pos=None, size=None, speed=None, life_time=None, spawn_rate=None,
                         max_particles=None, spread_range=None, rotation=None, rot_speed=None):
        """change specific parameters of the particle emitter"""
        if texture:
            self.texture = texture
        if pos:
            self.pos = pos
        if size:
            self.size = size
        if speed:
            self.speed = speed
        if life_time:
            self.life_time = life_time
        if max_particles:
            self.max_spawn = max_particles
        if spawn_rate:
            self.rate = spawn_rate
        if spread_range:
            self.spread = spread_range
        if rotation:
            self.rot = rotation
        if rot_speed:
            self.rot_speed = rot_speed
