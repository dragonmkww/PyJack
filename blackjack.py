from random import randint
import cools as cl
import seven
from turtle import*
from time import sleep
class Dealer(cl.Player):
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.position=[-395,-235,-75,85,245,405,565,725]
        self.offset=350
        self.faceup=[False,True,True,True,True,True,True,True]
        return
    def play(self):
        self.hand[0].drawing.face=True
        seven.move(self.position[0],self.offset)
        self.hand[0].show()
        score(mrhouse,-250,100)
        sleep(1)
        while count(bob)>count(mrhouse) and count(bob)<22 and not (count(bob)==21 and len(bob.hand)==2):
            mrhouse.draw(deck,1)
            score(mrhouse,-250,100)
            sleep(1)
        if (count(bob)-count(mrhouse)>0 and count(bob)<22) or (count(bob)==21 and len(bob.hand)==2) or (count(bob)<22 and count(mrhouse)>21):
            seven.move(-555,-55)
            color('lime')
            write('YOU WON! :)',False,align='left',font=('courier',45,'bold'))
            chips.chips_val+=len(chips.pot1)+10*len(chips.pot10)+50*len(chips.pot50)+100*len(chips.pot100)
        else:
            seven.move(-555,-55)
            color('red')
            write('YOU LOST! :(',False,align='left',font=('courier',45,'bold'))
            chips.chips_val-=len(chips.pot1)+10*len(chips.pot10)+50*len(chips.pot50)+100*len(chips.pot100)
        chips.clean_chips()
        sleep(1)
        return
class Chips:
    def __init__(self,ant):
        self.chips_val=ant
        self.chips1=[]
        self.pot1=[]
        self.chips10=[]
        self.pot10=[]
        self.chips50=[]
        self.pot50=[]
        self.chips100=[]
        self.pot100=[]
        self.all_chips=[self.chips1,self.chips10,self.chips50,self.chips100]
        self.all_pot=[self.pot1,self.pot10,self.pot50,self.pot100]
        return
    def clicky1(self,x,y):
        if y<80:
            q=self.chips1.pop()
            q.goto(randint(500,740),randint(130,270))
            self.pot1.append(q)
        else:
            q=self.pot1.pop()
            q.goto(740,0)
            self.chips1.append(q)
        mr_krabs(self)
        update()
        return
    def clicky10(self,x,y):
        if y<80:
            q=self.chips10.pop()
            q.goto(randint(500,740),randint(150,300))
            self.pot10.append(q)
        else:
            q=self.pot10.pop()
            q.goto(660,0)
            self.chips10.append(q)
        mr_krabs(self)
        update()
        return
    def clicky50(self,x,y):
        if y<80:
            q=self.chips50.pop()
            q.goto(randint(500,740),randint(150,300))
            self.pot50.append(q)
        else:
            q=self.pot50.pop()
            q.goto(580,0)
            self.chips50.append(q)
        mr_krabs(self)
        update()
        return
    def clicky100(self,x,y):
        if y<80:
            q=self.chips100.pop()
            q.goto(randint(500,740),randint(150,300))
            self.pot100.append(q)
        else:
            q=self.pot100.pop()
            q.goto(500,0)
            self.chips100.append(q)
        mr_krabs(self)
        update()
        return           
    def give_chips(self):
        v=self.chips_val
        while v>=300:#makes $100 chips
            chip100=Turtle()
            chip100.seth(90)
            chip100.shape('circle')
            chip100.color('gold')
            chip100.turtlesize(4,4,4)
            chip100.pu()
            chip100.goto(500,0)
            chip100.onclick(self.clicky100)
            self.chips100.append(chip100)
            v-=100  
        while v>=100:#makes $50 chips
            chip50=Turtle()
            chip50.seth(90)
            chip50.shape('circle')
            chip50.color('blue')
            chip50.turtlesize(4,4,4)
            chip50.pu()
            chip50.goto(580,0)
            chip50.onclick(self.clicky50)
            self.chips50.append(chip50)
            v-=50  
        while v>=20:#makes $10chips
            chip10=Turtle()
            chip10.shape('circle')
            chip10.color('green')
            chip10.turtlesize(4,4,4)
            chip10.pu()
            chip10.onclick(self.clicky10)
            self.chips10.append(chip10)
            chip10.goto(660,0)
            v-=10  
        while v>0:#makes $1 chips
            chip1=Turtle()
            chip1.shape('circle')
            chip1.turtlesize(4,4,4)
            chip1.pu()
            chip1.goto(740,0)
            chip1.onclick(self.clicky1)
            self.chips1.append(chip1)
            v-=1
        update()
        return
    def clean_chips(self):
        for i in self.all_chips:
            for j in i:
               j.hideturtle()
            i[:]=[]    
        for i in self.all_pot:
            for j in i:
                j.hideturtle()
            i[:]=[]
        return
