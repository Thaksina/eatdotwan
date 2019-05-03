import random
import arcade
import os

SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_COIN = 0.4
SPRITE_SCALING_COIN2 = 0.05
SPRITE_SCALING_COINkill = 0.3
SPRITE_SCALING_COINLIVE = 0.3
HEARTSIZE = 0.4

COIN_COUNT = 100
COINKILL_COUNT = 25
COINlive = 10

addmoredot = 1
addmorelive = 1


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Eat dot !!"


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
        self.heart = None
        self.heart2 = None
        self.heart3 = None
        self.broke = None

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

        self.broke = arcade.SpriteList()
        self.broke = arcade.Sprite("brokeheart.png", HEARTSIZE)
        self.broke.center_x = 220
        self.broke.center_y = 520


        #picture of heart1
        self.heart = arcade.SpriteList()
        self.heart = arcade.Sprite("heartlive.png", HEARTSIZE)
        self.heart.center_x = 120
        self.heart.center_y = 520

        self.heart2 = arcade.SpriteList()
        self.heart2 = arcade.Sprite("heartlive.png", HEARTSIZE)
        self.heart2.center_x = 170
        self.heart2.center_y = 520

        self.heart3 = arcade.SpriteList()
        self.heart3 = arcade.Sprite("heartlive.png", HEARTSIZE)
        self.heart3.center_x = 220
        self.heart3.center_y = 520


        # Score
        self.score = 0
        self.live = 3

        # Set up the player
        # Character
        self.player_sprite = arcade.Sprite("eat2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.background = arcade.load_texture("wallpaperdot.png")

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image
            coin = arcade.Sprite("dotdot.png", SPRITE_SCALING_COIN)
            # coinkill = arcade.Sprite("dot.png",SPRITE_SCALING_COINkill)
            # coinlive = arcade.Sprite("images.png",SPRITE_SCALING_COINLIVE)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT-100)
            # coinkill.center_x = random.randrange(SCREEN_WIDTH)
            # coinkill.center_y = random.randrange(SCREEN_HEIGHT)
            # coinlive.center_x = random.randrange(SCREEN_WIDTH)
            # coinlive.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)
            # self.coinkill_list.append(coinkill)
            # self.coinlive_list.append(coinlive)

        for i in range(COINKILL_COUNT):

            # Create the coin instance
            # Coin image
            coinkill = arcade.Sprite("min.png",SPRITE_SCALING_COINkill)

            # Position the coin
            coinkill.center_x = random.randrange(SCREEN_WIDTH)
            coinkill.center_y = random.randrange(SCREEN_HEIGHT-100)


            # Add the coin to the lists
            self.coinkill_list.append(coinkill)

        for i in range(COINlive):

            # Create the coin instance
            # Coin image
            coinlive = arcade.Sprite("4948-200.png",SPRITE_SCALING_COINLIVE)

            # Position the coin
            coinlive.center_x = random.randrange(SCREEN_WIDTH)
            coinlive.center_y = random.randrange(SCREEN_HEIGHT-100)

            # Add the coin to the lists

            self.coinlive_list.append(coinlive)




    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        self.heart.draw()
        self.heart2.draw()
        self.heart3.draw()
        self.coin_list.draw()
        self.coinkill_list.draw()
        self.coinlive_list.draw()
        self.player_list.draw()

        #title
        outputs = f"EAT DOT"
        arcade.draw_text(outputs, 10, 550, arcade.color.WHITE, 50)
        livee = f"LIFE : "
        arcade.draw_text(livee, 10, 510, arcade.color.WHITE, 30)

        livee = f"SCORE : "
        arcade.draw_text(livee, 280, 510, arcade.color.WHITE, 30)
        output = f"{self.score}"
        arcade.draw_text(output, 420, 510, arcade.color.WHITE, 30)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BABY_PINK, 14)
        output2 = f"Life: {self.live}"
        arcade.draw_text(output2, 10, 35, arcade.color.BABY_PINK, 14)
        if self.live <= 2:
            output2f = f"X"
            arcade.draw_text(output2f, 205, 500, arcade.color.WHITE, 50)
            if self.live <=1:
                x = f"X"
                arcade.draw_text(x, 150, 500, arcade.color.WHITE, 50)
                if self.live ==0:
                    y = f"X"
                    arcade.draw_text(output2f, 120, 520, arcade.color.WHITE, 30)



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


        if coins_hit_list :
            for i in range(addmoredot):
                # Create the coin instance
                # Coin image
                coin2 = arcade.Sprite("dotdot.png", SPRITE_SCALING_COIN)

                # Position the coin
                coin2.center_x = random.randrange(SCREEN_WIDTH)
                coin2.center_y = random.randrange(SCREEN_HEIGHT-100)

                # Add the coin to the lists
                self.coin_list.append(coin2)


        if coinskill_hit_list:
            for i in range(addmoredot):
                # Create the coin instance
                # Coin image
                coinkill = arcade.Sprite("min.png", SPRITE_SCALING_COINkill)

                # Position the coin
                coinkill.center_x = random.randrange(SCREEN_WIDTH)
                coinkill.center_y = random.randrange(SCREEN_HEIGHT-100)
                # Add the coin to the lists
                self.coinkill_list.append(coinkill)

        if coinlive_hit_list:
            for i in range(addmorelive):
                # Create the coin instance
                # Coin image
                coinlive = arcade.Sprite("4948-200.png", SPRITE_SCALING_COINLIVE)

                # Position the coin
                coinlive.center_x = random.randrange(SCREEN_WIDTH)
                coinlive.center_y = random.randrange(SCREEN_HEIGHT-100)

                # Add the coin to the lists

                self.coinlive_list.append(coinlive)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

        for coinkill in coinskill_hit_list:
            coinkill.kill()
            self.score -=1

        for coinlive in coinlive_hit_list:
            coinlive.kill()
            self.live -=1



        # if self.live == 2:
        #     output2f = f"Life"
        #     arcade.draw_text(output2f, 300, 300, arcade.color.WHITE, 80)
        #
        #     self.broke = arcade.SpriteList()
        #     self.broke = arcade.Sprite("brokeheart.png", HEARTSIZE)
        #     self.broke.center_x = 220
        #     self.broke.center_y = 520
        #     self.broke.draw()
        #     self.heart3.kill()




        if self.live == 0:
            getout = arcade.pause(5)
            getout()
            self.player_sprite.center_x = None
            self.player_sprite.center_y = None





def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()