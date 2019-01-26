import pygame,sys
import random
from pygame.locals import *
import math


pygame.init()

DIMENSIONS=[485,375]

screen=pygame.display.set_mode(DIMENSIONS,RESIZABLE)
pygame.display.set_caption('Guess The Word')
BG_COLOR=[50,50,50]
#BG_COLOR=[233,249,242]

screen.fill(BG_COLOR)
pygame.display.flip()


dictionary={"QUALIFICATION":"The act of qualifying","RECYCLE":"Convert waste into reusable form","SALVATION":"The saving of someone from harm","MALFUNCTION":"Fail to function normally",
"INTERCOM":"An electrical device allowing one-way or two-way communication","GYROSCOPE":"A rotating device used for maintaining stability or a fixed direction","CLAUSTROPHOBIA":"An extreme fear of being in an enclosed place",
"BARBECUE":"An outdoor meal at which food is grilled over an open fire ","ANNIHILATION":"To destroy compeletely","DELEGATE":"A person sent to represent","FONDUE":"A dish of melted cheese","JURISDICTION":"The official power to make legal decisions",
"KINDLE":"Light a flame","QUENCH":"To satisy thirst","LIQUORICE":"A black substance used as a sweet","PENTHOUSE":"A flat on the top floor of a tall building","RATATOUILLE":"A movie was made on this dish featuring a chef mouse","TODDLER":"A yound child who is just beginning to walk",
"UNDERTAKER":"A person whose job is to prepare dead bodies for burial","VICEROY":"A person sent by a monarch to govern a colony","WARRIOR":"An experienced or brave fighter","XEROX":"A photocopy","YOGA":"An exercise based on Hindu philosopy",
"ZENITH":"A point of gretest power or success","HOLOCAUST":"Destruction or killing on a mass scale","INFERNO":"A large uncontrollable fire","KAMIKAZE":"A sucide bomber",
"MARVEL":"A wonder","COMPUTER":"A programmable device used for big calculations","ORIGAMI":"Japanese art of paper folding","ISOSCELES":'Having 2 sides equal',"HAMBURGER":"An iconic American fast food",
"YESTERDAY":"The day before today","NOSTALGIC":"Remembering a memory of past","ORB":"A precious spherical ornament","PENNY":"Coin","SECLUSION":"The state of being private and apart from others","UNIVERSITY":"An educational institute/college",
"DISTICTION":"Outstanding excellence","DIGNITY":"State of being in respect","ALTIMETER":"A device to show altitude",
"FLOPPY":"A portable storage device used in 1990s","WISDOM":"The quality of being wise","TORNADO":"A voilent rotating windstorm","MASTERPIECE":"A work of outstanding skill","GUARANTEE":"A formal promise to do something","LAUGH":"An act of laughing"
,"FRIGHT":"A sudden strong felling of fear","MORTGAGE":"Transfer a property to a creditor as a security for a loan",'BLACKOUT':'A short period when all lights are gone','BOARDGAME':'A game played on a board',
'BREAKTHROUGH':'An game-changing scientific discovery','BUSNINESSMAN':'A person working in business','CALAMITY':'A natural disaster','CALCULATE':'Finding the result of an operation on 2 nos.','CARBONATED':'CO2 or fizz added drink','CARPENTER':'A person who makes wooden furniture',
'CONTRAST':'Opposite of each other','DARTBOARD':'A board used in darts game','DEFICIENCY':'Lack of something necessary','UNDISPUTED':'Cannot be doubted or questioned','UNRAVEL':'To come apert or collapse','UPSHOT':'The final result or outcome','VODKA':'A Russian strong alcoholic drink',
'SPINNER':'A spinning toy','PRESTIGE':'The power to impress others','PEN':'What is mightier than sword','OUST':'To remove someone from his job for oneself','OZONE LAYER':'Protective blanket which stops UV light','OUIJA BOARD':'A board to talk with the dead',
'NOSTALGIA':'The feeling of remembering the memories of past','INFIRMARY':'A small hospital or room for ill people','HERBICIDE':'A chemical to destroy unwanted plants','HACKSAW':'A tool to cut metal','GYMNASIUM':'A place for physical exercise','GRATITUDE':'To show thankfullness','FOURSOME':'F**R people playing a game',
'HALO':'The circle of light above an angel head','TRIUMPH':'A feeling of great satisfaction after victory','SWASTIKA':'A Nazi or Hindu mythology symbol','RUGBY':'American football','QUARTER':'A period of 4 months','QUARANTINE':'Harmfull','WAYFARER':'A traveller on foot',
'ZODIAC':'Astrological symbol','YESTERYEAR':'An year before','YAMMER':'To talk loudly continously','TRAPEZIUM':'A quadrilateral with two sides parallel','TELLTALE':'A secret going on from one generation to another','LASSITUDE':'A state of feeling very tired physically and mentally'}




word_list=list(dictionary.keys())
help_list=list(dictionary.values())
used_words=[]

#########------------------------sounds-----------

def play_keyboard_sound():
    mouse_sound = pygame.mixer.Sound("keyboard_sound.wav")
    pygame.mixer.Sound.play(mouse_sound)
    pygame.mixer.music.stop()

def play_mouse_sound():
    mouse_sound = pygame.mixer.Sound("mouse_sound.wav")
    pygame.mixer.Sound.play(mouse_sound)
    pygame.mixer.music.stop()
    






def getNewWord():
    return random.choice(word_list).upper()


def getHelp(current_word):
    return dictionary[current_word].capitalize()


def set_word(word,unlock_letters=''):
    temp=''
    for a in word:
        if a.upper() in unlock_letters.upper():
            temp+=a
        elif a.upper()  not in 'AEIOU':
            temp+='-'
        else:
            temp+=a
    return temp.upper()


