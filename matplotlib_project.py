#Souvik Basak, Aahan Shah, Aayush Chahal
from matplotlib import pyplot as plt, rcParams
import numpy as np
import matplotlib.patheffects as pe
import tkinter
from tkinter import simpledialog

rcParams["font.family"] = "Monospace"

def readFile(file):
    return open(file).read()

def rollingAverage(numbers, index):
    if index >= 3:
        return sum(numbers[index-3:index+1]) / 4.0
    return sum(numbers[:index+1]) / (index+1)

def westernConference():
    fig, ax = plt.subplots(layout="constrained")
    multiplier = 0
    x = np.arange(len(seasons))
    width = 0.15
    teamColors = ["gold", "purple", "gray", "darkblue", "red"]
    for team, average in westernWinRatios.items():
        offset = width * (multiplier - 1)
        rects = ax.bar(x+offset, average, width, label=team, color=teamColors[multiplier], zorder=3, alpha=0.5)
        multiplier += 1

    ax.set_xticks(x + width, seasons, rotation=45)
    ax.set_title("Western Conference Winning Ratios", fontsize=15)
    ax.legend(loc="upper right")
    ax.set_xlabel("Seasons", fontsize=12)
    ax.set_ylabel("Win Ratios", fontsize=12)
    plt.grid(axis='y', zorder=0)
    plt.plot(seasons, warriorsRollingAverage, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="gold")
    plt.plot(seasons, lakersRollingAverage, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="purple")
    plt.plot(seasons, mavericksRollingAverage, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="gray")
    plt.plot(seasons, nuggetsRollingAverage, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="darkblue")
    plt.plot(seasons, clippersRollingAverage, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="red")
    plt.show()

def westernDistribution():
    bins = np.arange(0, 1.05, 0.05)
    plt.hist(warriorsWinRatio + lakersWinRatio + mavericksWinRatio + nuggetsWinRatio + clippersWinRatio, edgecolor="black")
    plt.xlabel("Win Ratios")
    plt.ylabel("Frequency")
    plt.title("Win Ratio Distribution | Western Conference")
    plt.show()




def ThreePTavg10players():
    ThreePtData = readFile("3ptData.csv").split("\n")
    x = ThreePtData.pop(0)
    x = x.split(",")
    x.pop(0)
    lebron = ThreePtData[0].split(",")
    lebron.pop(0)
    curry = ThreePtData[1].split(",")
    curry.pop(0)
    kd = ThreePtData[2].split(",")
    kd.pop(0)
    kyrie = ThreePtData[3].split(",")
    kyrie.pop(0)
    russell = ThreePtData[4].split(",")
    russell.pop(0)
    klay = ThreePtData[5].split(",")
    klay.pop(0)
    bradley = ThreePtData[6].split(",")
    bradley.pop(0)
    damian = ThreePtData[7].split(",")
    damian.pop(0)
    anthony = ThreePtData[8].split(",")
    anthony.pop(0)
    butler = ThreePtData[9].split(",")
    butler.pop(0)

    lebron = list(map(float, lebron))
    curry = list(map(float, curry))
    kd = list(map(float, kd))
    kyrie = list(map(float, kyrie))
    russell = list(map(float, russell))
    klay = list(map(float, klay))
    bradley = list(map(float, bradley))
    damian = list(map(float, damian))
    anthony = list(map(float, anthony))
    butler = list(map(float, butler))

    plt.plot(x, lebron, linewidth=4)
    plt.plot(x, curry, linewidth=4)
    plt.plot(x, kd, linewidth=4)
    plt.plot(x, kyrie, linewidth=4)
    plt.plot(x, russell, linewidth=4)
    plt.plot(x, klay, linewidth=4)
    plt.plot(x, bradley, linewidth=4)
    plt.plot(x, damian, linewidth=4)
    plt.plot(x, anthony, linewidth=4)
    plt.plot(x, butler, linewidth=4)
    plt.ylabel("3 Point Averages", fontsize = 24)
    plt.xlabel("NBA Season", fontsize = 24)
    plt.legend(["Lebron James", "Steph Curry", "KD", "Kyrie Irving", "Russell Westbrook", "Klay Thompson", "Bradley Beal", "Damian Lillard", "Anthony Davis", "Jimmy Butler"])
    plt.title("3 Point Averages of 10 Different Players Over 11 Seasons")

    plt.show()





