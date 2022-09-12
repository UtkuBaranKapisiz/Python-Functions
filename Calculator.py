import numpy as np


class cal():
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def add(self):
        return self.left + self.right

    def mul(self):
        return self.left * self.right

    def div(self):
        return self.left / self.right

    def sub(self):
        return self.left - self.right

    def powr(self):
        return self.left ** self.right

    def roott(self):
        return self.left ** (1/self.right)

    def deriv(self):
        return np.gradient(self.left, self.right)  # self.left is y and self.right is dx

    def integ(self):
        return np.trapz(self.left, self.right)

    def take_mode(self):
        return self.left % self.right

    def abso(self):
        return abs(self.left)
