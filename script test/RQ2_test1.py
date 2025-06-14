import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os.path import exists
import re
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))




def getProfitinHistory(benchmark: str):
    profit = 0
    # TEST 1
    if benchmark == "bEarnFi":
        profit = 18077.148053847253
    elif benchmark == "Wdoge":
        profit = 78

    return int(profit)


def main():
    method = 0 # 0 for interpolation 
               # 1 for polynomial
    
    # TEST 1
    benchmarkList = ['bEarnFi', 'Wdoge']

    folder_list = ["precise"]

    print("benchmark", end="")
    for folder in folder_list:
        if "_noloop" in folder:
            print(folder[:-7], end = " ")
        else:
            print(folder, end = " ")
    print("")

    for index in range(len(benchmarkList)):
        benchmark = benchmarkList[index]
        if benchmark == "Harvest_USDC":
            print("Harvest_USDT", end = " ")
        elif benchmark == "Harvest_USDT":
            print("Harvest_USDC", end = " ")
        else:
            print(benchmark, end = " ")
        historyProfit = getProfitinHistory(benchmark)
        # print(historyProfit, end = ", ")

        folder = "precise"

        filename = SCRIPT_DIR + "/FlashSynData/" + folder + "/" + benchmark + "_precise.txt"
        # print(filename)

        file_exists = exists(filename)
        if file_exists:
            with open(filename) as file:
                globalbestProfit = 0
                profitPerRound = [0.0]
                round = [0.0]
                for line in file:

                    if "Best Global Profit:" in line:
                        split = line.split()
                        # if split[-1] != '0':
                        #     print(line.split())
                        profit = float(split[-2])
                        if profit > globalbestProfit:
                            globalbestProfit = profit
                            # print("New global Profit: ", globalbestProfit)
                        round.append(len(round))

                        profitPerRound.append(globalbestProfit)
                if globalbestProfit > 30:
                    print(int(globalbestProfit), end = " ")
                else:
                    print("/", end = " ")
        else:
            print("/", end = "  ")
        print("")


if __name__ == "__main__":
    main()

            