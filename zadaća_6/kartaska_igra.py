import random

class igra:
    def __init__(self):
        self.SPIL = [1,200]
        self.player_input = None
        self.total = 0
    def display_title_bar(self):
        print("\t*******************************************")
        print("\t*** Kartaška igra - Razvoj poslovnih aplikacija  ***")
        print("\t*******************************************")

    def get_user_choice(self):
        print("\n[1] Igraj Kartašku igru.")
        print("[x] Izlaz")
        return input ("Odaberite što želite napraviti?")

    def start_game(self):
        deck = [1, 200]
        random.shuffle(deck)
        self.player_num = int(input("Unesite broj koji želite odabrati od 1 do 200"))
        self.computer_num = random.randint(1,200)
        player_rand = [deck.pop() for _ in range(1)] 
        computer_rand = [deck.pop() for _ in range(1)]
        while True:
            if self.player_num == player_rand:
                print("Pogodili ste broj! Čestitamo!")
                break 
            elif self.player_num != player_rand:
                print("Niste pogodili! Vaš broj je premašio broj koji ste trebali pogoditi")
            elif computer_rand == self.computer_num:
                print("Računalo je pogodilo broj!")
                break
            elif computer_rand != self.computer_num:
                print("Računalo nije pogodilo zadani broj.")
            
            else:
                player_total = sum(self.SPIL[card] for card in player)
                computer_total = sum(self.SPIL[card] for card in self.computer_num)
                if player_total > computer_total:
                    print("Igrač pobjeđuje. Rezultat Igrač {} vs. Računalo {}".format(player_total, computer_total))
                else:
                    print("Računalo pobjeđuje. Rezultat: Računalo {} vs. Igrač {}".format(computer_total, player_total))
            self.total = sum(self.SPIL[card] for card in player)
    
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':    
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igranju. Pozdrav!")
            else:
                print("Hvatanje izuzetaka")

if __name__ == '__main__':
    game = igra()
    game.play()
