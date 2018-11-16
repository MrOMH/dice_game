from random import randint
import sys

def throws_to_ordinal( number ):#returns 1st for 1 ...
    n = number
    x = lambda n: "%d%s" %(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10, "th"))
    if number == 0:
        return 'Zero'
    else:
        return x(number)

def prompt( query ):
          
    reply = input( query )
        
    if reply =='r' or reply == 'yes':
        return True
    else:
        return False
    
def scores( score , throws ):
    
    vocab_points = 'points'
    
    if score == 1:
        vocab_points = 'point'
    else:
        vocab_points = 'points'
    
        
    return 'you have '+str(score) +' '+ vocab_points+ ' after your '+throws_to_ordinal(throws) +' throw!'
    
       
def check_python_version():
    
    #check python version before accepting any input.
    
    if sys.version_info < (3,0):
        sys.stdout.write ('\n\nPlease run with version 3 or higher\n\n')
        
        sys.exit( 'Bye!' )
    else:
        return

#the roll_dice() simulates the actual rolling and returns a number, respective to the face
def roll_dice():
    
    return randint(1,10)
    
def main():
   
    check_python_version()
       
    print ('Welcome to dice rolling game!\n Your dice got 10 faces\n To Play:')
    
    player_count = input('Please reply with 1 for single player and 2 for two players')
    
    if int(player_count) > 1 :
        
        print ('Assuming 2 players on board...')
        
    user_response = input('Reply with \'r\' to roll,\'e\' to exit: ')
    
    
    
    score_after_throw = 0
    
    throws = 0
    
    secondplayer_score_after_throw = 0
    
    secondplayer_throws = 0
    
    if user_response == 'r' or user_response == 'yes':
        
        new_score = roll_dice()
        
        score_after_throw = score_after_throw + new_score
        
        throws += 1
        
        print ('Dice face up: ' + str(new_score))
        
        print(scores(score_after_throw,throws))
    else:
        print('Bye!, Exiting...')
        sys.exit(0)
    
    while True:    
        replay_game  =  prompt('Like to roll again?  ')
    
        if replay_game:
            
            new_score_rerun = roll_dice()
            
            score_after_throw = score_after_throw + new_score_rerun
            
            throws += 1
            
            print('Dice face up: ' +str(new_score_rerun) )
            
            print(scores(score_after_throw,throws))
            
        else:
            print('Bye!')
            sys.exit(0)
    
if __name__ == '__main__':
    main()