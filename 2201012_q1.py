import random

class GameOfSticks:
    def __init__(self, initial_sticks):
        self.sticks = initial_sticks
        self.current_player = None
    
    def start_game(self):
        self.current_player = random.choice(["AI", "Human"])
        print("Start game sticks with", self.sticks, "sticks.")
        print("First turn:", self.current_player)
        self.play()
    
    def play(self):
        while self.sticks > 0:
            if self.current_player == "AI":
                self.ai_turn()
            else:
                self.human_turn()
            self.toggle_player()
        print("Game over! Winner:", "Human" if self.current_player == "AI" else "Human")
    
    def ai_turn(self):
        sticks_to_pick = min(3, self.sticks)
        sticks_to_pick = max(1, sticks_to_pick)  
        print("AI picks", sticks_to_pick, "sticks.")
        self.sticks -= sticks_to_pick
        print("Sticks remaining:", self.sticks)
    
    def human_turn(self):
        valid_input = False
        while not valid_input:
            try:
                sticks_to_pick = int(input("Enter the of sticks you want to pick (1-3): "))
                if 1 <= sticks_to_pick <= 3 and sticks_to_pick <= self.sticks:
                    valid_input = True
                else:
                    print("Invalid input! You must pick between 1 and 3 sticks, and there must be  sticks remaining.")
            except ValueError:
                print("Invalid input! enter a valid integer.")
        self.sticks -= sticks_to_pick
        print("You picked", sticks_to_pick, "sticks.")
        print("Sticks remaining:", self.sticks)
    
    def toggle_player(self):
        self.current_player = "Human" if self.current_player == "AI" else "AI"
def main():
    initial_sticks = 53
    game = GameOfSticks(initial_sticks)
    game.start_game()

if __name__ == "__main__":
    main()
