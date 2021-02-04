from flask import Flask, render_template, url_for, redirect
from forms import StworzGracza1
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '07417ccad673ce4dd00f31ca49620010'

current_player = 1
wynik = 0
specjalne_pole = [[0, 4], [1, 10], [2, 2], [3, 7], [6, 10], [7, 3], [9, 5], [10, 1], [5, 3], [0, 12], [2, 13], [4, 5], [4, 9], [6, 5], [8, 8], [8, 1], [9, 11], [10, 6], [2, 1], [1, 6], [0, 2], [8, 2], [7, 7], [3, 11], [7, 13], [10, 9], [0, 8], [3, 4], [6, 12], [10, 3], [5, 7]]

class Player:
    def __init__(self, name):
        self.name = name
    pionek1 = [0, 0]
    pionek2 = [0, 0]
    pole = [0, 0]
    gold = 0
    diamond = 0
    carbon = 0
    punkty = 0
    czy_rzucone = 0
    czy_surowiec = 0
    czy_cofa = 0

    def karnecofanie(self, other_player):
        if self.pionek1 == other_player.pionek1:
            other_player.pionek1 = [0, 0]
        if self.pionek1 == other_player.pionek2:
            other_player.pionek2 = [0, 0]
        if self.pionek2 == other_player.pionek1:
            other_player.pionek1 = [0, 0]
        if self.pionek2 == other_player.pionek2:
            other_player.pionek2 = [0, 0]
        self.czy_cofa = 0

    def surowce(self):
        if (self.pionek1[0] == 0 and self.pionek1[1] == 4) \
                or (self.pionek1[0] == 1 and self.pionek1[1] == 10) \
                or (self.pionek1[0] == 2 and self.pionek1[1] == 2) \
                or (self.pionek1[0] == 3 and self.pionek1[1] == 7) \
                or (self.pionek1[0] == 6 and self.pionek1[1] == 10) \
                or (self.pionek1[0] == 7 and self.pionek1[1] == 3) \
                or (self.pionek1[0] == 9 and self.pionek1[1] == 5) \
                or (self.pionek1[0] == 10 and self.pionek1[1] == 1) \
                or (self.pionek1[0] == 5 and self.pionek1[1] == 3) \
                or (self.pionek1[0] == 0 and self.pionek1[1] == 12) \
                or (self.pionek1[0] == 2 and self.pionek1[1] == 13) \
                or (self.pionek1[0] == 4 and self.pionek1[1] == 5) \
                or (self.pionek1[0] == 4 and self.pionek1[1] == 9) \
                or (self.pionek1[0] == 6 and self.pionek1[1] == 5) \
                or (self.pionek1[0] == 8 and self.pionek1[1] == 8) \
                or (self.pionek1[0] == 8 and self.pionek1[1] == 1) \
                or (self.pionek1[0] == 9 and self.pionek1[1] == 11) \
                or (self.pionek1[0] == 10 and self.pionek1[1] == 6):
            self.carbon += 1
        elif (self.pionek1[0] == 2 and self.pionek1[1] == 1) \
                or (self.pionek1[0] == 1 and self.pionek1[1] == 6) \
                or (self.pionek1[0] == 0 and self.pionek1[1] == 2) \
                or (self.pionek1[0] == 8 and self.pionek1[1] == 2) \
                or (self.pionek1[0] == 7 and self.pionek1[1] == 7) \
                or (self.pionek1[0] == 3 and self.pionek1[1] == 11) \
                or (self.pionek1[0] == 7 and self.pionek1[1] == 13) \
                or (self.pionek1[0] == 10 and self.pionek1[1] == 9):
            self.gold += 1
        elif (self.pionek1[0] == 0 and self.pionek1[1] == 8) \
                or (self.pionek1[0] == 3 and self.pionek1[1] == 4) \
                or (self.pionek1[0] == 6 and self.pionek1[1] == 12) \
                or (self.pionek1[0] == 10 and self.pionek1[1] == 3) \
                or (self.pionek1[0] == 5 and self.pionek1[1] == 7):
            self.diamond += 1

        elif (self.pionek2[0] == 0 and self.pionek2[1] == 4) \
                or (self.pionek2[0] == 1 and self.pionek2[1] == 10) \
                or (self.pionek2[0] == 2 and self.pionek2[1] == 2) \
                or (self.pionek2[0] == 3 and self.pionek2[1] == 7) \
                or (self.pionek2[0] == 6 and self.pionek2[1] == 10) \
                or (self.pionek2[0] == 7 and self.pionek2[1] == 3) \
                or (self.pionek2[0] == 9 and self.pionek2[1] == 5) \
                or (self.pionek2[0] == 10 and self.pionek2[1] == 1) \
                or (self.pionek2[0] == 5 and self.pionek2[1] == 3) \
                or (self.pionek2[0] == 0 and self.pionek2[1] == 12) \
                or (self.pionek2[0] == 2 and self.pionek2[1] == 13) \
                or (self.pionek2[0] == 4 and self.pionek2[1] == 5) \
                or (self.pionek2[0] == 4 and self.pionek2[1] == 9) \
                or (self.pionek2[0] == 6 and self.pionek2[1] == 5) \
                or (self.pionek2[0] == 8 and self.pionek2[1] == 8) \
                or (self.pionek2[0] == 8 and self.pionek2[1] == 1) \
                or (self.pionek2[0] == 9 and self.pionek2[1] == 11) \
                or (self.pionek2[0] == 10 and self.pionek2[1] == 6):
            self.carbon += 1
        elif (self.pionek2[0] == 2 and self.pionek2[1] == 1) \
                or (self.pionek2[0] == 1 and self.pionek2[1] == 6) \
                or (self.pionek2[0] == 0 and self.pionek2[1] == 2) \
                or (self.pionek2[0] == 8 and self.pionek2[1] == 2) \
                or (self.pionek2[0] == 7 and self.pionek2[1] == 7) \
                or (self.pionek2[0] == 3 and self.pionek2[1] == 11) \
                or (self.pionek2[0] == 7 and self.pionek2[1] == 13) \
                or (self.pionek2[0] == 10 and self.pionek2[1] == 9):
            self.gold += 1
        elif (self.pionek2[0] == 0 and self.pionek2[1] == 8) \
                or (self.pionek2[0] == 3 and self.pionek2[1] == 4) \
                or (self.pionek2[0] == 6 and self.pionek2[1] == 12) \
                or (self.pionek2[0] == 10 and self.pionek2[1] == 3) \
                or (self.pionek2[0] == 5 and self.pionek2[1] == 7):
            self.diamond += 1
        self.czy_surowiec = 0

    def kostka(self):
        global wynik
        wynik = random.randint(1, 6)
        self.czy_rzucone = 1

    def ruch(self, pionek, other_player):
        global pomoc,current_player
        pomoc = 0
        if pionek == '1':
            self.pole = self.pionek1
        elif pionek == '2':
            self.pole = self.pionek2
        kolumna = self.pole[1]
        if (self.pole[0] == 0 and self.pole[1] == 0) or (self.pole[0] == 0 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # zerwoy wiersz
            if self.pole[1] > 14:
                self.pole[1] = 14
                self.pole[0] += 1
                pomoc = wynik - 1 - (self.pole[1] - kolumna)
                self.pole[1] -= pomoc  # zejscie z zerowego wiersza (z ruchu od lewej) na wiersz nizej

        elif (self.pole[0] == 1 and self.pole[1] == 14) or self.pole[0] == 1 and self.pole[1] in range(0, 14):
            self.pole[1] -= wynik  # ruch na pierwszym wierszu
            if (self.pole[1] < 0):
                self.pole[1] = 0
                self.pole[0] += 1
                pomoc = wynik - 1 -(self.pole[1] + kolumna)
                self.pole[1] += pomoc #zejscie z pierwszego na drugi

        elif (self.pole[0] == 2 and self.pole[1] == 0) or (self.pole[0] == 2 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # drugi wiersz
            if self.pole[1] > 14:
                self.pole[1] = 14
                self.pole[0] += 1
                pomoc = wynik - 1 - (self.pole[1] - kolumna)
                self.pole[1] -= pomoc  # zejscie z drugiego wiersza na trzeci

        elif (self.pole[0] == 3 and self.pole[1] == 14) or self.pole[0] == 3 and self.pole[1] in range(0, 14):
            self.pole[1] -= wynik  # ruch na trzecim wierszu
            if (self.pole[1] < 0):
                self.pole[1] = 0
                self.pole[0] += 1
                pomoc = wynik - 1 -(self.pole[1] + kolumna)
                self.pole[1] += pomoc #zejscie z 3 na 4

        elif (self.pole[0] == 4 and self.pole[1] == 0) or (self.pole[0] == 4 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # 4 wiersz
            if self.pole[1] > 14:
                self.pole[1] = 14
                self.pole[0] += 1
                pomoc = wynik - 1 - (self.pole[1] - kolumna)
                self.pole[1] -= pomoc  # zejscie z 4 wiersza na 5

        elif (self.pole[0] == 5 and self.pole[1] == 14) or self.pole[0] == 5 and self.pole[1] in range(0, 14):
            self.pole[1] -= wynik  # 5 wiersz
            if (self.pole[1] < 0):
                self.pole[1] = 0
                self.pole[0] += 1
                pomoc = wynik - 1 -(self.pole[1] + kolumna)
                self.pole[1] += pomoc #zejscie z 5 na 6

        elif (self.pole[0] == 6 and self.pole[1] == 0) or (self.pole[0] == 6 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # 6 wiersz
            if self.pole[1] > 14:
                self.pole[1] = 14
                self.pole[0] += 1
                pomoc = wynik - 1 - (self.pole[1] - kolumna)
                self.pole[1] -= pomoc  # zejscie z 6 wiersza na 7

        elif (self.pole[0] == 7 and self.pole[1] == 14) or self.pole[0] == 7 and self.pole[1] in range(0, 14):
            self.pole[1] -= wynik  # ruch na 7
            if (self.pole[1] < 0):
                self.pole[1] = 0
                self.pole[0] += 1
                pomoc = wynik - 1 -(self.pole[1] + kolumna)
                self.pole[1] += pomoc #zejscie z 7 na 8

        elif (self.pole[0] == 8 and self.pole[1] == 0) or (self.pole[0] == 8 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # 8 wiersz
            if self.pole[1] > 14:
                self.pole[1] = 14
                self.pole[0] += 1
                pomoc = wynik - 1 - (self.pole[1] - kolumna)
                self.pole[1] -= pomoc  # zejscie z 8 wiersza na 9

        elif (self.pole[0] == 9 and self.pole[1] == 14) or self.pole[0] == 9 and self.pole[1] in range(0, 14):
            self.pole[1] -= wynik  # ruch na 7
            if (self.pole[1] < 0):
                self.pole[1] = 0
                self.pole[0] += 1
                pomoc = wynik - 1 -(self.pole[1] + kolumna)
                self.pole[1] += pomoc #zejscie z 9 na 10

        elif (self.pole[0] == 10 and self.pole[1] == 0) or (self.pole[0] == 10 and self.pole[1] in range(1, 15)):
            self.pole[1] += wynik  # ruch na 10
        if self.pole in specjalne_pole:
            self.czy_surowiec = 1
        else:
            self.czy_surowiec = 0
        if self.pionek1 == [0, 0] or self.pionek2 == [0, 0] or other_player.pionek1 == [0, 0] or other_player.pionek2 == [0, 0]:
            self.czy_cofa = 0
        elif self.pionek1 == other_player.pionek1 \
            or self.pionek1 == other_player.pionek2\
            or self.pionek2 == other_player.pionek1\
            or self.pionek2 == other_player.pionek2:
                self.czy_cofa = 1
        else:
            self.czy_cofa = 0
        if pionek == '1':
            self.pionek1 = self.pole
        elif pionek == '2':
            self.pionek2 = self.pole
        self.pole = [0, 0]
        self.czy_rzucone = 0
        current_player = current_player * -1 #zmiana z jednego gracza na drugiego
        return redirect(url_for('gra'))


@app.route('/')
def hello_world():
    return render_template('start.html')


@app.route("/stworzGracza", methods=['GET', 'POST'])
def stworzgracza():
    form = StworzGracza1()
    if form.validate_on_submit():
       global player1
       player1 = Player(name=form.username1.data)
       player1.pole = [0, 0]
       player1.punkty = 0
       player1.pionek1 = [0, 0]
       player1.pionek2 = [0, 0]
       global player2
       player2 = Player(name=form.username2.data)
       player2.pole = [0, 0]
       player2.punkty = 0
       player2.pionek1 = [0, 0]
       player2.pionek2 = [0, 0]
       return redirect(url_for('gra'))
    return render_template('stworzGracza.html', form=form)


@app.route('/odnowa')
def odnowa():
    player1.pionek1 = [10, 0]
    player1.pionek2 = [0, 0]
    player2.pionek1 = [0, 0]
    player2.pionek2 = [0, 0]
    return redirect(url_for('gra'))


@app.route('/karnecofanie/<cofanieid>')
def karnecofanie(cofanieid):
    if cofanieid == '1':
        player1.karnecofanie(player2)
    elif cofanieid == '2':
        player2.karnecofanie(player1)
    return redirect(url_for('gra'))


@app.route('/surowce/<PlayerID>')
def surowce(PlayerID):
    if PlayerID == '1':
        player1.surowce()
    elif PlayerID == '2':
        player2.surowce()
    return redirect(url_for('gra'))


@app.route('/kostka/<PlayerID>')
def kostka(PlayerID):
    if PlayerID == '1':
        player1.kostka()
    elif PlayerID == '2':
        player2.kostka()
    return redirect(url_for('gra'))

@app.route('/ruch/<pionek>/<player>')
def ruch(pionek, player):
    if player == 'pierwszy':
        player1.ruch(pionek, player2)
    elif player == 'drugi':
        player2.ruch(pionek, player1)
    return redirect(url_for('gra'))
@app.route('/gra')
def gra():
    global wygrany
    global przegrany
    if (player1.pionek1[0] == 10 and player1.pionek1[1] >= 14) \
        or (player1.pionek2[0] == 10 and player2.pionek1[1] >= 14) \
        or (player2.pionek1[0] == 10 and player2.pionek1[1] >= 14)\
        or (player2.pionek2[0] == 10 and player2.pionek2[1] >= 14):
            player1.punkty = player1.carbon * 1 + player1.gold * 2 + player1.diamond * 5
            player2.punkty = player2.carbon * 1 + player2.gold * 2 + player2.diamond * 5
            if player1.punkty == player2.punkty:
                return render_template('remis.html', player1=player1, player2=player2)
            elif player1.punkty > player2.punkty:
                wygrany = player1
                przegrany = player2
            elif player2.punkty > player1.punkty:
                wygrany = player2
                przegrany = player1
            return render_template('wygrana.html', player1=player1, player2=player2, wygrany=wygrany, przegrany=przegrany)
    else:
        return render_template('gra.html', player1=player1, player2=player2, wynik=wynik, current_player=current_player)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5126, debug=True)


