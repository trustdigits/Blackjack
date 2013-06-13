from random import choice

class BJ:

    def __init__(self): 
        self.init()

    def init(self):
        self.lst  = [6,7,8,9,10,10,10,10,10,11]
        self.lst += self.lst
        self.lst += self.lst
        self.your_hand = [self.random_gen(), self.random_gen()]
        self.dealer_hand = [self.random_gen(), self.random_gen()]
        self.ace()

    def random_gen(self):
        indx = choice(range(len(self.lst)))
        rd = self.lst[indx]
        self.lst = self.lst[:indx] + self.lst[indx+1:]
        return rd

    def getHands(self):
        return [self.your_hand, self.dealer_hand]
    
    def play(self):
        print("Welcome to Alex's awesome BlackJack \n")
        self.print_your_hand()
        print("Dealer: "+  str(self.dealer_hand[0]) + ", * \n")

        if(self.validate_game()):
            return
        
        self.hit_or_stand()


    def ace(self):
        if(self.your_hand[0] == 11 and self.dealer_hand[1] == 11 ):
            self.your_hand[0] = 1
        
    def print_your_hand(self):
        str_ = "You: "
        k=0
        for i in self.your_hand:
            str_ += str(i)
            if(k < len(self.your_hand)-1):
                str_ += ", "
            k+=1
            
        print(str_)
        
    def black_jack(self):

        print("Dealer's hidden card was ", self.dealer_hand[1])
        print("Your score is ", sum(self.your_hand))
        print("Dealer's score is " + str(sum(self.dealer_hand)) + "\n" )
        
        if(self.validate_game()):
            return
        
        if(sum(self.your_hand) < sum(self.dealer_hand)):
            print("YOU LOST :0(\n")
        else:
            print("YOU WON!!!!!!!\n")

    def validate_game(self):
        
        if(self.test_equal()):
            return True

        if(sum(self.your_hand) == 21):
            print("YOU WON, YOU HIT BLACK JACK!!!!!!!\n")
            return True
        elif(sum(self.dealer_hand) == 21):
            print("YOU LOST, DEALER HIT BLACK JACK :0( \n")
            return True
        elif(sum(self.your_hand) > 21):
            print("GAME OVER, BUST! YOU LOST :0( \n")
            return True
        elif(sum(self.dealer_hand) > 21):
            print("GAME OVER, BUST! YOU WIN \n")
            return True

        return False
        
    def test_equal(self):
        if(sum(self.dealer_hand) == sum(self.your_hand)):
            print("Dealer's hidden card was ", self.dealer_hand[1])
            print("Your score is ", sum(self.your_hand))
            print("Dealer's score is " + str(sum(self.dealer_hand)) + "\n" )
            mydata = input('PUSH! You and dealer hit same score, let\'s play again...\n')
            self.init()
            self.play()
            return True
         

    def hit_or_stand(self):
        hs = input('Hit (H) or Stand (S)?  ')
        print("")
        if(hs == 'H'):
            self.your_hand = self.your_hand + [self.random_gen()]
            self.print_your_hand()
            print("Dealer: "+  str(self.dealer_hand[0]) + ", " + str(self.dealer_hand[0]))
            print("")
            self.hit_or_stand()
        elif(hs == 'S'):
            self.black_jack()
        else:
            print('You should press H or S to Hit or Stand')
            self.hit_or_stand()
            
 
while True:
    bj = BJ()
    bj.play()
    mydata = input('Want to play again? Press ENTER key...')


 
      
 