mrhouse=Dealer('Mr. house')
bob=cl.Player('bob')
deck=cl.Deck()
chips=Chips(5*10**2)
def start123():
    seven.move(-680,380)
    color('black','orange')
    seven.move(xcor()+6,ycor())
    width(4)
    begin_fill()
    for Φ in range(2):
        fd(138)
        for r in range(90):
            fd(0.105)
            rt(1)
        fd(208)
        for e in range(90):
            fd(0.105)
            rt(1)
    end_fill()
    seven.move(xcor()-6,ycor())
    seven.move(-635,120)
    color('orange')
    write('Hit',False,align='left',font=('courier',24,'bold'))
    seven.move(-840,350)
    color('orange')
    begin_fill()
    for i in range(4):
        fd(120)
        for s in range(90):
            rt(1)
            fd(0.15)
    end_fill()
    seven.move(-830,270)
    color('black')
    write('Stand',False,align='left',font=('courier',24,'bold'))
    for i in range(len(bob.hand)):
        deck.cards.append(bob.hand.pop())
    for i in range(len(mrhouse.hand)):
        deck.cards.append(mrhouse.hand.pop())
    deck.shuffle()
    chips.clean_chips()
    chips.give_chips()
    mr_krabs(chips)
    #betting
    t=10
    while t>0:
        seven.move(-250,-10)
        write('Time left to bet:{}'.format(t),False,align='left',font=('courier',30,'bold'))
        sleep(1)
        t-=1
        color(53,55,0)
        seven.move(-250,40)
        begin_fill()
        for s in range(2):
            fd(450)
            rt(90)
            fd(50)
            rt(90)
        end_fill()
        color('orange')
    for b in chips.all_chips:
        for c in b:
            c.onclick(None)
    for m in chips.all_pot:
        for l in m:
            l.onclick(None)
    bob.draw(deck,2)
    mrhouse.draw(deck,2)
    score(bob,-740,-100)
    win_lose()
    print(count(bob))
    return
def win_lose():
    sleep(0.5)
    if count(bob)==21:
        print('Blackjack! :)')
        mrhouse.play()
        clear()
        start123()
    elif count(bob)>21:
        print('YOU LOSE! :(')
        mrhouse.play()
        clear()
        start123()
    else:
        pass
    return
def clicky(x,y):
    Screen().onclick(None)
    if x>-680 and x<-530 and y<380 and y>160 and len(bob.hand)<11 and count(bob)<21:
        bob.draw(deck,1)
        print(count(bob))
        score(bob,-740,-100)
        win_lose()
    if x>-840 and x<-720 and y<350 and y>230:
        print('Stand')
        mrhouse.play()
        clear()
        start123()
    Screen().onclick(clicky)
    return
Screen().onclick(clicky)
pen=Turtle()
pen.color('white')
pen.hideturtle()
def score(Player,x,y):
    color(53,55,0)
    seven.move(x,y)
    begin_fill()
    for i in range(4):
        fd(50)
        rt(90)
    end_fill()
    color('white')
    seven.move(x,y-35)
    write(count(Player),False,align='left',font=('courier',23,'bold'))
    return
def mr_krabs(Chips):
    seven.move(350,350)
    color(53,55,0)
    begin_fill()
    for i in range(4):
        fd(100)
        rt(90)
    end_fill()
    color('orange')
    seven.move(350,300)
    pot_chips=len(Chips.pot1)+10*len(Chips.pot10)+50*len(Chips.pot50)+100*len(Chips.pot100)
    write('${}'.format(pot_chips),False,align='left',font=('courier',30,'bold'))
    seven.move(350,50)
    color(53,55,0)
    begin_fill()
    for i in range(4):
        fd(100)
        rt(90)
    end_fill()
    color('orange')
    seven.move(350,0)
    player_chips=len(Chips.chips1)+10*len(Chips.chips10)+50*len(Chips.chips50)+100*len(Chips.chips100)
    write('${}'.format(player_chips),False,align='left',font=('courier',30,'bold'))
def count(Player):
    num=0
    aces=0
    for w in Player.hand:
        if w.value>1 and w.value<11:
             num+=w.value
        elif w.value>10:
             num+=10
        else:
            num+=11
            aces+=1
        while aces>0:
            if num>21:
                num-=10
            aces-=1
    return num
start123()