import pyautogui
import pyexcel as pe
import random
import time
import webbrowser
import threading



n=random.randint(1, 1920)
y=random.randint(1, 1080)
pyautogui.moveTo(n, y)
t=1
r=0
q=r+1
valeur=50



def enregistrement():
    webbrowser.open('https://www.google.com/recaptcha/api2/demo')
    départx=random.randint(1, 1920)
    départy=random.randint(1, 1080)
    pyautogui.moveTo(départx, départy)
    a,b=pyautogui.position()
    sheet=pe.get_sheet(file_name="Corécupjupy.xlsx")
    while (a<=47 or a>=71) or (b<=434 or b>=459)  :
            time.sleep(0.03)
            a,b=pyautogui.position()
            global t
            global r
            sheet[r,t]= a
            sheet[q,t]= b
            t = t + 1
    sheet[r,148]=0
    sheet[q,148]=0
    sheet[r,0]= 'X'
    sheet[q,0]= 'Y'         
    t=1
    time.sleep(1)
    sheet.save_as("Corécupjupy.xlsx")  

def mouvement():
    for i in range(valeur):
        vi=random.uniform(0.3, 3)
        cox = random.randint(48, 70)
        coy = random.randint(435,458)
        pyautogui.moveTo(cox,coy,vi)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(1.5)
    
    
#th1=threading.Thread(target=mouvement)


#th1.start()

for i in range(valeur):
    enregistrement()
    r += 2
    q=r+1
    

#th1.join()   
        
    

print("Merci")