def displayLogo():
    inputName = tkinter.simpledialog.askstring("Team Logos", "Enter the team whose logo you want to display. Enter the full name or the team's short name. Type \"teams\" to display all team names.")
    inputName = inputName.lower()
    teamNames = ["warriors", "lakers", "mavericks", "nuggets", "clippers", "knicks", "76ers", "heat", "bulls", "pacers"]
    name = inputName.split(' ')[-1]
    if inputName == "teams":
        tk = tkinter.Tk()
        tk.geometry("610x360")
        label = tkinter.Label(tk, text="Golden State Warriors\nLos Angeles Lakers\nDallas Mavericks\nDenver Nuggets\nLos Angeles Clippers\nNew York Knicks\nPhiladelphia 76ers\nMiami Heat\nChicago Bulls\nIndiana Pacers")
        label.pack()
    elif name not in teamNames:
        tk = tkinter.Tk()
        tk.geometry("610x360")
        label = tkinter.Label(tk, text="Invalid team name. Type \"teams\" to see all the valid team names")
        label.pack()
    else:
        image = plt.imread(name + "logo.png")
        plt.imshow(image)
        plt.axis("off")
        plt.show()

westernData = readFile("WesternData.csv").split("\n")
westernData.pop(0)
westernData.pop(0)

seasons = []
warriorsWinRatio = []
warriorsRollingAverage = []
lakersWinRatio = []
lakersRollingAverage = []
mavericksWinRatio = []
mavericksRollingAverage = []
nuggetsWinRatio = []
nuggetsRollingAverage = []
clippersWinRatio = []
clippersRollingAverage = []

for i in reversed(range(11)):
    warriorsWinRatio.append(float(westernData[i].split(",")[3]))
    warriorsRollingAverage.append(round(rollingAverage(warriorsWinRatio, 10-i), 3))
    lakersWinRatio.append(float(westernData[i+13].split(",")[3]))
    lakersRollingAverage.append(round(rollingAverage(lakersWinRatio, 10-i), 3))
    mavericksWinRatio.append(float(westernData[i+26].split(",")[3]))
    mavericksRollingAverage.append(round(rollingAverage(mavericksWinRatio, 10-i), 3))
    nuggetsWinRatio.append(float(westernData[i+39].split(",")[3]))
    nuggetsRollingAverage.append(round(rollingAverage(nuggetsWinRatio, 10-i), 3))
    clippersWinRatio.append(float(westernData[i+52].split(",")[3]))
    clippersRollingAverage.append(round(rollingAverage(clippersWinRatio, 10-i), 3))
    seasons.append(westernData[i].split(",")[0])

westernWinRatios = {
    "Warriors": warriorsWinRatio,
    "Lakers": lakersWinRatio,
    "Mavericks": mavericksWinRatio,
    "Nuggets": nuggetsWinRatio,
    "Clippers": clippersWinRatio
}

test_file = open('EastDataahan.csv').read()
text = test_file
text = text.split("\n")
text.pop(0)
text.pop(0)

#list winning averages
avgs = []
for line in text:
    line = line.split(',')
    avgs.append(line[3])
for i in avgs:
    if i == '%':
        avgs.remove(i)
for i in avgs:
    if i == '':
        avgs.remove(i)

seasonsextracted = []
seasons = []
for line in text:
    line = line.split(',')
    seasonsextracted.append(line[0])
for i in range(11):
    seasons.append(seasonsextracted[i])

newpercentages= []
for decimal_str in avgs:
    newpercentages.append(float(decimal_str))
