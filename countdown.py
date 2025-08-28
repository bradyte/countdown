# http://code.activestate.com/recipes/124894-stopwatch-in-tkinter/
from tkinter import *
import time

class StopWatch(Frame):  
    GREEN = "dark green"
    YELLOW = "DarkGoldenrod3"
    RED = "red3"
    BLACK = "black"

    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None):        
        Frame.__init__(self, parent)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self.lim = 120.0
        self._running = 0
        self.timestr = StringVar()        
        self.makeWidgets()  
        self._setTime(self._elapsedtime) 
        self.configure(background=self.GREEN)
       
    def makeWidgets(self):                         
        """ Make the time label. """
        self.label = Label(self, textvariable=self.timestr,font=("Courier", 270))
        self._setTime(self._elapsedtime)
        self.label.pack(fill=X, expand=YES, pady=self.winfo_screenheight() / 4)
        self.label.config(bg=self.GREEN)

    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(10, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int((self.lim - elap) / 60)
        seconds = int((self.lim - elap) % 60)
        hseconds = int(99 - ((elap * 100) % 99))           
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

        if int(self.lim - elap) < 1:
            self.label.config(bg=self.BLACK)
            self.configure(background=self.BLACK)
        elif int(self.lim - elap) < 30:
            self.label.config(bg=self.RED)
            self.configure(background=self.RED)
        elif int(self.lim - elap) < 60:
            self.label.config(bg=self.YELLOW)
            self.configure(background=self.YELLOW)

    def start(self, event=None):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        

    def stop(self, event=None):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0

    def reset(self, event=None):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        self.label.config(bg = self.GREEN)
        self.configure(background = self.GREEN)
            
def main():
    root = Tk()
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    sw = StopWatch(root)

    sw.pack(side=TOP)
 
    root.bind("<space>", sw.reset)
    root.bind("p", sw.stop)
    root.bind("s", sw.start)

    Button(root, text='Reset', command=sw.reset).pack(side=BOTTOM) 
    Button(root, text='Stop', command=sw.stop).pack(side=BOTTOM)    
    Button(root, text='Start', command=sw.start).pack(side=BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    main()
