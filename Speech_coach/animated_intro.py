import os
import time
import random
from datetime import datetime
import math


# Get the current date and time
current_datetime = datetime.now()

# Extract hours, minutes, and seconds
hours = current_datetime.hour
minutes = current_datetime.minute
seconds = current_datetime.second

# Format the time as "h:m:s"
def clock():
    clocks= f"{hours:02}:{minutes:02}:{seconds:02}"
    return clocks





class walker:
    def __init__(self, percentage, count, totalCount):
        self.percentage = percentage
        self.count = count
        self.totalCount = totalCount
    def step0(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f' O                           ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('/|\                          ////////////////////////x')
        print('/ \                          |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
    
    def step1(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'  O                          ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print(' /|\                         ////////////////////////x')
        print('  |                          |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
        
    def step2(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'   O                         ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('  /|\                        ////////////////////////x')
        print('  / \                        |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
        
    def step3(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'   O                         ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('  /|\                        ////////////////////////x')
        print('   |                         |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
        
    def step4(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'    O                        ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('   /|\                       ////////////////////////x')
        print('   / \                       |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
    
    def step5(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'      O                      ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('     /|\                     ////////////////////////x')
        print('      |                      |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------') 
    def step6(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'       O                     ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('      /|\                    ////////////////////////x')
        print('      / \                    |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
    
    def step7(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'         O                   ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('        /|\                  ////////////////////////x')
        print('         |                   |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')
    
    def step8(self):
        print(f'count: {self.count}                                  {clock()}')
        print('-----------------------------------------------------------------')    
        print('                             /////////////////////////')
        print('                             || Filler Word Counter ||')
        print(f'                             ||                     ||')
        print(f'            O                ||   {self.percentage}% ||   {self.count}/{self.totalCount}!  ||')
        print('           /|\               ////////////////////////x')
        print('           / \               |||||||||||||||||||||||x')
        print('-----------------------------------------------------------------')  
        
    def walk(self):
        timer = 0.2
        for step in range(8):
            os.system('clear')
            getattr(self, f'step{step}')()
            time.sleep(timer)
    def walkaway(self):
        timer = 0.8
        
        for step in range(8, -1, -1):
            os.system('clear')
            getattr(self, f'step{step}')()
            time.sleep(timer)


def walking(percentage, count, totalCount):    
    walk = walker(str(percentage), int(count), int(totalCount))
    walking = walk.walk()
    
def walk_away(percentage, count, totalCount):    
    walk = walker(str(percentage), int(count), int(totalCount))
    walking = walk.walkaway()