seasons.reverse()
newpercentages.reverse()
pacerswinspercentages = newpercentages[0:11]
bullswinspercentages = newpercentages[11:22]
heatwinspercentages = newpercentages[22:33]
phillywinspercentages = newpercentages[33:44]
knickswinspercentages = newpercentages[44:55]

def easternDistribution():
    bins = np.arange(0, 1.05, 0.05)
    plt.hist(newpercentages, bins=bins, edgecolor='black')
    plt.xlabel('Win Ratios', fontname = 'monospace')
    plt.ylabel('Frequency(Seasons)', fontname = 'monospace')
    plt.title('Win Ratio Distribution | Eastern Conference', fontname = 'serif')
    plt.show()

Easterndict = {'Knicks': knickswinspercentages, '76ers': phillywinspercentages, 'Heat': heatwinspercentages, 'Bulls': bullswinspercentages, 'Pacers': pacerswinspercentages}
knicksRollingAvg = []
phillyRollingAvg = []
heatRollingAvg = []
bullsRollingAvg = []
pacersRollingAvg = []

for i in range(11):
    knicksRollingAvg.append(rollingAverage(knickswinspercentages, i))
    phillyRollingAvg.append(rollingAverage(phillywinspercentages, i))
    heatRollingAvg.append(rollingAverage(heatwinspercentages, i))
    bullsRollingAvg.append(rollingAverage(bullswinspercentages, i))
    pacersRollingAvg.append(rollingAverage(pacerswinspercentages, i))
def all_teams_record():
    x = np.arange(len(seasons))
    width = 0.17 #bar width
    multiplier = 0
    colors = ['orange', 'dodgerblue', 'red', 'black', 'darkblue']
    fig, ax = plt.subplots(layout='constrained')
    for key, value in Easterndict.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=key, color=colors[multiplier], zorder = 3, alpha = 0.75)
        multiplier += 1
    #Labels
    ax.set_xlabel('Seasons')
    ax.set_ylabel('Win Ratio(Wins/Games)')
    ax.set_title('Win Ratios Over The Past Eleven Seasons', fontname = 'monospace')
    ax.set_xticks(x + 0.34, seasons, rotation=45)
    ax.legend(loc='upper right')
    ax.set_ylim(0.100, 0.900)
    plt.grid(axis='y', zorder=0)
    plt.plot(seasons, knicksRollingAvg, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="orange")
    plt.plot(seasons, phillyRollingAvg, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="dodgerblue")
    plt.plot(seasons, heatRollingAvg, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="red")
    plt.plot(seasons, bullsRollingAvg, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="black")
    plt.plot(seasons, pacersRollingAvg, zorder=4, path_effects=[pe.Stroke(linewidth=4, foreground='black'), pe.Normal()], color="darkblue")
    plt.show()

tk = tkinter.Tk()
label = tkinter.Label(tk, text="We have 5 different graphs on the Western Conference, Eastern Conference, and 3 point data for select players, as well as a team logo displayer.")
label2 = tkinter.Label(tk, text="Welcome to NBA Stats!")
label.config(font=("Comic Sans MS", 15))
westernButton = tkinter.Button(tk, text="Western Conference Data", command=westernConference)
westernDistribution = tkinter.Button(tk, text="Western Conference Win Ratio Distribution", command=westernDistribution)
easternButton = tkinter.Button(tk, text="Eastern Conference Data", command=all_teams_record)
easternDistr = tkinter.Button(tk, text="Eastern Conference Win Ratio Distribution", command=easternDistribution)
threePointButton = tkinter.Button(tk, text="Three Point Data", command=ThreePTavg10players)
teamLogos = tkinter.Button(tk, text="Team Logos", command=displayLogo)
label2.pack()
label.pack()
westernButton.pack()
westernDistribution.pack()
easternButton.pack()
easternDistr.pack()
threePointButton.pack()
teamLogos.pack()
tkinter.mainloop()
