import random
import arcade
import os

SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_COIN2 = 0.05
SPRITE_SCALING_COINkill = 0.2
SPRITE_SCALING_COINLIVE = 0.2

COIN_COUNT = 100
COINKILL_COUNT = 20
COINlive = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"


class MyGame(arcade.Window):

    def __init__(self):


        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.coinkill_list = None
        self.coinlive_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.live = 3

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)
        self.background = None

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coinkill_list = arcade.SpriteList()
        self.coinlive_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.live = 3

        # Set up the player
        # Character
        self.player_sprite = arcade.Sprite("eat2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.background = arcade.load_texture("6.jpg")

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image
            coin = arcade.Sprite("dotdot.png", SPRITE_SCALING_COIN)
            coinkill = arcade.Sprite("dot.png",SPRITE_SCALING_COINkill)
            coinlive = arcade.Sprite("images.png",SPRITE_SCALING_COINLIVE)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coinkill.center_x = random.randrange(SCREEN_WIDTH)
            coinkill.center_y = random.randrange(SCREEN_HEIGHT)
            coinlive.center_x = random.randrange(SCREEN_WIDTH)
            coinlive.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)
            self.coinkill_list.append(coinkill)
            self.coinlive_list.append(coinlive)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.coin_list.draw()
        self.coinkill_list.draw()
        self.coinlive_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BABY_PINK, 14)
        output2 = f"Life: {self.live}"
        arcade.draw_text(output2, 10, 35, arcade.color.BABY_PINK, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        # Call update
        self.coin_list.update()
        self.coinkill_list.update()
        self.coinlive_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        coinskill_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coinkill_list)
        coinlive_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coinlive_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

        for coinkill in coinskill_hit_list:
            coinkill.kill()
            self.score -=1

        for coinlive in coinlive_hit_list:
            coinlive.kill()
            self.live -=1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()