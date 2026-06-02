import tkinter
from tkinter import messagebox
import random
import csv
import time
import codecs

BackgroundColour = (f"#{40:02x}{40:02x}{40:02x}")
Font = "Bahnschrift Light"

Player1Score = 0
Player2Score = 0

def Results(Users):
    File = __file__
    File = File.replace("DiceGame.py", "ExternalStores.csv")
    Usernames = [row[0] for row in Data]
    User1Save = Usernames.index(Users[0])
    User2Save = Usernames.index(Users[1])
    Scores = [row[2] for row in Data]
    if int(Scores[User1Save]) < Player1Score:
        lines = list()
        with codecs.open(File, 'r', encoding="utf-8") as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[User1Save][2] = Player1Score

        with codecs.open(File, 'w', encoding="utf-8") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    if int(Scores[User2Save]) < Player2Score:
        lines = list()
        with codecs.open(File, 'r', encoding="utf-8") as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[User2Save][2] = Player2Score

        with codecs.open(File, 'w', encoding="utf-8") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    ###############################
    time.sleep(1)
    with codecs.open(File, "r", encoding="utf-8") as file:
        FileData = list(csv.reader(file, delimiter=","))
    HighScoreList = ""
    for row in FileData:
            HighScoreList = HighScoreList+"\n"+str(row[0])+" - "+str(row[2])
    End = tkinter.Tk()
    End.title("Dice Game - End")
    End.attributes('-topmost', True)
    End.resizable(False, False)
    End.geometry("700x400")
    End.config(bg=BackgroundColour)

    Title = tkinter.Label(End, text=str(Users[0])+" vs "+str(Users[1]), bg=BackgroundColour, fg="white", font=(Font, 40, "bold"))
    Title.pack(pady=5)
    if Player1Score > Player2Score:
        SubTitle = tkinter.Label(End, text=Users[0]+" won the Dice Game!", bg=BackgroundColour, fg="white", font=(Font, 20, "bold"))
        SubTitle.pack(pady=2)
    elif Player1Score < Player2Score:
        SubTitle = tkinter.Label(End, text=Users[1]+" won the Dice Game!", bg=BackgroundColour, fg="white", font=(Font, 20, "bold"))
        SubTitle.pack(pady=2)
    PlayerScores = tkinter.Label(End, text=Users[0]+" with "+str(Player1Score)+" points and "+Users[1]+" with "+str(Player2Score)+" points!", bg=BackgroundColour, fg="white", font=(Font, 10, "bold"))
    PlayerScores.pack(pady=2)
    TopScores = tkinter.Label(End, text=HighScoreList, bg=BackgroundColour, fg="white", font=(Font, 10, "bold"))
    TopScores.pack(pady=10)

    ExitButton = tkinter.Button(End, text="EXIT", font=(Font, 15, "bold"), width=20, height=1, command=exit, bg=(f"#{43:02x}{182:02x}{38:02x}"), fg="white", borderwidth=3, activebackground=(f"#{43:02x}{182:02x}{38:02x}"), activeforeground="white")
    ExitButton.pack(pady=20)

    End.mainloop()

