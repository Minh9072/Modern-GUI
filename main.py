########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

# import function
from src.Functions import GuiFunctions, TemperatureChart, HumidityChart, HeatIndexChart
from src.ui_interface import Ui_MainWindow


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        #############################################
        # APPLICATION FUNCTIONS AND EVENTS
        #############################################
        self.app_functions = GuiFunctions(self)

        #############################################
        # create chart
        #############################################
        self.chartWidget = HumidityChart(self.ui.humdChart)
        layout_humd = QVBoxLayout(self.ui.humdChart)
        layout_humd.addWidget(self.chartWidget)

        self.chartWidget = TemperatureChart(self.ui.tempChart)
        layout_temp = QVBoxLayout(self.ui.tempChart)
        layout_temp.addWidget(self.chartWidget)

        #self.ui.humdChart.setMaximumWidth(600)
        #self.ui.tempChart.setMaximumWidth(600)

        self.ui.humdChart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.tempChart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.chartWidget = HeatIndexChart(self.ui.HeatIndexChart)
        layout_temp = QVBoxLayout(self.ui.HeatIndexChart)
        layout_temp.addWidget(self.chartWidget)

    #######################################################################
    # GET THE THEME CHANGE PROGRESS
    #######################################################################
    # sassCompilationProgress() is the default function that sass compiler
    # will look for and return the progress value to
    def sassCompilationProgress(self, n):
        # n is the percentage progress value
        # print(n)
        self.ui.activeProgress.setValue(n)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
