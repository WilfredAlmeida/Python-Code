import sqlite3

import tkinter.font as font

try:
    # Python2
    import Tix as tix
except ImportError:
    # Python3
    import tkinter.tix as tix
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy.distutils.fcompiler import none
import os
# -------------------Start:DATABASE and variables declaration-----------------------------------------------------------

# ------------------------------Start:Connection--------------------------------
# database = mysql.connector.connect(host="localhost", user="root", passwd="", database="capstone")
database = sqlite3.connect('patient.sqlite')
# ------------------------------End:Connection--------------------------------


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)




# ------------------Start:cursor to database----------------------
cursor = database.cursor()  # this will execute query using its execute() method.
# ------------------End:cursor to database--------------------

# ----------------Start: Creating table if it does not exist---------------------------------------------
try:
    cursor.execute(
        "CREATE TABLE `patient` (  `patient_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  `patient_name` text DEFAULT NULL,  `patient_gender` text DEFAULT NULL,  `patient_age` decimal(2,0) DEFAULT NULL,  `patient_address` tinytext DEFAULT NULL,  `mobile_number` decimal(10,0) DEFAULT NULL,  `air_pollution` int(1) DEFAULT NULL,  `alcohol_use` int(1) DEFAULT NULL,  `dust_allergy` int(1) DEFAULT NULL,  `occupational_hazard` int(1) DEFAULT NULL,  `genetic_risk` int(1) DEFAULT NULL,  `chronic_lung_disease` int(1) DEFAULT NULL,  `balanced_diet` int(3) DEFAULT NULL,  `obesity` int(1) DEFAULT NULL,  `smoking` int(1) DEFAULT NULL,  `chest_pain` int(1) DEFAULT NULL,  `coughing_of_blood` int(1) DEFAULT NULL,  `fatigue` int(1) DEFAULT NULL,  `weight_loss` int(1) DEFAULT NULL,  `shortness_of_breath` int(1) DEFAULT NULL,  `wheezing` int(1) DEFAULT NULL,  `swallowing` int(1) DEFAULT NULL,  `frequent_cold` int(1) DEFAULT NULL,  `dry_cough` int(1) DEFAULT NULL);")
except sqlite3.OperationalError:
    pass
# ----------------End: Creating table if it does not exist----------------------------------------------
root = tix.Tk()
root.title('Cancer Rate Predication System-Home Page')
root.state('zoomed')

# -------------------Start:Variables Declaration---------------------------------
patient_id = none  # assigned in database
patient_name = ""
patient_gender = ""
patient_age = ""
patient_address = ""
mobile_number = ""
air_pollution = ""
alcohol_use = ""
dust_allergy = ""
occupational_hazard = ""
genetic_risk = ""
chronic_lung_disease = ""
balanced_diet = ""
p_obesity = ""
smoking = ""
chest_pain = ""
coughing_of_blood = ""
p_fatigue = ""
weight_loss = ""
shortness_of_breath = ""
p_wheezing = ""
swallowing = ""
frequent_cold = ""
dry_cough = ""

tx1 = ""
selected_value1 = ""
balloon = tix.Balloon(root)
global selected_value2
selected_value2 = ""


# -------------------End:Variables Declaration-----------------------------

# --------------------End:DATABASE--------------------------------------------------------------------------------------

