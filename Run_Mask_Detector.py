from tkinter import *
from face_mask_detector import face_mask

root= Tk()
Tk.wm_title(root,"Face Mask Detector") #to add title to window
topFrame = Frame(root)

photo = PhotoImage(file='dsce_logo.png')
#You can't directly put a photo inside GUI directly using Tkinter, so you make use of Label

label_1 = Label(topFrame, image= photo) #assigning our image to Label
label_1.pack(side= 'top')
label_2 = Label(topFrame,text= 'FACE MASK DETECTOR', font=("Courier", 44, 'bold'))
label_2.pack(side='top')
label_3 = Label(topFrame, text='Created by the students of \n Information Science and Engineering Department ', font=("Courier", 20, 'bold'))
label_3.pack(side='top')
label_4 = Label(topFrame, text='Under the Guidance of Dr. Rajeshwari J', font=("Courier", 20,'bold'))
label_4.pack(side='top')

topFrame.pack(side='top')
def runProject():
    face_mask()
button_1 = Button(topFrame, text="CLICK TO RUN", command= runProject, font=("Courier", 15, 'bold'), bg='Blue', fg='white') #when clicked call the function printName
button_1.pack()

bottomFrame = Frame(root)
label_5 = Label(bottomFrame, text = "About: COVID 19 is an infectious disease caused by coronavirus\n According to experts use of face mask can reduce the spread \n  of COVID-19. But it is very expensive to manually check each \n individual for face mask. Hence we have created a program which\n  will aid the authorities in detecting whether a person is wearing \na mask or not ", font=("Courier", 15), bg='black', fg='white')
label_5.pack()

bottomFrame.pack()

root.mainloop()
