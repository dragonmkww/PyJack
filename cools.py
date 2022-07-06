from random import randint
import seven
class Card:    
    def __init__(self,suit,val):
        self.suit=suit
        self.value=val
        self.drawing=seven.Card_d(suit,val)
        return    
    def show(self):
        print('{} of {}'.format(self.drawing.values[self.value],self.drawing.suits[self.suit]))
        self.drawing.draw_f()
        return  
class Deck:    
    def __init__(self):
        self.cards=[]
        self.build()
        return    
    def build(self):
        for s in range(0,4):
            for v in range(1,14):
                self.cards.append(Card(s,v))
        return       
    def show(self):
        for c in self.cards:
            c.show()
        return    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
        return    
    def draw_card(self):
        return self.cards.pop()    
class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.offset=-165
        self.faceup=[True,True,True,True,True,True,True,True,True,True,True]
        self.position=[-875,-715,-555,-395,-235,-75,85,245,405,565,725]
        return
    def draw(self,deck,n=1):
        for c in range(n):
            self.hand.append(deck.draw_card())
            lastcard=len(self.hand)-1
            seven.move(self.position[lastcard],self.offset)
            self.hand[lastcard].drawing.face=self.faceup[lastcard]
            self.hand[lastcard].show()
        return
#     def show_hand(self):
#         print("{}'s hand:".format(self.name))
#         for (card,pos) in zip(self.hand,self.position):
#             seven.move(pos,-165)
#             card.show()
#         return
    def discard(self):
        return self.hand.pop()