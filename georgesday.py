import turtle

num = -1
while (num != 0):
    print("                                          ......... , . - . - , _ , .........")
    print("                                          ......... ) ` - . .> ' `( .........")
    print("                                          ........ / . . . .`.. . . .. ......")
    print("                                          ........ |. . . . . |. . .| .......")
    print("                                          ......... .. . . . ./ . ./ ........")
    print("                                          ........... `=(.. /.=` ............")
    print(" ======= Saint George's DAY ========      ............. `-;`.-' .............")
    print("-------------------------------------     ............... `)| ... , .........")
    print("|1 --> characters of the history    |     .................|| _.-'| .........")
    print("|2 --> story explanation            |     ............. , _|| .._, / ........")
    print("|3 --> what we do in Catalonia?     |     ....... . ..... .|| .' ............")
    print("|4 --> the author of this programm  |     .... ... |.. , . ||/ ..............")
    print("|                                   |     . ..... | /|., |Y.., ..............")
    print("|0 --> Exit this program            |     .........'-._....||/ ..............")
    print("-------------------------------------     ........ >_.-`...|| ...............")
    print("                                          .................|| ...............")
    print("                                          .................|| ...............")
    print("                                          .................|| ...............")
    print("                                          .................|| ...............")
    print("                                          .................|/ ...............")
    print("                                          ...................................")
    print()
    num = int(input("What do you want to see? "))

    if(num == 1):
        print()
        print(f"There are only three main charaacters:")
        print(f"1 --> The knight George")
        print(f"2 --> The Princess")
        print(f"3 --> The enemy Dragon")
        print()
    elif(num == 2):
        print()
        print(f"According to legend, Saint George saved the princess by killing the dragon that left a flower on his body.")
        print(f"That is why some consider it to be the Catalan Saint Valentine, because Saint George is said to be the patron") 
        print(f"saint of lovers in Catalonia.")
        print()
    elif(num == 3):
        print()
        print(f"Here in Barcelona, boys give a rose to girls and the girls give a book to them")
        print()
    elif(num == 4):
        print()
        print(f"This program is made by Narcís Gómez (a19nargomcar@inspedralbes.cat)")
        print(f"♥ I really enjoy working out with Python ♥")
        print()
    elif(num == 0):
        print(f"Thanks for using my preject, cheers!.")
        # Set initial position
        nar = turtle.Turtle()
        wn = turtle.Screen()
        turtle.colormode(255)
        wn.bgcolor(158,155,122)
        wn.title("Saint George's Day")
        nar.penup ()

        nar.left (90)
        nar.fd (200)
        nar.pendown ()
        nar.right (90)
                
        # flower base
        nar.fillcolor ("red")
        nar.begin_fill ()
        nar.circle (10,180)
        nar.circle (25,110)
        nar.left (50)
        nar.circle (60,45)
        nar.circle (20,170)
        nar.right (24)
        nar.fd (30)
        nar.left (10)
        nar.circle (30,110)
        nar.fd (20)
        nar.left (40)
        nar.circle (90,70)
        nar.circle (30,150)
        nar.right (30)
        nar.fd (15)
        nar.circle (80,90)
        nar.left (15)
        nar.fd (45)
        nar.right (165)
        nar.fd (20)
        nar.left (155)
        nar.circle (150,80)
        nar.left (50)
        nar.circle (150,90)
        nar.end_fill ()
                
                # Petal 1
        nar.left (150)
        nar.circle (-90,70)
        nar.left (20)
        nar.circle (75,105)
        nar.setheading (60)
        nar.circle (80,98)
        nar.circle (-90,40)
                
                # Petal 2
        nar.left (180)
        nar.circle (90,40)
        nar.circle (-80,98)
        nar.setheading (-83)
                
                # Leaves 1
        nar.fd (30)
        nar.left (90)
        nar.fd (25)
        nar.left (45)
        nar.fillcolor ("green")
        nar.begin_fill ()
        nar.circle (-80,90)
        nar.right (90)
        nar.circle (-80,90)
        nar.end_fill ()
        nar.right (135)
        nar.fd (60)
        nar.left (180)
        nar.fd (85)
        nar.left (90)
        nar.fd (80)
                
                # Leaves 2
        nar.right (90)
        nar.right (45)
        nar.fillcolor ("green")
        nar.begin_fill ()
        nar.circle (80,90)
        nar.left (90)
        nar.circle (80,90)
        nar.end_fill ()
        nar.left (135)
        nar.fd (60)
        nar.left (180)
        nar.fd (60)
        nar.right (90)
        nar.circle (200,60)
        nar.left(20)


        #Nombre
        nar.color('red')
        nar.forward(5)
        nar.left(90)
        nar.forward(90)
        nar.right(155)
        nar.forward(90)
        nar.left(155)
        nar.forward(90)
        nar.backward(90)
        nar.right(90)

        nar.forward(10)

        nar.color('white')
        nar.left(75)
        nar.forward(80)
        nar.right(150)
        nar.forward(80)
        nar.backward(40)
        nar.right(120)
        nar.forward(30)
        nar.backward(30)
        nar.left(120)
        nar.forward(40)
        nar.left(75)

        nar.forward(10)

        nar.color('red')
        nar.left(90)
        nar.forward(80)
        nar.right(90)
        nar.forward(35)
        nar.right(90)
        nar.forward(35)
        nar.right(90)
        nar.forward(35)
        nar.left(140)
        nar.forward(75)
        nar.left(40)

        nar.forward(10)

        nar.color('white')
        nar.forward(50)
        nar.backward(60)
        nar.left(90)
        nar.forward(80)
        nar.right(90)
        nar.forward(40)
        nar.backward(40)
        nar.right(90)
        nar.forward(80)
        nar.left(90)
        nar.forward(50)

        nar.forward(10)

        nar.color('red')
        nar.forward(50)
        nar.backward(30)
        nar.left(90)
        nar.forward(80)
        nar.right(90)
        nar.forward(30)
        nar.backward(60)
        nar.forward(30)
        nar.right(90)
        nar.forward(80)
        nar.left(90)

        nar.forward(10)

        nar.color('white')
        nar.forward(75)
        nar.left(90)
        nar.forward(40)
        nar.left(90)
        nar.forward(50)
        nar.right(90)
        nar.forward(40)
        nar.right(90)
        nar.forward(50)

        nar.color(158,155,122)
        nar.forward(4000)
    else:
        print(f"This number is not appropriate, try it again...")