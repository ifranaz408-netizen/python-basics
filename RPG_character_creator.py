print("=====================================")
print("welcomto day 10 :RGB chracter creator")
print("=====================================")
from typing import TYPE_CHECKING
class Character:
    """
    Represents a base character within the RPG engine.
    
    Handles core attributes such as health, base power, and state tracking,
    providing foundational mechanics for combat interactions.
    """
    def __init__(self, name: str, health: int, power: int) -> None:
        """Initializes the character with basic combat stats."""
        self.name: str = name
        self.max_health: int = health
        self.health: int = health
        self.power: int = power

    @property
    def is_alive(self) -> bool:
        """Returns True if the character's health is above zero."""
        return self.health > 0

    def attack(self, target: 'Character') -> None:
        """
        Executes an attack against a target character instance.
        
        Demonstrates dependency injection / object interaction.
        """
        if not self.is_alive:
            print(f"{self.name} cannot attack because they are defeated!")
            return
            
        print(f" {self.name} attacks {target.name} for {self.power} damage!")
        target.take_damage(self.power)

    def take_damage(self, amount: int) -> None:
        """
        Reduces character health by a specified amount.
        
        Includes boundary safeguards to prevent negative health states.
        """
        if not self.is_alive:
            return

        self.health -= amount
        if self.health < 0:
            self.health = 0
            
        print(f"{self.name} took {amount} damage. Remaining Health: {self.health}/{self.max_health}")
        
        if not self.is_alive:
            print(f"{self.name} has been defeated!")

# ==========================================
# Demonstration / Simulation Script
# ==========================================
if __name__ == "__main__":
    print("--- RPG Battle Simulation Starting --- \n")
    
    # Instantiate two distinct character objects
    hero = Character(name="Arthur", health=100, power=25)
    villain = Character(name="Malakor", health=60, power=35)

    # Turn-based combat loop simulation
    print(f"Initial State: {hero.name} ({hero.health} HP) vs {villain.name} ({villain.health} HP)\n")
    
    hero.attack(villain)
    print("---")
    villain.attack(hero)
    print("---")
    hero.attack(villain)
    print("---")
    hero.attack(villain) # Final blow
