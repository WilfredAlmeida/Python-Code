from tkinter import *
import mysql.connector
from mysql import *
from numpy.distutils.fcompiler import none
from numpy import array

# -------------------Start:DATABASE and variables declaration-----------------------------------------------------------

# ------------------------------Start:Connection--------------------------------
database = mysql.connector.connect(host="localhost", user="root", passwd="", database="capstone")
# ------------------------------End:Connection--------------------------------

# ------------------Start:cursor to database----------------------
cursor = database.cursor(buffered=True)  # this will execute query using its execute() method.
# ------------------End:cursor to database--------------------

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

selected_value1 = ""

# -------------------End:Variables Declaration-----------------------------

# --------------------End:DATABASE--------------------------------------------------------------------------------------
root = Tk()
root.title('Cancer Rate Predication System-Home Page')
root.state('zoomed')


def InsertWindow():
    # =================================================== Form 1 ======================================================

    # ------StackOverflow
    form1 = Toplevel()
    form1.lift()
    form1.focus_force()
    form1.grab_set()
    form1.grab_release()
    # ---------------------
    form1.geometry("650x500+300+80")
    form1.title('Cancer Rate Predication System- Insert Details')

    mainFrame = LabelFrame(form1, text="Customer Details", padx=10, pady=10)
    mainFrame.grid(row=0, column=0, padx=50, pady=20, rowspan=50)

    # ----------------Event Handling-------------------

    def SaveData():
        # -----------------------Begin:Getting input from GUI to variables-------------------------------
        patient_name = name.get()

        patient_gender = "Male" if (gender.get() == 1) else "Female"

        patient_age = int(sAge.get())

        patient_address = eAddress.get(1.0, END)

        mobile_number = int(mobile.get())

        air_pollution = air.get()

        alcohol_use = alcohol.get()

        dust_allergy = dust.get()

        occupational_hazard = occupationHzd.get() 

        genetic_risk = genes.get()

        chronic_lung_disease = chronic.get()

        balanced_diet = diet.get()

        p_obesity = obesity.get()

        smoking = smoke.get()

        chest_pain = chest.get() 

        coughing_of_blood = cough.get() 

        p_fatigue = fatigue.get()

        weight_loss = weightloss.get()

        shortness_of_breath =breath.get()

        p_wheezing = wheezing.get() 

        swallowing = swallow.get()

        frequent_cold = cold.get() 

        dry_cough = drycough.get() 

        # -------------End:Getting input from user-------------------------------------------------
        # -----------------------------Database insertion below------------------------------------

        def insert_into_database():  # function defined to execute query. It wont work without function.
            query = "INSERT INTO patient (patient_name, patient_gender, patient_age, patient_address, mobile_number," \
                    "air_pollution, alcohol_use, dust_allergy, occupational_hazard, genetic_risk," \
                    "chronic_lung_disease, balanced_diet, obesity, smoking, chest_pain, coughing_of_blood, fatigue," \
                    "weight_loss, shortness_of_breath, wheezing, swallowing, frequent_cold,dry_cough) VALUES (%s,%s," \
                    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            values = (
                patient_name, patient_gender, patient_age, patient_address, mobile_number, air_pollution, alcohol_use,
                dust_allergy, occupational_hazard, genetic_risk, chronic_lung_disease, balanced_diet, p_obesity,
                smoking,
                chest_pain, coughing_of_blood, p_fatigue, weight_loss, shortness_of_breath, p_wheezing, swallowing,
                frequent_cold, dry_cough)

            cursor.execute(query, values)
            database.commit()

        # ---------------------------------------Database insertion Completed------------------------------------------
        insert_into_database()  # function defined above is called. It wont work without function.

    # ---------------------End:Getting input from GUI to variables and putting into database---------------------------

    # ----------------!Event Handling -------------------

    Submit = Button(form1, text="Save and Submit", command=SaveData)
    Submit.grid(row=4, column=1)
    Exit = Button(form1, text="Close Window", command=form1.destroy)  # destroy because quit stops mainloop
    Exit.grid(row=6, column=1)

    # Name
    lName = Label(mainFrame, text="Name")
    lName.grid(row=0, column=0)

    name = StringVar()
    eName = Entry(mainFrame, textvariable=name)
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

    sAge = Spinbox(mainFrame, from_=1, to=100)
    sAge.grid(row=2, column=1)

    # Address
    lAddress = Label(mainFrame, text="Address")
    lAddress.grid(row=3, column=0)

    eAddress = Text(mainFrame, width=15, height=2)
    eAddress.grid(row=3, column=1)

    # Mobile
    lMobile = Label(mainFrame, text="Mobile Number")
    lMobile.grid(row=4, column=0)

    mobile = StringVar()
    eMobile = Entry(mainFrame, textvariable=mobile)
    eMobile.grid(row=4, column=1)

    #Common List
    List_Options=[0,1,2,3,4,5,6]
    # Air Pollution
    lAir = Label(mainFrame, text="Air Pollution")
    lAir.grid(row=5, column=0)

    air = IntVar()
    air.set(List_Options[0])

    omAirPollution=OptionMenu(mainFrame,air,*List_Options)
    omAirPollution.grid(row=5,column=1)

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
    dust.set(List_Options)
        
    omDust = OptionMenu(mainFrame, dust, *List_Options)
    omDust.grid(row=7, column=1)

    # Occupational Hazard
    lOccHzd = Label(mainFrame, text="Occupational Hazard")
    lOccHzd.grid(row=8, column=0)

    occupationHzd = IntVar()
    occupationHzd.set(List_Options[0])

    omOccHzd=OptionMenu(mainFrame,occupationHzd,*List_Options)
    omOccHzd.grid(row=8, column=1)

    # Geneti Risk
    lGenetic = Label(mainFrame, text="Genetic Risk")
    lGenetic.grid(row=9, column=0)

    genes = IntVar()
    genes.set(List_Options[0])

    omGenetic=OptionMenu(mainFrame,genes,*List_Options)
    omGenetic.grid(row=9, column=1)

    # Chronic Lung Disease
    lChronic = Label(mainFrame, text="Chronic Lung Disease")
    lChronic.grid(row=10, column=0)

    chronic = IntVar()
    chronic.set(List_Options[0])

    omChronic=OptionMenu(mainFrame,chronic,*List_Options)
    omChronic.grid(row=10, column=1)

    # Balanced Diet
    lDiet = Label(mainFrame, text="Balanced Diet")
    lDiet.grid(row=11, column=0)

    diet = IntVar()
    dust.set(List_Options[0])

    omDiet=OptionMenu(mainFrame,dust,*List_Options)
    omDiet.grid(row=11, column=1)


    # Obesity
    lObesity = Label(mainFrame, text="Obesity")
    lObesity.grid(row=12, column=0)

    obesity = IntVar()
    obesity.set(List_Options[0])

    omObesity=OptionMenu(mainFrame,obesity,*List_Options)
    omObesity.grid(row=12, column=1)

    # Smoking
    lSmoke = Label(mainFrame, text="Smoking")
    lSmoke.grid(row=13, column=0)

    smoke = IntVar()
    smoke.set(List_Options[0])

    omSmoke = OptionMenu(mainFrame, smoke, *List_Options)
    omSmoke.grid(row=13, column=1)

    # Chest Pain
    lChestpain = Label(mainFrame, text="ChestPain")
    lChestpain.grid(row=5, column=2)

    chest = IntVar()
    chest.set(List_Options[0])

    omChest=OptionMenu(mainFrame,chest,*List_Options)
    omChest.grid(row=5, column=3)

    # Choughing of Blood
    lCough = Label(mainFrame, text="Choughing of Blood")
    lCough.grid(row=6, column=2)

    cough = IntVar()
    cough.set(List_Options[0])

    omCough=OptionMenu(mainFrame,cough,*List_Options)
    omCough.grid(row=6, column=3)

    # Fatigue
    lFatigue = Label(mainFrame, text="Fatigue")
    lFatigue.grid(row=7, column=2)

    fatigue = IntVar()
    fatigue.set(List_Options[0])

    omFatigue=OptionMenu(mainFrame,fatigue,*List_Options)
    omFatigue.grid(row=7, column=3)


    # Weight Loss
    lWeightLoss = Label(mainFrame, text="Weight Loss")
    lWeightLoss.grid(row=8, column=2)

    weightloss = IntVar()
    weightloss.set(List_Options[0])
    
    omWeight=OptionMenu(mainFrame,weightloss,*List_Options)
    omWeight.grid(row=8, column=3)

    # ShortNess Of Breath
    lBreath = Label(mainFrame, text="ShortNess of Breath")
    lBreath.grid(row=9, column=2)

    breath = IntVar()
    breath.set(List_Options[0])

    omBreath=OptionMenu(mainFrame,breath,*List_Options)
    omBreath.grid(row=9, column=3)

    # Wheezing
    lWheezing = Label(mainFrame, text="Wheezing")
    lWheezing.grid(row=10, column=2)

    wheezing = IntVar()
    wheezing.set(List_Options[0])

    omWheezing=OptionMenu(mainFrame,wheezing,*List_Options)
    omWheezing.grid(row=10, column=3)

    # Swallowing Difficulty
    lSwallowing = Label(mainFrame, text="Swoolnig Difficulty")
    lSwallowing.grid(row=11, column=2)

    swallow = IntVar()
    swallow.set(List_Options[0])

    omSwallow=OptionMenu(mainFrame,swallow,*List_Options)
    omSwallow.grid(row=11, column=3)

    # Frequent Cold
    lFrequentCold = Label(mainFrame, text="Frequent Cold")
    lFrequentCold.grid(row=12, column=2)

    cold = IntVar()
    cold.set(List_Options[0])

    omCold=OptionMenu(mainFrame,cold,*List_Options)
    omCold.grid(row=12, column=3)

    # Dry Cough
    lDryCough = Label(mainFrame, text="Dry Cough")
    lDryCough.grid(row=13, column=2)

    drycough = IntVar()
    drycough.set(List_Options[0])

    omDryCough=OptionMenu(mainFrame,drycough,*List_Options)
    omDryCough.grid(row=13, column=3)



