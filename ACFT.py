import time, sys
import agerangetest as ar # utilizes agerangetest for age ranges
import mdlpoints as mdlp # utilizes the dictionary for maximum dead lift points
import sptpoints as sptp # utilizes the dictionary for standing power throw points
import hrppoints as hrpp # utilizes the dictionary for hand release pushup points
import sdcpoints as sdcp # utilizes the dictionary for sprint drag carry points
import plnkpoints as plnkp # utilizes the dictionary for the plank points
import tmrpoints as tmrp # utilizes the dictionary for the two mile run points

def rsinput():
    rank = input("Enter Soldier's Rank: ")
    name = input("Enter Soldier's Name: Last, First: ")
    gender = input("Enter Soldier's Gender (M/F): ")
    age = int(input("Enter Soldier's Age: ")) 

    print(rank, name)
    print("Gender: ", gender)
    print("Age: ", age)

    def verify():
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts: #verifies that all information is correct; mainly housekeeping/verification purposes
            time.sleep(0.5)
            response = input("Verify that all information is correct. Enter Y to proceed, and N to reenter the information correctly. ").lower()
            if response in ["y", "Y"]:
                print("Enter Soldier's Raw Scores")
                time.sleep(0.5) 
                break
            elif response in ["n", "N"]:
                rsinput()
                break
            else:
                print("Invalid response.")
                attempts += 1

            if attempts == max_attempts:
                print("Maximum number of attempts reached. Exiting program.")
                sys.exit
    verify()

    #calculates maximum dead lift score based on age/gender, user input will return calculated score

        #male scores
    if gender in ['m', 'M'] and age in ar.ranges.agerange1m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl1721m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange2m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl2226m_dict.get(input_key,)    
    elif gender in ['m', 'M'] and age in ar.ranges.agerange3m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl2731m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange4m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl3236m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange5m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl3741m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange6m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl4246m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange7m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl4751m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange8m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl5256m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange9m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl5761m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange10m:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl62m_dict.get(input_key,)
    #the following mdl row is for female scores
    elif gender in ['f', 'F'] and age in ar.ranges.agerange1f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl1721f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange2f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl2226f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange3f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl2731f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange4f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl3236f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange5f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl3741f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange6f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl4246f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange7f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl4751f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange8f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl5256f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange9f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl5761f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange10f:
        input_key = int(input("Enter Raw MDL Score in LBS: "))
        mdl = mdlp.mdl62f_dict.get(input_key,)
    while mdl == None: mdl = 0
    print("Maximum Deadlift Event: ", mdl, "points")

    #calculates standing power throw score based on age, gender, user input will return calculated score
    #spt for male scores


    if gender in ['m', 'M'] and age in ar.ranges.agerange1m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt1721m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange2m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt2226m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange3m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt2731m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange4m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt3236m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange5m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt3741m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange6m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt4246m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange7m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt4751m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange8m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt5256m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange9m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt5761m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange10m:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt62m_dict.get(input_key,)
        #spt for females
    elif gender in ['f', 'f'] and age in ar.ranges.agerange1f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt1721f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange2f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt2226f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange3f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt2731f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange4f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt3236f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange5f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt3741f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange6f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt4246f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange7f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt4751f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange8f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt5256f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange9f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt5761f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange10f:
        input_key = float(input("Enter Raw SPT Score: "))
        spt = sptp.spt62f_dict.get(input_key,)
    while spt == None: spt = 0
    print("Standing Power Throw Event Score: ", spt, "points")

        #hrp score calculation for males
    if gender in ['m', 'M'] and age in ar.ranges.agerange1m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp1721m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange2m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp2226m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange3m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp2731m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange4m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp3236m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange5m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp3741m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange6m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp4246m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange7m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp4751m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange8m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp5256m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange9m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp5761m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange10m:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp62m_dict.get(input_key,)
    #hrp score calculation for females
    elif gender in ['f', 'f'] and age in ar.ranges.agerange1f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp1721f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange2f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp2226f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange3f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp2731f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange4f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp3236f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange5f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp3741f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange6f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp4246f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange7f:
        input_key = int(input("Enter Raw HRP Score: "))
        hrp = hrpp.hrp4751f_dict.get(input_key,)
    elif gender in ['f', 'f'] and age in ar.ranges.agerange8f:
        input_key = int(input("Enter Raw HRP Score: "))
    while hrp == None: hrp = 0
    print("Hand Release Pushup Event: ", hrp, "points")

    #sprint drag carry score calculation for males
    if gender in ['m', 'M'] and age in ar.ranges.agerange1m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc1721m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange2m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc2226m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange3m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc2731m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange4m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc3236m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange5m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc3741m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange6m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc4246m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange7m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc4751m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange8m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc5256m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange9m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc5761m_dict.get(input_key,)
    elif gender in ['m', 'M'] and age in ar.ranges.agerange10m:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc62m_dict.get(input_key,)
    #sprint drag carry score calculation for females
    elif gender in ['f', 'F'] and age in ar.ranges.agerange1f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc1721f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange2f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc2226f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange3f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc2731f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange4f:
            input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
            sdc = sdcp.sdc3236f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange5f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc3741f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange6f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc4246f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange7f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc4751f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange8f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc5256f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange9f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc5761f_dict.get(input_key,)
    elif gender in ['f', 'F'] and age in ar.ranges.agerange10f:
        input_key = str(input("Enter Raw SDC Score (Format M:SS): "))
        sdc = sdcp.sdc62f_dict.get(input_key,)
    while sdc == None: sdc = 0
    print("Spring Drag Carry Event: " + str(sdc), "points")

    #plank score calculation for all genders
    if age in ar.ranges.agerange1m:
        input_key = str(input("Enter Raw Plank Score (Format M:SS): "))
        plnk = plnkp.plnk1721_dict.get(input_key,)
    elif age in ar.ranges.agerange2m:
        input_key = str(input("Enter Raw Plank Score (Format M:SS): "))
        plnk = plnkp.plnk2226_dict.get(input_key,)
    elif age in ar.ranges.agerange3m:
        input_key = str(input("Enter Raw Plank Score (Format M:SS): "))
        plnk = plnkp.plnk2731_dict.get(input_key,)
    elif age in ar.ranges.agerange4m:
        input_key = str(input("Enter Raw Plank Score (Format M:SS): "))
        plnk = plnkp.plnk3236_dict.get(input_key,)
    elif age in ar.ranges.agerangeplnkmax:
        input_key = str(input("Enter Raw Plank Score (Format M:SS): "))
        plnk = plnkp.plnk3762_dict.get(input_key,)
    while plnk == None: plnk = 0
    print("Plank Event: " + str(plnk), "points")

    #calculates two mile run score based on gender and age, starting with males
    if age in ar.ranges.agerange1m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr1721m_dict.get(input_key,)
    elif age in ar.ranges.agerange2m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr2226m_dict.get(input_key,)
    elif age in ar.ranges.agerange3m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr2731m_dict.get(input_key,)
    elif age in ar.ranges.agerange4m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr3236m_dict.get(input_key,)
    elif age in ar.ranges.agerange5m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr3741m_dict.get(input_key,)
    elif age in ar.ranges.agerange6m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr4246m_dict.get(input_key,)
    elif age in ar.ranges.agerange7m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr4751m_dict.get(input_key,)
    elif age in ar.ranges.agerange8m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr5256m_dict.get(input_key,)
    elif age in ar.ranges.agerange9m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr5761m_dict.get(input_key,)
    elif age in ar.ranges.agerange10m:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr62m_dict.get(input_key,)
        #female score calculations
    elif age in ar.ageranges.agerange1f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr1721f_dict.get(input_key,)
    elif age in ar.ranges.agerange2f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr2226f_dict.get(input_key,)
    elif age in ar.ranges.agerange3f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr2731f_dict.get(input_key,)
    elif age in ar.ranges.agerange4f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr3236f_dict.get(input_key,)
    elif age in ar.ranges.agerange5f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr3741f_dict.get(input_key,)
    elif age in ar.ranges.agerange6f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr4246f_dict.get(input_key,)
    elif age in ar.ranges.agerange7f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr4751f_dict.get(input_key,)
    elif age in ar.ranges.agerange8f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr5256f_dict.get(input_key,)
    elif age in ar.ranges.agerange9f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format MM:SS): "))
        tmr = tmrp.tmr5761f_dict.get(input_key,)
    elif age in ar.ranges.agerange10f:
        input_key = str(input("Enter Raw Two Mile Run Score (Format M:SS): "))
        tmr = tmrp.tmr62f_dict.get(input_key,)
    while tmr == None: tmr = 0
    print("Two Mile Run Event: " + str(tmr), "points")

    def mastercalc():
        print ("Rank: " + str(rank))
        print ("Name: " + str(name))
        print ("Age: " + str(age))
        print ("Gender: " + str(gender))
        print ("Maximum Deadlift Event Score: " + str(mdl) + " points")
        print ("Standing Power Throw Event Score: " + str(spt) + " points")
        print ("Hand Release Pushup Event Score: " + str(hrp) + " points")
        print ("Sprint Drag Carry Event Score: " + str(sdc) + " points")
        print ("Plank Event Score: " + str(plnk) + " points")
        print ("Two Mile Run Event Score: " + str(tmr) + " points")
        total = mdl + spt + hrp + sdc + plnk + tmr
        print ("Total Score: " + str(total) + " points")
        if total >= 360:
            print("PASS")
            print ("Congratulations! You have sucessfully completed the Army Combat Fitness Test!")
        elif total <= 360:
            print ("FAIL")
            print ("You have not reached a satisfactory score based on your age and gender. Please continue to train and try again.")
        elif mdl < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Maximum Deadlift Event. Please continue to train and try again.")
        elif spt < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Standing Power Throw Event. Please continue to train and try again.")
        elif hrp < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Hand Release Pushup Event. Please continue to train and try again.")
        elif sdc < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Sprint Drag Carry Event. Please continue to train and try again.")
        elif plnk < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Plank Event. Please continue to train and try again.")
        elif tmr < 60:
            print ("FAIL")
            print ("You have not reached a satisfactory score in the Two Mile Run Event. Please continue to train and try again.")
    mastercalc()
    def scoreout():
        def prntout():
            with open("ACFT_Score.txt", "w") as text_file:
                print(f"Rank: {rank}", file=text_file)
                print(f"Name: {name}", file=text_file)
                print(f"Age: {age}", file=text_file)
                print(f"Gender: {gender}", file=text_file)
                print(f"Maximum Deadlift Event Score: {mdl} points", file=text_file)
                print(f"Standing Power Throw Event Score: {spt} points", file=text_file)
                print(f"Hand Release Pushup Event Score: {hrp} points", file=text_file)
                print(f"Sprint Drag Carry Event Score: {sdc} points", file=text_file)
                print(f"Plank Event Score: {plnk} points", file=text_file)
                print(f"Two Mile Run Event Score: {tmr} points", file=text_file)
                total = mdl + spt + hrp + sdc + plnk + tmr
                print(f"Total Score: {total} points", file=text_file)
                if total >= 360:
                    print ("PASS", file=text_file)
                    time.sleep(2)
                elif total <= 360:
                    print ("FAIL", file=text_file)
                    time.sleep(2)
                elif mdl < 60:
                    print ("FAIL", file=text_file)
                elif spt < 60:
                    print ("FAIL", file=text_file)
                elif hrp < 60:
                    print ("FAIL", file=text_file)
                elif sdc < 60:
                    print ("FAIL", file=text_file)
                elif plnk < 60:
                    print ("FAIL", file=text_file)
                elif tmr < 60:
                    print ("FAIL", file=text_file)

        wannaprnt = input("Would you like to save your scores to a text file? (Y/N): ")
        if wannaprnt in ["Y", "y"]:
            print ("Saving scores to text file...")
            time.sleep(2)
            prntout()
            print ("Scores saved to text file.")
            time.sleep(2)
            print ("Goodbye")
            exit()
        elif wannaprnt in ["N", "n"]:
            print ("Goodbye")
            exit()
        else:
            print ("Invalid input. Please try again.")
            scoreout()
    scoreout()          

rsinput()

