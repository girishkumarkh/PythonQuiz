import Tkinter as tk
import tkMessageBox
from Tkinter import *
from Response import Response
from PIL import Image, ImageTk



class logicreason(Frame):
    #GUI Setup

    def __init__(self, master):
        #Initialise Questionnaire Class

        Frame.__init__(self, master, bg="white")
        self.pack(side='bottom', expand='no')
        self.createProgSelect()
        self.Answers()
        self.radio()
        self.button()
        self.clearResponse()
        self.pictureqt()

       
    def pictureqt(self):
        canvasqt.pack(side='top', expand='no')
        #canvas.grid(row=0, column=4, sticky= E)
        #a=2
        #canvas.pack(side='top', expand='yes')
    def fpic(self):
        global pic
        global butSubmit
        global butSkip
        canvasqt.pack_forget()
        canvasq1.pack_forget()
        canvasq2.pack_forget()
        canvasq3.pack_forget()
        butSubmit.grid_forget()
        butSkip.grid_forget()
        pic = pic + 1
        print pic
        

        
    def pictureq1(self):
        canvasq1.pack(side='top', expand='no')
        
    def pictureq2(self):
        canvasq2.pack(side='top', expand='no')
        
    def pictureq3(self):
        canvasq3.pack(side='top', expand='no')
        
    def createProgSelect(Frame):
        
        lblProg = Label(Frame, text='Your Answer:', font=('ms', 18,'bold'))
        lblProg.grid(row=1, column=0, sticky=NE,columnspan = 2)

    
    def Answers(self):
        lblProg = Label(self, text = 'A)', font=('ms',12,'bold'))
        lblProg.grid(row=2,column= 3,)

        lblStrAgr = Label(self, text = 'B)', font=('ms',12,'bold'))
        lblStrAgr.grid(row=2,column= 5,)

        lblStrAgr = Label(self, text = 'C)', font=('ms',12,'bold'))
        lblStrAgr.grid(row=2,column= 9,)

        lblStrAgr = Label(self, text = 'D)', font=('ms',12,'bold'))
        lblStrAgr.grid(row=2,column= 13,)

     #The radio buttons   
    def radio(self):
        self.varQ1 = IntVar()
        R1Q1 = Radiobutton(self, variable=self.varQ1, value=1)
        R1Q1.grid(row=2,column= 4)

        
        R2Q1 = Radiobutton(self, variable=self.varQ1, value=2)
        R2Q1.grid(row=2,column= 7)

        
        R3Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        R3Q1.grid(row=2 ,column= 11)

        
        R3Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R3Q1.grid(row=2 ,column= 15)

        
    def submit(self):
        global butSubmit
        global butSkip
        butSubmit= Button(self, text='Submit',font=('MS', 8,'bold'))
        butSkip= Button(self, text='Skip',font=('MS', 8,'bold'))
        if pic == 0:
            butSubmit['command']= self.first
            print "submit one created"
            butSkip['command']= self.sfirst
            print "skip one created"
        elif pic == 1:
            butSubmit['command']= self.second
            print "submit two created"
            butSkip['command']= self.ssecond
            print "skip two created"
        elif pic == 2:
            butSubmit['command']= self.third
            print "submit three created"
            butSkip['command']= self.sthird
            print "skip three created"
        elif pic == 3:
            butSubmit['command']= self.forth
            print "submit four created"
            butSkip['command']= self.sforth
            print "skip four created"
            
        butSubmit.grid(row=20, column=1, columnspan=2)
        butSkip.grid(row=20, column=5, columnspan=2)

    def button(self):     
        self.submit()
        butReset= Button(self, text='Reset',font=('MS', 8,'bold'))
        butReset['command']=self.clearResponse
        butReset.grid(row=20, column=3, columnspan=2)

    def clearResponse(self):
        self.varQ1.set(0)

    # submit button pressed for Question 1
    def first(self):
        if (self.varQ1.get() == 0):
            tkMessageBox.showwarning(title="Errow !",message=" please select your answer and try again")
        else:
            self.storeResponsept()
            self.fpic()
            self.submit()
            self.pictureq1()
        
    # submit button pressed for Question 2    
    def second(self):
        if (self.varQ1.get() == 0):
            tkMessageBox.showwarning(title="Errow !",message=" please select your answer and try again")
        else:
            self.storeResponseq1()
            self.fpic()
            self.submit()
            self.pictureq2()
        
    # submit button pressed for Question 3    
    def third(self):
        if (self.varQ1.get() == 0):
            tkMessageBox.showwarning(title="Errow !",message=" please select your answer and try again")
        else:
            self.storeResponseq2()
            self.fpic()
            self.submit()
            self.pictureq3()
        
    # submit button pressed for Question 4    
    def forth(self):
        if (self.varQ1.get() == 0):
            tkMessageBox.showwarning(title="Errow !",message=" please select your answer and try again")
        else:
            self.storeResponseq3()
            self.fpic()
            self.feedb1()
            #self.submit()

    # Skip button pressed for Question 1
    def sfirst(self):
        tkMessageBox.showwarning(title="Alert !",message="You are now skiping the question")
        #self.storeResponsept()
        self.clearResponse()
        self.fpic()
        self.submit()
        self.pictureq1()
        
    # Skip button pressed for Question 2    
    def ssecond(self):
        tkMessageBox.showwarning(title="Alert !",message="You are now skiping the question")
        #self.storeResponseq1()
        self.clearResponse()
        self.fpic()
        self.submit()
        self.pictureq2()
        
    # Skip button pressed for Question 3    
    def sthird(self):
        tkMessageBox.showwarning(title="Alert !",message="You are now skiping the question")
        #self.storeResponseq2()
        self.clearResponse()
        self.fpic()
        self.submit()
        self.pictureq3()
        
    # Skip button pressed for Question 4    
    def sforth(self):
        tkMessageBox.showwarning(title="Alert !",message="Sorry, There is nothing to skip !")
        self.clearResponse()
        self.fpic()
        self.feedb1()
        #self.storeResponseq3()
        #self.submit()
    
    def storeResponsept(self):

        if (self.varQ1.get() == 0):
           print "You need to answer Questions to Continue for PT"              
        #check correct answers    
        elif self.varQ1.get() == 3:
            ans = "The Practice Question is answered CORRECTLY"
            print "The Practice Question is answered CORRECTLY"
        else:
            ans = "The Practice Question is answered INCORRECTLY"
            print "The Practice Question is answered INCORRECTLY"
        if (self.varQ1.get() != 0):
            tkMessageBox.showinfo(title="Your Result !",message="%s press ok to continue"%(ans))
        self.varQ1.set(0)

    def storeResponseq1(self):
        global lans1
        
        if (self.varQ1.get() == 0):
            print "You need to answer Questions to Continue for PT"
         #check correct answers    
        elif self.varQ1.get() == 1:
            print "The Question 1 is answered CORRECTLY"
            lans1 = "CORRECT"   # saving the User's Answers to a object
        else:
            print "The Question 1 is answered INCORRECTLY"
            lans1 = "INCORRECT"
        self.varQ1.set(0)

    def storeResponseq2(self):

        global lans2
        
        if (self.varQ1.get() == 0):
            print "You need to answer Questions to Continue for PT"
         #check correct answers    
        elif self.varQ1.get() == 2:
            print "The Question 2 is answered CORRECTLY"
            lans2 = "CORRECT"
        else:
            print "The Question 2 is answered INCORRECTLY"
            lans2 = "INCORRECT"
        self.varQ1.set(0)

    def storeResponseq3(self):

        global lans3
        
        if (self.varQ1.get() == 0):
            print "You need to answer Questions to Continue for PT"
         #check correct answers    
        elif self.varQ1.get() == 3:
            print "The Question 3 is answered CORRECTLY"
            lans3 = "CORRECT"
        else:
            print "The Question 3 is answered INCORRECTLY"
            lans3 = "INCORRECT"
        tkMessageBox.showinfo(title="Success !",message="You Have COP Quiz")
        self.varQ1.set(0)
    
    def feedb1(self):
        global app
        app.destroy()
        app = feedback1(root)

