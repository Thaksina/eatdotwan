import arcade
import random
from models import World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

        self.player_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0

    def setup(self):
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("dot.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)



    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.sync_with_model()
        super().draw()

class EatdotWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
        arcade.set_background_color(arcade.color.PEARL)
        # self.eatdotpom = arcade.Sprite('eat.png')
        # self.eatdotpom.set_position(30,30)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.eatdotpom = ModelSprite('eat.png',
                                        model=self.world.pom)
        self.eatdotpom.set_position(30, 30)


    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.eatdotpom.draw()


    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

def main():
    window = EatdotWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()











# class EatdotPom:
#     def __init__(self,pom):
#         self.pom = pom
#         self.pom_sprite = arcade.Sprite('homekoro.png')
#
#     def draw(self):
