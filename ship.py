import pygame


class Ship:
    """ A class to manage the ship"""

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and gets its rectangle
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.bmp'), (80, 80))

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value fo the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect. Make sure the ship will remain in the field of view of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