class Main_Menu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        global lans1
        global lans2
        global lans3
        global ldegree
        lans1 = ""
        lans2 = ""
        lans3 = ""
        ldegree = ""
        self.pack(side='bottom', expand='no')
        self.grid()
        self.createButtons()
        
    def exit1(self):
        print 'You Have Exited The Program'
        root.destroy()

    def createButtons(self):
        global app
        lblProb1 = Label(self, text='Main Menu', font=('MS', 21,'bold'))
        lblProb1.grid(row=1, column =1, padx=40, pady=20)

        butprint = Button(self, text='START QUIZ', width=15, height = 3, font=('MS', 15,'bold'))
        butprint['command']= self.clogic 
        butprint.grid(row=10, column=1, padx=5, pady=5)
        
        butprint = Button(self, text='OVERALL RESULT', width=15, height = 3, font=('MS', 15,'bold'))
        butprint['command']= self.passcode
        butprint.grid(row=11, column=1, padx=5, pady=5)
        
        """butprint = Button(self, text='Statistics', width=10, font=('MS', 10,'bold'))
        butprint['command']= 'NULL'
        butprint.grid(row=12, column=1, padx=5, pady=5)

        butprint = Button(self, text='Settings', width=10, font=('MS', 10,'bold'))
        butprint['command']= 'NULL'
        butprint.grid(row=13, column=1, padx=5, pady=5)"""
        
        butexit = Button(self, text='Exit', width=15, height = 3, font=('MS', 15,'bold'))
        butexit['command']= self.exit1
        butexit.grid(row=14, column=1, padx=5, pady=5)
    def passcode (self):
        global app
        app.destroy()
        app = DisplayResults(root)
        
    def clogic(self):
        global app
        global pic
        pic = 0 ## to make sure the root starts form begining
        app.destroy()
        app = logicreason(root)

class feedback1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        self.pack(side='bottom', expand='no')
        self.grid()
        self.createButtons()

    def createButtons(self):
        global app
        global lans1
        global lans2
        global lans3
        ##lblProb1 = Label(self, text='Main Menu', font=('MS', 18,'bold'))
        ##lblProb1.grid(row=1, column =1, padx=40, pady=20)

        lblProg = Label(self, text = 'Your Answer for the Question 1 is %s'%(lans1), font=('ms',18))
        lblProg.grid(row=1,column= 1,)
        if (lans1 == "INCORRECT"):
            lblProg = Label(self, text = 'because of A reason', font=('ms',18))
            lblProg.grid(row=3,column= 1,)
            

        lblStrAgr = Label(self, text = 'Your Answer for the Question 2 is %s'%(lans2), font=('ms',18))
        lblStrAgr.grid(row=6,column= 1,)
        if (lans2 == "INCORRECT"):
            lblProg = Label(self, text = 'because of A reason', font=('ms',18))
            lblProg.grid(row=8,column= 1,)

        lblStrAgr = Label(self, text = 'Your Answer for the Question 3 is %s'%(lans3), font=('ms',18))
        lblStrAgr.grid(row=11,column= 1,)
        if (lans3 == "INCORRECT"):
            lblProg = Label(self, text = 'because of A reason', font=('ms',18))
            lblProg.grid(row=13,column= 1,)

        butprint = Button(self, text='Continue', width=30, height = 10, font=('MS', 15,'bold'))
        butprint['command']= self.c10que
        butprint.grid(row=15, column=1, padx=5, pady=5)
        
    def c10que(self):
        global app
        app.destroy()
        app = a10question(root)
        
