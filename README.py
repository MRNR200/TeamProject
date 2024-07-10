# TeamProject
#backend is :
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

#frontend is :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Computer" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test js</title>
    
    <!-- <script>
     alert("hello golpesar")
     
    </script> -->
<style>
*{
    background-color: rgb(88, 169, 142);
}
</style>
</head>
<body>
    <h2><center>Test JAVA project </center></h2>
</body>
</html>

#in develop marge

# Devops has :
#!/bin/bash
echo "plz tell me name:"
read name

echo " hi $name! welcome."
