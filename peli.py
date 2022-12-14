


#       ██████╗   █████╗  ███████╗ ██╗  ██╗  █████╗  ██╗  ██╗  ██████╗  ██╗   ██╗ ███████╗ ██╗   ██╗    
#       ██╔══██╗ ██╔══██╗ ██╔════╝ ██║ ██╔╝ ██╔══██╗ ██║  ██║ ██╔═══██╗ ██║   ██║ ██╔════╝ ██║   ██║    
#       ██████╔╝ ███████║ ███████╗ █████╔╝  ███████║ ███████║ ██║   ██║ ██║   ██║ ███████╗ ██║   ██║    
#       ██╔═══╝  ██╔══██║ ╚════██║ ██╔═██╗  ██╔══██║ ██╔══██║ ██║   ██║ ██║   ██║ ╚════██║ ██║   ██║    
#       ██║      ██║  ██║ ███████║ ██║  ██╗ ██║  ██║ ██║  ██║ ╚██████╔╝ ╚██████╔╝ ███████║ ╚██████╔╝    
#       ╚═╝      ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝   ╚═════╝  ╚══════╝  ╚═════╝     

#       ██████╗  ██╗   ██╗
#       ██╔══██╗ ╚██╗ ██╔╝
#       ██████╔╝  ╚████╔╝ 
#       ██╔══██╗   ╚██╔╝  
#       ██████╔╝    ██║   
#       ╚═════╝     ╚═╝  

#       ██╗   ██╗  █████╗  ██╗   ████████╗ ████████╗ ███████╗ ██████╗  ██╗
#       ██║   ██║ ██╔══██╗ ██║   ╚══██╔══╝ ╚══██╔══╝ ██╔════╝ ██╔══██╗ ██║
#       ██║   ██║ ███████║ ██║      ██║       ██║    █████╗   ██████╔╝ ██║
#       ╚██╗ ██╔╝ ██╔══██║ ██║      ██║       ██║    ██╔══╝   ██╔══██╗ ██║
#        ╚████╔╝  ██║  ██║ ███████╗ ██║       ██║    ███████╗ ██║  ██║ ██║
#         ╚═══╝   ╚═╝  ╚═╝ ╚══════╝ ╚═╝       ╚═╝    ╚══════╝ ╚═╝  ╚═╝ ╚═╝


# Jos jäljellä vain kuvakortteja, peli ei toimi
# 2 jää pyörimään


import pickle
from random import sample, uniform
from time import sleep

class Player():

    def __init__(self, lastCard = 0):
        self.hand = []
        self.lastCard = lastCard



    def draw(self, count):
        """Lisää pelaajan käteen halutun määrän kortteja pakasta"""
        if len(deck.deck) != 0:
            for i in range(count):
                self.hand.append(deck.deck.pop(0))



    def drawTable(self):
        """Nostaa pöydän käteen"""
        self.hand.extend(table.onTable)
        table.onTable = []



    def askUser(self, validNums, extra):
        """Inputin kysyminen ja virheilmotusten muodostaminen"""
        choice = input(": ")

        # Käytetään, jos pelaajalla ei ole sopivia kortteja ja täytyy nostaa pöytä.
        if extra == 1:
            validNums[1] += 1

        # Jos numeerinen
        if choice.isnumeric():
            choice = int(choice)

        # Jos ei numeerinen niin soosoo
        else:
            if choice == "menu":
                table.gameState = "menu"
                return "Kirjoita menu poistuaksesi"
            return "Vastaa vain numeroilla!"

        # Palautetaan valinta, jos se on sallitulla alueella
        if validNums[0] <= choice and validNums[1] >= choice:
            return choice
        else:
            return "Vastaa vain sallituilla numeroilla!"

        

    def playCard(self, card):
        """Pelaaja pelaa määritetyn kortin pöydälle"""
        self.lastCard = self.hand.pop(card)

        # Jos kortteja kädessä alle 5, nostetaan kortti jos mahdollista
        if len(self.hand) < 5 and len(deck.deck) > 0:
            self.draw(1)

        # Viimeinen kortti lisätään pöydällä olevien listaan
        table.onTable.append(self.lastCard)

        # Jos kortti on arvoltaan 10 tai A, pöytä kaatuu ja siirtyy pelattujen listaan
        if self.lastCard.arvo == 10 or self.lastCard.arvo == 1:
            table.out.extend(table.onTable)
            table.onTable = []



