import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os.path import exists
import re
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def getProfitinHistory(benchmark: str):
    profit = 0
    # TEST 2
    if benchmark == "bEarnFi":
        profit = 18077.148053847253
    elif benchmark == "Wdoge":
        profit = 78

    return int(profit)

def main():
    method = 0 # 0 for interpolation 
               # 1 for polynormial

    benchmarkList = ['bEarnFi', 'Wdoge'] # TEST 2
    #  skipped for now
    # 'Puppet', 'PuppetV2' skipped for now
    #  skipped for now

    poly_folder = SCRIPT_DIR + "/FlashSynData/2000+X/"
    inte_folder = SCRIPT_DIR + "/FlashSynData/2000+X/"

    Profit_inte = [] # list of profit for interpolation
    Profit_poly = [] # list of profit for polynomial
    Profit_his = [] # list of profit for history
    Time_inte = [] # list of time for interpolation
    Time_poly = [] # list of time for polynomial
    
    print("          ||   FlashSyn-poly    ||   FlashSyn-inte  || ")
    print("benchmark", "GP", "IDP", "TDP", "Profit", "Time",  "TDP", "Profit", "Time")
    for index in range(len(benchmarkList)):
        benchmark = benchmarkList[index]
        if benchmark == "Harvest_USDC":
            print("Harvest_USDT", end = " ")
        elif benchmark == "Harvest_USDT":
            print("Harvest_USDC", end = " ")
        else:
            print(benchmark, end = " ")

        historyProfit = getProfitinHistory(benchmark)
        print(historyProfit, end = " ")
        Profit_his.append(historyProfit)
        if benchmark == "Yearn" or benchmark == "InverseFi":  # they cannot be solved
            print(" ---------------------------------------")
            continue 
        
        IC_Time = 0
        for method in [1, 0]:
            IC_filename = ""
            if method == 0:
                IC_filename = SCRIPT_DIR + "/../Results-Expected/FlashSynData/2000+X/" + "/data/" + benchmark + "_initial_data.txt"
            elif method == 1:
                IC_filename = SCRIPT_DIR + "/../Results-Expected/FlashSynData/2000+X/" + "/data/" + benchmark + "_initial_data.txt"

            file_exists = exists(IC_filename)
            if file_exists:
                with open(IC_filename) as file:
                    Time = 0
                    for line in file:
                        if "in total it takes " in line:
                            rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)
                            time = rr[-1]
                            Time = float(time)

                    if Time > 0:
                        # print(int(Time), end = " ")
                        IC_Time = int(Time)
                    else:
                        # print("/", end = " ")
                        IC_Time = None


            filename = ""
            if method == 0:
                folder = inte_folder
                filename = folder + "/" + benchmark + "_inte.txt"
            elif method == 1:
                folder = poly_folder
                filename = folder + "/" + benchmark + "_poly.txt"
            file_exists = exists(filename)
            if file_exists:
                with open(filename) as file:
                    globalbestProfit = 0
                    profitPerRound = [0.0]
                    round = [0.0]
                    startDataPoints = False
                    NumPointsList = []
                    NumPoints = 0
                    Time = 0
                    for line in file:
                        if "time" in line:
                            rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)
                            time = rr[-1]
                            Time = float(time)


                        if "Best Global Profit:" in line:
                            split = line.split()
                            # if split[-1] != '0':
                            #     print(line.split())
                            profit = float(split[-2])
                            profit = int(profit)
                            if profit > globalbestProfit:
                                globalbestProfit = profit
                                # print("New global Profit: ", globalbestProfit)
                            round.append(len(round))

                            profitPerRound.append(globalbestProfit)

                        # if "Check Contract: 	VaultBankDeposit, Curve_DAI2USDC, Curve_USDC2USDT, Curve_USDT2USDC, ValueWithdrawFor, Curve_USDC2DAI    Profit of Previous Interation: 	6777469.0  time: 5386.665939331055" in line:
                        #     print("now is the time")
                        #     print(NumPoints)

                        if "number of points:" in line:
                            startDataPoints = True
                        elif startDataPoints and "skip" not in line \
                            and "Check" not in line and "======" not in line \
                            and "For" not in line and "Best" not in line :
                            split = line.split()
                            # print(line)
                            NumPoints += int(split[0])
                        
                        if startDataPoints and ("Check Contract:" in line or "======" in line):
                            startDataPoints = False
                            NumPointsList.append(NumPoints)
                            NumPoints = 0

                    if len(NumPointsList) >= 2:
                        if method == 1:
                            print(NumPointsList[0], end = " ")
                        print(NumPointsList[-1], end = " ")
                        # print("(", len(NumPointsList), ")")
                    else:
                        print("not two ", end = " ")

                    if globalbestProfit > 0: # TEST 2
                        print(int(globalbestProfit), end = " ")
                        if method == 1:
                            Profit_poly.append(int(globalbestProfit))
                        elif method == 0:
                            Profit_inte.append(int(globalbestProfit))
                    else:
                        print("/", end = " ")
                        if method == 1:
                            Profit_poly.append(0)
                        elif method == 0:
                            Profit_inte.append(0)

                    if Time > 0:
                        if Time < 10000:
                            if globalbestProfit > 0: # TEST 2
                                if method == 1:
                                    Time_poly.append(int(Time) + IC_Time)
                                elif method == 0:
                                    Time_inte.append(int(Time) + IC_Time)
                                print(int(Time) + IC_Time, end = " ")
                            else:
                                if method == 1:
                                    Time_poly.append("/")
                                elif method == 0:
                                    # Time_inte.append("/")
                                    pass
                                print("/", end = " ")

                        else:  # if in log file the last <Time> > 10000, then it reaches time limit of 4 hours
                            if method == 1:
                                Time_poly.append(10800 + IC_Time)
                            elif method == 0:
                                Time_inte.append(10800 + IC_Time)
                            print(str(10800 + IC_Time), end = " ")
                    else:
                        print("/", end = " ")
                        if method == 1:
                            Time_poly.append("/")
                        elif method == 0:
                            Time_inte.append("/")
                    
            else:
                if method == 1:
                    Profit_poly.append(0)
                    Time_poly.append("/")
                elif method == 0:
                    Profit_inte.append(0)
                    Time_inte.append("/")
                
                print("-", end = " ")
        print("")

    # TEST 1
    print("Profit_inte", Profit_inte)
    print("len: ", len(Profit_inte))
    print("Profit_poly", Profit_poly)
    print("len: ", len(Profit_poly))
    print("Profit_his", Profit_his)
    print("len: ", len(Profit_his))
    print("Time_inte", Time_inte) 
    print("len: ", len(Time_inte))
    print("Time_poly", Time_poly)
    print("len: ", len(Time_poly))

    # print("=========================================================================================")
    # NumOfSolved_poly = 0
    # for profit in Profit_poly:
        # if profit > 0:
            # NumOfSolved_poly += 1
    # print("Solved(poly): ", NumOfSolved_poly, "out of 18", end = "  ")
    # print("Avg Time:", int(sum(Time_poly)/len(Time_poly)), end = "  ")

    # # print(Time_poly)
    # NumOfSolved_inte = 0
    # for profit in Profit_inte:
        # if profit > 0:
            # NumOfSolved_inte += 1
    # print("Solved(inte): ", NumOfSolved_inte, "out of 18", end = "  ")
    # print("Avg Time:", int(sum(Time_inte)/len(Time_inte)), end = "  \n")
    
    # print("")
    
    print("=========================================================================================")
    NumOfSolved_poly = 0
    for profit in Profit_poly:
        if profit > 0:
            NumOfSolved_poly += 1
    print("Solved(poly): ", NumOfSolved_poly, "out of 18", end = "  ")
    filtered_Time_poly = [t for t in Time_poly if isinstance(t, int)]
    if filtered_Time_poly:
        print("Avg Time:", int(sum(filtered_Time_poly)/len(filtered_Time_poly)), end = "  ")
    else:
        print("Avg Time: /", end = "  ")

    NumOfSolved_inte = 0
    for profit in Profit_inte:
        if profit > 0:
            NumOfSolved_inte += 1
    print("Solved(inte): ", NumOfSolved_inte, "out of 18", end = "  ")
    filtered_Time_inte = [t for t in Time_inte if isinstance(t, int)]
    if filtered_Time_inte:
        print("Avg Time:", int(sum(filtered_Time_inte)/len(filtered_Time_inte)), end = "  \n")
    else:
        print("Avg Time: /", end = "  \n")


if __name__ == "__main__":
    main()