class character:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
            
    def take_damage(self, amount):
        self.__health -= amount
        
        if self.__health <= 0:
            self.__health = 0
            print(f" {self.name} has been defeated!")
        else:
            print(f" {self.name} took {amount} damage! remaining health: {self.__health}")
    def get_health(self):
        return self.__health          
            
class player(character):
    def attack(self, target):
        print(f"{self.name} attacks {target.name} with a heavy sword!")
        target.take_damage(25)                 
            

class enemy(character):
    def attack(self, target):
        print(f"{self.name} breathes fire on {target.name}!")
        target.take_damage(15)
        
hero =player("alex", 100)
bad_dragon = enemy("red dragon", 60)
print("---fight start!---")
hero.attack(bad_dragon)
print("-" * 20)
bad_dragon.attack(hero)
print(f"Alex's real health is: {hero.get_health()}")
           