class a10question(Frame):
    # GUI Setup

    def __init__(self, master):
        # Initialise Questionnaire Class

        Frame.__init__(self, master, bg="white")
        self.pack(side='bottom', expand='no')
        self.grid()
        self.createQuizQSN()
        self.createButtons()

    def createQuizQSN(self):
        # Create Widgets for Quiz Questions

        lblY = Label(self, text = 'Yes', font=('MS', 14, 'bold'))
        lblY.grid(row=3, column= 12, rowspan=2)
        
        lblN = Label(self, text = 'No', font=('MS', 14, 'bold'))
        lblN.grid(row=3, column= 14, rowspan=2)
        

        lblTLE = Label(self, text = 'Quiz Questions', font=('MS', 14, 'bold'))
        lblTLE.grid(row=4, column= 2, columnspan=4)

        lblQ1 = Label(self, text = '1. Do you have hobbies or interests?', font=('MS', 13, ))
        lblQ1.grid(row=5, column= 2, columnspan=4, sticky=W)

        self.varQ1 = IntVar()

        self.R1Q1 = Radiobutton(self, variable = self.varQ1, value=1)
        self.R1Q1.grid(row=5, column= 12)

        self.R2Q1 = Radiobutton(self, variable = self.varQ1, value=2)
        self.R2Q1.grid(row=5, column= 14)


        lblQ2 = Label(self, text = '2. Are you part of a team/organisation?', font=('MS', 13,))
        lblQ2.grid(row=6, column= 2, columnspan=4, sticky=W)

        self.varQ2 = IntVar()

        self.R1Q2 = Radiobutton(self, variable = self.varQ2, value=1)
        self.R1Q2.grid(row=6, column= 12)

        self.R2Q2 = Radiobutton(self, variable = self.varQ2, value=2)
        self.R2Q2.grid(row=6, column= 14)


        self.varQ3 = IntVar()

        lblQ3 = Label(self, text = '3. Do you like working on group and individual projects?', font=('MS', 13,))
        lblQ3.grid(row=7, column= 2, columnspan=4, sticky=W)

        self.R1Q3 = Radiobutton(self, variable = self.varQ3, value=1)
        self.R1Q3.grid(row=7, column= 12)

        self.R2Q3 = Radiobutton(self, variable = self.varQ3, value=2)
        self.R2Q3.grid(row=7, column= 14)

        self.varQ4 = IntVar()

        lblQ4 = Label(self, text = '4. Do you have creative skills?', font=('MS', 13,))
        lblQ4.grid(row=8, column= 2, columnspan=4, sticky=W)

        self.R1Q4 = Radiobutton(self, variable = self.varQ4, value=1)
        self.R1Q4.grid(row=8, column= 12)

        self.R2Q4 = Radiobutton(self, variable = self.varQ4, value=2)
        self.R2Q4.grid(row=8, column= 14)
        
        self.varQ5 = IntVar()

        lblQ5 = Label(self, text = '5. Do you own any computer based technologies?', font=('MS', 13,))
        lblQ5.grid(row=9, column= 2, columnspan=4, sticky=W)

        self.R1Q5 = Radiobutton(self, variable = self.varQ5, value=1)
        self.R1Q5.grid(row=9, column= 12)

        self.R2Q5 = Radiobutton(self, variable = self.varQ5, value=2)
        self.R2Q5.grid(row=9, column= 14)

    
        self.varQ6 = IntVar()

        lblQ6 = Label(self, text = '6. Do you like using different kind of cutting edge technologies?', font=('MS', 13,))
        lblQ6.grid(row=10, column= 2, columnspan=4, sticky=W)

        self.R1Q6 = Radiobutton(self, variable = self.varQ6, value=1)
        self.R1Q6.grid(row=10, column= 12)

        self.R2Q6 = Radiobutton(self, variable = self.varQ6, value=2)
        self.R2Q6.grid(row=10, column= 14)

        self.varQ7 = IntVar()

        lblQ7 = Label(self, text = '7. Are you good at making direct decisions?', font=('MS', 13,))
        lblQ7.grid(row=11, column= 2, columnspan=4, sticky=W)

        self.R1Q7 = Radiobutton(self, variable = self.varQ7, value=1)
        self.R1Q7.grid(row=11, column= 12)

        self.R2Q7 = Radiobutton(self, variable = self.varQ7, value=2)
        self.R2Q7.grid(row=11, column= 14)

        self.varQ8 = IntVar()

        lblQ8 = Label(self, text = '8. Do you consider yourself having good communication and management skills ?', font=('MS', 13,))
        lblQ8.grid(row=12, column= 2, columnspan=4, sticky=W)

        self.R1Q8 = Radiobutton(self, variable = self.varQ8, value=1)
        self.R1Q8.grid(row=12, column= 12)

        self.R2Q8 = Radiobutton(self, variable = self.varQ8, value=2)
        self.R2Q8.grid(row=12, column= 14)

        self.varQ9 = IntVar()

        lblQ9 = Label(self, text = '9. Would like to learn how applications and components interact?', font=('MS', 13,))
        lblQ9.grid(row=13, column= 2, columnspan=4, sticky=W)

        self.R1Q9 = Radiobutton(self, variable = self.varQ9, value=1)
        self.R1Q9.grid(row=13, column= 12)

        self.R2Q9 = Radiobutton(self, variable = self.varQ9, value=2)
        self.R2Q9.grid(row=13, column= 14)

        self.varQ10 = IntVar()

        lblQ10 = Label(self, text = '10. Do you take your own initiative for learning new skills?', font=('MS', 13,))
        lblQ10.grid(row=14, column= 2, columnspan=4, sticky=W)

        self.R1Q10 = Radiobutton(self, variable = self.varQ10, value=1)
        self.R1Q10.grid(row=14, column= 12)

        self.R2Q10 = Radiobutton(self, variable = self.varQ10, value=2)
        self.R2Q10.grid(row=14, column= 14)

    def createButtons(self):
        # Display buttons on quiz questions

        butSubmit = Button(self, text='Submit', font=('MS', 12, 'bold'))
        butSubmit.grid(row=16, column=2, columnspan=4)
        butSubmit['command'] = self.IdentCourse

        butSkip = Button(self, text='Skip', font=('MS', 12, 'bold'))
        butSkip.grid(row=16, column=4, columnspan=4)
        butSkip['command'] = self.IdentCourse

        #When it's clicked, run the IdentCourse() function <--- HOW DOES THIS BIT HAPPEN!??

    def IdentCourse(self):
        global ldegree
        global CS
        global IS
        #index = self.listProg.curselection()[0]
        #strProg = str(self.listProg.get(index))
        #strMsg=""
        
        IS = 0 #IS is the number of answers which pertain to an IS degree
        CS = 0 #CS is the number of answers which pertain to a CS degree

        #Question 1
        if self.varQ1.get() == 1:
            IS = IS + 1
        elif self.varQ1.get() == 2:
            CS = CS + 1
        

       #Question 2
        if self.varQ2.get() == 1:
            IS = IS + 1
        elif self.varQ2.get() == 2:
            CS = CS + 1
        

       #Question 3
        if self.varQ3.get() == 1:
            IS = IS + 1
        elif self.varQ3.get() == 2:
            CS = CS + 1
       

       #Question 4
        if self.varQ4.get() == 1:
            IS = IS + 1
        elif self.varQ4.get() == 2:
            CS = CS + 1
      

       #Question 5
        if self.varQ5.get() == 2:
            IS = IS + 1
        elif self.varQ5.get() == 1:
            CS = CS + 1

       #Question 6
        if self.varQ6.get() == 2:
            IS = IS + 1
        elif self.varQ6.get() == 1:
            CS = CS + 1

       #Question 7
        if self.varQ7.get() == 1:
            IS = IS + 1
        elif self.varQ7.get() == 2:
            CS = CS + 1

       #Question 8
        if self.varQ8.get() == 1:
            IS = IS + 1
        elif self.varQ8.get() == 2:
            CS = CS + 1

       #Question 9
        if self.varQ9.get() == 2:
            IS = IS + 1
        elif self.varQ9.get() == 1:
            CS = CS + 1

       #Question 10
        if self.varQ10.get() == 1:
            IS = IS + 1
            CS = CS + 1
        elif self.varQ10.get() == 2:
            CS = CS + 1
            IS = IS + 1

        self.contact()
        #Show appropriate window
        
    def contact(self):
        global app
        app.destroy()
        app = Contact(root)
    
        
