# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 779)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(55, 51))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(157, 163))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.homeBtn = QPushButton(self.widget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataAnalysisBtn = QPushButton(self.widget_2)
        self.dataAnalysisBtn.setObjectName(u"dataAnalysisBtn")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_solid/icons/font_awesome/solid/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataAnalysisBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.dataAnalysisBtn)

        self.reportsBtn = QPushButton(self.widget_2)
        self.reportsBtn.setObjectName(u"reportsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportsBtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.reportsBtn)

        self.graphsBtn = QPushButton(self.widget_2)
        self.graphsBtn.setObjectName(u"graphsBtn")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_solid/icons/font_awesome/solid/chart-pie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphsBtn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.graphsBtn)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(154, 362, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(141, 126))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.settingsBtn = QPushButton(self.widget_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.informationBtn = QPushButton(self.widget_3)
        self.informationBtn.setObjectName(u"informationBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/perm_device_information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.informationBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.informationBtn)

        self.helpBtn = QPushButton(self.widget_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.helpBtn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/font_awesome_solid/icons/font_awesome/solid/circle-xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.frame)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_8.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.widget_5, 0, Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_9 = QVBoxLayout(self.informationPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.informationPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignVCenter)

        self.centerMenuPages.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_9 = QWidget(self.helpPage)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_24 = QVBoxLayout(self.widget_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 100))
        self.label_5.setMaximumSize(QSize(100, 100))
        self.label_5.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/earth-asia.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_20 = QLabel(self.widget_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_20, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.widget_9, 0, Qt.AlignVCenter)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_11 = QVBoxLayout(self.mainBody)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.titleTxt = QLabel(self.header)
        self.titleTxt.setObjectName(u"titleTxt")

        self.horizontalLayout_7.addWidget(self.titleTxt)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.notificationBtn = QPushButton(self.frame_3)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreBtn = QPushButton(self.frame_3)
        self.moreBtn.setObjectName(u"moreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/material_design/icons/material_design/more_horiz.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_3)
        self.profileBtn.setObjectName(u"profileBtn")
        icon11 = QIcon()
        icon11.addFile(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_7.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.searchCont = QFrame(self.header)
        self.searchCont.setObjectName(u"searchCont")
        self.searchCont.setMaximumSize(QSize(294, 16777215))
        self.searchCont.setFrameShape(QFrame.StyledPanel)
        self.searchCont.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.searchCont)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.searchCont)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.searchInp = QLineEdit(self.searchCont)
        self.searchInp.setObjectName(u"searchInp")
        self.searchInp.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_8.addWidget(self.searchInp)

        self.searchBtn = QPushButton(self.searchCont)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_8.addWidget(self.searchBtn)


        self.horizontalLayout_7.addWidget(self.searchCont)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, -1, 5)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.header, 0, Qt.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.mainPageContents = QWidget(self.mainContents)
        self.mainPageContents.setObjectName(u"mainPageContents")
        self.verticalLayout_5 = QVBoxLayout(self.mainPageContents)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.mainPage = QCustomQStackedWidget(self.mainPageContents)
        self.mainPage.setObjectName(u"mainPage")
        self.homePage = QCustomSlideMenu()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_12 = QVBoxLayout(self.homePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_7 = QWidget(self.homePage)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lightBulbControl = QWidget(self.widget_7)
        self.lightBulbControl.setObjectName(u"lightBulbControl")
        self.verticalLayout_20 = QVBoxLayout(self.lightBulbControl)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_8 = QLabel(self.lightBulbControl)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.lightBulbIcon = QLabel(self.lightBulbControl)
        self.lightBulbIcon.setObjectName(u"lightBulbIcon")
        self.lightBulbIcon.setMinimumSize(QSize(80, 80))
        self.lightBulbIcon.setMaximumSize(QSize(80, 80))
        self.lightBulbIcon.setLayoutDirection(Qt.LeftToRight)
        self.lightBulbIcon.setAutoFillBackground(False)
        self.lightBulbIcon.setPixmap(QPixmap(u":/material_design/icons/material_design/flashlight_off.png"))
        self.lightBulbIcon.setScaledContents(True)
        self.lightBulbIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.lightBulbIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lightBulbOnBtn = QPushButton(self.lightBulbControl)
        self.lightBulbOnBtn.setObjectName(u"lightBulbOnBtn")
        self.lightBulbOnBtn.setMinimumSize(QSize(0, 0))
        icon15 = QIcon()
        icon15.addFile(u":/material_design/icons/material_design/radio_button_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lightBulbOnBtn.setIcon(icon15)
        self.lightBulbOnBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.lightBulbOnBtn, 0, Qt.AlignVCenter)

        self.lightBulbOffBtn = QPushButton(self.lightBulbControl)
        self.lightBulbOffBtn.setObjectName(u"lightBulbOffBtn")
        icon16 = QIcon()
        icon16.addFile(u":/material_design/icons/material_design/check_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lightBulbOffBtn.setIcon(icon16)
        self.lightBulbOffBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.lightBulbOffBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)


        self.horizontalLayout_12.addWidget(self.lightBulbControl)

        self.fanControl = QWidget(self.widget_7)
        self.fanControl.setObjectName(u"fanControl")
        self.verticalLayout_21 = QVBoxLayout(self.fanControl)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_17 = QLabel(self.fanControl)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_17, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.fanIcon = QLabel(self.fanControl)
        self.fanIcon.setObjectName(u"fanIcon")
        self.fanIcon.setMinimumSize(QSize(80, 80))
        self.fanIcon.setMaximumSize(QSize(80, 80))
        self.fanIcon.setPixmap(QPixmap(u":/material_design/icons/material_design/mode_fan_off.png"))
        self.fanIcon.setScaledContents(True)
        self.fanIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.fanIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.fanOnBtn = QPushButton(self.fanControl)
        self.fanOnBtn.setObjectName(u"fanOnBtn")
        self.fanOnBtn.setIcon(icon15)
        self.fanOnBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.fanOnBtn)

        self.fanOffBtn = QPushButton(self.fanControl)
        self.fanOffBtn.setObjectName(u"fanOffBtn")
        self.fanOffBtn.setIcon(icon16)
        self.fanOffBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.fanOffBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)


        self.horizontalLayout_12.addWidget(self.fanControl)

        self.tvControl = QWidget(self.widget_7)
        self.tvControl.setObjectName(u"tvControl")
        self.verticalLayout_22 = QVBoxLayout(self.tvControl)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_18 = QLabel(self.tvControl)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_18, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.tvIcon = QLabel(self.tvControl)
        self.tvIcon.setObjectName(u"tvIcon")
        self.tvIcon.setMinimumSize(QSize(80, 80))
        self.tvIcon.setMaximumSize(QSize(80, 80))
        self.tvIcon.setPixmap(QPixmap(u":/material_design/icons/material_design/tv_off.png"))
        self.tvIcon.setScaledContents(True)
        self.tvIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.tvIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tvOnBtn = QPushButton(self.tvControl)
        self.tvOnBtn.setObjectName(u"tvOnBtn")
        self.tvOnBtn.setIcon(icon15)
        self.tvOnBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_22.addWidget(self.tvOnBtn)

        self.tvOffBtn = QPushButton(self.tvControl)
        self.tvOffBtn.setObjectName(u"tvOffBtn")
        self.tvOffBtn.setIcon(icon16)
        self.tvOffBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_22.addWidget(self.tvOffBtn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)


        self.horizontalLayout_12.addWidget(self.tvControl)

        self.acControl = QWidget(self.widget_7)
        self.acControl.setObjectName(u"acControl")
        self.verticalLayout_23 = QVBoxLayout(self.acControl)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_19 = QLabel(self.acControl)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_19, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.acIcon = QLabel(self.acControl)
        self.acIcon.setObjectName(u"acIcon")
        self.acIcon.setMinimumSize(QSize(80, 80))
        self.acIcon.setMaximumSize(QSize(80, 80))
        self.acIcon.setPixmap(QPixmap(u":/material_design/icons/material_design/subtitles_off.png"))
        self.acIcon.setScaledContents(True)
        self.acIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.acIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.acOnBtn = QPushButton(self.acControl)
        self.acOnBtn.setObjectName(u"acOnBtn")
        self.acOnBtn.setIcon(icon15)
        self.acOnBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_23.addWidget(self.acOnBtn)

        self.acOffBtn = QPushButton(self.acControl)
        self.acOffBtn.setObjectName(u"acOffBtn")
        self.acOffBtn.setIcon(icon16)
        self.acOffBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_23.addWidget(self.acOffBtn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_7)


        self.horizontalLayout_12.addWidget(self.acControl)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.homePage)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tempChart = QWidget(self.widget_8)
        self.tempChart.setObjectName(u"tempChart")
        self.tempChart.setMinimumSize(QSize(0, 0))
        self.tempChart.setMaximumSize(QSize(10000, 10000))

        self.horizontalLayout_13.addWidget(self.tempChart)

        self.humdChart = QWidget(self.widget_8)
        self.humdChart.setObjectName(u"humdChart")
        self.humdChart.setMinimumSize(QSize(0, 0))
        self.humdChart.setMaximumSize(QSize(10000, 10000))

        self.horizontalLayout_13.addWidget(self.humdChart)


        self.verticalLayout_12.addWidget(self.widget_8)

        self.mainPage.addWidget(self.homePage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_13 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.dataAnalysisPage)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPage.addWidget(self.dataAnalysisPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_14 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.reportsPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPage.addWidget(self.reportsPage)
        self.graphsPage = QWidget()
        self.graphsPage.setObjectName(u"graphsPage")
        self.verticalLayout_15 = QVBoxLayout(self.graphsPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.HeatIndexChart = QWidget(self.graphsPage)
        self.HeatIndexChart.setObjectName(u"HeatIndexChart")

        self.verticalLayout_15.addWidget(self.HeatIndexChart)

        self.mainPage.addWidget(self.graphsPage)

        self.verticalLayout_5.addWidget(self.mainPage)


        self.horizontalLayout_10.addWidget(self.mainPageContents)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(180, 0))
        self.verticalLayout_16 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.widget_6 = QWidget(self.rightMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.closeRightMenuBtn = QPushButton(self.widget_6)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeRightMenuBtn.setIcon(icon17)

        self.horizontalLayout_11.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_16.addWidget(self.widget_6, 0, Qt.AlignRight)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.verticalLayout_17 = QVBoxLayout(self.notificationsPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.notificationsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rightMenuPages.addWidget(self.notificationsPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_18 = QVBoxLayout(self.morePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_15 = QLabel(self.morePage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rightMenuPages.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_19 = QVBoxLayout(self.profilePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.profilePage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rightMenuPages.addWidget(self.profilePage)

        self.verticalLayout_16.addWidget(self.rightMenuPages)


        self.horizontalLayout_10.addWidget(self.rightMenu)


        self.verticalLayout_11.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.activeProgress = QProgressBar(self.frame_2)
        self.activeProgress.setObjectName(u"activeProgress")
        self.activeProgress.setMaximumSize(QSize(16777215, 10))
        self.activeProgress.setValue(24)
        self.activeProgress.setTextVisible(False)

        self.horizontalLayout_5.addWidget(self.activeProgress)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignRight)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"    Home", None))
        self.dataAnalysisBtn.setText(QCoreApplication.translate("MainWindow", u"     Analysis", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"    Reports", None))
        self.graphsBtn.setText(QCoreApplication.translate("MainWindow", u"    Graphs", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"    Settings", None))
        self.informationBtn.setText(QCoreApplication.translate("MainWindow", u"    Information", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"    Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Control Interface UI v1 </p><p>Copyright Qt Designer<br/>Tr\u01b0\u01a1ng Ng\u1ecdc Minh</p></body></html>", None))
        self.label_5.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#1f1f1f;\">Access for support:</span></p><p>https://www.qt.io/</p></body></html>", None))
        self.titleTxt.setText(QCoreApplication.translate("MainWindow", u"Control UI", None))
        self.notificationBtn.setText("")
        self.moreBtn.setText("")
        self.profileBtn.setText("")
        self.label_9.setText("")
        self.searchInp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Light Bulb", None))
        self.lightBulbIcon.setText("")
        self.lightBulbOnBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.lightBulbOffBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fan", None))
        self.fanIcon.setText("")
        self.fanOnBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.fanOffBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TV", None))
        self.tvIcon.setText("")
        self.tvOnBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.tvOffBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.acIcon.setText("")
        self.acOnBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.acOffBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Truong Ngoc Minh", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright Truong Ngoc Minh", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme Process", None))
    # retranslateUi