class Bot(Player):

    def playTurn(self):
        """Botti pelaa pöydälle sopivan kortin"""
        table.clean()                                               
        frame.refresh()

        print("Bot is thinking...")
        sleep(uniform(1,2.5))
        
        # Luodaan lista kädessä olevista pelattavista korteista
        playableCards = table.validCards(self.hand)

        # Jos ei pysty pelaamaan, nostetaan pöytä
        if len(playableCards) == 0:
            self.drawTable()
        else:

            # Käsi ja pelattavat kortit järjestellään painoarvon mukaan pienimmästä suurimpaan
            playableCards.sort(key=lambda x: x.painoArvo)
            self.hand.sort(key=lambda x: x.painoArvo)

            # Pelattavia kortteja verrataan kädessä oleviin, ja heti kun vastaan tulee pelattava kortti, se pelataan
            for i in range(len(self.hand)):
                if playableCards.count(self.hand[i]):
                    self.playCard(i)
                    break

        # Jos käsi tyhjä, peli päättyy
        if len(player.hand) == 0:
            table.gameState = "gameover"
            table.winner = "player"
        if len(bot.hand) == 0:
            table.gameState = "gameover"
            table.winner = "bot"
        

class ASCII():

    def __init__(self):

        self.paskahousu = [
            "                               __                 __ ",
            "                              |  \               |  \ ",
            "  ______    ______    _______ | $$   __  ______  | $$____    ______   __    __   _______  __    __ ",
            " /      \  |      \  /       \| $$  /  \|      \ | $$    \  /      \ |  \  |  \ /       \|  \  |  \ ",
            "|  $$$$$$\  \$$$$$$\|  $$$$$$$| $$_/  $$ \$$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$$| $$  | $$ ",
            "| $$  | $$ /      $$ \$$    \ | $$   $$ /      $$| $$  | $$| $$  | $$| $$  | $$ \$$    \ | $$  | $$ ",
            "| $$__/ $$|  $$$$$$$ _\$$$$$$\| $$$$$$\|  $$$$$$$| $$  | $$| $$__/ $$| $$__/ $$ _\$$$$$$\| $$__/ $$ ",
            "| $$    $$ \$$    $$|       $$| $$  \$$\ $$    $$| $$  | $$ \$$    $$ \$$    $$|       $$ \$$    $$",
            "| $$$$$$$   \$$$$$$$ \$$$$$$$  \$$   \$$\ $$$$$$$ \$$   \$$  \$$$$$$   \$$$$$$  \$$$$$$$   \$$$$$$ ",
            "| $$",
            "| $$ ",
            " \$$  \n"]

        self.winner = [
            "               __ ",
            "              |  \ ",
            " __   __   __  \$$ _______   _______    ______    ______  ",
            "|  \ |  \ |  \|  \|       \ |       \  /      \  /      \ ",
            "| $$ | $$ | $$| $$| $$$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\ ",
            "| $$ | $$ | $$| $$| $$  | $$| $$  | $$| $$    $$| $$   \$$",
            "| $$_/ $$_/ $$| $$| $$  | $$| $$  | $$| $$$$$$$$| $$ ",
            " \$$   $$   $$| $$| $$  | $$| $$  | $$ \$$     \| $$   ",
            "  \$$$$$\$$$$  \$$ \$$   \$$ \$$   \$$  \$$$$$$$ \$$  \n "]

        self.loser = [
            " __  ",
            "|  \ ",
            "| $$  ______    _______   ______    ______  ",
            "| $$ /      \  /       \ /      \  /      \ ",
            "| $$|  $$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\ ",
            "| $$| $$  | $$ \$$    \ | $$    $$| $$   \$$",
            "| $$| $$__/ $$ _\$$$$$$\| $$$$$$$$| $$ ",
            "| $$ \$$    $$|       $$ \$$     \| $$",
            " \$$  \$$$$$$  \$$$$$$$   \$$$$$$$ \$$ \n"]



    def printAscii(self, text):
        """Tulostaa ascii taidetta"""
        for i in text:
            print(i)

