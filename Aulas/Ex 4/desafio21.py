from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
import time
print('-'*30)
print('Tocando... ')
time.sleep(10)
print('Finalizado.')
print('-'*30)