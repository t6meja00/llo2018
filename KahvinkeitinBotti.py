# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import datetime
import sys
import time
import telepot
import telegram
from telepot.loop import MessageLoop
       
GPIO.setmode(GPIO.BCM)
#Kahvinkeiton aloittamisen nappi
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Keitettävien kahvikuppien määrä
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Telegram-botin token
bot = telepot.Bot('546598924:AAHoDfS6Qj-q3DDrv6Vi2njFM0a_2osOISk')
#Keitettävien kahvikuppien määrä
amountOfCoffee = 1
#Aika kahvin valmistumiseen
timeToSleep = 10.0
#Maksimi määrä kahvia
maxAmountOfCoffee = 10

bot.sendMessage(494911182, "KahviBotti valmiudessa!")
print("Kahvin määrä: " + str(amountOfCoffee) + " kupillinen.")
bot.sendMessage(494911182, "Kahvin määrä: " + str(amountOfCoffee) + " kupillinen.")
                    
while True:
    startPin = GPIO.input(18)
    increasePin = GPIO.input(23)
    
    if startPin== False:
        if amountOfCoffee == 1:
            bot.sendMessage(494911182, "Kahvinkeitin käynnistetty: Kahvia keitetään " + str(amountOfCoffee) + " kupillinen. " + str(datetime.datetime.now()))
            time.sleep(timeToSleep * amountOfCoffee)
            bot.sendMessage(494911182, "Kahvi valmista! Kahvia keitettiin: " + str(amountOfCoffee) + " kupillinen. " + str(datetime.datetime.now()))
        else:
            bot.sendMessage(494911182, "Kahvinkeitin käynnistetty: Kahvia keitetään " + str(amountOfCoffee) + " kupillista. " + str(datetime.datetime.now()))
            time.sleep(timeToSleep * amountOfCoffee)
            bot.sendMessage(494911182, "Kahvi valmista! Kahvia keitettiin: " + str(amountOfCoffee) + " kupillista. " + str(datetime.datetime.now()))
            amountOfCoffee = 1
        
    if increasePin == False:
        amountOfCoffee = amountOfCoffee + 1
        if amountOfCoffee > maxAmountOfCoffee:
            print("Ei voida keittää noin montaa kupillista kahvia! Asetetaan kahvin määrä 1:ksi.")
            bot.sendMessage(494911182, "Ei voida keittää noin montaa kupillista kahvia! Asetetaan kahvin määrä 1:ksi.")
            amountOfCoffee = 1
            print("Kahvin määrä: " + str(amountOfCoffee) + " kupillinen.")
            bot.sendMessage(494911182, "Kahvin määrä: " + str(amountOfCoffee) + " kupillinen.")
            time.sleep(0.5)
        else:
            bot.sendMessage(494911182, "Kahvin määrä: " + str(amountOfCoffee) + " kupillista.")
            print("Kahvin määrä: " + str(amountOfCoffee) + " kupillista.")
            time.sleep(0.5)
        




        


