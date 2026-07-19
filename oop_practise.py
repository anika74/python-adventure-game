class player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        print(f"hero {self.name} has entered the dragon dungeon!")
        
    def attack(self, target_enemy):
        print(f"{self.name} attacks the{target_enemy.name} with a sword!")
        target_enemy.take_damage(20)    
        
    
    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.health = 0
            print(f"the monster {self.name} has been slain! you win!")
        else:
            print(f"the monster {self.name} took {amount} damage! monster health health: {self.health}")       
            

class enemy:
    def __init__(self, name, health,):
        self.name = name
        self.health = health
    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.health = 0
            print(f"the monster {self.name} has been slain! you win!")
        else:
            print(f"the monster {self.name} took {amount} damage! monster health health: {self.health}")       
            

hero =player("alex")
bad_dragon = enemy("red dragon", 50)
hero.attack(bad_dragon)
           