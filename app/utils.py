def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."

def load_game():
    return '''<form method="post">
              Please choose a game to play: <br>
              1. Memory Game <br>
              2. Guess Game <br>
              3. Currency Roulette <br>
              <input type="text" name="game_choice"><br>
              Please choose game difficulty from 1 to 5: <br>
              <input type="text" name="difficulty"><br>
              <input type="submit" value="Submit">
              </form>'''