# form1.mainloop()

# ============================================================= Form 2 ====================================================================
def OpenWindow():
    form2 = Toplevel()
    form2.lift()
    form2.focus_force()
    form2.grab_set()
    form2.grab_release()
    form2.geometry("550x580+350+80")
    form2.title("Selecting a Customer")

    mainFrame = LabelFrame(form2, text="Select Your Name", padx=35, pady=35)
    mainFrame.grid(row=0, column=0, padx=120, pady=50, rowspan=50)

    # ---------------------End: Getting values from Database to insert them into GUI--------------------------
    def openEdit():

        # -----------------------------------------------------Form 4 --------------------------------------------------
        form4 = Toplevel()
        form4.lift()
        form4.focus_force()
        form4.grab_set()
        form4.grab_release()
        form4.geometry("650x500+300+80")
        form4.title('Cancer Rate Predication System- Insert Details')

        mainFrame = LabelFrame(form4, text="Welcome Customer- (Verify Your Info)", padx=10, pady=10)
        mainFrame.grid(row=0, column=0, padx=50, pady=20, rowspan=50)

        # ------------------------Start: Converting list selection tuple to string----------------------------------
        # The list selection is returned as a tuple and below it is converted to string
        actual_list_selection = ''
        for j in selected_value1:
            if j != '(' or j != ')' or j != ',' or j != "'":
                actual_list_selection += j
        # -----------------------End: Converting list selection tuple to string-------------------------------------

        # -----------------------Start: Getting selection ID from database------------------------------------------
        q2 = 'select patient_id from patient where patient_name=%s'
        l2 = (actual_list_selection,)
        cursor.execute(q2, l2)
        patient_id = cursor.fetchone()[0]  # the 0th element is id and it is fetched

        # ---------------------End: Getting Selection ID from database----------------------------------------------

        # ---------------------Start: Getting values from Database into variables to insert them into GUI---------------

        id_list = (patient_id,)  # It is needed. It wont work otherwise
        cursor.execute('select * from patient where patient_id=%s', id_list)
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

        # ----------------Event Handling-------------------

        def SaveData():
            # -----------------------Start: open/edit to Database.------------------------------------------------------

            # ---------------------Start: Updating the database---------------------------------------------------------

            patient_name = name.get()

            patient_gender = "Male" if (gender.get() == 1) else "Female"

            patient_age = int(sAge.get())

            patient_address = eAddress.get()

            mobile_number = int(mobile.get())

            air_pollution = air.get()

            alcohol_use = alcohol.get()

            dust_allergy = dust.get()

            occupational_hazard = occupationHzd.get()

            genetic_risk = genes.get()

            chronic_lung_disease = chronic.get() 

            balanced_diet = diet.get()

            p_obesity = obesity.get()

            smoking = smoke.get()

            chest_pain = chest.get() 

            coughing_of_blood = cough.get()

            p_fatigue = fatigue.get()

            weight_loss = weightloss.get()

            shortness_of_breath = breath.get()

            p_wheezing = wheezing.get()

            swallowing = swallow.get()

            frequent_cold = cold.get() 

            dry_cough = drycough.get()

            # -------------End:Getting input from user-------------------------------------------------
            # -----------------------------Database insertion below------------------------------------

            def updating_database():  # function defined to execute query. It wont work without function.
                query = "update patient set patient_name=%s, patient_gender=%s, patient_age=%s, patient_address=%s, mobile_number=%s," \
                        "air_pollution=%s, alcohol_use=%s, dust_allergy=%s, occupational_hazard=%s, genetic_risk=%s," \
                        "chronic_lung_disease=%s, balanced_diet=%s, obesity=%s, smoking=%s, chest_pain=%s, coughing_of_blood=%s, fatigue=%s," \
                        "weight_loss=%s, shortness_of_breath=%s, wheezing=%s, swallowing=%s, frequent_cold=%s,dry_cough=%s where patient_id = %s"

                values = (
                    patient_name, patient_gender, patient_age, patient_address, mobile_number, air_pollution,
                    alcohol_use,
                    dust_allergy, occupational_hazard, genetic_risk, chronic_lung_disease, balanced_diet, p_obesity,
                    smoking,
                    chest_pain, coughing_of_blood, p_fatigue, weight_loss, shortness_of_breath, p_wheezing, swallowing,
                    frequent_cold, dry_cough)

                cursor.execute(query, values)
                database.commit()

            # ---------------------------------------Database insertion Completed---------------------------------------
            updating_database()  # function defined above is called. It wont work without function.

            # ---------------------End: Updating the Database-----------------------------------------------------------

            Edit.configure(state='normal')
            Save.configure(state='disabled')
            for child in mainFrame.winfo_children():
                child.configure(state='disabled')

        def EditData():
            # --------------Enabling the Details
            Save.configure(state='normal')
            Edit.configure(state='disabled')
            for child in mainFrame.winfo_children():
                child.configure(state='normal')

        # ---------------------------------

        # ----------------!Event Handling -------------------

        Edit = Button(form4, text="Edit My Details", command=EditData)
        Edit.grid(row=4, column=1)

        Save = Button(form4, text="Save Changes", command=SaveData)
        Save.grid(row=6, column=1)

        Exit = Button(form4, text="Close Window", command=form4.destroy)
        Exit.grid(row=8, column=1)

        # Name
        lName = Label(mainFrame, text="Name")
        lName.grid(row=0, column=0)

        name = StringVar()
        eName = Entry(mainFrame, textvariable=name)
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

        age = StringVar()

        sAge = Spinbox(mainFrame, from_=1, to=100, textvariable=age)
        sAge.grid(row=2, column=1)

        # Address
        lAddress = Label(mainFrame, text="Address")
        lAddress.grid(row=3, column=0)

        address = StringVar()

        eAddress = Entry(mainFrame, textvariable=address)
        eAddress.grid(row=3, column=1)

        # Mobile
        lMobile = Label(mainFrame, text="Mobile Number")
        lMobile.grid(row=4, column=0)

        mobile = StringVar()
        eMobile = Entry(mainFrame, textvariable=mobile)
        eMobile.grid(row=4, column=1)


        #Common List
        List_Options=[0,1,2,3,4,5,6]
        # Air Pollution
        lAir = Label(mainFrame, text="Air Pollution")
        lAir.grid(row=5, column=0)

        air = IntVar()
        air.set(List_Options[0])

        omAirPollution=OptionMenu(mainFrame,air,*List_Options)
        omAirPollution.grid(row=5,column=1)

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
        dust.set(List_Options)
            
        omDust = OptionMenu(mainFrame, dust, *List_Options)
        omDust.grid(row=7, column=1)

        # Occupational Hazard
        lOccHzd = Label(mainFrame, text="Occupational Hazard")
        lOccHzd.grid(row=8, column=0)

        occupationHzd = IntVar()
        occupationHzd.set(List_Options[0])

        omOccHzd=OptionMenu(mainFrame,occupationHzd,*List_Options)
        omOccHzd.grid(row=8, column=1)

        # Geneti Risk
        lGenetic = Label(mainFrame, text="Genetic Risk")
        lGenetic.grid(row=9, column=0)

        genes = IntVar()
        genes.set(List_Options[0])

        omGenetic=OptionMenu(mainFrame,genes,*List_Options)
        omGenetic.grid(row=9, column=1)

        # Chronic Lung Disease
        lChronic = Label(mainFrame, text="Chronic Lung Disease")
        lChronic.grid(row=10, column=0)

        chronic = IntVar()
        chronic.set(List_Options[0])

        omChronic=OptionMenu(mainFrame,chronic,*List_Options)
        omChronic.grid(row=10, column=1)

        # Balanced Diet
        lDiet = Label(mainFrame, text="Balanced Diet")
        lDiet.grid(row=11, column=0)

        diet = IntVar()
        dust.set(List_Options[0])

        omDiet=OptionMenu(mainFrame,dust,*List_Options)
        omDiet.grid(row=11, column=1)


        # Obesity
        lObesity = Label(mainFrame, text="Obesity")
        lObesity.grid(row=12, column=0)

        obesity = IntVar()
        obesity.set(List_Options[0])

        omObesity=OptionMenu(mainFrame,obesity,*List_Options)
        omObesity.grid(row=12, column=1)

        # Smoking
        lSmoke = Label(mainFrame, text="Smoking")
        lSmoke.grid(row=13, column=0)

        smoke = IntVar()
        smoke.set(List_Options[0])

        omSmoke = OptionMenu(mainFrame, smoke, *List_Options)
        omSmoke.grid(row=13, column=1)

        # Chest Pain
        lChestpain = Label(mainFrame, text="ChestPain")
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
        lBreath = Label(mainFrame, text="ShortNess of Breath")
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
        lSwallowing = Label(mainFrame, text="Swoolnig Difficulty")
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
        lDryCough = Label(mainFrame, text="Dry Cough")
        lDryCough.grid(row=13, column=2)

        drycough = IntVar()
        drycough.set(List_Options[0])

        omDryCough = OptionMenu(mainFrame, drycough, *List_Options)
        omDryCough.grid(row=13, column=3)
        # Chest Pain
        lChestpain = Label(mainFrame, text="ChestPain")
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
        lBreath = Label(mainFrame, text="ShortNess of Breath")
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
        lSwallowing = Label(mainFrame, text="Swoolnig Difficulty")
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
        lDryCough = Label(mainFrame, text="Dry Cough")
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

    # --------------------------------

    # form4.mainloop()
    # ---------------------------------------------------------------------------------------------------------------

    Open_Edit = Button(form2, text="Open/Edit", command=openEdit)
    Open_Edit.grid(row=15, column=1)

    Exit = Button(form2, text="Exit Window", command=form2.destroy)
    Exit.grid(row=18, column=1)

    List = Listbox(mainFrame)
    List.grid(row=0, column=0)

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
        print("You Selected item %d: %s" % (selected_index, myselected_value))

    List.bind('<<ListboxSelect>>', onListSelect)

    # -----------------------
    Open_Edit.configure(state='disabled')