class Frame():

    def refresh(self, fault=""):
        """Päivittää ruudulle uusimmat tiedot"""

        cards = player.hand
        botsCards = len(bot.hand)

        # Jos pöytä on tyhjä
        if table.onTable == []:
            lastCard = blank
        else:
            lastCard = table.onTable[-1]

        # Koodi muodostaa listan, jonka jokainen elementti tulee olemaan yksi rivi näytöllä
        lines = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]      

        # Ensimmäiset 6 riviä on botin kortit  
        lines[0] = ".--------."
        lines[1] = "|  ----. |"
        lines[2] = "| : {} : |".format((2 - len(str(botsCards))) * " " + str(botsCards))
        lines[3] = "| : kpl: |"
        lines[4] = "| '----  |"
        lines[5] = "`--------'"

        # Pöydällä olevat kortit, pelatut ja nostopakka
        lines[9] = lastCard.visual[0] + int(11 * (len(cards) - 2)) * " " + ".--------."
        lines[10] = lastCard.visual[1] + int(11 * (len(cards) - 2)) * " " + "|  ----. |"
        lines[11] = lastCard.visual[2] + int(11 * (len(cards) - 2)) * " " + "| : {} : |".format((2 - len(str(len(deck.deck)))) * " " + str(len(deck.deck)))
        lines[12] = lastCard.visual[3] +  int(11 * (len(cards) - 2)) * " " + "| : kpl: |"
        lines[13] = lastCard.visual[4] + int(11 * (len(cards) - 2)) * " " + "| '----  |"
        lines[14] = lastCard.visual[5] + int(11 * (len(cards) - 2)) * " " + "`--------'"

        # Keskittää tekstit korttien määrän mukaan
        lines[8] = int(10 * len(cards) / 2) * " " + "Pöytä"
        lines[6] = int(10 * len(cards) / 2) * " " + "Bot"
        lines[15] = int(10 * len(cards) / 2) * " " + "Pöytä"
        lines[17] = int(10 * len(cards) / 2) * " " + "Käsi"
        
        # Luo näytölle niin monta korttia, kuin kädessä on, mutta maksimissaan 12
        for i in range(len(cards)):
            if i > 11:
                break                             
            lines[7].append("===========")
            lines[16].append("===========")
            lines[18].append(cards[i].visual[0])
            lines[19].append(cards[i].visual[1])
            lines[20].append(cards[i].visual[2])
            lines[21].append(cards[i].visual[3])
            lines[22].append(cards[i].visual[4])
            lines[23].append(cards[i].visual[5])
            lines[24].append("    {}{}{} ".format(i+1, ".", (5 - len(str(i+1))) * " "))

        # Aikaisemmin luotujen rivejen formatointi parempaan muotoon ja tulostaminen
        for i in lines:
            if type(i) == list:
                i = ''.join(i)
            print(i)
        print(fault)    # Jos käyttäjä kirjoittaa inputtiin ihmeellisyyksiä, virhe näkyy tässä 

class Table():

    def __init__(self):
        self.gameState = "menu"
        self.winner = ""
        self.onTable = []       # Pöydällä olevat kortit
        self.out = []           # Ulkona olevat kortit
        self.inputError = ""



    def menu(self):
        """Menu ruutu"""
        art.printAscii(art.paskahousu)
        print("1. Start new game")
        print("2. Resume")
        print("3. Save and exit")
        print("4. How to play " + "\n" + self.inputError)
        self.inputError = ""

        choice = player.askUser([1, 4], 0)
        if type(choice) == str:
            self.inputError = choice        # Jos input ei ole haluttu, luodaan virheilmoitus
        elif choice == 1:
            self.gameState = "newgame"
        elif choice == 2:
            self.gameState = "resume"
        elif choice == 3:
            self.gameState = "save"
        elif choice == 4:
            self.gameState = "howto"



    def validCards(self, hand):
        """Palauttaa listan kädestä olevista korteista, joita voi sillä hetkellä pelata"""
        validCards = []

        # Tyhjä pöytä
        if table.onTable == []:
            value = 0

        # Kättä verrataan pöydällä olevien korttien päälimmäiseen korttiin
        else:
            value = table.onTable[-1].arvo


        for i in hand:

            # Kaikki kortit arvolla 2 on automaattisesti kelpaavia
            if i.arvo == 2:
                validCards.append(i)

            # Jos pöydällä oleva kortti on 3-6 ja kädessä olevan kortin arvo on alle 11, mutta korkeampi, kuin pöydällä oleva. 
            if (2 < value < 7 or value == 0) and 10 >= i.arvo >= value:
                if (value == 0 and i.arvo == 1) == False:  # Korttia A ei voi laittaa tyhjälle pöydälle
                    validCards.append(i)

            #  Jos pöydällä oleva kortti on 7-K, ja kädessä oleva kortti on suurempi, kuin pöydällä oleva.
            if 7 <= value <= 13 and i.arvo >= value:
                validCards.append(i)

            # Jos pöydällä oleva kortti on J-K ja kädessä on ässä
            if (10 < value <= 13 and i.arvo == 1):
                validCards.append(i)

        return validCards



    def clean(self):
        """Luo tyhjän sivun"""
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


