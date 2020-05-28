#prvo pretvorimo stringove (tekst) u brojeve i rješavanje s modulom, a to znači (igrač_1 - računalo_igrač_2) %5...ostatak 1 ili 2 - win igrač_1...3,4 win igrač 2
#"rock", "spock", "paper", "lizard", "scissors" pretvoriti u sljedeće brojeve:
#
# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
from rpslsError import RpslsError 

class Rpsls:
    
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None

    def display_title_bar(self):
            print("\t*************************************************")
            print("\t*** Igra Rock, paper, Scissors, Lizard i Spock***")
            print("\t*************************************************")

    def get_user_choice(self):
        print("\n[1] Igraj Rock Paper Scissors Lizard Spock")
        print("[2] Izlaz")
        print("\n")
        print("-"*50)
        self.player = int(input("Što želite napraviti?"))

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2, 3, 4) u nazive/tekst (rock, spock, paper, lizard, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name ="lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name


    def string_u_broj(self):
        """
    	pretvara naziv/tekst (rock, spock, paper, lizard, scissors) u broj (0, 1, 2, 3, 4)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4 
        else:
            self.player_number = -1
            raise RpslsError(102)
        return self.player_number

    def play(self):
        """
        Glavna logika.
        Prvo, radi se korisnikov input, zatim pretvara korisnikov input u broj (metoda string_u_broj), utvrđuje pobjednika i 
        na kraju pretvara odabrani broj računalo_igrač_2-a u tekst(metoda broj_u_string) i ispisuje pobjenika (Winner-a) 
        """
        
        #unos korisnikovog teksta
        self.display_title_bar()
        self.get_user_choice()

        while (self.player != 2):
            playerZbroj = 0
            computerZbroj = 0

            if(self.player > 2 or self.player < 1):
                raise RpslsError(101)
            else:
                while (playerZbroj < 3 and computerZbroj < 3):
                    print("-"*50)
                    self.player_input = input("Odaberite rock, Spock, paper, lizard ili scissors: ").lower()
                    self.player_number = self.string_u_broj()
                    
                    self.computer_number = random.randrange(0,5)
                    ostatak = (self.player_number - self.computer_number)%5
                    
                    if(self.player_number == -1):
                        winner = "Greška"
                        raise RpslsError(101)
                    else:
                        if ostatak == 0:
                            winner = "Neriješeno"
                        elif ostatak == 1 or ostatak == 2:
                            winner = "Vi (čovjek) pobjeđujete"
                            playerZbroj += 1
                        elif ostatak == 3 or ostatak == 4:
                            winner = "Računalo pobjeđuje"
                            computerZbroj += 1
           
                    self.computer_choice_name = self.broj_u_string()
                    
                    print("-"*50)
                    print("\n")
                    print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
                    print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
                    print("-"*50)
                    print("Pobjednik ove runde je: {}".format(winner))
                    print("-"*50)
                    print("Igrač ima {} bodova.".format(playerZbroj))
                    print("Računalo ima {} bodova.".format(computerZbroj))

                if playerZbroj == 3:
                    print("Pobjednik igre je Igrač!")
                elif computerZbroj == 3:
                    print("Pobjednik igre je Računalo!")

                self.get_user_choice()

                print("-"*50)
                print("Ovo je kraj igre, hvala vam na igranju!")
                print("-"*50)

if __name__ == "__main__":
    game = Rpsls()
    game.play()
    
