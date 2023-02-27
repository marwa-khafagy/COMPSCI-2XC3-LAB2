import matplotlib.pyplot as plot

class PlotGroup:

    def __init__(self, _label, _color = None):
        self.xpoints = []
        self.ypoints = []
        self.label = _label
        self.count = 0
        self.colour = _color

        self.placelineAtFirstY1 = False
        self.placeVerticalLineAtX = 0
        self.placedLine = False;

    def add_point(self, x, y):
        self.xpoints.append(x)
        self.ypoints.append(y)
        self.count += 1

    def plot(self):

        if (self.colour == None):
            plot.plot(self.xpoints, self.ypoints, label=self.label)
        else:
            plot.plot(self.xpoints, self.ypoints, color=self.colour, label=self.label)

        #Plot If
        self.plot_vertical_line_after_y1()

    def plot_vertical_line_after_y1(self):

        #Exit
        if not self.placelineAtFirstY1:
            return

        #Count
        lastYbiggerthan1 = self.count

        #Find When Y < 1
        while (lastYbiggerthan1 >= 0):
            #Found, Exit

            if (self.ypoints[lastYbiggerthan1-1] < 1):
                break;

            lastYbiggerthan1 -= 1

        #None Found, Therefor Always bigger than 1
        if lastYbiggerthan1 <= 0 or lastYbiggerthan1 == self.count:
            return
        
        #Get X
        x=self.xpoints[lastYbiggerthan1]
        plot.axvline(x=x, color = '#BFBFBF', label=f'Always 1 at & after x={x}')