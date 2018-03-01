def hm():
    word = raw_input('what is the word ')
    guess=''
    for i in range(5):
        output=''
        guess += raw_input('what is your guess ')
        for letter in word:
            if letter ==' ':
                output += ' '
                continue
            if letter in guess:
                output+=letter
            else: 
                output += '-'
        print (output)
        if output == word:
            print ('finsh')
            hm()