def DiceGame(Users, Round):
    Dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    DiceGameUI = tkinter.Tk()
    DiceGameUI.title("Dice Game")
    DiceGameUI.attributes('-topmost', True)
    DiceGameUI.resizable(False, False)
    DiceGameUI.geometry("700x350")
    DiceGameUI.config(bg=BackgroundColour)
    DiceGameUI.protocol("WM_DELETE_WINDOW", exit)

    def DiceRoll(DiceUI, Button):
        Player1TempScore = 0
        Player2TempScore = 0
        global Player1Score
        global Player2Score
        DiceUI.destroy()
        Button.destroy()
        P1DiceRoll1 = random.randint(1,6)
        P1DiceRoll2 = random.randint(1,6)
        DiceUI = tkinter.Label(DiceGameUI, text=(Dice[P1DiceRoll1 - 1]+Dice[P1DiceRoll2 - 1]), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
        DiceUI.pack(pady=2)
        DiceRollUI = tkinter.Label(DiceGameUI, text=Users[0]+" scored: "+str(P1DiceRoll1)+" & "+str(P1DiceRoll2), bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
        DiceRollUI.pack(pady=20)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        DiceUI.destroy()
        DiceRollUI.destroy()
        P2DiceRoll1 = random.randint(1,6)
        P2DiceRoll2 = random.randint(1,6)
        DiceUI = tkinter.Label(DiceGameUI, text=(Dice[P2DiceRoll1 - 1]+Dice[P2DiceRoll2 - 1]), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
        DiceUI.pack(pady=2)
        DiceRollUI = tkinter.Label(DiceGameUI, text=Users[1]+" scored: "+str(P2DiceRoll1)+" & "+str(P2DiceRoll2), bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
        DiceRollUI.pack(pady=20)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        Player1TempScore = P1DiceRoll1 + P1DiceRoll2
        Player2TempScore = P2DiceRoll1 + P2DiceRoll2
        time.sleep(3)
        DiceUI.destroy()
        DiceRollUI.destroy()
        TextPrompt1 = tkinter.Label(DiceGameUI, text="But its not over...", bg=BackgroundColour, fg="white", font=(Font, 30))
        TextPrompt1.pack(pady=40)
        TextPrompt2 = tkinter.Label(DiceGameUI, text="Time for the rule book!", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
        TextPrompt2.pack(pady=2)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(2)
        TextPrompt1.destroy()
        TextPrompt2.destroy()
        if Player1TempScore % 2 == 0:
            Player1TempScore = Player1TempScore + 10
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[0]+" scored +10 points (Score was even)", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        else:
            if not Player1TempScore - 5 < 0:
                Player1TempScore = Player1TempScore - 5
                TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[0]+" scored -5 points (Score was odd)", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
                TextPrompt1.pack(pady=40)
            else:
                Player1TempScore = 0
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        TextPrompt1.destroy()
        TextPrompt2.destroy()
        if Player2TempScore % 2 == 0:
            Player2TempScore = Player2TempScore + 10
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[1]+" scored +10 points (Score was even)", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        else:
            if not Player2TempScore - 5 < 0:
                Player2TempScore = Player2TempScore - 5
                TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[1]+" scored -5 points (Score was odd)", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
                TextPrompt1.pack(pady=40)
            else:
                Player2TempScore = 0
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        TextPrompt1.destroy()
        TextPrompt2.destroy()
        if P1DiceRoll1 == P1DiceRoll2:
            ExtraDice = random.randint(1,6)
            Player1TempScore = Player1TempScore + ExtraDice
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[0]+" scored double, so got another dice ("+str(ExtraDice)+")", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        else:
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[0]+" did not score double, maybe next time", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        TextPrompt1.destroy()
        TextPrompt2.destroy()
        if P2DiceRoll1 == P2DiceRoll2:
            ExtraDice = random.randint(1,6)
            Player2TempScore = Player2TempScore + ExtraDice
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[1]+" scored double, so got another dice ("+str(ExtraDice)+")", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        else:
            TextPrompt1 = tkinter.Label(DiceGameUI, text=Users[1]+" did not score double, maybe next time", bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
            TextPrompt1.pack(pady=40)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        TextPrompt1.destroy()
        TextPrompt1 = tkinter.Label(DiceGameUI, text="So results for the round:", bg=BackgroundColour, fg="white", font=(Font, 20, "bold"))
        TextPrompt1.pack(pady=40)
        TextPrompt2 = tkinter.Label(DiceGameUI, text=Users[0]+": "+str(Player1TempScore), bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
        TextPrompt2.pack(pady=2)
        TextPrompt3 = tkinter.Label(DiceGameUI, text=Users[1]+": "+str(Player2TempScore), bg=BackgroundColour, fg="white", font=(Font, 15, "bold"))
        TextPrompt3.pack(pady=2)
        DiceGameUI.update()
        DiceGameUI.update()
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        time.sleep(0.1)
        DiceGameUI.update()
        ###############################
        time.sleep(3)
        Player1Score = Player1Score + Player1TempScore
        Player2Score = Player2Score + Player2TempScore
        DiceGameUI.destroy()

    Title = tkinter.Label(DiceGameUI, text="Dice Game", bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
    Title.pack(pady=2)
    SubTitle = tkinter.Label(DiceGameUI, text="Round: "+str(Round + 1)+" - "+Users[0]+" ("+str(Player1Score)+" points)"+" vs "+Users[1]+" ("+str(Player2Score)+" points)", bg=BackgroundColour, fg="white", font=(Font, 10, "bold"))
    SubTitle.pack(pady=1)

    DiceUI = tkinter.Label(DiceGameUI, text=("◻"+"◻"), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
    DiceUI.pack(pady=2)

    RollButton = tkinter.Button(DiceGameUI, text="ROLL", font=(Font, 15, "bold"), width=20, height=1, command=lambda:DiceRoll(DiceUI, RollButton), bg=(f"#{127:02x}{13:02x}{115:02x}"), fg="white", borderwidth=3, activebackground=(f"#{127:02x}{13:02x}{115:02x}"), activeforeground="white")
    RollButton.pack(pady=10)

    DiceGameUI.mainloop()

UsersPlaying = []
LoginReturnVal = "User Exit Before Login"

def PlayScreen(Users, TopScores):
    Play = tkinter.Tk()
    Play.title("Dice Game - Play")
    Play.attributes('-topmost', True)
    Play.resizable(False, False)
    Play.geometry("700x350")
    Play.config(bg=BackgroundColour)

    def ButtonClick():
        Play.destroy()
        for Round in range(0,1):
            DiceGame(UsersPlaying, Round)
        while Player1Score == Player2Score:
            Dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
            DiceGameUI = tkinter.Tk()
            DiceGameUI.title("Dice Game")
            DiceGameUI.attributes('-topmost', True)
            DiceGameUI.resizable(False, False)
            DiceGameUI.geometry("700x350")
            DiceGameUI.config(bg=BackgroundColour)
            DiceGameUI.protocol("WM_DELETE_WINDOW", exit)

            def DiceRoll(DiceUI, RollButton):
                DiceUI.destroy()
                RollButton.destroy()
                ###############################
                DiceUI.destroy()
                RollButton.destroy()
                P1DiceRoll = random.randint(1,6)
                DiceUI = tkinter.Label(DiceGameUI, text=(Dice[P1DiceRoll - 1]), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
                DiceUI.pack(pady=2)
                DiceRollUI = tkinter.Label(DiceGameUI, text=Users[0]+" scored: "+str(P1DiceRoll), bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
                DiceRollUI.pack(pady=20)
                DiceGameUI.update()
                DiceGameUI.update()
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                ###############################
                time.sleep(3)
                DiceUI.destroy()
                DiceRollUI.destroy()
                P2DiceRoll = random.randint(1,6)
                DiceUI = tkinter.Label(DiceGameUI, text=(Dice[P2DiceRoll - 1]), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
                DiceUI.pack(pady=2)
                DiceRollUI = tkinter.Label(DiceGameUI, text=Users[1]+" scored: "+str(P2DiceRoll), bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
                DiceRollUI.pack(pady=20)
                DiceGameUI.update()
                DiceGameUI.update()
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                time.sleep(0.1)
                DiceGameUI.update()
                ###############################
                time.sleep(3)
                global Player1Score
                global Player2Score
                Player1Score = Player1Score + P1DiceRoll
                Player2Score = Player2Score + P2DiceRoll
                DiceGameUI.destroy()

            Title = tkinter.Label(DiceGameUI, text="Dice Game", bg=BackgroundColour, fg="white", font=(Font, 30, "bold"))
            Title.pack(pady=2)
            SubTitle = tkinter.Label(DiceGameUI, text="Round: Overtime - "+Users[0]+" ("+str(Player1Score)+" points)"+" vs "+Users[1]+" ("+str(Player2Score)+" points)", bg=BackgroundColour, fg="white", font=(Font, 10, "bold"))
            SubTitle.pack(pady=1)

            DiceUI = tkinter.Label(DiceGameUI, text=("◻"), bg=BackgroundColour, fg="white", font=(Font, 60, "bold"))
            DiceUI.pack(pady=2)

            RollButton = tkinter.Button(DiceGameUI, text="ROLL", font=(Font, 15, "bold"), width=20, height=1, command=lambda:DiceRoll(DiceUI, RollButton), bg=(f"#{127:02x}{13:02x}{115:02x}"), fg="white", borderwidth=3, activebackground=(f"#{127:02x}{13:02x}{115:02x}"), activeforeground="white")
            RollButton.pack(pady=10)

            DiceGameUI.mainloop()
        Results(UsersPlaying)

    Title = tkinter.Label(Play, text=str(Users[0])+" vs "+str(Users[1]), bg=BackgroundColour, fg="white", font=(Font, 40, "bold"))
    Title.pack(pady=5)
    SubTitle = tkinter.Label(Play, text="head to head in the Dice Game", bg=BackgroundColour, fg="white", font=(Font, 20, "bold"))
    SubTitle.pack(pady=2)
    TopScores = tkinter.Label(Play, text=TopScores, bg=BackgroundColour, fg="white", font=(Font, 10, "bold"))
    TopScores.pack(pady=10)

    PlayButton = tkinter.Button(Play, text="PLAY", font=(Font, 15, "bold"), width=20, height=1, command=ButtonClick, bg=(f"#{43:02x}{182:02x}{38:02x}"), fg="white", borderwidth=3, activebackground=(f"#{43:02x}{182:02x}{38:02x}"), activeforeground="white")
    PlayButton.pack(pady=20)

    Play.mainloop()

def DiceGameLogin(UserLabel, Colour):
    Login = tkinter.Tk()
    Login.title("Dice Game - Login")
    Login.attributes('-topmost', True)
    Login.resizable(False, False)
    Login.geometry("500x275")
    Login.config(bg=BackgroundColour)

    Title = tkinter.Label(Login, text="Login for "+str(UserLabel), bg=Colour, fg="white", font=(Font, 20, "bold"))
    Title.pack(pady=10)
    UserTitle = tkinter.Label(Login, text="Username:", bg=BackgroundColour, fg="white", font=(Font, 12))
    UserTitle.pack(pady=2)
    Username = tkinter.Entry(Login, font=(Font, 12, "bold"), width=20, bg=BackgroundColour, fg="white", borderwidth=3, insertbackground="white")
    Username.pack(pady=2)
    PassTitle = tkinter.Label(Login, text="Password:", bg=BackgroundColour, fg="white", font=(Font, 12))
    PassTitle.pack(pady=2)
    Password = tkinter.Entry(Login, font=(Font, 12, "bold"), width=20, bg=BackgroundColour, fg="white", borderwidth=3, insertbackground="white")
    Password.pack(pady=2)

    def LoginAction():
        global LoginReturnVal
        global UsersPlaying
        User = Username.get()
        Pass = Password.get()
        File = __file__
        File = File.replace("DiceGame.py", "ExternalStores.csv")
        with codecs.open(File, "r", encoding="utf-8") as file:
            global Data
            Data = list(csv.reader(file, delimiter=","))
        Usernames = [row[0] for row in Data]
        Passwords = [row[1] for row in Data]
        if User in Usernames:
            if Pass == Passwords[Usernames.index(User)]:
                Login.destroy()
                if User in UsersPlaying:
                    LoginReturnVal = "Invalid"
                else:
                    LoginReturnVal = "Valid"
                    UsersPlaying.append(User)
            else:
                Login.destroy()
                LoginReturnVal = "Invalid"
        else:
            Login.destroy()
            LoginReturnVal = "Invalid"

    LoginButton = tkinter.Button(Login, text="Login", font=(Font, 15), width=20, height=1, command=LoginAction, bg=BackgroundColour, fg="white", borderwidth=3, activebackground=BackgroundColour, activeforeground="white")
    LoginButton.pack(pady=20)

    Login.mainloop()

def LoginFail():
    messagebox.showerror(title="Cannot login", message="The username or password provided is incorrect or has already been used for player 1/2.")

DiceGameLogin("Player 1", (f"#{141:02x}{0:02x}{0:02x}"))
if LoginReturnVal == "Valid":
    LoginReturnVal = "User Exit Before Login"
    DiceGameLogin("Player 2", (f"#{0:02x}{0:02x}{141:02x}"))
    if LoginReturnVal == "Valid":
        HighScoreList = "High Scores:"
        for row in Data:
            HighScoreList = HighScoreList+"\n"+str(row[0])+" - "+str(row[2])
        PlayScreen(UsersPlaying, HighScoreList)
    elif LoginReturnVal == "User Exit Before Login":
        exit()
    else:
        LoginFail()
elif LoginReturnVal == "User Exit Before Login":
    exit()
else:
    LoginFail()