class Deck():

    def __init__(self):
        self.deck = []
 


    def newDeck(self):
        """Luo listaan 52 korttia. Loopissa maa vaihtuu jokaisen 13 kortin jälkeen"""

        self.deck = []
        for i in range(52):
            self.deck.append(i)

            if i < 13:
                name = "hertta"
                arvo = i + 1
            elif 13 <= i < 26:
                name = "ruutu"
                arvo = i -12
            elif 26 <= i < 39:
                name = "risti"
                arvo = i - 25
            elif 36 <= i:
                name = "pata"
                arvo = i -38

            # Luo jokaisesta listan elementistä card objektin
            self.deck[i] = Card(name, arvo, i)



    def suffle(self):
        """Sekoittaa pakan"""
        self.deck = sample(self.deck, len(self.deck))


class Card():

    # Jokaiselle kortille annetaan visuaali arvon mukaan. arvot ovat 1-13
    def __init__(self, maa, arvo, id):
        self.maa = maa
        self.arvo = arvo
        self.id = id
        arvoStr = arvo
        self.painoArvo = arvo - 2
        if arvo == 0:
            arvoStr = ""        # Blank
        if arvo == 1:
            arvoStr = "A"       # Ässä
        if arvo == 11:
            arvoStr = "J"       # Jätkä
        if arvo == 12:
            arvoStr = "Q"       # Akka
        if arvo == 13:
            arvoStr = "K"       # Kuningas
        self.arvoStr = str(arvoStr)

        self.visual = [".--------. ", 
                    "|{}----. | ".format((2 - len(self.arvoStr)) * " " + self.arvoStr), 
                    "| :    : | ", 
                    "| :    : | ", 
                    "| '----{}| ".format(self.arvoStr + (2 - len(self.arvoStr)) * " "), 
                    "`--------' "]

        if self.painoArvo == -1:
            self.painoArvo = 12

        if self.painoArvo == 0:
            self.painoArvo = 13
                    
        if self.maa == "hertta":
            self.visual[2] = "| :(\/): | "
            self.visual[3] = "| : \/ : | "

        if self.maa == "pata":
            self.visual[2] = "| : /\ : | "
            self.visual[3] = "| :(__): | "

        if self.maa == "ruutu":
            self.visual[2] = "| : /\ : | "
            self.visual[3] = "| : \/ : | "

        if self.maa == "risti":
            self.visual[2] = "| : () : | "
            self.visual[3] = "| :()(): | "



    def __str__(self):
        return self.maa + self.arvoStr




