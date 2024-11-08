import arcade

SCREEN_WIDTH = 800         # Ширина окна
SCREEN_HEIGHT = 600        # Высота окна
SCREEN_TITLE = 'Pong Game' # Название окна


class Ball(arcade.Sprite):      #  мяч
    def __init__(self):
        super().__init__('ball.png', 0.03)   # берем логику работы с родителя работу с файла
        self.change_x = 3             # скорость мяча
        self.change_y = 3

    def update(self):               # движение мяча  переопределение метода update
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x   # соприкосновение со стенкой
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y

class Bar(arcade.Sprite):  # ракетка

    def __init__(self):
        super().__init__('bar.png', 0.3)  # берем логику работы с родителя работу с файла

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()                                    # создаем ракетку
        self.ball = Ball()                                  # создаем мяч
        self.setap()

    def setap(self):                                        # положение ракетки     собственный метод, не относится к родителю класса
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2



    def on_draw(self):  # отрисовка белого фона
        self.clear((255, 255, 255))    # очистка экрана
        self.bar.draw()                                         # отрисовываем ракетку
        self.ball.draw()                                        # отрисовываем мяч

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5


    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0




if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

