import random 
javab = random.randint(1,99)
name = input('what is your name?  ')
hads = input('what answer?  ')
hads = int(hads)
attempt=0
while hads != javab:
    if javab > hads:
        print('I am bigger =/')
    else:
        print('I am smaller =/')
        
    hads = input('what answer?  ')
    hads = int(hads)
    attempt+=1
    if attempt==5:
        print ('Game Over ):')
        exit()
    
print('Wooooooooooow', name ,'you did it :))))')
