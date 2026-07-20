import sqlite3
def init_db():
    conn = sqlite3.connect("adventure_game.db")

    cursor = conn.cursor()

    cursor.execute("""               
    CREATE TABLE IF NOT EXISTS game_saves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        health INTEGER,
        score INTEGER    
    )               

    """)
    conn.commit()
    conn.close()

def save_player_data(name, health, score):
    conn = sqlite3.connect("adventure_game.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    INSERT OR REPLACE INTO game_saves (name, health, score)
    VALUES (?, ?, ?)""" ,
        (name, health , score),           
    )
    conn.commit()
    conn.close()

def load_player_data(name):
    conn = sqlite3.connect("adventure_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT health, score FROM game_saves WHERE NAME =?", (name,))
    data = cursor.fetchone()
    conn.close()
    return data


class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
            
    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.health = 0
            print(f" {self.name} has been defeated!")
        else:
            print(f" {self.name} took {amount} damage! remaining health: {self.health}")
    def get_health(self):
        return self.health          
            
class player(character):
    def __init__(self, name, health=100, score=0):
        super() .__init__(name, health)
        self.score =score
                        
                        
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(20) 
        if target.health ==0:
            self.score += 50
            print(f"you defeated {target.name}! +50 score. tatal score: {self.score}")                    
            
init_db()
player_name = "ALEX"
print(f"loading data for {player_name} from database....")
saved_data = load_player_data(player_name)

if saved_data:
    saved_health, saved_score = saved_data
    print(f"welcome back {player_name}! loaded health: {saved_health}, score: {saved_score}")
    hero = player(player_name, saved_health, saved_score)
else:    
    print(f"creating a new character for {player_name}...") 
    hero = player(player_name)
    
dragon = character("red dragon", 40)
hero.attack(dragon)
dragon.take_damage(10)
hero.take_damage(10)
hero.attack(dragon)
print(f"\n saving {hero.name}'s progress to the database...")
save_player_data(hero.name, hero.health, hero.score)
print("game state saved sucessfully!")    
    
               
           