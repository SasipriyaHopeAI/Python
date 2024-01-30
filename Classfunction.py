class ArtificialIntelligence():
    def Subfields():
        a="Machine Learning"
        b="Neural Networks"
        c="Vision"
        d="Robotics"
        e="Speech Processing"
        f="Natural Language Processing"
        lists=[a,b,c,d,e,f]
        AI=input("Sub-fields in AI are")
        for message in lists:
            print(message)
            
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
            message=(num, "is Even number")
        else:
            print(num,"is Odd number")
            message=(num, "is Odd number")
        return message
            
    def Eligibility():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=='Male' and Age>21):
            print("Eligible")
            message="Eligible"
        elif(Gender=='Female' and Age>18):
            print("Eligible")
            message="Eligible"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        return message
    
    def percentage():
        Sub1=int(input("Subject1= "))
        Sub2=int(input("Subject2= "))
        Sub3=int(input("Subject3= "))
        Sub4=int(input("Subject4= "))
        Sub5=int(input("Subject5= "))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total : ",Total)
        Percent=Total/5
        print("Percentage : ",Percent)
        
    def triangle():
        Ht=int(input("Height:"))
        Br=int(input("Breadth:"))
        Area=(Ht*Br)/2
        print("Area of Triangle:",Area)
        Ht1=int(input("Height1:"))
        Ht2=int(input("Height2:"))
        Br1=int(input("Breadth1:"))
        Peri=Ht1+Ht2+Br1
        print("Perimeter of Triangle: ",Peri)