class resultcs(Frame):
    # GUI Setup

    def __init__(self, master):
        # Initialise Questionnaire Class


        Frame.__init__(self, master)
        self.grid()
        self.SummaryScreen()
        self.createbuttons()

    def SummaryScreen(self):
        # display detailed summary of course details.
    
        lblTLE = Label(self, text = 'Summary Screen', font=('MS', 12, 'bold'))
        lblTLE.grid(row=2, column= 8)

        lbldtn = Label(self, text = 'You are best suited to a computer science after completing the questionnaire. You seem eager to learn the concepts \n of how software applications and hardware components can be developed as well as understand thay may interact with one \n another. Computer science can offer and involves learning concepts from a mathematical and scientific principles \n which underlay various types of computing systems. This can span from a range of functions such as \n mobile phones, internet and supercomputers and other systems. You will be able to gain a lot of skills \n and knowledge which could be applied across various careers such as website developer, game developer, \n computer programmer, system analyst and many other fields to advance in. You are now able to procedure and \n complete the contact details section allowing us to get in touch with additional information you may need.      ', font=('MS', 10, ))
        lbldtn.grid(row=3, column= 8)

    def createbuttons(self):
       # Display buttons on quiz questions

        butSubmit = Button(self, text='Okey', font=('MS', 8, 'bold'))
        butSubmit.grid(row=4, column=8)
        butSubmit['command'] = self.mainmenu

    def mainmenu(self):
        global app
        app.destroy()
        app = Main_Menu(root)
        
class resultbis(Frame):
    # GUI Setup

    def __init__(self, master):
        # Initialise Questionnaire Class


        Frame.__init__(self, master)
        self.grid()
        self.SummaryScreen()
        self.createbuttons()

    def SummaryScreen(self):
        # display detailed summary of course details.
    
        lblTLE = Label(self, text = 'Summary Screen', font=('MS', 12, 'bold'))
        lblTLE.grid(row=2, column= 8)

        lbldtn = Label(self, text = 'You are best suited to a business information systems after completing the questionnaire. You seem eager to gain an \n understanding and examine how information can be used tatically by organisations. This could be a form \n of web-based concepts as well as management systems. Business information system can offer and focus on the quality \n of the management of implementing and maintaining systems. In addition, it can also focus on strategically understanding \n the legal and regulatory implications of different types of information systems in the business world. \n Taking up the BIS course in the future will equip you with gaining technical and analytical skills required for \n management roles across many career paths. You will be able to gain a lot of skills and knowledge \n which could be applied across various careers such as ICT manager, systems designer, systems developer,\n business analyst  and many other fields to advance in. You are now able to procedure and \n complete the contact details section allowing us to get in touch with additional information you may need.', font=('MS', 10, ))
        lbldtn.grid(row=3, column= 8)

    def createbuttons(self):
       # Display buttons on quiz questions

        butSubmit = Button(self, text='Submit', font=('MS', 8, 'bold'))
        butSubmit.grid(row=4, column=8)
        butSubmit['command'] = self.mainmenu      

    def mainmenu(self):
        global app
        app.destroy()
        app = Main_Menu(root)

