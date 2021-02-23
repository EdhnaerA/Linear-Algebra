def semestralgrades():

    print ("Enter your name:")
    name = str (input())

    print ("Enter your course:")
    course = str (input())

    print("Enter Prelim Grade:")
    prelimgrades = int (input())

    print("Enter Midterm Grade:")
    midtermgrades = int (input())

    print("Enter Final Grade:")
    finalgrades = int (input())

    sum=(prelimgrades+midtermgrades+finalgrades)
    avge=sum/3


    print ("Your Final Grade Average is:" +str(avge))
    print ("Remarks:")

    Happy = ('\U0001F600:>' + 'Good job! You deserve it!' )
    Laugh = ('\U0001F606:/' + 'I knew you can do it! Good job!')
    Sad = ("\U0001F62D :<" + 'Never give up!')

    if avge > 70:
        print(""+ Happy)
    elif avge == 70:
       print(""+ Laugh)
    else:
        print(""+ Sad)
    return avge


semestralgrades()
