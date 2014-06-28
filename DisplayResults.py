# DisplayResults.py
from Tkinter import *
from Response import Response

class DisplayResults(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.pack()
        #self.grid()
        
        self.retrieveResponse()
        
    def retrieveResponse(self):
        #Set default values for variables    
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
        sumP1CBIS = 0

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
# Main
root = Tk()
root.title("Display Results")
root.geometry("800x600")
app = DisplayResults(root)
root.mainloop()
