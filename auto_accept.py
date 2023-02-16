import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

# Constants
acceptButtonImg = './sample.png'
acceptedButtonImg = './sample-accepted.png'
playButtonImg = './play-button.png'
IMAGE_THRESHOLD = 0.8
TIMELAPSE = 1

pyautogui.FAILSAFE = False

def click_image(img_path):
    pos = imagesearch(img_path, IMAGE_THRESHOLD)
    if pos[0] == -1:
        return False
    pyautogui.click(pos[0], pos[1])
    return True

def wait_for_image(img_path):
    while True:
        if click_image(img_path):
            break
        time.sleep(TIMELAPSE)

def is_game_cancelled():
    accepted = imagesearch(acceptedButtonImg, IMAGE_THRESHOLD)
    play = imagesearch(playButtonImg, IMAGE_THRESHOLD)
    return accepted[0] == -1 and not play[0] == -1

def run():
    while True:
        wait_for_image(acceptButtonImg)

        while True:
            if is_game_cancelled():
                print(Fore.YELLOW + "[ + ] Game has been cancelled [ + ]" + Style.RESET_ALL)
                break
            checkGameAvailableLoop()

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print(Fore.GREEN + "[ + ] Game accepted [ + ]" + Style.RESET_ALL)
            break
        
        time.sleep(TIMELAPSE)

if __name__ == '__main__':
    print(Fore.LIGHTCYAN_EX + """\ 
 ▄  █ ████▄ ████▄ ▄█▄      ▄▄▄▄▄   
█   █ █   █ █   █ █▀ ▀▄   █     ▀▄ 
██▀▀█ █   █ █   █ █   ▀ ▄  ▀▀▀▀▄   
█   █ ▀████ ▀████ █▄  ▄▀ ▀▄▄▄▄▀    
   █              ▀███▀            
  ▀                                
                                    """ + Style.RESET_ALL)
    print(Fore.BLUE + "[ + ] Started Searching [ + ]" + Style.RESET_ALL)
    try:
        run()
    except Exception as e:
        print(Fore.RED + "An error occurred: " + str(e) + Style.RESET_ALL)
