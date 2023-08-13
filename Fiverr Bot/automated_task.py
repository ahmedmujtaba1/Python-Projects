# Fiverr Link
seller_dashboard = "https://www.fiverr.com/users/khizranmohsin/seller_dashboard"
inbox_page = "https://www.fiverr.com/inbox"

# Random Waiting Timehttps://www.fiverr.com/users/akifofficial/seller_dashboard
waiting_time_start_range = 120  #in seconds
waiting_time_end_range = 300 #in seconds

import pyautogui
import time 
import random 
import datetime

# Type something on SearchBar
def type_in_search_bar(address):
    print("Typing in Search Bar\n")
    pyautogui.moveTo(x=556, y=89)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(address)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    
def reload():
    print("Reloading\n")
    xx = random.randint(0,waiting_time_start_range)
    yy = random.randint(xx,waiting_time_end_range)
    waiting_time = random.randint(xx,yy)
    
    pyautogui.moveTo(x=88,y=86)
    pyautogui.click()

    time.sleep(waiting_time)

    
def drag_mouse():
    print("Dragging\n")
    xx = random.randint(0,waiting_time_start_range)
    yy = random.randint(xx,waiting_time_end_range)
    waiting_time = random.randint(xx,yy)
    
    x_pos = random.randint(0,800)
    y_pos = random.randint(0,800)
    pyautogui.moveTo(x_pos,y_pos)
    time.sleep(waiting_time)
    pyautogui.scroll(-20)
    time.sleep(waiting_time)
    pyautogui.scroll(20)


def action():


    # waiting_time_start_range = int(input("Enter Lower Limit of Waiting Time : "))
    # waiting_time_end_range = int(input("Enter Upper Limit of Waiting Time : "))

    print("Fiverr BOT is ready for action. Waiting 5 second for screen positioning")

    
    time.sleep(5)
    count = 1
    while(True):
        with open("fiver_bot_log.txt","a") as f:
            type_in_search_bar(seller_dashboard)
            print(f"{count}.{datetime.datetime.now()} Typed in Search Bar - Seller Dashboard\n")
            f.write(f"{count}.{datetime.datetime.now()} Typed in Search Bar - Seller Dashboard\n")
            count+=1
            
            reload()
            
            f.write(f"{count}.{datetime.datetime.now()} Reloaded Seller Board\n")
            count+=1
            
            for i in range (0,10):
                drag_mouse()
                f.write(f"{count}.{datetime.datetime.now()} Dragged Mouse\n")
                count+=1
                
            type_in_search_bar(inbox_page)

            f.write(f"{count}.{datetime.datetime.now()} Typed in Search Bar - Inbox\n")
            count+=1

            reload()
            f.write(f"{count}.{datetime.datetime.now()} Reloaded Seller Board\n")
            count+=1
        f.close()

action()
