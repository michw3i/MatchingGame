import random
import pygame as p


def draw(screen, NumOfNeedles, Success, ExperProb, TheorProb, PiEstimate, directions=0):
    font = p.font.SysFont("Arial Black", 14)
    NeedleStat = font.render("Total needles: " + str(NumOfNeedles), True, "black")
    Successes = font.render("Total needles crossing lines: " + str(Success), True, "black")
    ExperimentalStat = font.render("Experimental probability: " + str(ExperProb), True, "black")
    TheoreticalStat = font.render("Theoretical probability: " + str(TheorProb), True, "black")
    Pi = font.render("Pi estimate: " + str(PiEstimate), True, "black")
    StatisticsText = [NeedleStat, Successes, ExperimentalStat, TheoreticalStat, Pi]
    directions = None
    for text in range(len(StatisticsText)):
        screen.blit(StatisticsText[text], (605, text * 100))


    listx = ["A floor is made of parallel strips","of wood and you drop a needle", "onto the floor. What is the",
             "probability that the needle will", "lie across two strips of wood", "Hit the Green button to start", "throwing the needles. "
    "Look at the","side panel to see statistics", "and estimation of pi."]
    x = 440
    for i in range(len(listx)):
        font = p.font.SysFont('Arial Black', 16)
        text1 = font.render(str(listx[i]), True, 'black')
        screen.blit(text1, (600, x))
        x = x + 20