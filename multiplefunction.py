class multiplefunction():
            def subfieldsInAI():
                print("Sub-fields in AI are:")
                Lists = ["Machine Learning", "natural network", "vision", "Robatics", "speech processing", "natural language processing"]
                for AI in Lists:
                    print(AI)
        
            def My_number():
                num=int(input("Enter the number:"))
                if(num%2==0):
                    print(num,"is Even number")
                else:  
                    print(num,"is Odd Number")
        
            def MY_Function():
                gender = input("Your Gender:")
                age = int(input("your age:"))
                if gender == 'Male' and age>=21:
                    print("Elegible")
                elif gender == 'Female' and age>=18:
                    print("Elegible")
                else:
                    print("Not Elegible")

            def My_subject():
                sub1 = int(input("Subject1="))
                sub2 = int(input("subject2="))
                sub3 = int(input("subject3="))
                sub4 = int(input("subject4="))
                sub5 = int(input("subject5="))
                total = (sub1+sub2+sub3+sub4+sub5)
                print("Total:",total)
                per = float(total)*(100/500)
                print("prrcentage:",per)
                
            def Triangle():
                Height=int(input("Height:"))
                Breadth=int(input("Breadth:"))
                a=(Height*Breadth)/2
                print("Area fomula:(Height*Breadth)/2")
                print("Area of triangle:",a)
                Height1=int(input("Height1:"))
                Height2=int(input("Height2:"))
                Breadth=int(input("Breadth:"))
                g=(Height1+Height2+Breadth)
                print("Perimeter formula:Height1+Height2+Breadth")
                print("perimeter of Triangle:", g) 