def AnalyseWindow():
    # =============================================== form3 ==================================================================================
    form3 = Toplevel()
    form3.lift()
    form3.focus_force()
    form3.grab_set()
    form3.grab_release()
    form3.geometry("550x580+350+80")
    form3.title("Selecting a Customer")

    mainFrame = LabelFrame(form3, text="Select Your Name", padx=35, pady=35)
    mainFrame.grid(row=0, column=0, padx=120, pady=50, rowspan=50)

    def analyseData():
        print("Analyse Data")
        analyseFrame = LabelFrame(form3, text="Your Result", padx=20, pady=20)
        analyseFrame.grid(row=52, column=0)
        temp = Label(analyseFrame, text="You Have Cancer")
        temp.pack()

    Button_Analyse = Button(form3, text="Analyse Data", command=analyseData)
    Button_Analyse.grid(row=15, column=1, columnspan=2)

    Exit = Button(form3, text="Exit Window", command=form3.destroy)
    Exit.grid(row=18, column=1, columnspan=2)

    List = Listbox(mainFrame)
    List.grid(row=0, column=0)

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
        value = w.get(index)
        print("You Selected item %d: %s" % (index, value))

    List.bind('<<ListboxSelect>>', onListSelect)

    # -----------------------
    Button_Analyse.configure(state='disabled')


# form3.mainloop()
# =================================================================================================================================
# =================================================================================================================================
def AskWindow():
    print("Window Question")


def AboutWindow():
    print("Window About")


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


# ------------------PanedWindow----------------------------------
panel = PanedWindow(root, bg="grey")
panel.place(x=80, y=80, height=500, width=1200)

insertButton = Button(panel, text="Insert", command=InsertWindow).place(x=330, y=330)
openButton = Button(panel, text="Open/Edit", command=OpenWindow).place(x=640, y=330)
analyseButton = Button(panel, text="Analyse", command=AnalyseWindow).place(x=930, y=330)

# ------------------!PanedWindow----------------------------------

root.mainloop()
