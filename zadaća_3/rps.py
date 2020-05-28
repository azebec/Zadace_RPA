# 0 - rock
# 1  - paper
# 2 - scissors

import random
from rpsError import RpsError 
class rps:
    def _init_(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name =  None

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2) u nazive/tekst (rock, paper, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "paper"
        elif self.computer_number == 2:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpsError(103)
        return self.computer_choice_name

    def string_u_broj(self):
        """
    	pretvara naziv/tekst (rock, paper, scissors) u broj (0, 1, 2)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "paper":
            self.player_number = 1
        elif self.player_input == "scissors":
            self.player_number = 2
        else:
            self.player_number = -1
            raise RpsError(102)
        return self.player_number

    def play(self):
        """
        Glavna logika.
        Prvo, radi se korisnikov input, zatim pretvara korisnikov input u broj (metoda string_u_broj), utvrđuje pobjednika i 
        na kraju pretvara odabrani broj računalo_igrač_2-a u tekst(metoda broj_u_string) i ispisuje pobjenika (Winner-a) 
        """
        #unos korisnikovog teksta
        self.player_input = input("Odaberite rock, paper ili scissors: ").lower()
        #pretvorba korisnikovog teksta u broj 
        self.player_number = self.string_u_broj()
        #računalo odabire pomoću random metode
        self.computer_number = random.randrange (0,3)
        ostatak = (self.player_number - self.computer_number)%3
        if(self.player_number == -1):
            winner = "Greška"
            raise RpsError(101)
        else:
            if ostatak == 0:
                winner = "Neriješeno"
            elif ostatak == 1:
                winner = "Vi (čovjek) pobjeđujete"
            elif ostatak == 2:
                winner = "Računalo pobjeđuje"
        self.computer_choice_name = self.broj_u_string()
        print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
        print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
        print(winner)

if __name__ == "__main__":
    game = rps()
    game.play()
    
