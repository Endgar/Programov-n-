import random

# Character class
class Character:
  def __init__(self, name, race, health, attack, defense, max_mana):
    self.name = name
    self.race = race
    self.health = health
    self.attack = attack
    self.defense = defense
    self.max_mana = max_mana
    self.mana = max_mana

  def __str__(self):
    return f"{self.name} ({self.race})"

  # Attack method
  def attack_enemy(self, enemy):
    if self.mana >= 2:
      damage = max(0, self.attack - enemy.defense)
      enemy.health -= damage
      self.mana -= 2
      print(f"{self} attacks {enemy} and deals {damage} damage. {self} uses 2 mana.")
    else:
      print(f"{self} does not have enough mana to attack. Skipping turn.")

  # Defend method
  def defend(self):
    if self.mana >= 1:
      self.defense += 2
      self.mana -= 1
      print(f"{self} defends and increases their defense by 2. {self} uses 1 mana.")
    else:
      print(f"{self} does not have enough mana to defend. Skipping turn.")

  # Use potion method
  def use_potion(self):
    if self.mana < self.max_mana:
      self.mana = self.max_mana
      print(f"{self} uses a mana potion and regains all their mana.")
    else:
      print(f"{self} does not need to use a mana potion.")

# Create two characters
player = Character("Player", "Human", 20, 5, 3, 5)
enemy = Character("Enemy", "Orc", 20, 4, 2, 3)

# Give the player one mana potion and the enemy none
player_mana_potions = 1
enemy_mana_potions = 0

# Main game loop
while player.health > 0 and enemy.health > 0:
  # Print character information
  print(f"{player} - Health: {player.health}, Attack: {player.attack}, Defense: {player.defense}, Mana: {player.mana}/{player.max_mana}")
  print(f"{enemy} - Health: {enemy.health}, Attack: {enemy.attack}, Defense: {enemy.defense}, Mana: {enemy.mana}/{enemy.max_mana}")

  # Player's turn
  print("Player's turn.")
  choice = input("Do you want to (a)ttack, (d)efend, or use a (p)otion? ")
  if choice == "a":
    player.attack_enemy(enemy)
  elif choice == "d":
    player.defend()
  elif choice == "p":
    if player_mana_potions > 0:
      player.use_potion()
      player_mana_potions -= 1
    else:
      print("You do not have any mana potions.")

  # Enemy's turn
  print("Enemy's turn.")
  if enemy.mana >= 2:
    if random.random() < 0.5:
      enemy.attack_enemy(player)
    else:
      enemy.defend()
  else:
    enemy.defend()
  
  # Regenerate mana at the end of the turn
  player.mana = min(player.mana + 1, player.max_mana)
  enemy.mana = min(enemy.mana + 1, enemy.max_mana)

# Print the result of the game
if player.health > 0:
  print("Player wins!")
else:
  print("Enemy wins!")