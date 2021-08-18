# http://code.activestate.com/recipes/124894-stopwatch-in-tkinter/
# C:\Python\Python37\python.exe "$(FULL_CURRENT_PATH)"
from tkinter import *
import time

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self.lim = 120.0
        self._running = 0
        self.timestr = StringVar()        
        self.makeWidgets()  
        self._setTime(self._elapsedtime) 
       

    def makeWidgets(self):                         
        """ Make the time label. """
        self.label = Label(self, textvariable=self.timestr,font=("Courier", 250))
        self._setTime(self._elapsedtime)
        self.label.pack(fill=X, expand=YES, pady=250)
        self.label.config(bg = "green")
        
    
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
            self.label.config(bg = "black")
        elif int(self.lim - elap) < 30:
            self.label.config(bg = "red")
        elif int(self.lim - elap) < 60:
            self.label.config(bg = "yellow")

        
    def Start(self, event=None):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    
    def Stop(self, event=None):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    
    def Reset(self, event=None):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        self.label.config(bg = "green")
        
        
def main():
    root = Tk()
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # use the next line if you also want to get rid of the titlebar
 #   root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    
    sw = StopWatch(root)

    sw.pack(side=TOP)
 
    root.bind("<space>",sw.Reset)
    root.bind("p",sw.Stop)
    root.bind("s",sw.Start)

 #   Button(root, text='Quit', command=root.quit).pack(side=BOTTOM)
    Button(root, text='Reset', command=sw.Reset).pack(side=BOTTOM) 
    Button(root, text='Stop', command=sw.Stop).pack(side=BOTTOM)    
    Button(root, text='Start', command=sw.Start).pack(side=BOTTOM)



    
    root.mainloop()

if __name__ == '__main__':
    main()
