q1="""Who has the highest fanbase?
a.Prabas
b.Mahesh Babu
c.Pawan Kalyan
d.Ntr"""
q2="""What is most liked sport in India?
a.Basketball
b.Cricket
c.Football
d.Hockey"""
q3="""Who is the Caption of our Indian Cricket Team?
a.Hardik Pandya
b.Rohit Sharma
c.Dhoni
d.Virat Kohli"""
q4="""What is the most loved mobile brand?
a.Samsung
b.Nokia
c.Oppo
d.Apple"""
q5="""Who won the 2011 International Cricket Oneday World Cup?
a.India
b.England
c.Sri Lanka
d.Australia"""
questions={q1:"c",q2:"b",q3:"b",q4:"d",q5:"a"}
name=input("enter your name: ")
print("Hello",name," Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques (yes/no): ")
    if flag1=="yes":
        continue
    ans=input("Enter your answer: ")
    if ans==questions[i]:
        print("Wow! Your answer is correct")
        score=score+1
        print("Your score is: ",score)
    else:
        print("Your answer was wrong")
        score=score-1
        print("Your current score is: ",score)
    flag2=input("Do you want to quit the game (yes/no): ")
    if flag2=="yes":
        break
print("Thank You for playing the quiz")
print("Your total score is: ",score)