def display_word(word,color,cord,size):
    f=pygame.font.match_font('erasmediumitc')
    font = pygame.font.Font(f, int(size))
    text = font.render(word, True, color)
    screen.blit(text, cord)
    
def draw_gfx(round_no=0,gussed_word=' '):
    screen.fill(BG_COLOR)
    help_box=pygame.draw.rect(screen,[0,255,0],[302,315,182,60])
    display_word('HINT',BG_COLOR,[300,300],80)

    display_word(gussed_word,[255,201,14],[10,100],(560/len(gussed_word)))
    display_word('POINTS: '+str(points),[255,0,0],[20,20],30)
    display_round(round_no+1)
    
    return help_box




def display_round(round_no):
    f1=pygame.font.match_font('AGENCYFB')
    f2=pygame.font.match_font('lcd')
    font1 = pygame.font.Font(f1, 60)
    font2 = pygame.font.Font(f2, 60)
    text1 = font1.render('ROUND:', True, [255,0,255])
    text2 = font2.render(str(round_no), True, [255,255,0])
    screen.blit(text1, [280,10])
    screen.blit(text2, [432,37])
    

def display_name(name='Guest Player'):
    display_won()
    f1=pygame.font.match_font('ARIAL')
    font1 = pygame.font.Font(f1, 30)
    text1 = font1.render('Please Enter your name: ', True, [255,0,255])
    text2 = font1.render(name, True, [255,255,0])
    screen.blit(text1, [120,235])
    screen.blit(text2, [120,270])
    pygame.display.update()


def display_won():
    screen.fill([50,50,50])
    f1=pygame.font.match_font('AGENCYFB')
    font1 = pygame.font.Font(f1, 80)
    text1 = font1.render('WON', True, [255,255,255])
    screen.blit(text1,[190,150])
    return
    
    
def display_continue():
    screen.fill(BG_COLOR)
    f1=pygame.font.match_font('AGENCYFB')
    font1 = pygame.font.Font(f1, 55)
    text1 = font1.render('ROUND FINISHED', True, [0,0,0])
    text2 = font1.render('Shall we continue...', True, [255,255,255])
    screen.blit(text1,[100,170])
    screen.blit(text2,[70,225])
    flagg=True
    pygame.display.update()
    while flagg:
        for e in pygame.event.get():
            if e.type==MOUSEMOTION:
                flagg=False
            if e.type==MOUSEBUTTONDOWN:
                flagg=False
            if e.type==KEYDOWN:
                flagg=False

def show_fps(time):
    pygame.draw.rect(screen,BG_COLOR,[0,360,120,15])
    
    f1=pygame.font.match_font('ARIAL')
    font1 = pygame.font.Font(f1, 20)
    text1 = font1.render('FPS: '+str(math.ceil(int(time.get_fps()))), True, [120,120,140])
    screen.blit(text1,[0,360])
    #pygame.display.update()
    
def show_promo():
    f1=pygame.font.match_font('ARIAL')
    font1 = pygame.font.Font(f1,55)
    text1 = font1.render('Guess The Word', True, [125,125,125])
    screen.blit(text1,[70,60])
    font2 = pygame.font.Font(f1,25)
    text2 = font2.render('-TJ Productions 2017', True, [200,200,200])
    screen.blit(text2,[120,110])
    pygame.display.update()
    
show_promo()
used_words=[]



def main():
    global round_no,points,used_words
    flag=True

    while True:
        current_word=getNewWord()
        if current_word not in used_words:
            used_words+=[current_word]
            break
    
    gussed_word=set_word(current_word)
    hint=getHelp(current_word)
 
    
    if round_no!=0:
        display_continue()
        pygame.display.update()

    clock=pygame.time.Clock()
    hint_shown=False
    change=True
    won=False
    letters=''
    i=0
    while flag:
        if i<60:
            help_box=draw_gfx()
            change=False
            i+=1
        elif i==60:
            change=True
            i+=1
        else:
            change=False
            
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
                points=0
                sys.exit()

            elif e.type==KEYDOWN:
                play_keyboard_sound()
                letter=e.unicode.upper()
                if letter not in current_word:
                    points+=-10
                
                
                elif letter in current_word:
                    if letter in gussed_word and letter!='-':
                        points+=-5
                        change=True
                        continue
                    letters+=letter
                    points+=20
                    gussed_word=set_word(current_word,letters)
                change=True


            elif e.type==MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                play_mouse_sound()
                change=True
                if help_box.collidepoint(mouse_pos):
                    if not hint_shown:
                        hint_shown=True
                        points+=-60
                        change=True

            elif gussed_word==current_word:
                points+=40
                won=True


            else:
                pass
                #change=False
                


        
        
        if change:
            draw_gfx(round_no,gussed_word)
            if hint_shown==True:
                display_word(hint,[250,250,250],[0,200],16)
            if won and round_no==19:
                display_won()
                return [False,1,clock]
            if won:
                return [True,0]
            pygame.display.update()
            
        clock.tick(30)
        
                    
                
    return False


points=0
for round_no in range(20):
    a=main()
    if not a[0]:
        if a[1]:
            display_name()
            clock=a[2]
            name=''
            qq=0
            while True:
                if qq==1:
                    f=open('Point List.txt','a')
                    f.write(name+':                                 '+str(points)+'\n')
                    f.close()
                    break
                for e in pygame.event.get():
                    if e.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if e.type==KEYDOWN:
 
                        if e.key==13:
                            qq=1
                        name+=e.unicode
                        display_name(name)
                        
                clock.tick(30)
                
pygame.quit()
        
        
        
