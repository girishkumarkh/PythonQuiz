'''
Created on Mar 23, 2012

@author: oliver
'''
#does some magic stuff!
class Response:
    
    def __init__(self, respNo="", ans1="", ans2="", ans3="", degree="", name="\n",
                 email="\n",addressLine1="\n",addressLine2="\n",city="\n",
                 postCode="\n",school="\n", pr1=0, pr2=0, pr3=0, pr4=0, pr5=0, pr6=0, pr7=0):
        self.respNo=respNo           
        self.q1=ans1
        self.q2=ans2
        self.q3=ans3
        self.ldegree=degree
        self.name=name
        self.email=email
        self.addressLine1=addressLine1
        self.addressLine2=addressLine2
        self.city=city
        self.postCode=postCode
        self.school=school
        self.pr1=pr1
        self.pr2=pr2
        self.pr3=pr3
        self.pr4=pr4
        self.pr5=pr5
        self.pr6=pr6
        self.pr7=pr7

    
