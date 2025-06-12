#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Snake Game - A simple implementation of the classic Snake game using Pygame
"""

import pygame
import sys

# Initialize constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
FPS = 60

def main():
    """
    Main entry point of the game.
    Initializes Pygame, sets up the game window, and runs the main game loop.
    """
    # Initialize pygame
    pygame.init()
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    
    # Initialize clock for controlling game speed
    clock = pygame.time.Clock()
    
    # Center the game window on the screen
    # Removed redundant call to pygame.display.set_mode
    
    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            # Check for quit event (window close button)
            if event.type == pygame.QUIT:
                running = False
            
        # Fill the screen with background color
        screen.fill(BACKGROUND_COLOR)
        
        # Update the display
        pygame.display.flip()
        
        # Control the game speed
        clock.tick(FPS)
    
    # Clean up and quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()