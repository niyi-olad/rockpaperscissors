# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def rockScissors():
    # [assignment] Add your code here

    import random
    choicelist = ['R', 'P', 'S']
    playerChoice = ''
    cpuChoice = ''

    while playerChoice == cpuChoice:

       while playerChoice not in choicelist:
          playerChoice = input (' Pick an option between R for Rock, P for Paper  or  S for Scissors  ').upper()
       cpuChoice = random.choice (choicelist)
       if cpuChoice == 'R': 
         fcpuChoice = 'Rock'
       elif cpuChoice == 'P':
         fcpuChoice = 'Paper'
       else:
         fcpuChoice = 'Scissors'

       if playerChoice == 'R': 
        fplayerChoice = 'Rock'
       elif playerChoice == 'P':
        fplayerChoice = 'Paper'
       else:
        fplayerChoice = 'Scissors'
    
       print (' Player ( ' + fplayerChoice  + ') : CPU (' + fcpuChoice + ')' )

       if playerChoice == cpuChoice:
        print ('The result is a tie !  \n') 
           #Pick an option between R for Rock, P for Paper  or  S for Scissors')
        playerChoice = ''
        cpuChoice    = ''
       elif (playerChoice == 'R' and cpuChoice == 'P')  or (playerChoice == 'P' and cpuChoice == 'S'):
        print ('Computer Wins !')
       else:
        print ('Player Wins !')
    
    return True
     
    #return True

rockScissors()



