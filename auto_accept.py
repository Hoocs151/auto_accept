import pyautogui
from python_imagesearch.imagesearch import imagesearch
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
pyautogui.PAUSE = 0.5

def click_image(img_path):
    pos = imagesearch(img_path, IMAGE_THRESHOLD)
    if pos[0] == -1:
        return False
    pyautogui.click(pos[0], pos[1])
    return True

def wait_for_image(img_path):
    pos = imagesearch(img_path, IMAGE_THRESHOLD)
    while pos[0] == -1:
        pos = imagesearch(img_path, IMAGE_THRESHOLD)
    pyautogui.click(pos[0], pos[1])

def is_game_cancelled():
    accepted, play = imagesearch(acceptedButtonImg, IMAGE_THRESHOLD), imagesearch(playButtonImg, IMAGE_THRESHOLD)
    return accepted[0] == -1 and not play[0] == -1

def print_message(message, color):
    print(f"{color}[ + ] {message} [ + ]{Style.RESET_ALL}")

def run():
    while True:
        wait_for_image(acceptButtonImg)

        while True:
            if is_game_cancelled():
                print_message("Game has been cancelled", Fore.YELLOW)
                break
            checkGameAvailableLoop()

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print_message("Game accepted", Fore.GREEN)
            break

if __name__ == '__main__':
    print(Fore.LIGHTCYAN_EX + """\ 
 ▄  █ ████▄ ████▄ ▄█▄      ▄▄▄▄▄   
█   █ █   █ █   █ █▀ ▀▄   █     ▀▄ 
██▀▀█ █   █ █   █ █   ▀ ▄  ▀▀▀▀▄   
█   █ ▀████ ▀████ █▄  ▄▀ ▀▄▄▄▄▀    
   █              ▀███▀            
  ▀                                
                                    """ + Style.RESET_ALL)
    print_message("Started Searching", Fore.BLUE)
    try:
        run()
    except Exception as e:
        print_message(f"An error occurred: {str(e)}", Fore.RED)