class Contact(Frame):
    # GUI Setup
    
    def __init__(self, master):
        # Initialise Questionnaire Class
        global x
        x=0
        Frame.__init__(self, master, bg="white")
        self.grid()
        self.pack(side='top',expand='no')
     
        self.createName()
        self.createEmail()
        self.createAddressLine1()
        self.createAddressLine2()
        self.createCity()
        self.createPostCode()
        self.createMajor()
        self.createSchool()
        #self.creatComments()
        self.createButtons()
        self.createButtons2()
        self.createButtons3()
        #self.welcomeMessage()   
        self.createButtonHelp()

    def welcomeMessage(self):   
        tkMessageBox.showwarning("Instructions", "If you would like us to contact you with further details about the courses available then please fill in your details on this screen ")
        #self.clearResponse() 
    def createName(self):
        # Create widgets to select a degree programme from a list

        lblProg = Label(self, text='CONTACT DETAILS', font=('MS', 21,'bold'))
        lblProg.grid(row=0, column=1, columnspan=5, sticky=W)
        
        lblProg1 = Label(self, text='Name:', font=('MS', 14,'bold'))
        lblProg1.grid(row=1, column=0, columnspan=2, sticky=W)

        self.txtName = Text(self, height=1,width=20)

        self.txtName.grid(row=1, column=1, columnspan=2)
        
     
    def createEmail(self):
       
        
        lblProg = Label(self, text='Email:', font=('MS', 14,'bold'))
        lblProg.grid(row=2, column=0, columnspan=2, sticky=W)

        self.txtEmail = Text(self, height=1,width=20)
        self.txtEmail.grid(row=2, column=1, columnspan=2)

    def createAddressLine1(self):
       
        
        lblProg = Label(self, text='Address Line 1:', font=('MS', 14,'bold'))
        lblProg.grid(row=4, column=0, columnspan=2, sticky=W)

        self.txtAddressLine1 = Text(self, height=1,width=20)        
        self.txtAddressLine1.grid(row=4, column=1, columnspan=2)

    def createAddressLine2(self):
       
        
        lblProg = Label(self, text='Address Line 2:', font=('MS', 14,'bold'))
        lblProg.grid(row=6, column=0, columnspan=2, sticky=W)

        self.txtAddressLine2 = Text(self, height=1,width=20) 
        self.txtAddressLine2.grid(row=6, column=1, columnspan=2)

    def createCity(self):
       
        
        lblProg = Label(self, text='City:', font=('MS', 14,'bold'))
        lblProg.grid(row=8, column=0, columnspan=2, sticky=W)

        self.txtCity = Text(self, height=1,width=20)   
        self.txtCity.grid(row=8, column=1, columnspan=2)

    def createPostCode(self):
       
        
        lblProg = Label(self, text='Post Code:', font=('MS', 14,'bold'))
        lblProg.grid(row=10, column=0, columnspan=2, sticky=W)

        self.txtPostCode = Text(self, height=1,width=20)
        self.txtPostCode.grid(row=10, column=1, columnspan=2)

    def createSchool(self):
       
        
        lblProg = Label(self, text='School Name:', font=('MS', 14,'bold'))
        lblProg.grid(row=12, column=0, columnspan=2, sticky=W)

        self.txtSchool = Text(self, height=1,width=20)    
        self.txtSchool.grid(row=12, column=1, columnspan=2)
        
    

   

    def createMajor(self):
        #Create Widgets to show degree specialisation

        lblProb1 = Label(self, text='Choose your major:', font=('MS', 12,'bold'))
        lblProb1.grid(row=16, column = 0)
        
        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text="Business Information Systems", variable=self.varCB1)
        CB1.grid(row=18, column=0, columnspan=4, sticky=W)

        self.varCB2 = IntVar()
        CB2 = Checkbutton(self, text="Computer Science", variable=self.varCB2)
        CB2.grid(row=18, column=4, columnspan=4, sticky=W)

        self.varCB3 = IntVar()
        CB3 = Checkbutton(self, text="Computer science with high performance computing", variable=self.varCB3)
        CB3.grid(row=20, column=0, columnspan=4, sticky=W)

        self.varCB4 = IntVar()
        CB4 = Checkbutton(self, text="Computer science with visual computing", variable=self.varCB4)
        CB4.grid(row=20, column=4, columnspan=4, sticky=W)

        self.varCB5 = IntVar()
        CB5 = Checkbutton(self, text="Computer systems engineering", variable=self.varCB5)
        CB5.grid(row=22, column=0, columnspan=4, sticky=W)

        self.varCB6 = IntVar()
        CB6 = Checkbutton(self, text="Joint Honours computing & mathematics", variable=self.varCB6)
        CB6.grid(row=22, column=4, columnspan=4, sticky=W)

        self.varCB7 = IntVar()
        CB7 = Checkbutton(self, text="Computer Science with Security and Forensics", variable=self.varCB7)
        CB7.grid(row=24, column=0, columnspan=4, sticky=W)



    def createButtons(self):
         butSubmit = Button(self, text='Submit',font=('MS',10,'bold'))
         butSubmit.grid(row=14, column=1, columnspan=1)
         butSubmit['command']=self.storeDetails

    def createButtons2(self):
         butReset = Button(self, text='Reset',font=('MS',10,'bold'))
         butReset.grid(row=14, column=2, columnspan=1)
         butReset['command']=self.clearResponse
    def createButtons3(self):
         butSkip = Button(self, text='Skip',font=('MS',10,'bold'))
         butSkip.grid(row=14, column=3, columnspan=1)
         butSkip['command']=self.final
         #tkMessageBox.showwarning("Instructions", "If you would like us to contact you with further details about the courses available then please fill in your details on this screen ")
    def createButtonHelp(self):
         butHelp = Button(self, text='Help',font=('MS',10,'bold'))
         butHelp.grid(row=14, column=4, columnspan=1)
         butHelp['command']=self.welcomeMessage
    def skip(self):
        #skips the details and closes window
        root.destroy()

    def final(self):
        global app
        global ldegree
        global CS
        global IS
        app.destroy()
        if CS > IS:
            print "CS is best"
            ldegree = "CS"
            self.cs()

        elif IS > CS:
            print "BIS is best"
            ldegree = "BIS"
            self.bis()

    def cs(self):
        global app
        app = resultcs(root)

    def bis(self):
        global app
        app = resultbis(root)
    def storeDetails(self):
            global x
            global lans1
            global lans2
            global lans3
            global ldegree

            #stores the users response
            strMsg=""
            

    #Checks that at least some txt has been entered into every field - however some smart checks maybe nice eg email verification.
               
            if (self.txtName.get(1.0,END)=="\n") or (self.txtEmail.get(1.0,END)=="\n")or(self.txtAddressLine1.get(1.0,END)=="\n")or (self.txtAddressLine2.get(1.0,END)=="\n")or(self.txtCity.get(1.0,END)=="\n")or (self.txtPostCode.get(1.0,END)=="\n")or (self.txtSchool.get(1.0,END)=="\n"):
                strMsg= strMsg + "You need to fill in all the details"                   

            #create detailsdb to store the data
           
            if strMsg=="":
                import shelve
                db=shelve.open('responsedb')
                
                responseCount=len(db)
                Ans=Response(str(responseCount+1), lans1, lans2, lans3, ldegree, self.txtName.get(1.0,END),
                                    self.txtEmail.get(1.0,END),self.txtAddressLine1.get(1.0,END),
                                    self.txtAddressLine2.get(1.0,END),self.txtCity.get(1.0,END),
                                    self.txtPostCode.get(1.0,END),self.txtSchool.get(1.0,END),
                                    self.varCB1.get(),self.varCB2.get(),self.varCB3.get(),
                                    self.varCB4.get(),self.varCB5.get(),self.varCB6.get(),
                                    self.varCB7.get())

                db[Ans.respNo]=Ans
                db.close

                #prints the info that is being stored to the consoleself.txtAddressLine2.get(1.0,END)
                detailStr=self.txtName.get(1.0,END),self.txtEmail.get(1.0,END),self.txtAddressLine1.get(1.0,END),self.txtAddressLine2.get(1.0,END),self.txtCity.get(1.0,END),self.txtPostCode.get(1.0,END),self.txtSchool.get(1.0,END),self.varCB1.get(),self.varCB2.get(),self.varCB3.get(),self.varCB4.get(),self.varCB5.get(),self.varCB6.get(),self.varCB7.get()
                self.printToShell(detailStr)
                global b
                b=0
                while (b<1):
                    print "HI!"
                    headings="First Name,Middle Name,Last Name,Title,Suffix,Initials,Web Page,Gender,Birthday,Anniversary,Location,Language,Internet Free Busy,Notes,Email Address,Email 2 Address,Email 3 Address,Primary Phone,Home Phone,Home Phone 2,Mobile Phone,Pager,HomeFax,Home Address,Home Street,Home Street 2,Home Street 3,Home Address PO Box,Home City,Home State,Home Postal Code,Home Country,Spouse,Children,Managers Name,Assistants Name,Referred By,Company Main Phone,Business Phone,Business Phone 2,Business Fax,Assistants Phone,Company,Job Title,Department,Office Location,Organizational ID Number,Profession,Account,Business Address,Business Street,Business Street 2,Business Street 3,Business Address PO Box,Business City,Business State,Business Postal Code,Business Country,Other Phone,Other Fax,Other Address,Other Street,Other Street 2,Other Street 3,Other Address PO Box,Other City,Other State,Other Postal Code,Other Country,Callback,Car Phone,ISDN,Radio Phone,TTY_TDD Phone,Telex,User1,User2,User3,User4,Keywords,Mileage,Hobby,Billing Information,Directory Server,Sensitivity,Priority,Private,Categories \n"
                    file=open("My School_AddressBook.csv","w") 
                    file.write(headings)
                    file.close()
                    b=1
                #exportCSVAddressBook(self.txtName.get(1.0,END),"",self.txtEmail.get(1.0,END),,,,,,ldegree,"")
                a=""
                #first off split the name into first and second. We can make an assumption and just split the name by the first whitespace found
                
                import shlex
                FirstName=self.txtName.get(1.0,END)
                nameArray=shlex.split(FirstName)
                #store the complete name in an array that has
                #been seperated by its spaces. Might have problems with double
                #barrel first names.
                #
                FirstName=nameArray[0]
                SecondName=""
                for i in range(len(nameArray)-1):
                    SecondName=SecondName+str(nameArray[1])+" "
                print FirstName,",",SecondName

            #    print "shlex is not available on this python installation."

                #THIS line of loveliness takes:
                
                SecondName=""
                Notes=""#(might use this for scores from logic test?)
                EmailAddress=self.txtEmail.get(1.0,END)
                HomeAddress=self.txtAddressLine1.get(1.0,END)
                HomeStreet=self.txtAddressLine2.get(1.0,END)
                HomePostalCode=self.txtPostCode.get(1.0,END)
                HomeCity =self.txtCity.get(1.0,END)
                Company = self.txtSchool.get(1.0,END)
                Department=ldegree # degree programme
                centreName ="MySchool"# use this to filter addresses once imported to outlook for mailshots.
                #another fun fact, CSV files for AddressLine 2 don't seem to work so we shall combine them thusly:
                #HomeAddress=HomeAddress
                Categories="ComSciQuiz"
                userDetails=str(FirstName)+"a,"+"b,"+str(SecondName)+"c,"+"d,"+"e,"+"f,"+"g,"+"h,"+"i,"+"j,"+"k,"+"l,"+"m,"+str(Notes)+"n,"+str(EmailAddress)+"o,"+"p,"+"q,"+"r,"+"s,"+"t,"+"u,"+"v,"+"w,"+"x,"+str(HomeAddress)+" "+str(HomeStreet)+","+str(HomeCity)+"1,"+"2,"+str(HomeCity)+"3,"+str(HomeCity)+","+"4,"+str(HomePostalCode)+","+"6,"+"7,"+"8,"+"9,"+"10,"+"11,"+"12,"+"13,"+"14,"+"15,"+str(Company)+"16,"+str(Company)+","+"18,"+str(Department)+","+str(centreName)+","+"21,"+"22,"+"23,"+"24,"+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+"Normal"+","+","+str(Categories)+"\n"    
                file=open(str(centreName)+"_AddressBook.csv","a")
                file.write(userDetails)
                file.close
                #print detailStr
                tkMessageBox.showinfo("Contact details", "Contact details stored.")
                self.clearResponse()
                      
            else:
                tkMessageBox.showwarning("Entry Error", strMsg)       

            self.final()
            
    def createCSVAddressBook(centreName):
        headings="First Name,Middle Name,Last Name,Title,Suffix,Initials,Web Page,Gender,Birthday,Anniversary,Location,Language,Internet Free Busy,Notes,Email Address,Email 2 Address,Email 3 Address,Primary Phone,Home Phone,Home Phone 2,Mobile Phone,Pager,HomeFax,Home Address,Home Street,Home Street 2,Home Street 3,Home Address PO Box,Home City,Home State,Home Postal Code,Home Country,Spouse,Children,Managers Name,Assistants Name,Referred By,Company Main Phone,Business Phone,Business Phone 2,Business Fax,Assistants Phone,Company,Job Title,Department,Office Location,Organizational ID Number,Profession,Account,Business Address,Business Street,Business Street 2,Business Street 3,Business Address PO Box,Business City,Business State,Business Postal Code,Business Country,Other Phone,Other Fax,Other Address,Other Street,Other Street 2,Other Street 3,Other Address PO Box,Other City,Other State,Other Postal Code,Other Country,Callback,Car Phone,ISDN,Radio Phone,TTY_TDD Phone,Telex,User1,User2,User3,User4,Keywords,Mileage,Hobby,Billing Information,Directory Server,Sensitivity,Priority,Private,Categories \n"
        file=open(str(centreName)+"_AddressBook.csv","w") 
        file.write(headings)
        file.close()
    
    
    #this will export in a format that is suitable for importing to microsoft outlook address book.
    def exportCSVAddressBook(FirstName,Notes,EmailAddress,HomeAddress,HomeStreet,HomeCity,HomePostalCode,Company,Department,centreName):
        a=""
        #first off split the name into first and second. We can make an assumption and just split the name by the first whitespace found
        
        import shlex
        nameArray=shlex.split(FirstName)
        #store the complete name in an array that has
        #been seperated by its spaces. Might have problems with double
        #barrel first names.
        #
        FirstName=nameArray[0]
        SecondName=""
        for i in range(len(nameArray)-1):
            SecondName=SecondName+str(nameArray[1])+" "
        print FirstName,",",SecondName

    #    print "shlex is not available on this python installation."

        #THIS line of loveliness takes:
        #FirstName
        #SecondName
        #Notes(might use this for scores from logic test?)
        #email address
        #HomeAddress(addressLine1)
        #HomeStreet (addressLine2)
        #HomePostalCode (postCode)
        #HomeCity (city)
        #Company = School
        #Department degree programme
        #categories  - use this to filter addresses once imported to outlook for mailshots.
        #another fun fact, CSV files for AddressLine 2 don't seem to work so we shall combine them thusly:
        #HomeAddress=HomeAddress
        Categories="ComSciQuiz"
        userDetails=str(FirstName)+"a,"+"b,"+str(SecondName)+"c,"+"d,"+"e,"+"f,"+"g,"+"h,"+"i,"+"j,"+"k,"+"l,"+"m,"+str(Notes)+"n,"+str(EmailAddress)+"o,"+"p,"+"q,"+"r,"+"s,"+"t,"+"u,"+"v,"+"w,"+"x,"+str(HomeAddress)+" "+str(HomeStreet)+","+str(HomeCity)+"1,"+"2,"+str(HomeCity)+"3,"+str(HomeCity)+","+"4,"+str(HomePostalCode)+","+"6,"+"7,"+"8,"+"9,"+"10,"+"11,"+"12,"+"13,"+"14,"+"15,"+str(Company)+"16,"+str(Company)+","+"18,"+str(Department)+","+str(centreName)+","+"21,"+"22,"+"23,"+"24,"+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+"Normal"+","+","+str(Categories)+"\n"    
        file=open(str(centreName)+"_AddressBook.csv","a")
        file.write(userDetails)
        file.close
    def retrieveResponse(self):
        countAll
    def clearResponse(self):
            #clear the form