if __name__ == "__main__":
    art = ASCII()                           # Luokka ascii taidetta varten
    blank = Card("      ", 0, 0)            # Kortti, jolla ei ole sisältöä
    lastCard = blank                        # Viimeinen kortti, joka näkyy aina pöydällä
    frame = Frame()                         # Pelin visuaali
    player = Player()                       # Pelaaja
    deck = Deck()                           # Nostopakka
    table = Table()                         # Pelin säännöt
    bot = Bot()                             # Botti
    fault = "Kirjoita menu poistuaksesi"    # Ilmotus joka näkyy syöttörivin yläpuolella
    state = "menu"                          # Ohjelma alkaa menusta
    botTurn = 0
    drawTable = 0
    deck.newDeck()                          # Luodaan uusi pakka
    gameHasNotStarted = 1

    while True:

        if table.gameState == "menu":
            table.clean()
            table.menu()
        
        if table.gameState == "newgame":
            botTurn = 0
            drawTable = 0
            deck.deck = []
            player.hand = []
            bot.hand = []
            table.onTable = []
            table.out = []
            deck.newDeck()
            deck.suffle()
            player.draw(5)
            bot.draw(5)
            table.gameState = "game"

        if table.gameState == "resume":

            # Jos peliä pelataan ensimmäistä kertaa tässä sessiossa, niin vasta sitten luetaan tiedostoa
            # Muutoin samassa sessiossa peliin palattaessa peli palauttaisi aina edellisen tallenteen
            if gameHasNotStarted:
                try:
                    # Oliot ladataan binääritiedostosta
                    with open ("savedata.pkl", "rb") as savefile:
                        player = pickle.load(savefile)
                        bot = pickle.load(savefile)
                        table = pickle.load(savefile)
                        deck = pickle.load(savefile)
                except:
                    print("Tallennustiedoston avaaminen epäonnistui!")
                    exit()
            
            # Päälimmäinen kortti pöydälle ja peli käy
            if len(table.onTable) > 0:
                lastCard = table.onTable[-1]
            table.onTable.append(lastCard)
            table.gameState = "game"


        if table.gameState == "howto":
            table.clean()
            art.printAscii(art.paskahousu)
            print( "Pelin kulku: \n  Peli päättyy, kun koko pakka on pelattu ja voittaja on se, kenellä loppuu kädestä kortit ensimmäisenä.\n  Pelaaja aloittaa pelin ja pöytään on laitettava aina vähintään saman arvoinen \n  kortti tai sitä suurempi.\n  Kuvakortteja voi laittaa vasta, kun pöydällä on 7 tai sitä suurempi kortti. \n \n  2:n päälle voi laittaa vain 2. \n  10 kaataa pakan jossa päälimmäinen kortti on maksimissaan 9. \n  A kaataa pakan jossa on päälimmäisenä kuvakortti. \n \n  Jos et pysty pelaamaan korttia, täytyy sinun nostaa pöydältä kaikki kortit. \n  Pelattava kortti valitaan kirjoittamalla syötteeseen kortin alta löytyvä numero.\n \nPoistu valitsemalla 1")
            player.askUser([1, 1], 0)
            table.gameState = "menu"

        if table.gameState == "save":

            # Pelin tärkeimmät muuttujat tallennetaan .json tiedostoon
            # Tiedostoon merkataan jokaisen yksittäisen kortin paikka id:n mukaan
            if gameHasNotStarted == 0:
                try:
                    # Oliot tallennetaan binääritiedostoon
                    with open("savedata.pkl", "wb") as savefile:
                        pickle.dump(player, savefile)
                        pickle.dump(bot, savefile)
                        pickle.dump(table, savefile)
                        pickle.dump(deck, savefile)

                except:
                    print("Tallennustiedoston avaaminen epäonnistui!")
            exit()

        if table.gameState == "game":
            gameHasNotStarted = 0

            # Jos kädessä ei ole yhtään laillisten korttien listassa olevaa korttia, pyydetään käyttäjää nostamaan pöytä
            if len(table.validCards(player.hand)) == 0:
                drawTable = 1
                fault = f"Nosta kortit pöydältä valitsemalla {len(player.hand) + 1}"

            table.clean()                                               # Tilaa uudelle pöydälle
            frame.refresh(fault)                                        # Pöydän päivitys
            fault = "Kirjoita menu poistuaksesi"                        # Virheilmoituksen nollaus

            # Kysyy valinnan
            choice = player.askUser([1, len(player.hand)], drawTable)
            drawTable = 0                                              # drawTable muuttuja keroo funktiolle, että laillisia inputteja on 1 enemmän, jotta voidaan valita pöytdän nosto

            # Jos virheellinen input, luodaan virheilmotus
            if type(choice) == str:
                fault = choice 

            # Nostaa kortit pöydältä
            elif choice == len(player.hand) + 1:
                player.drawTable()
                botTurn = 1

            # Jos pelaajan valitsema kortti on laillisten korttien listassa, pelataan kortti
            elif table.validCards(player.hand).count(player.hand[choice - 1]):
                player.playCard(choice - 1)
                botTurn = 1

            # Botin vuoro
            if botTurn == 1:
                bot.playTurn()
                botTurn = 0

        # Peli loppu
        if table.gameState == "gameover":
            table.clean()

            # Jos pelaaja voitti
            if table.winner == "player":
                art.printAscii(art.winner)
                
            print("Poistu valitsemalla 1")
            player.askUser([1,1], 0)

            # Jos botti voitti
            if table.winner == "bot":
                art.printAscii(art.loser)
                
            print("Poistu valitsemalla 1")
            player.askUser([1,1], 0)
            table.gameState = "menu"