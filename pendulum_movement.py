from math import sin, pi

GTY = 0.0489

class pendulum:

    def __init__(self, length, mass, theta):
        self.length = length
        self.mass = mass
        self.theta = theta
        self.a_vel = 0


    def movement(self):
        self.s = sin(self.theta)
        self.a_acc = -GTY/self.length * self.s
        self.a_vel += self.a_acc 
        self.theta += self.a_vel
        self.x = self.length * self.s
        self.y = -self.length * (1 - self.s**2)**0.5
        return self.x, self.y