#            self.listProg.selection_clear(0,END)
#            self.listProg.selection_set(END)
            
            #clear radiobuttons and checkboxes
#            self.varQ1.set(0)
#            self.varQ2.set(0)
#            self.varQ3.set(0)
            
            self.varCB1.set(0)
            self.varCB2.set(0)
            self.varCB3.set(0)
            self.varCB4.set(0)
            self.varCB5.set(0)
            self.varCB6.set(0)
            self.varCB7.set(0)
            
            self.txtName.delete(1.0,END)
            self.txtEmail.delete(1.0, END)	
            self.txtAddressLine1.delete(1.0, END)    
            self.txtAddressLine2.delete(1.0, END)    
            self.txtCity.delete(1.0, END)    
            self.txtPostCode.delete(1.0, END)    
            self.txtSchool.delete(1.0, END)  
            
    def printToShell(self,msg):  #prints info to console at the request of Girish.
        msg=msg
        print msg

class DisplayResults(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.pack()
        self.retrieveResponse()
        self.button()
        self.grid()
        
    def retrieveResponse(self):
        #Set default values for variables
        """respnumber = 0
        answer1 = 0
        answer2 = 0
        answer3 = 0
        degree = ""
        name = ""
        email = ""
        add1 = ""
        add2 = ""
        city = ""
        pcode = ""
        school = ""
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        q5 = 0
        q6 = 0
        q7 = 0"""
              
        countAll = 0
        countCS = 0
        countBIS = 0

        sumQ1All = 0.0
        sumQ1CS = 0.0
        sumQ1BIS = 0.0
        
        sumQ2All = 0.0
        sumQ2CS = 0.0
        sumQ2BIS = 0.0

        sumQ3All = 0.0
        sumQ3CS = 0.0
        sumQ3BIS = 0.0

        sumP1All = 0
        sumP1CS = 0
        sumP1BIS = 0

        sumP2All = 0
        sumP2CS = 0
        sumP2BIS = 0

        sumP3All = 0
        sumP3CS = 0
        sumP3BIS = 0

        sumP4All = 0
        sumP4CS = 0
        sumP4BIS = 0

        sumP5All = 0
        sumP5CS = 0
        sumP5BIS = 0
        
        sumP6All = 0
        sumP6CS = 0
        sumP6BIS = 0

        sumP7All = 0
        sumP7CS = 0
        sumP7BIS = 0
        
        #Open the database and check the number of responses.

        import shelve
        db=shelve.open('responsedb')
        respNo = len(db)

        #Retreive each response and update the variables
        for i in range (1, respNo):
            Ans = db.get(str(i))

            countAll +=1
            print "testaa"
            if Ans.q1=="CORRECT":
                Ans.q1=1
                print Ans.q1
            else:
                Ans.q1=0
                print Ans.q1
            if Ans.q2=="CORRECT":
                Ans.q2=1
            else:
                Ans.q2=0
            if Ans.q3=="CORRECT":
                Ans.q3=1
            else:
                Ans.q3=0
            sumQ1All += Ans.q1
            sumQ2All += Ans.q2
            sumQ3All += Ans.q3
            sumP1All += Ans.pr1
            sumP2All += Ans.pr2
            sumP3All += Ans.pr3
            sumP4All += Ans.pr4
            sumP5All += Ans.pr5
            sumP6All += Ans.pr6
            sumP7All += Ans.pr7

            if Ans.ldegree == "CS":
                countCS +=1
                sumQ1CS += Ans.q1
                sumQ2CS += Ans.q2
                sumQ3CS += Ans.q3
                sumP1CS += Ans.pr1
                sumP2CS += Ans.pr2
                sumP3CS += Ans.pr3
                sumP4CS += Ans.pr4
                sumP5CS += Ans.pr5
                sumP6CS += Ans.pr6
                sumP7CS += Ans.pr7
                
            if Ans.ldegree == "BIS":
                countBIS +=1
                sumQ1BIS += Ans.q1
                sumQ2BIS += Ans.q2
                sumQ3BIS += Ans.q3
                sumP1BIS += Ans.pr1
                sumP2BIS += Ans.pr2
                sumP3BIS += Ans.pr3
                sumP4BIS += Ans.pr4
                sumP5BIS += Ans.pr5
                sumP6BIS += Ans.pr6
                sumP7BIS += Ans.pr7


        db.close
        #Configure the Display
        self.txtDisplay = Text(self, height=14,width=85)
        self.txtDisplay.tag_configure('boldfont', font =('MS', 8, 'bold'))
        self.txtDisplay.tag_configure('normfont', font =('MS', 8))
        
        self.txtDisplay.pack()
        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")
        self.txtDisplay.insert(END,"DegreeProgramme"+ tabResults +"ALL"+"\t" +"CS"+"\t"+ "BIS" + '\n', 'boldfont')

        # Display response counts for all and each programme
        self.txtDisplay.insert(END, "Number of Responses:" + tabResults + str(countAll) + "\t" + str(countCS) + "\t"
                                + str(countBIS) + "\t"+'\n', 'normfont')

        # Display average scores for Team Experience Questions
        self.txtDisplay.insert(END, "\nLogic Test STATS: \n", 'boldfont')
        self.txtDisplay.insert(END, "(Score: 3=Maximum score to 0=Mimimum score)\n", 'normfont')

        if countAll > 0:
            Q1All = sumQ1All/countAll
            Q2All = sumQ2All/countAll
            Q3All = sumQ3All/countAll
            P1All = sumP1All*100/countAll
            P2All = sumP2All*100/countAll
            P3All = sumP3All*100/countAll
            P4All = sumP4All*100/countAll
            P5All = sumP5All*100/countAll
            P6All = sumP6All*100/countAll
            P7All = sumP7All*100/countAll
        else:
            Q1All = 0
            Q2All = 0
            Q3All = 0
            P1All = 0
            P2All = 0
            P3All = 0
            P4All = 0
            P5All = 0
            P6All = 0
            P7All = 0

        if countCS > 0:
            Q1CS = sumQ1CS/countCS
            Q2CS = sumQ2CS/countCS
            Q3CS = sumQ3CS/countCS
            P1CS = sumP1CS*100/countCS
            P2CS = sumP2CS*100/countCS
            P3CS = sumP3CS*100/countCS
            P4CS = sumP4CS*100/countCS
            P5CS = sumP5CS*100/countCS
            P6CS = sumP6CS*100/countCS
            P7CS = sumP7CS*100/countCS

        else:
            Q1CS=0
            Q2CS=0
            Q3CS=0
            P1CS=0
            P2CS=0
            P3CS=0
            P4CS=0
            P5CS=0
            P6CS=0
            P7CS=0

        if countBIS > 0:
            Q1BIS = sumQ1BIS/countBIS
            Q2BIS = sumQ2BIS/countBIS
            Q3BIS = sumQ3BIS/countBIS
            P1BIS = sumP1BIS*100/countBIS
            P2BIS = sumP2BIS*100/countBIS
            P3BIS = sumP3BIS*100/countBIS
            P4BIS = sumP4BIS*100/countBIS
            P5BIS = sumP5BIS*100/countBIS
            P6BIS = sumP6BIS*100/countBIS
            P7BIS = sumP7BIS*100/countBIS
            
        else:
            Q1BIS=0
            Q2BIS=0
            Q3BIS=0
            P1BIS=0
            P2BIS=0
            P3BIS=0
            P4BIS=0
            P5BIS=0
            P6BIS=0
            P7BIS=0


        self.txtDisplay.insert(END, "Question 1" + tabResults +"\t"+"%.1f" % Q1All + "\t %.1f" % Q1CS + "\t %.1f" % Q1BIS +"%\n", 'normfont')
        self.txtDisplay.insert(END, "Question 2" + tabResults +"\t"+"%.1f" % Q2All + "\t %.1f" % Q2CS + "\t %.1f" % Q2BIS +"%\n", 'normfont')
        self.txtDisplay.insert(END, "Question 3" + tabResults +"\t"+"%.1f" % Q3All + "\t %.1f" % Q3CS + "\t %.1f" % Q3BIS +"%\n", 'normfont')

# Display counts for Problems experienced
        self.txtDisplay.insert(END, "\nDegree Options preffered by students: \n", 'boldfont')
        self.txtDisplay.insert(END, "Business Info. Systems" + tabResults + "%d" % P1All + "% \t" + "%d" % P1CS + "% \t" +"%d"%P1BIS+"%\n",'normfont')
        self.txtDisplay.insert(END, "Computer Science"+ tabResults + "%d" % P2All + "% \t" + "%d" % P2CS + "% \t" +"%d"%P2BIS+"%\n",'normfont')
        self.txtDisplay.insert(END,"Computer Science with HPC"+tabResults +"%d"%P3All+"%\t"+"%d"%P3CS+"%\t"+"%d"%P3BIS+"%\n",'normfont')
        self.txtDisplay.insert(END,"Computer Science with VC"+ tabResults+"%d"%P4All+"%\t"+"%d"%P4CS+ "%\t"+"%d"%P4BIS+"%\n",'normfont')
        self.txtDisplay.insert(END, "Computer Science Eng." + tabResults + "%d" % P5All + "% \t" + "%d" % P5CS + "% \t" +"%d"%P5BIS+"%\n",'normfont')
        self.txtDisplay.insert(END, "JH Computing and Maths" + tabResults + "%d" % P6All + "% \t" + "%d" % P6CS + "% \t" +"%d"%P6BIS+"%\n",'normfont')
        self.txtDisplay.insert(END, "Computer Science with SAF" + tabResults + "%d" % P7All + "% \t" + "%d" % P7CS + "% \t" + "%d"%P7BIS+"%\n",'normfont')

        self.txtDisplay['state'] = DISABLED

        self.txtDisplay.pack()
    def button(self):
        butSubmit = Button(self, text='MAIN MENU',font=('MS',10,'bold'))
        butSubmit.pack()
        #butSubmit.grid(row=14, column=1, columnspan=1)
        butSubmit['command']=self.mainmenu

        butSubmit1 = Button(self, text='EXPORT',font=('MS',10,'bold'))
        butSubmit1.pack()
        #butSubmit1.grid(row=14, column=3, columnspan=1)
        butSubmit1['command']='NULL' #Export function called

    def mainmenu(self):
        global app
        app.destroy()
        app = Main_Menu(root)
     
# Main
root = tk.Tk()
root.title("Logic Resoning Test")
root.geometry("800x600")
root.configure(background='white')
global pic
global app
pic = 0
# PT Creating a CANVAS image to be used in the class for Question 1
canvasqt = tk.Canvas(root, bg="black", height=550, width=697)
filename1 = ImageTk.PhotoImage(file = "q1.gif")
imagept = canvasqt.create_image(351, 270, image=filename1)

# Q1 Creating a CANVAS image to be used in the class for Question 2
canvasq1 = tk.Canvas(root, bg="black", height=550, width=697)
filename2 = ImageTk.PhotoImage(file = "q2.gif")
imageq1 = canvasq1.create_image(351, 270, image=filename2)

# Q2 Creating a CANVAS image to be used in the class for Question 3
canvasq2 = tk.Canvas(root, bg="black", height=550, width=697)
filename3 = ImageTk.PhotoImage(file = "q3.gif")
imageq2 = canvasq2.create_image(351, 270, image=filename3)

# Q3 Creating a CANVAS image to be used in the class for Question 4
canvasq3 = tk.Canvas(root, bg="black", height=550, width=697)
filename4 = ImageTk.PhotoImage(file = "q4.gif")
imageq3 = canvasq3.create_image(351, 270, image=filename4)
app = Main_Menu(root)
#app = Questionaire(root)
root.mainloop()
       
