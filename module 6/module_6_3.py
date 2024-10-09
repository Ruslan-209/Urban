class Horse:
    x_distance = 0
    sound = 'Frr'

    def run(self, dx):
        self.x_distance += int(dx)

class Eagle:
        y_distance = 0
        sound = 'I train, eat, sleep, and repeat'

    def fly(dy):
        y_distance += int(dy)

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()