def InsertWindow():
    # =================================================== Form 1 ======================================================
    form1 = Toplevel()  # For Creating sub - window
    form1.lift()  # Place window Above Other
    form1.focus_force()  # Give Focus to Form
    form1.grab_set()  # Make form Modeless
    # form1.resizable(False,False) # Make Form Not resizable
    form1.geometry("850x530+300+80")
    form1.title('Cancer Rate Predication System- Insert Details')

    mainFrame = LabelFrame(form1, text="Customer Details", padx=10, pady=10)
    mainFrame.grid(row=0, column=0, padx=50, pady=20, rowspan=50)
    helpFrame = LabelFrame(form1, text="How to Select Corrcet Options: ", padx=5)
    helpFrame.place(x=580, y=170)

    personNames = ["Air Pollution", "Alcohol Use", "Dust Allergy", "Occupational Hazard", "Genetic Risk",
                   "Chronic Lung Disease", "Balanced Diet", "Obesity", "Smoking", "Chest Pain", "Choughing of Blood",
                   "Fatigue", "Weigth Loss", "Shortness Of Breath", "Wheezing", "Swallowing Difficulty",
                   "Frequent Cold", "Clubbing of Finger Nails"]  # <- Database Entry

    cbox = ttk.Combobox(helpFrame, state='readonly', values=personNames)
    cbox.grid(row=0, column=0, columnspan=10)

    def cbox_event(evt):
        value = cbox.get()
        index = cbox.current()
        if (index == 0):
            mvar.set(
                "0=If AQI between 0-50\n\n1=If AQI between 51-100\n\n2=If AQI between 101-150\n\n3=If AQI between 150-200\n\n4=If AQI between 201-300\n\n5=If AQI between 300-350\n\n=If AQI between 350+")
        elif (index == 1):
            mvar.set(
                "0=No Use\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (At parties, events, etc)\n\n3=If Normal (Few times a month)\n\n4=If Frequent (Multiple times a week)\n\n5=If High (Daily)\n\n6=If Severe(Multiplt times a day) ")
        elif (index == 2):
            mvar.set(
                "0=No Allergy\n\n1=If Negligible \n\n2=If Slightly Allergic (E.g- A few sneezes)\n\n3=If Properly Allergic(E.g- Itching)\n\n4=If More Allergic(E.g- Running or Stuffy Nose)\n\n5=If Highly Allergic (E.g- Red, itchy or teary eyes)\n\n6=If Severely Allergic(E.g- Wheezing, coughing, tightness in the chest and shortness of breath)")
        elif (index == 3):
            mvar.set(
                "0=No Risk\n\n1=If Negligible Risk (E.g- At offices with proper Air conditioning)\n\n2=If Slightly High Risk(E.g- At offices near Pollution sources)\n\n3=If Intermediate Risk(E.g- At Argicultural Sites)\n\n4=If More Risk(E.g- At Industries)\n\n5=If High Risk(E.g- At Construction sites)\n\n6=If Severe Risk(E.g- At Chemical Industries, Power Plants, etc) ")
        elif (index == 4):
            mvar.set(
                "0=No Risk\n\n1=If Negligible Risk (E.g- Family history of minor lung diseases)\n\n2=If Slightly High Risk(E.g-Family history of common lung diseases)\n\n3=If Intermediate Risk(E.g- Family history of Asthama)\n\n4=If More Risk(E.g- Famaily history Asthama, Brochitis)\n\n5=If High Risk(E.g- Family history of TB, Pneumonia)\n\n6=If Severe Risk(E.g- Family History of Lung Cancer)")
        elif (index == 5):
            mvar.set(
                "0=No Disease\n\n1=If Negligilbe Diseases(E.g- common cough, common cold, etc)\n\n2=If Slightly High Risk Diseases(E.g-chronic cough, chronic cold)\n\n3=If Intermediate Risk Diseases(E.g- Asthama)\n\n4=If More Risk Diseases(E.g- Asbestosis, Brochitis)\n\n5=If High Risk Diseases(E.g- TB, Pneumonia)\n\n6=If Severe Risk Diseases(E.g- COPD)")
        elif (index == 6):
            mvar.set(
                "0=None \n\n1=If Low\n\n2=If Meduim\n\n3=If Good\n\n=If Well Balanced\n\n5=If Highly Balanced\n\n6=If Perfectly balanced")
        elif (index == 7):
            mvar.set(
                "0=None (BMI in 18.5 to 22.9)\n\n1=If Low (BMI in 22.9 to 24.9)\n\n2=If Meduim (BMI in 24.9 to 26.9)\n\n3=If Semi-Medium(BMI in 26.9 to 30.9)\n\n4=If High (BMI in 30.9 to 35.9)\n\n5=If Very High (BMI in 35.9 to 39.9)\n\n6=If Severely High (BMI above 40)")
        elif (index == 8):
            mvar.set(
                "0=No Use\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (At certain occasions)\n\n3=If Normal (Few times a month)\n\n4=If Frequent (Multiple times a week)\n\n5=If High (Daily)\n\n6=If Severe(Multiple times a day)")
        elif (index == 9):
            mvar.set(
                "0=None\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (Only a few times)\n\n3=If Recurring (Once or twice in a month))\n\n4=If Frequent (Multiple times a month)\n\n5=If High (Multiple times a week)\n\n6=If Severe (Daily)")
        elif (index == 10):
            mvar.set(
                "0=None\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (Only a few times)\n\n3=If Recurring (Once or twice in a month))\n\n4=If Frequent (Multiple times a month)\n\n5=If High (Multiple times a week)\n\n6=If Severe (Daily)")
        elif (index == 11):
            mvar.set(
                "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
        elif (index == 12):
            mvar.set(
                "0=None\n\n1=If Negligible (1-2 Kg in last 2 months)\n\n2=If Low (2-5 kg in last 2 months)\n\n3=If Medium (5-7 kg in last 2 months)\n\n4=If High (7-8 kg in last 2 months)\n\n5=If Very High (8-10 kg in last 2 months)\n\n6=If Severe (10kg + in last 2 months)")
        elif (index == 13):
            mvar.set(
                "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
        elif (index == 14):
            mvar.set(
                "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
        elif (index == 15):
            mvar.set(
                "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
        elif (index == 16):
            mvar.set(
                "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
        else:
            mvar.set(
                "0=None\n\n1=If Negligible (Slight pale color of nails)\n\n2=If Low (More pale color of nails)\n\n3=If Medium (Slight distorted nail angle)\n\n4=If High (More Distorted nail angle)\n\n5=If Very High (Slight Swelling of finger)\n\n6=If Severe (More Swelling of finger)")

    cbox.bind("<<ComboboxSelected>>", cbox_event)
    mvar = StringVar()
    m = Message(helpFrame, textvariable=mvar, width=220)
    m.grid(row=1, column=0)

    def VerifyData():
        Temp = True
        n = name.get()
        regex = "^[A-Za-z\s]{3,20}$"
        if re.search(regex, n):
            errorName.set("")
        else:
            Temp = False
            errorName.set("Please Enter Correct Name")

        age = sAge.get()
        if (type(int(age)) == type(1)):
            age = int(age)
            if (age > 0 and age <= 100):
                errorAge.set("")
            else:
                Temp = False
                errorAge.set("Please Enter Valid Age")
        else:
            Temp = False
            errorAge.set("Only number Allowed are Allowed in Age")

        address = eAddress.get(1.0, END)
        regex = "^[A-Za-z0-9'\.\-\s\,\=]{10,50}$"
        if re.search(regex, address):
            errorAddress.set("")
        else:
            Temp = False
            errorAddress.set("Please Enter Correct Address")

        phonenumber = mobile.get()
        regex = "^\d{10}$"
        if re.search(regex, phonenumber):
            errorMobile.set("")
        else:
            Temp = False
            errorMobile.set("Please Enter Correct phone number")

        if (Temp):
            for child in mainFrame.winfo_children():
                child.configure(state='disabled')
            Submit.configure(state='normal')

    def SaveData():
        # -----------------------Begin:Getting input from GUI to variables-------------------------------
        patient_name = name.get()
        patient_gender = "Male" if (gender.get() == 1) else "Female"
        patient_age = int(sAge.get())
        patient_address = eAddress.get(1.0, END)
        mobile_number = mobile.get()
        air_pollution = int(air.get())
        alcohol_use = int(alcohol.get())
        dust_allergy = int(dust.get())
        occupational_hazard = int(occupationHzd.get())
        genetic_risk = int(genes.get())
        chronic_lung_disease = int(chronic.get())
        balanced_diet = int(diet.get())
        p_obesity = int(obesity.get())
        smoking = int(smoke.get())
        chest_pain = int(chest.get())
        coughing_of_blood = int(cough.get())
        p_fatigue = int(fatigue.get())
        weight_loss = int(weightloss.get())
        shortness_of_breath = int(breath.get())
        p_wheezing = int(wheezing.get())
        swallowing = int(swallow.get())
        frequent_cold = int(cold.get())
        dry_cough = int(drycough.get())

        # -------------End:Getting input from user-------------------------------------------------
        # -----------------------------Database insertion below------------------------------------

        def insert_into_database():  # function defined to execute query. It wont work without function.
            query = "INSERT INTO patient (patient_name, patient_gender, patient_age, patient_address, mobile_number," \
                    "air_pollution, alcohol_use, dust_allergy, occupational_hazard, genetic_risk," \
                    "chronic_lung_disease, balanced_diet, obesity, smoking, chest_pain, coughing_of_blood, fatigue," \
                    "weight_loss, shortness_of_breath, wheezing, swallowing, frequent_cold,dry_cough) VALUES (?,?," \
                    "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) "

            values = (
                patient_name, patient_gender, patient_age, patient_address, mobile_number, air_pollution, alcohol_use,
                dust_allergy, occupational_hazard, genetic_risk, chronic_lung_disease, balanced_diet, p_obesity,
                smoking,
                chest_pain, coughing_of_blood, p_fatigue, weight_loss, shortness_of_breath, p_wheezing, swallowing,
                frequent_cold, dry_cough)

            cursor.execute(query, values)
            database.commit()
            messagebox.showinfo("Success!!", "Data Saved Successfully!")
            form1.destroy()

        # ---------------------------------------Database insertion Completed------------------------------------------
        insert_into_database()  # function defined above is called. It wont work without function.

    # ---------------------End:Getting input from GUI to variables and putting into database---------------------------
    Check = Button(form1, text="Validate Data", command=VerifyData, width=15)
    Check.place(x=580, y=30)

    Submit = Button(form1, text="Save and Submit", command=SaveData, width=15)
    Submit.place(x=580, y=70)
    Submit.configure(state='disabled')

    Exit = Button(form1, text="Close Window", command=form1.destroy, width=15)
    Exit.place(x=580, y=110)

    # Name
    lName = Label(mainFrame, text="Name")
    lName.grid(row=0, column=0)
    errorName = StringVar()
    errName = Label(mainFrame, textvariable=errorName, fg='red')
    errName.grid(row=0, column=2)
    name = StringVar()
    eName = Entry(mainFrame, textvariable=name, width=20)
    eName.grid(row=0, column=1)

    # Gender
    lGender = Label(mainFrame, text="Gender")
    lGender.grid(row=1, column=0)
    gender = IntVar()
    rMale = Radiobutton(mainFrame, text="Male", variable=gender, value=1)
    rFemale = Radiobutton(mainFrame, text="Female", variable=gender, value=2)
    rMale.grid(row=1, column=1)
    rFemale.grid(row=1, column=2)

    # Age
    lAge = Label(mainFrame, text="Age")
    lAge.grid(row=2, column=0)
    errorAge = StringVar()
    errAge = Label(mainFrame, textvariable=errorAge, fg='red')
    errAge.grid(row=2, column=2)
    sAge = Spinbox(mainFrame, from_=1, to=100, width=18)
    sAge.grid(row=2, column=1)

    # Address
    lAddress = Label(mainFrame, text="Address")
    lAddress.grid(row=3, column=0)
    errorAddress = StringVar()
    errAddress = Label(mainFrame, textvariable=errorAddress, fg='red')
    errAddress.grid(row=3, column=2)
    eAddress = Text(mainFrame, width=15, height=2)
    eAddress.grid(row=3, column=1)

    # Mobile
    lMobile = Label(mainFrame, text="Mobile Number")
    lMobile.grid(row=4, column=0)
    errorMobile = StringVar()
    errMobile = Label(mainFrame, textvariable=errorMobile, fg='red')
    errMobile.grid(row=4, column=2)
    mobile = StringVar()
    eMobile = Entry(mainFrame, textvariable=mobile)
    eMobile.grid(row=4, column=1)

    # Common List
    List_Options = [0, 1, 2, 3, 4, 5, 6]
    # Air Pollution
    lAir = Label(mainFrame, text="Air Pollution")
    lAir.grid(row=5, column=0)
    air = IntVar()
    air.set(List_Options[0])
    omAirPollution = OptionMenu(mainFrame, air, *List_Options)
    omAirPollution.grid(row=5, column=1)

    # Alcohol USe
    lAlcohol = Label(mainFrame, text="Alcohol Use")
    lAlcohol.grid(row=6, column=0)
    alcohol = IntVar()
    alcohol.set(List_Options[0])
    omAlcohol = OptionMenu(mainFrame, alcohol, *List_Options)
    omAlcohol.grid(row=6, column=1)

    # Dust Allergy
    lDustAllergy = Label(mainFrame, text="Dust Allergy")
    lDustAllergy.grid(row=7, column=0)
    dust = IntVar()
    dust.set(List_Options[0])
    omDust = OptionMenu(mainFrame, dust, *List_Options)
    omDust.grid(row=7, column=1)

    # Occupational Hazard
    lOccHzd = Label(mainFrame, text="Occupational Hazard")
    lOccHzd.grid(row=8, column=0)
    occupationHzd = IntVar()
    occupationHzd.set(List_Options[0])
    omOccHzd = OptionMenu(mainFrame, occupationHzd, *List_Options)
    omOccHzd.grid(row=8, column=1)

    # Geneti Risk
    lGenetic = Label(mainFrame, text="Genetic Risk")
    lGenetic.grid(row=9, column=0)
    genes = IntVar()
    genes.set(List_Options[0])
    omGenetic = OptionMenu(mainFrame, genes, *List_Options)
    omGenetic.grid(row=9, column=1)

    # Chronic Lung Disease
    lChronic = Label(mainFrame, text="Chronic Lung Disease")
    lChronic.grid(row=10, column=0)
    chronic = IntVar()
    chronic.set(List_Options[0])
    omChronic = OptionMenu(mainFrame, chronic, *List_Options)
    omChronic.grid(row=10, column=1)

    # Balanced Diet
    lDiet = Label(mainFrame, text="Balanced Diet")
    lDiet.grid(row=11, column=0)
    diet = IntVar()
    diet.set(List_Options[0])
    omDiet = OptionMenu(mainFrame, diet, *List_Options)
    omDiet.grid(row=11, column=1)

    # Obesity
    lObesity = Label(mainFrame, text="Obesity")
    lObesity.grid(row=12, column=0)
    obesity = IntVar()
    obesity.set(List_Options[0])
    omObesity = OptionMenu(mainFrame, obesity, *List_Options)
    omObesity.grid(row=12, column=1)

    # Smoking
    lSmoke = Label(mainFrame, text="Smoking")
    lSmoke.grid(row=13, column=0)
    smoke = IntVar()
    smoke.set(List_Options[0])
    omSmoke = OptionMenu(mainFrame, smoke, *List_Options)
    omSmoke.grid(row=13, column=1)

    # Chest Pain
    lChestpain = Label(mainFrame, text="Chest Pain")
    lChestpain.grid(row=5, column=2)
    chest = IntVar()
    chest.set(List_Options[0])
    omChest = OptionMenu(mainFrame, chest, *List_Options)
    omChest.grid(row=5, column=3)

    # Choughing of Blood
    lCough = Label(mainFrame, text="Choughing of Blood")
    lCough.grid(row=6, column=2)
    cough = IntVar()
    cough.set(List_Options[0])
    omCough = OptionMenu(mainFrame, cough, *List_Options)
    omCough.grid(row=6, column=3)

    # Fatigue
    lFatigue = Label(mainFrame, text="Fatigue")
    lFatigue.grid(row=7, column=2)
    fatigue = IntVar()
    fatigue.set(List_Options[0])
    omFatigue = OptionMenu(mainFrame, fatigue, *List_Options)
    omFatigue.grid(row=7, column=3)

    # Weight Loss
    lWeightLoss = Label(mainFrame, text="Weight Loss")
    lWeightLoss.grid(row=8, column=2)
    weightloss = IntVar()
    weightloss.set(List_Options[0])
    omWeight = OptionMenu(mainFrame, weightloss, *List_Options)
    omWeight.grid(row=8, column=3)

    # ShortNess Of Breath
    lBreath = Label(mainFrame, text="Shortness of Breath")
    lBreath.grid(row=9, column=2)
    breath = IntVar()
    breath.set(List_Options[0])
    omBreath = OptionMenu(mainFrame, breath, *List_Options)
    omBreath.grid(row=9, column=3)

    # Wheezing
    lWheezing = Label(mainFrame, text="Wheezing")
    lWheezing.grid(row=10, column=2)
    wheezing = IntVar()
    wheezing.set(List_Options[0])
    omWheezing = OptionMenu(mainFrame, wheezing, *List_Options)
    omWheezing.grid(row=10, column=3)

    # Swallowing Difficulty
    lSwallowing = Label(mainFrame, text="Swallowing Difficulty")
    lSwallowing.grid(row=11, column=2)
    swallow = IntVar()
    swallow.set(List_Options[0])
    omSwallow = OptionMenu(mainFrame, swallow, *List_Options)
    omSwallow.grid(row=11, column=3)

    # Frequent Cold
    lFrequentCold = Label(mainFrame, text="Frequent Cold")
    lFrequentCold.grid(row=12, column=2)
    cold = IntVar()
    cold.set(List_Options[0])
    omCold = OptionMenu(mainFrame, cold, *List_Options)
    omCold.grid(row=12, column=3)

    # Dry Cough
    lDryCough = Label(mainFrame, text="Clubbing of Finger Nails")
    lDryCough.grid(row=13, column=2)
    drycough = IntVar()
    drycough.set(List_Options[0])
    omDryCough = OptionMenu(mainFrame, drycough, *List_Options)
    omDryCough.grid(row=13, column=3)


# ============================================================= Form 2 ====================================================================
def OpenWindow():
    form2 = Toplevel()
    form2.lift()
    form2.focus_force()
    form2.grab_set()
    form2.geometry("550x340+350+80")
    form2.title("Selecting a Customer")

    mainFrame = LabelFrame(form2, text="Select Your Name", padx=25, pady=25)
    mainFrame.grid(row=0, column=0, padx=100, pady=30, rowspan=30)

    # ---------------------End: Getting values from Database to insert them into GUI--------------------------
    def openEdit():
        # -----------------------------------------------------Form 4 --------------------------------------------------
        form4 = Toplevel()
        form4.lift()
        form4.focus_force()
        form4.grab_set()
        # form4.resizable(False,False)
        form4.geometry("850x530+300+80")
        form4.title('Cancer Rate Predication System- Update Details')
        mainFrame = LabelFrame(form4, text="Welcome Customer- (Verify Your Info)", padx=10, pady=10)
        mainFrame.grid(row=0, column=0, padx=50, pady=20, rowspan=50)
        helpFrame = LabelFrame(form4, text="How to Select Corrcet Options: ", padx=5)
        helpFrame.place(x=580, y=200)
        personNames = ["Air Pollution", "Alcohol Use", "Dust Allergy", "Occupational Hazard", "Genetic Risk",
                       "Chronic Lung Disease", "Balanced Diet", "Obesity", "Smoking", "Chest Pain",
                       "Choughing of Blood", "Fatigue", "Weigth Loss", "Shortness Of Breath", "Wheezing",
                       "Swallowing Difficulty", "Frequent Cold", "Clubbing of Finger Nails"]  # <- Database Entry

        cbox = ttk.Combobox(helpFrame, state='readonly', values=personNames)
        cbox.grid(row=0, column=0, columnspan=10)

        def cbox_event(evt):
            value = cbox.get()
            index = cbox.current()
            if (index == 0):
                mvar.set(
                    "0=If AQI between 0-50\n\n1=If AQI between 51-100\n\n2=If AQI between 101-150\n\n3=If AQI between 150-200\n\n4=If AQI between 201-300\n\n5=If AQI between 300-350\n\n=If AQI between 350+")
            elif (index == 1):
                mvar.set(
                    "0=No Use\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (At parties, events, etc)\n\n3=If Normal (Few times a month)\n\n4=If Frequent (Multiple times a week)\n\n5=If High (Daily)\n\n6=If Severe(Multiplt times a day) ")
            elif (index == 2):
                mvar.set(
                    "0=No Allergy\n\n1=If Negligible \n\n2=If Slightly Allergic (E.g- A few sneezes)\n\n3=If Properly Allergic(E.g- Itching)\n\n4=If More Allergic(E.g- Running or Stuffy Nose)\n\n5=If Highly Allergic (E.g- Red, itchy or teary eyes)\n\n6=If Severely Allergic(E.g- Wheezing, coughing, tightness in the chest and shortness of breath)")
            elif (index == 3):
                mvar.set(
                    "0=No Risk\n\n1=If Negligible Risk (E.g- At offices with proper Air conditioning)\n\n2=If Slightly High Risk(E.g- At offices near Pollution sources)\n\n3=If Intermediate Risk(E.g- At Argicultural Sites)\n\n4=If More Risk(E.g- At Industries)\n\n5=If High Risk(E.g- At Construction sites)\n\n6=If Severe Risk(E.g- At Chemical Industries, Power Plants, etc) ")
            elif (index == 4):
                mvar.set(
                    "0=No Risk\n\n1=If Negligible Risk (E.g- Family history of minor lung diseases)\n\n2=If Slightly High Risk(E.g-Family history of common lung diseases)\n\n3=If Intermediate Risk(E.g- Family history of Asthama)\n\n4=If More Risk(E.g- Famaily history Asthama, Brochitis)\n\n5=If High Risk(E.g- Family history of TB, Pneumonia)\n\n6=If Severe Risk(E.g- Family History of Lung Cancer)")
            elif (index == 5):
                mvar.set(
                    "0=No Disease\n\n1=If Negligilbe Diseases(E.g- common cough, common cold, etc)\n\n2=If Slightly High Risk Diseases(E.g-chronic cough, chronic cold)\n\n3=If Intermediate Risk Diseases(E.g- Asthama)\n\n4=If More Risk Diseases(E.g- Asbestosis, Brochitis)\n\n5=If High Risk Diseases(E.g- TB, Pneumonia)\n\n6=If Severe Risk Diseases(E.g- COPD)")
            elif (index == 6):
                mvar.set(
                    "0=None \n\n1=If Low\n\n2=If Meduim\n\n3=If Good\n\n=If Well Balanced\n\n5=If Highly Balanced\n\n6=If Perfectly balanced")
            elif (index == 7):
                mvar.set(
                    "0=None (BMI in 18.5 to 22.9)\n\n1=If Low (BMI in 22.9 to 24.9)\n\n2=If Meduim (BMI in 24.9 to 26.9)\n\n3=If Semi-Medium(BMI in 26.9 to 30.9)\n\n4=If High (BMI in 30.9 to 35.9)\n\n5=If Very High (BMI in 35.9 to 39.9)\n\n6=If Severely High (BMI above 40)")
            elif (index == 8):
                mvar.set(
                    "0=No Use\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (At certain occasions)\n\n3=If Normal (Few times a month)\n\n4=If Frequent (Multiple times a week)\n\n5=If High (Daily)\n\n6=If Severe(Multiple times a day)")
            elif (index == 9):
                mvar.set(
                    "0=None\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (Only a few times)\n\n3=If Recurring (Once or twice in a month))\n\n4=If Frequent (Multiple times a month)\n\n5=If High (Multiple times a week)\n\n6=If Severe (Daily)")
            elif (index == 10):
                mvar.set(
                    "0=None\n\n1=If Negligible (Very Rarely)\n\n2=If Occassional (Only a few times)\n\n3=If Recurring (Once or twice in a month))\n\n4=If Frequent (Multiple times a month)\n\n5=If High (Multiple times a week)\n\n6=If Severe (Daily)")
            elif (index == 11):
                mvar.set(
                    "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
            elif (index == 12):
                mvar.set(
                    "0=None\n\n1=If Negligible (1-2 Kg in last 2 months)\n\n2=If Low (2-5 kg in last 2 months)\n\n3=If Medium (5-7 kg in last 2 months)\n\n4=If High (7-8 kg in last 2 months)\n\n5=If Very High (8-10 kg in last 2 months)\n\n6=If Severe (10kg + in last 2 months)")
            elif (index == 13):
                mvar.set(
                    "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
            elif (index == 14):
                mvar.set(
                    "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
            elif (index == 15):
                mvar.set(
                    "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
            elif (index == 16):
                mvar.set(
                    "0=Never\n\n1=If Negligible \n\n2=If Occassional \n\n3=If Recurring\n\n4=If Frequent \n\n5=If High \n\n6=If Severe")
            else:
                mvar.set(
                    "0=None\n\n1=If Negligible (Slight pale color of nails)\n\n2=If Low (More pale color of nails)\n\n3=If Medium (Slight distorted nail angle)\n\n4=If High (More Distorted nail angle)\n\n5=If Very High (Slight Swelling of finger)\n\n6=If Severe (More Swelling of finger)")

        cbox.bind("<<ComboboxSelected>>", cbox_event)
        mvar = StringVar()
        m = Message(helpFrame, textvariable=mvar, width=220)
        m.grid(row=1, column=0)
        # ------------------------Start: Converting list selection tuple to string----------------------------------
        # The list selection is returned as a tuple and below it is converted to string
        actual_list_selection = ''
        for j in selected_value1:
            if j != '(' or j != ')' or j != ',' or j != "'":
                actual_list_selection += j
        # -----------------------End: Converting list selection tuple to string-------------------------------------

        # -----------------------Start: Getting selection ID from database------------------------------------------
        q2 = 'select patient_id from patient where patient_name=?'
        l2 = (actual_list_selection,)
        cursor.execute(q2, l2)
        patient_id = cursor.fetchone()[0]  # the 0th element is id and it is fetched

        # ---------------------End: Getting Selection ID from database----------------------------------------------
        # ---------------------Start: Getting values from Database into variables to insert them into GUI---------------

        id_list = (patient_id,)  # It is needed. It wont work otherwise
        cursor.execute('select * from patient where patient_id=?', id_list)
        resultSet = cursor.fetchall()  # Data fetched fom Database is stored in cursor and here it is taken into list using fetchall() method
        results = []  # resultSet[0] returns a tuple and the value from that tuple is fetched in below for loops and kept here
        for m in resultSet:  # Get individual tuple
            for n in range(1, 24):  # There are 23 values in Database
                results.append(m[n])  # Fetch value from tuple and append put it into list
        # ---------------------Start: Putting values into variables----------------------------------------------------
        patient_name = results[0]
        patient_gender = results[1]
        patient_age = results[2]
        patient_address = results[3]
        mobile_number = results[4]
        air_pollution = results[5]
        alcohol_use = results[6]
        dust_allergy = results[7]
        occupational_hazard = results[8]
        genetic_risk = results[9]
        chronic_lung_disease = results[10]
        balanced_diet = results[11]
        p_obesity = results[12]
        smoking = results[13]
        chest_pain = results[14]
        coughing_of_blood = results[15]
        p_fatigue = results[16]
        weight_loss = results[17]
        shortness_of_breath = results[18]
        p_wheezing = results[19]
        swallowing = results[20]
        frequent_cold = results[21]
        dry_cough = results[22]

        # ---------------------End:Putting values into variables-------------------------------------------------------
        # ---------------------End: Getting values from Database into variables to insert them into GUI-------------

        # ----------------Event Handling-------------------

        def SaveData():
            # -----------------------Start: open/edit to Database.------------------------------------------------------
            # ---------------------Start: Updating the database---------------------------------------------------------
            patient_name = name.get()
            patient_gender = "Male" if (gender.get() == 1) else "Female"
            patient_age = int(sAge.get())
            patient_address = eAddress.get()
            mobile_number = int(mobile.get())
            air_pollution = int(air.get())
            alcohol_use = int(alcohol.get())
            dust_allergy = int(dust.get())
            occupational_hazard = int(occupationHzd.get())
            genetic_risk = int(genes.get())
            chronic_lung_disease = int(chronic.get())
            balanced_diet = int(diet.get())
            p_obesity = int(obesity.get())
            smoking = int(smoke.get())
            chest_pain = int(chest.get())
            coughing_of_blood = int(cough.get())
            p_fatigue = int(fatigue.get())
            weight_loss = int(weightloss.get())
            shortness_of_breath = int(breath.get())
            p_wheezing = int(wheezing.get())
            swallowing = int(swallow.get())
            frequent_cold = int(cold.get())
            dry_cough = int(drycough.get())

            # -------------End:Getting input from user-------------------------------------------------
            # -----------------------------Database insertion below------------------------------------

            def updating_database():  # function defined to execute query. It wont work without function.
                query = "update patient set patient_name=?, patient_gender=?, patient_age=?, patient_address=?, " \
                        "mobile_number=?," \
                        "air_pollution=?, alcohol_use=?, dust_allergy=?, occupational_hazard=?, genetic_risk=?," \
                        "chronic_lung_disease=?, balanced_diet=?, obesity=?, smoking=?, chest_pain=?, " \
                        "coughing_of_blood=?, fatigue=?," \
                        "weight_loss=?, shortness_of_breath=?, wheezing=?, swallowing=?, frequent_cold=?,dry_cough=? " \
                        "where patient_id = ? "

                values = (
                    patient_name, patient_gender, patient_age, patient_address, mobile_number, air_pollution,
                    alcohol_use,
                    dust_allergy, occupational_hazard, genetic_risk, chronic_lung_disease, balanced_diet, p_obesity,
                    smoking,
                    chest_pain, coughing_of_blood, p_fatigue, weight_loss, shortness_of_breath, p_wheezing, swallowing,
                    frequent_cold, dry_cough, patient_id)

                cursor.execute(query, values)
                database.commit()
                messagebox.showinfo("Success!!", "Data Updated Successfully!")

            # ---------------------------------------Database insertion Completed---------------------------------------
            updating_database()  # function defined above is called. It wont work without function.

            # ---------------------End: Updating the Database-----------------------------------------------------------

            Edit.configure(state='normal')
            Save.configure(state='disabled')
            for child in mainFrame.winfo_children():
                child.configure(state='disabled')

        def EditData():
            # --------------Enabling the Details
            Save.configure(state='disabled')
            Edit.configure(state='disabled')
            Check.configure(state='normal')
            for child in mainFrame.winfo_children():
                child.configure(state='normal')

        # ---------------------------------

        def VerifyData():
            Temp = True
            n = name.get()
            regex = "^[A-Za-z\s]{3,20}$"
            if re.search(regex, n):
                errorName.set("")
            else:
                Temp = False
                errorName.set("Please Enter Correct Name")

            age = sAge.get()
            if (type(int(age)) == type(1)):
                age = int(age)
                if (age > 0 and age <= 100):
                    errorAge.set("")
                else:
                    Temp = False
                    errorAge.set("Please Enter Valid Age")
            else:
                Temp = False
                errorAge.set("Only number Allowed are Allowed in Age")

            eaddress = address.get()
            regex = "^[A-Za-z0-9'\.\-\s\,\=]{10,50}$"
            if re.search(regex, eaddress):
                errorAddress.set("")
            else:
                Temp = False
                errorAddress.set("Please Enter Correct Address")

            phonenumber = mobile.get()
            regex = "^\d{10}$"
            if re.search(regex, phonenumber):
                errorMobile.set("")
            else:
                Temp = False
                errorMobile.set("Please Enter Correct phone number")

            if (Temp):
                messagebox.showinfo("Verified!!", "Entered data is correct!")
                for child in mainFrame.winfo_children():
                    child.configure(state='disabled')
                Save.configure(state='normal')
                Check.configure(state='disabled')
                Edit.configure(state='normal')

                # ----------------!Event Handling -------------------

        Edit = Button(form4, text="Edit My Details", command=EditData, width=15)
        Edit.place(x=580, y=30)

        Check = Button(form4, text="Validate Data", command=VerifyData, width=15)
        Check.place(x=580, y=70)

        # Edit.grid(row=4, column=1)
        Save = Button(form4, text="Save Changes", command=SaveData, width=15)
        Save.place(x=580, y=110)
        # Save.grid(row=6, column=1)

        Exit = Button(form4, text="Close Window", command=form4.destroy, width=15)
        Exit.place(x=580, y=150)
        # Exit.grid(row=8, column=1)

        # Name
        lName = Label(mainFrame, text="Name")
        lName.grid(row=0, column=0)
        errorName = StringVar()
        errName = Label(mainFrame, textvariable=errorName, fg='red')
        errName.grid(row=0, column=2)
        name = StringVar()
        eName = Entry(mainFrame, textvariable=name, width=20)
        eName.grid(row=0, column=1)

        # Gender
        lGender = Label(mainFrame, text="Gender")
        lGender.grid(row=1, column=0)
        gender = IntVar()
        rMale = Radiobutton(mainFrame, text="Male", variable=gender, value=1)
        rFemale = Radiobutton(mainFrame, text="Female", variable=gender, value=2)
        rMale.grid(row=1, column=1)
        rFemale.grid(row=1, column=2)

        # Age
        lAge = Label(mainFrame, text="Age")
        lAge.grid(row=2, column=0)
        errorAge = StringVar()
        errAge = Label(mainFrame, textvariable=errorAge, fg='red')
        errAge.grid(row=2, column=2)
        age = StringVar()
        sAge = Spinbox(mainFrame, from_=1, to=100, width=18, textvariable=age)
        sAge.grid(row=2, column=1)

        # Address
        lAddress = Label(mainFrame, text="Address")
        lAddress.grid(row=3, column=0)
        errorAddress = StringVar()
        errAddress = Label(mainFrame, textvariable=errorAddress, fg='red')
        errAddress.grid(row=3, column=2)
        address = StringVar()
        eAddress = Entry(mainFrame, width=18, textvariable=address)
        eAddress.grid(row=3, column=1)

        # Mobile
        lMobile = Label(mainFrame, text="Mobile Number")
        lMobile.grid(row=4, column=0)
        errorMobile = StringVar()
        errMobile = Label(mainFrame, textvariable=errorMobile, fg='red')
        errMobile.grid(row=4, column=2)
        mobile = StringVar()
        eMobile = Entry(mainFrame, textvariable=mobile)
        eMobile.grid(row=4, column=1)

        # Common List
        List_Options = [0, 1, 2, 3, 4, 5, 6]
        # Air Pollution
        lAir = Label(mainFrame, text="Air Pollution")
        lAir.grid(row=5, column=0)
        air = IntVar()
        air.set(List_Options[0])
        omAirPollution = OptionMenu(mainFrame, air, *List_Options)
        omAirPollution.grid(row=5, column=1)

        # Alcohol USe
        lAlcohol = Label(mainFrame, text="Alcohol Use")
        lAlcohol.grid(row=6, column=0)
        alcohol = IntVar()
        alcohol.set(List_Options[0])
        omAlcohol = OptionMenu(mainFrame, alcohol, *List_Options)
        omAlcohol.grid(row=6, column=1)

        # Dust Allergy
        lDustAllergy = Label(mainFrame, text="Dust Allergy")
        lDustAllergy.grid(row=7, column=0)
        dust = IntVar()
        dust.set(List_Options[0])
        omDust = OptionMenu(mainFrame, dust, *List_Options)
        omDust.grid(row=7, column=1)

        # Occupational Hazard
        lOccHzd = Label(mainFrame, text="Occupational Hazard")
        lOccHzd.grid(row=8, column=0)
        occupationHzd = IntVar()
        occupationHzd.set(List_Options[0])
        omOccHzd = OptionMenu(mainFrame, occupationHzd, *List_Options)
        omOccHzd.grid(row=8, column=1)

        # Geneti Risk
        lGenetic = Label(mainFrame, text="Genetic Risk")
        lGenetic.grid(row=9, column=0)
        genes = IntVar()
        genes.set(List_Options[0])
        omGenetic = OptionMenu(mainFrame, genes, *List_Options)
        omGenetic.grid(row=9, column=1)

        # Chronic Lung Disease
        lChronic = Label(mainFrame, text="Chronic Lung Disease")
        lChronic.grid(row=10, column=0)
        chronic = IntVar()
        chronic.set(List_Options[0])
        omChronic = OptionMenu(mainFrame, chronic, *List_Options)
        omChronic.grid(row=10, column=1)

        # Balanced Diet
        lDiet = Label(mainFrame, text="Balanced Diet")
        lDiet.grid(row=11, column=0)
        diet = IntVar()
        diet.set(List_Options[0])
        omDiet = OptionMenu(mainFrame, diet, *List_Options)
        omDiet.grid(row=11, column=1)

        # Obesity
        lObesity = Label(mainFrame, text="Obesity")
        lObesity.grid(row=12, column=0)
        obesity = IntVar()
        obesity.set(List_Options[0])
        omObesity = OptionMenu(mainFrame, obesity, *List_Options)
        omObesity.grid(row=12, column=1)

        # Smoking
        lSmoke = Label(mainFrame, text="Smoking")
        lSmoke.grid(row=13, column=0)
        smoke = IntVar()
        smoke.set(List_Options[0])
        omSmoke = OptionMenu(mainFrame, smoke, *List_Options)
        omSmoke.grid(row=13, column=1)

        # Chest Pain
        lChestpain = Label(mainFrame, text="Chest Pain")
        lChestpain.grid(row=5, column=2)
        chest = IntVar()
        chest.set(List_Options[0])
        omChest = OptionMenu(mainFrame, chest, *List_Options)
        omChest.grid(row=5, column=3)

        # Choughing of Blood
        lCough = Label(mainFrame, text="Choughing of Blood")
        lCough.grid(row=6, column=2)
        cough = IntVar()
        cough.set(List_Options[0])
        omCough = OptionMenu(mainFrame, cough, *List_Options)
        omCough.grid(row=6, column=3)

        # Fatigue
        lFatigue = Label(mainFrame, text="Fatigue")
        lFatigue.grid(row=7, column=2)
        fatigue = IntVar()
        fatigue.set(List_Options[0])
        omFatigue = OptionMenu(mainFrame, fatigue, *List_Options)
        omFatigue.grid(row=7, column=3)

        # Weight Loss
        lWeightLoss = Label(mainFrame, text="Weight Loss")
        lWeightLoss.grid(row=8, column=2)
        weightloss = IntVar()
        weightloss.set(List_Options[0])
        omWeight = OptionMenu(mainFrame, weightloss, *List_Options)
        omWeight.grid(row=8, column=3)

        # ShortNess Of Breath
        lBreath = Label(mainFrame, text="Shortness of Breath")
        lBreath.grid(row=9, column=2)
        breath = IntVar()
        breath.set(List_Options[0])
        omBreath = OptionMenu(mainFrame, breath, *List_Options)
        omBreath.grid(row=9, column=3)

        # Wheezing
        lWheezing = Label(mainFrame, text="Wheezing")
        lWheezing.grid(row=10, column=2)
        wheezing = IntVar()
        wheezing.set(List_Options[0])
        omWheezing = OptionMenu(mainFrame, wheezing, *List_Options)
        omWheezing.grid(row=10, column=3)

        # Swallowing Difficulty
        lSwallowing = Label(mainFrame, text="Swallowing Difficulty")
        lSwallowing.grid(row=11, column=2)
        swallow = IntVar()
        swallow.set(List_Options[0])
        omSwallow = OptionMenu(mainFrame, swallow, *List_Options)
        omSwallow.grid(row=11, column=3)

        # Frequent Cold
        lFrequentCold = Label(mainFrame, text="Frequent Cold")
        lFrequentCold.grid(row=12, column=2)
        cold = IntVar()
        cold.set(List_Options[0])
        omCold = OptionMenu(mainFrame, cold, *List_Options)
        omCold.grid(row=12, column=3)

        # Dry Cough
        lDryCough = Label(mainFrame, text="Clubbing of Finger Nails")
        lDryCough.grid(row=13, column=2)
        drycough = IntVar()
        drycough.set(List_Options[0])
        omDryCough = OptionMenu(mainFrame, drycough, *List_Options)
        omDryCough.grid(row=13, column=3)

        # --------------------Start: Setting GUI fields values---------------------------------------------------------

        name.set(patient_name)
        tgender = 1 if (patient_gender == "Male") else 2  # Converting Yes, No to 1, 2 as radiobutton is
        # selected on the basis 1, 2 values
        rMale.select() if (tgender == 1) else rFemale.select()  # Setting Radiobutton value
        age.set(patient_age)  # setting value to GUI fetched from database at the beginning of OpenEdit()
        address.set(patient_address)  # setting value to GUI fetched from database at the beginning of OpenEdit()
        mobile.set(mobile_number)  # setting value to GUI fetched from database at the beginning of OpenEdit()
        air.set(air_pollution)  # Converting Yes, No to 1, 2 as radiobutton is selected on the
        alcohol.set(alcohol_use)
        dust.set(dust_allergy)
        occupationHzd.set(occupational_hazard)
        genes.set(genetic_risk)
        chronic.set(chronic_lung_disease)
        diet.set(balanced_diet)
        obesity.set(p_obesity)
        smoke.set(smoking)
        chest.set(chest_pain)
        cough.set(coughing_of_blood)
        fatigue.set(p_fatigue)
        weightloss.set(weight_loss)
        breath.set(shortness_of_breath)
        wheezing.set(p_wheezing)
        swallow.set(swallowing)
        cold.set(frequent_cold)
        drycough.set(dry_cough)
        # --------------------Start: Setting GUI fields values---------------------------------------------------------

        # ----------------Disabling Fields

        for child in mainFrame.winfo_children():
            child.configure(state='disabled')
        Save.configure(state='disabled')
        Check.configure(state='disabled')

    # --------------------------------

    # form4.mainloop()
    # ---------------------------------------------------------------------------------------------------------------

    Open_Edit = Button(form2, text="Open/Edit", command=openEdit, width=15)
    Open_Edit.grid(row=5, column=1)
    Open_Edit.configure(state='disabled')

    Exit = Button(form2, text="Exit Window", command=form2.destroy, width=15)
    Exit.grid(row=10, column=1)

    frame = Frame(mainFrame)
    frame.pack()
    List = Listbox(frame)
    List.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=List.yview)
    scrollbar.pack(side="right", fill="y")

    List.config(yscrollcommand=scrollbar.set)
    # ----------------------------------------Start:Database to Persons name List--------------------------------------
    que = "select patient_name from patient"
    cursor.execute(que)

    personNames = cursor.fetchall()
    for pname in personNames:
        List.insert(END, pname)

    # --------------------------------------End:Database to Persons name List----------------------------------------
    # ---List Box Events

    def onListSelect(evt):  # default argument- event object by tkinter
        Open_Edit.configure(state='normal')
        w = evt.widget
        selected_index = int(w.curselection()[0])
        myselected_value = w.get(selected_index)
        global selected_value1
        selected_value1 = myselected_value
        # print("You Selected item", (selected_index, globals()[myselected_value]))

    List.bind('<<ListboxSelect>>', onListSelect)


def AnalyseWindow():
    # =============================================== form3 ==================================================================================
    form3 = Toplevel()
    form3.lift()
    form3.focus_force()
    form3.grab_set()
    form3.geometry("580x340+350+80")
    form3.title("Selecting a Customer")

    mainFrame = LabelFrame(form3, text="Select Your Name", padx=25, pady=25)
    mainFrame.grid(row=0, column=0, padx=100, pady=30, rowspan=30)
    analyseFrame = LabelFrame(form3, text="Your Result", padx=20, pady=20)

    analyseFrame.place(x=375, y=150)
    mvar = StringVar()
    temp = Message(analyseFrame, textvariable=mvar, width=130)
    temp.pack()

    def analyseData():

        print("Analyse Data")
        actual_list_selection = ''
        for j in globals()[selected_value2]:
            if j != '(' or j != ')' or j != ',' or j != "'":
                actual_list_selection += j
        # -----------------------End: Converting list selection tuple to string-------------------------------------

        # -----------------------Start: Getting selection ID from database------------------------------------------
        q2 = 'select patient_id from patient where patient_name=?'
        l2 = (actual_list_selection,)
        print("LookHere", cursor.execute(q2, l2))

        patient_id = cursor.fetchone()[0]  # the 0th element is id and it is fetched

        # ---------------------End: Getting Selection ID from database----------------------------------------------

        # ---------------------Start: Getting values from Database into variables to feed them to algorithm-------------

        id_list = (patient_id,)  # It is needed. It wont work otherwise
        cursor.execute('select * from patient where patient_id=?', id_list)
        resultSet = cursor.fetchall()  # Data fetched fom Database is stored in cursor and here it is taken into list using fetchall() method
        results = []  # resultSet[0] returns a tuple and the value from that tuple is fetched in below for loops and kept here
        for m in resultSet:  # Get individual tuple
            for n in range(1, 24):  # There are 23 values in Database
                results.append(m[n])  # Fetch value from tuple and append put it into list
        # ---------------------Start: Putting values into variables----------------------------------------------------
        patient_name = results[0]
        patient_gender = results[1]
        patient_age = results[2]
        patient_address = results[3]
        mobile_number = results[4]
        air_pollution = results[5]
        alcohol_use = results[6]
        dust_allergy = results[7]
        occupational_hazard = results[8]
        genetic_risk = results[9]
        chronic_lung_disease = results[10]
        balanced_diet = results[11]
        p_obesity = results[12]
        smoking = int(results[13])
        chest_pain = results[14]
        coughing_of_blood = results[15]
        p_fatigue = results[16]
        weight_loss = results[17]
        shortness_of_breath = results[18]
        p_wheezing = results[19]
        swallowing = results[20]
        frequent_cold = results[21]
        dry_cough = results[22]

        if smoking > 2:
            if coughing_of_blood > 5:
                tx1 = "Severe \n\nProbablity of cancer ocuurence is very high. You may already have cancer. Immediate Measures are highly recommended."
            else:
                tx1 = "High \n\nProbablity of cancer occurence is high. Medical checkup and change in attributes is highly recommended."
        else:
            if air_pollution > 2:
                tx1 = "Medium \n\nProbablity of cancer occurence is slightly more. You may need to perform a medical checkup."
            else:
                if p_obesity > 2:
                    if chronic_lung_disease > 3:
                        tx1 = "High\n\nProbablity of cancer occurence is high. Medical checkup and change in attributes is highly recommended."
                    else:
                        tx1 = "Meduim\n\n Probablity of cancer occurence is slightly more. You may need to perform a medical checkup."
                else:
                    if swallowing > 3:
                        if dry_cough > 2:
                            tx1 = "Medium\n\n Probablity of cancer occurence is slightly more. You may need to perform a medical checkup."
                        else:
                            tx1 = "Low\n\nProbablity of cancer occurence is low. No measures are required."
                    else:
                        tx1 = "Low\n\nProbablity of cancer occurence is low. No measures are required."

        mvar.set("Cancer Level: " + tx1)

        # ---------------------End:Putting values into variables-------------------------------------------------------

        # ---------------------End: Getting values from Database into variables to feed them to algorithm-------------

    Button_Analyse = Button(form3, text="Analyse Data", command=analyseData, width=15)
    Button_Analyse.grid(row=4, column=1, columnspan=2)

    Exit = Button(form3, text="Exit Window", command=form3.destroy, width=15)
    Exit.grid(row=6, column=1, columnspan=2)

    frame = Frame(mainFrame)
    frame.pack()
    List = Listbox(frame)
    List.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=List.yview)
    scrollbar.pack(side="right", fill="y")

    List.config(yscrollcommand=scrollbar.set)

    # ---------------------Start:Databaase to List---------------------------------------------------------------------

    cursor.execute('select patient_name from patient')
    resultSet = cursor.fetchall()

    # personNames = ["person A", "person B", "person C", "person D", "person E"]  # <- Database Entry
    for pname in resultSet:
        List.insert(END, pname)

    # ---------------------End:Databaase to List-----------------------------------------------------------------------
    # ---List Box Events
    def onListSelect(evt):  # default argument- event object by tkinter
        Button_Analyse.configure(state='normal')
        w = evt.widget
        index = int(w.curselection()[0])
        globals()[selected_value2] = w.get(
            index)  # Putting List selection into variable for accessing it above. Accessing global variable. This is
        # the only method.

    #        print("You Selected item %d: ?" % (index, globals()[selected_value2]))

    List.bind('<<ListboxSelect>>', onListSelect)
    # -----------------------
    Button_Analyse.configure(state='disabled')


# form3.mainloop()
# =================================================================================================================================
# =================================================================================================================================
def AskWindow():
    print("Window Question")


def AboutWindow():
    about_win = Toplevel()
    about_win.grab_set()
    about_win.overrideredirect(True)
    about_win.resizable(False, False)
    about_win.geometry("650x500+300+80")

    # 1. Load Image
    loadImg = Image.open("about.png")
    render = ImageTk.PhotoImage(loadImg)

    # 2. Associate it with a label
    backImg = Label(about_win, image=render)
    backImg.image = render
    backImg.pack()
    button = Button(about_win, text="X", bg="red", command=about_win.destroy)
    button.place(x=590, y=10)


# Adding Background Image
# 1. Load Image
root.configure(background='black')
loadImg = Image.open("LungImg.png")
render = ImageTk.PhotoImage(loadImg)

# 2. Associate it with a label
backImg = Label(root, image=render)
backImg.image = render
backImg.pack()

# --------------Menu-------------------------
menubar = Menu(root)
root.config(menu=menubar)

# file
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Insert", command=InsertWindow)
fileMenu.add_command(label="Open/Edit", command=OpenWindow)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)

# tools
toolMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tool", menu=toolMenu)

toolMenu.add_command(label="Analyse", command=AnalyseWindow)

# Help
helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)

helpMenu.add_command(label="About", command=AboutWindow)
helpMenu.add_command(label="AskQuestions", command=AskWindow)
# ------------------!Menu-----------------------------------


# ------------------LabelFrame----------------------------------

panel = LabelFrame(root, bg="#6e8cb5")
# 1f042b
panel.place(x=180, y=180, height=300, width=1000)

# Label Text  of Button
buttonFont = font.Font(weight="bold", family="Times New Roman", size=20)

insertButton = Button(panel, text="INSERT", command=InsertWindow, width=12)
insertButton.place(x=90, y=120)
insertButton['font'] = buttonFont

openButton = Button(panel, text="OPEN/EDIT", command=OpenWindow, width=12)
openButton.place(x=400, y=120)
openButton['font'] = buttonFont

analyseButton = Button(panel, text="ANALYSE", command=AnalyseWindow, width=12)
analyseButton.place(x=720, y=120)
analyseButton['font'] = buttonFont

# ------------------!PanedWindow----------------------------------
root.mainloop()
