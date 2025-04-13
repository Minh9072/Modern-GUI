# GUI functions

# Import necessary modules from PySide6 and custom widgets
import random
import requests

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer, QPointF
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPen
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QVBoxLayout, QGraphicsSimpleTextItem

from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QLineSeries
from PySide6.QtGui import QPainter

from PySide6.QtGui import QPixmap, QIcon
from Qss.icons.iconsSrc import *

import numpy as np

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow  # Store the mainwindow instance
        self.ui = MainWindow.ui  # Store the ui instance

        # apply font
        self.loadProductSansFont()

        # init app theme
        self.initializeAppTheme()

        # add click event to search button
        self.ui.searchBtn.clicked.connect(self.showSearchResults)
        
        # connect menu btn
        self.connectMenuButtons()

        # connect on off button
        self.connectOnOffButtons()

    # connect menu buttons
    def connectMenuButtons(self):
        """Connect buttons to expand/collapse menu widgets."""
        # Expand center menu widget
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.informationBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        # Close center menu widget
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        # Expand right menu widget
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        # Close right menu widget
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())


    # connect on off buttons
    def connectOnOffButtons(self):
        """Connect buttons to change image."""
        self.ui.lightBulbOnBtn.clicked.connect(lambda: self.ui.lightBulbIcon.setPixmap(QPixmap(":/material_design/icons/material_design/flashlight_on.png" )))
        self.ui.lightBulbOnBtn.clicked.connect(lambda: self.ui.lightBulbOnBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.lightBulbOnBtn.clicked.connect(lambda: self.ui.lightBulbOffBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.lightBulbOffBtn.clicked.connect(lambda: self.ui.lightBulbIcon.setPixmap(QPixmap(":/material_design/icons/material_design/flashlight_off.png" )))
        self.ui.lightBulbOffBtn.clicked.connect(lambda: self.ui.lightBulbOffBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.lightBulbOffBtn.clicked.connect(lambda: self.ui.lightBulbOnBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.fanOnBtn.clicked.connect(lambda: self.ui.fanIcon.setPixmap(QPixmap(":/font_awesome_solid/icons/font_awesome/solid/fan.png" )))
        self.ui.fanOnBtn.clicked.connect(lambda: self.ui.fanOnBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.fanOnBtn.clicked.connect(lambda: self.ui.fanOffBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.fanOffBtn.clicked.connect(lambda: self.ui.fanIcon.setPixmap(QPixmap(":/material_design/icons/material_design/mode_fan_off.png" )))
        self.ui.fanOffBtn.clicked.connect(lambda: self.ui.fanOffBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.fanOffBtn.clicked.connect(lambda: self.ui.fanOnBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.tvOnBtn.clicked.connect(lambda: self.ui.tvIcon.setPixmap(QPixmap(":/material_design/icons/material_design/tv.png" )))
        self.ui.tvOnBtn.clicked.connect(lambda: self.ui.tvOnBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.tvOnBtn.clicked.connect(lambda: self.ui.tvOffBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.tvOffBtn.clicked.connect(lambda: self.ui.tvIcon.setPixmap(QPixmap(":/material_design/icons/material_design/tv_off.png" )))
        self.ui.tvOffBtn.clicked.connect(lambda: self.ui.tvOffBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.tvOffBtn.clicked.connect(lambda: self.ui.tvOnBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.acOnBtn.clicked.connect(lambda: self.ui.acIcon.setPixmap(QPixmap(":/material_design/icons/material_design/subtitles.png" )))
        self.ui.acOnBtn.clicked.connect(lambda: self.ui.acOnBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.acOnBtn.clicked.connect(lambda: self.ui.acOffBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

        self.ui.acOffBtn.clicked.connect(lambda: self.ui.acIcon.setPixmap(QPixmap(":/material_design/icons/material_design/subtitles_off.png" )))
        self.ui.acOffBtn.clicked.connect(lambda: self.ui.acOffBtn.setIcon(QIcon(":/material_design/icons/material_design/check_circle.png")))
        self.ui.acOffBtn.clicked.connect(lambda: self.ui.acOnBtn.setIcon(QIcon(":/material_design/icons/material_design/radio_button_unchecked.png")))

    # Create search tooltip
    def createSearchTipOverlay(self):
        """Create a search tip overlay under the search input"""
        self.searchTooltip = QCustomTipOverlay(
            title="Search results.",
            description="Searching...",
            icon=self.main.theme.PATH_RESOURCES + "feather/search.png",  # icon path from theme resources
            isClosable=True,
            target=self.ui.searchCont,  # put tip overlay under search input
            parent=self.main,
            deleteOnClose=True,
            duration=-1,  # set duration to -1 to prevent auto-close
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES + "material_design/close.png",
            toolFlag=True
        )

        # Create loader
        loader = QCustom3CirclesLoader(
            parent=self.searchTooltip,
            color=QColor(self.main.theme.COLOR_ACCENT_1),  # color from theme
            penWidth=20,
            animationDuration=400
        )

        # add loader to the tip overlay
        self.searchTooltip.addWidget(loader)


    # show tip overlay
    def showSearchResults(self):
        # only show search container if search phrase is not empty
        searchPhrase = self.ui.searchInp.text()
        # if phrase is empty
        if not searchPhrase:
            return

        try:
            self.searchTooltip.show()
        except:  # tooltip deleted
            # re-init
            self.createSearchTipOverlay()
            self.searchTooltip.show()
        
        # update search descriptions
        self.searchTooltip.setDescription("Showing search results for: " + searchPhrase)

    # initialize app theme
    def initializeAppTheme(self):
        """Initialize the application theme from settings"""
        settings = QSettings()
        current_theme = settings.value("THEME")
        # print("Current theme is: ", current_theme)

        # Add theme to the theme list
        self.populateThemeList(current_theme)

        # Connect theme change signal to change app theme
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    def populateThemeList(self, current_theme):
        """Populate the list from available app themes"""
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # check default theme/current theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)  # select theme

    
    # change app theme
    def changeAppTheme(self):
        """Change app theme based on user selection"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            # apply new theme
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    # apply custom font
    def loadProductSansFont(self):
        """Load and apply product sans font"""
        font_id = QFontDatabase.addApplicationFont(":/fonts/google-sans-cufonts/ProductSans-Regular.ttf")
        if font_id == -1:
            print("Failed to load Product Sans font")
            return

        # Apply font
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")

        # apply to main window
        self.main.setFont(product_sans)

class BarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        setA = QBarSet("A")
        setB = QBarSet("B")
        setC = QBarSet("C")
        setD = QBarSet("D")

        setA.append(10)
        setB.append(15)
        setC.append(7)
        setD.append(12)

        series = QBarSeries()
        series.append(setA)
        series.append(setB)
        series.append(setC)
        series.append(setD)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Biểu đồ cột")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)


class CustomChartView(QChartView):
    """Lớp kế thừa QChartView để xử lý sự kiện di chuột và hiển thị tooltip di động"""
    
    def __init__(self, chart, data_points, parent=None):
        super().__init__(chart, parent)
        self.data_points = data_points
        self.tooltip = None
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if not self.chart():
            return  # Tránh lỗi nếu chart chưa được thiết lập

        pos = event.pos()
        chart_pos = self.mapToScene(pos)
        chart_value = self.chart().mapToValue(QPointF(chart_pos.x(), chart_pos.y()))

        if chart_value.isNull():
            return  # Đảm bảo giá trị hợp lệ trước khi sử dụng

        # Tìm điểm gần nhất trên đường biểu đồ
        if self.data_points:
            closest_point_x = min(self.data_points, key=lambda p: abs(p.x() - chart_value.x()))
            closest_point_y = min(self.data_points, key=lambda p: abs(p.y() - chart_value.y()))
            distance_x = abs(closest_point_x.x() - chart_value.x())
            distance_y = abs(closest_point_y.y() - chart_value.y())

            if distance_x < 1 and distance_y < 1:  # Giới hạn khoảng cách hiển thị tooltip
                self.show_tooltip(closest_point_x, pos)
                #self.show_tooltip(closest_point_y, pos)
            else:
                if self.tooltip:
                    self.scene().removeItem(self.tooltip)
                    self.tooltip = None  # Giải phóng bộ nhớ

    def show_tooltip(self, point, cursor_pos):
        """Hiển thị tooltip tại vị trí con trỏ chuột"""
        if self.tooltip:
            self.scene().removeItem(self.tooltip)  # Xóa tooltip cũ nếu có

        self.tooltip = QGraphicsSimpleTextItem(f"({point.x():.0f}h, {point.y():.1f})")
        self.tooltip.setBrush(Qt.black)

        # Đặt vị trí tooltip theo con trỏ chuột
        # Lấy vị trí con trỏ chuột trong hệ tọa độ scene
        scene_pos = self.mapToScene(cursor_pos)
        # Đặt tooltip cao hơn con trỏ chuột một chút
        offset = QPointF(-20, -20)  # Dịch lên trên 20 pixel
        self.tooltip.setPos(scene_pos + offset)

        self.scene().addItem(self.tooltip)  # Thêm tooltip vào scene

class TemperatureChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Lấy dữ liệu nhiệt độ từ OpenWeather
        temperatures = self.get_temperature_data()

        temperatures_more = []
        for i in range(len(temperatures) - 1):
            temperatures_more.append(temperatures[i])  # Thêm giá trị hiện tại
            avg = (temperatures[i] + temperatures[i + 1]) / 2  # Tính trung bình cộng
            temperatures_more.append(avg)  # Thêm giá trị trung bình
        temperatures_more.append(temperatures[-1])  # Thêm phần tử cuối cùng

        # Tạo danh sách thời gian từ API
        base_hours = [i * 3 for i in range(len(temperatures))]  # Mốc 3 giờ từ API (0h, 3h, 6h,...)
        hours_more = []
        for i in range(len(base_hours) - 1):
            hours_more.append(base_hours[i])  # Giữ nguyên giờ từ API
            avg_hour = (base_hours[i] + base_hours[i + 1]) / 2  # Thêm giờ trung bình giữa hai mốc
            hours_more.append(avg_hour)
        hours_more.append(base_hours[-1])  # Thêm mốc cuối cùng

        # Tạo Line Series (đường biểu đồ)
        series = QLineSeries()
        data_points = []
        for hour, temp in zip(hours_more, temperatures_more):
            point = QPointF(hour, temp)
            series.append(hour, temp)
            data_points.append(point)

        # Thiết lập màu và độ dày đường vẽ
        pen = QPen(QColor("#CD6889"))
        pen.setWidth(4)
        series.setPen(pen)

        # Tạo biểu đồ
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Temperature Forecast for Today in 24 hours")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Cấu hình trục X (giờ)
        axisX = QValueAxis()
        axisX.setRange(0, 23)
        axisX.setTickCount(9)
        axisX.setLabelFormat("%d")
        axisX.setTitleText("Time (hour)")
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Cấu hình trục Y (nhiệt độ)
        axisY = QValueAxis()
        axisY.setRange(min(temperatures) - 1, max(temperatures) + 1)
        axisY.setTickCount(5)
        axisY.setLabelFormat("%d")
        axisY.setTitleText("Temp (Celsius)")
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        # Tạo giao diện biểu đồ có hỗ trợ tooltip
        chartView = CustomChartView(chart, data_points)
        chartView.setRenderHint(QPainter.Antialiasing)

        # Tạo giao diện biểu đồ
        #chartView = QChartView(chart)
        #chartView.setRenderHint(QPainter.Antialiasing)

        # Thêm vào layout
        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)

    def get_temperature_data(self):
        """Lấy dữ liệu nhiệt độ 24 giờ từ OpenWeather API"""
        API_KEY = "0c03dbf427110d6965566014b8ea57f1"  
        CITY_CODE = "1566083"  
        URL = f"http://api.openweathermap.org/data/2.5/forecast?id={CITY_CODE}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(URL)
            data = response.json()

            # Lấy 24 giá trị nhiệt độ tiếp theo (cập nhật mỗi 3 giờ)
            temperatures = [entry['main']['temp'] for entry in data['list'][:8]]

            return temperatures

        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return [random.uniform(30, 32) for _ in range(24)]  # Trả về giá trị giả lập nếu lỗi

class HumidityChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Lấy dữ liệu độ ẩm từ OpenWeather
        humidity_levels = self.get_humidity_data()

        humidity_more = []
        for i in range(len(humidity_levels) - 1):
            humidity_more.append(humidity_levels[i])  # Thêm giá trị hiện tại
            avg = (humidity_levels[i] + humidity_levels[i + 1]) / 2  # Tính trung bình cộng
            humidity_more.append(avg)  # Thêm giá trị trung bình
        humidity_more.append(humidity_levels[-1])  # Thêm phần tử cuối cùng

        # Tạo danh sách thời gian từ API
        base_hours = [i * 3 for i in range(len(humidity_more))]  # Mốc 3 giờ từ API (0h, 3h, 6h,...)
        hours_more = []
        for i in range(len(base_hours) - 1):
            hours_more.append(base_hours[i])  # Giữ nguyên giờ từ API
            avg_hour = (base_hours[i] + base_hours[i + 1]) / 2  # Thêm giờ trung bình giữa hai mốc
            hours_more.append(avg_hour)
        hours_more.append(base_hours[-1])  # Thêm mốc cuối cùng

        # Tạo Line Series (đường biểu đồ)
        series = QLineSeries()
        data_points = []
        for hour, hum in zip(hours_more,  humidity_more):
            point = QPointF(hour, hum)
            series.append(hour, hum)
            data_points.append(point)

        # Thiết lập màu và độ dày đường vẽ
        pen = QPen(QColor("#4CAF50"))  
        pen.setWidth(4)
        series.setPen(pen)

        # Tạo biểu đồ
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Humidity Forecast for Today in 24 Hours")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Cấu hình trục X (giờ)
        axisX = QValueAxis()
        axisX.setRange(0, 23)
        axisX.setTickCount(9)
        axisX.setLabelFormat("%d")
        axisX.setTitleText("Time (hour)")
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Cấu hình trục Y 
        min_humidity = min(humidity_levels) - 5
        max_humidity = max(humidity_levels) + 5
        axisY = QValueAxis()
        axisY.setRange(min_humidity, max_humidity)
        axisY.setTickCount(5)
        axisY.setLabelFormat("%d%%")
        axisY.setTitleText("Heat Index (Celius)")
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        # Tạo giao diện biểu đồ có hỗ trợ tooltip
        chartView = CustomChartView(chart, data_points)
        chartView.setRenderHint(QPainter.Antialiasing)

        # Tạo giao diện biểu đồ
        #chartView = QChartView(chart)
        #chartView.setRenderHint(QPainter.Antialiasing)

        # Thêm vào layout
        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)

    def get_humidity_data(self):
        """Lấy dữ liệu độ ẩm 24 giờ từ OpenWeather API"""
        API_KEY = "0c03dbf427110d6965566014b8ea57f1"  # Thay bằng API Key của bạn
        CITY_CODE = "1566083"  # Thay bằng thành phố bạn muốn
        URL = f"http://api.openweathermap.org/data/2.5/forecast?id={CITY_CODE}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(URL)
            data = response.json()

            # Lấy độ ẩm và thời gian
            humidity_levels = [entry["main"]["humidity"] for entry in data['list'][:8]]

            return humidity_levels


        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return [random.uniform(20, 85) for _ in range(24)]  # Trả về giá trị giả lập nếu lỗi
        

class HeatIndexChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Lấy dữ liệu độ ẩm từ OpenWeather
        heatIndex = self.get_heat_index_data()

        heatIndex_more = []
        for i in range(len(heatIndex) - 1):
            heatIndex_more.append(heatIndex[i])  # Thêm giá trị hiện tại
            avg = (heatIndex[i] + heatIndex[i + 1]) / 2  # Tính trung bình cộng
            heatIndex_more.append(avg)  # Thêm giá trị trung bình
        heatIndex.append(heatIndex[-1])  # Thêm phần tử cuối cùng

        # Tạo danh sách thời gian từ API
        base_hours = [i * 3 for i in range(len(heatIndex_more))]  # Mốc 3 giờ từ API (0h, 3h, 6h,...)
        hours_more = []
        for i in range(len(base_hours) - 1):
            hours_more.append(base_hours[i])  # Giữ nguyên giờ từ API
            avg_hour = (base_hours[i] + base_hours[i + 1]) / 2  # Thêm giờ trung bình giữa hai mốc
            hours_more.append(avg_hour)
        hours_more.append(base_hours[-1])  # Thêm mốc cuối cùng

        # Tạo Line Series (đường biểu đồ)
        series = QLineSeries()
        data_points = []
        for hour, hum in zip(hours_more,  heatIndex_more):
            point = QPointF(hour, hum)
            series.append(hour, hum)
            data_points.append(point)

        # Thiết lập màu và độ dày đường vẽ
        pen = QPen(QColor("#AC95DF"))  
        pen.setWidth(4)
        series.setPen(pen)

        # Tạo biểu đồ
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Heat Index Forecast for Today in 24 Hours")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Cấu hình trục X (giờ)
        axisX = QValueAxis()
        axisX.setRange(0, 23)
        axisX.setTickCount(9)
        axisX.setLabelFormat("%d")
        axisX.setTitleText("Time (hour)")
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Cấu hình trục Y  
        min_humidity = min(heatIndex_more) - 1
        max_humidity = max(heatIndex_more) + 1
        axisY = QValueAxis()
        axisY.setRange(min_humidity, max_humidity)
        axisY.setTickCount(5)
        axisY.setLabelFormat("%d")
        axisY.setTitleText("Heat Index (Celius)")
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        # Tạo giao diện biểu đồ có hỗ trợ tooltip
        chartView = CustomChartView(chart, data_points)
        chartView.setRenderHint(QPainter.Antialiasing)

        # Tạo giao diện biểu đồ
        #chartView = QChartView(chart)
        #chartView.setRenderHint(QPainter.Antialiasing)

        # Thêm vào layout
        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)

    def get_heat_index_data(self):
        """Lấy dữ liệu độ ẩm 24 giờ từ OpenWeather API"""
        API_KEY = "0c03dbf427110d6965566014b8ea57f1"  # Thay bằng API Key của bạn
        CITY_CODE = "1566083"  # Thay bằng thành phố bạn muốn
        URL = f"http://api.openweathermap.org/data/2.5/forecast?id={CITY_CODE}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(URL)
            data = response.json()

            # Lấy độ ẩm và thời gian
            humd = [entry["main"]["humidity"] for entry in data['list'][:8]]
            temp = [entry["main"]["temp"] for entry in data['list'][:8]]
            T = np.array(temp)
            R = np.array(humd)

            c1 = -42.379
            c2 = 2.04901523
            c3 = 10.14333127
            c4 = 0.22475541
            c5 = 6.83783 * 10^(-3)
            c6 = 5.481717 * 10^(-2)
            c7 = 1.22874 * 10^(-3)
            c8 = 8.5282 * 10^(-4)
            c9 = 1.99 * 10^(-6)

            heat_index = c1 + np.multiply(T, c2) + np.multiply(R, c3) + np.multiply(T, R, c4) + np.multiply(T, T, c5) + np.multiply(R, R, c6) + np.multiply(T, T, R, c7) + np.multiply(T, R, R, c8) + np.multiply(T, T, R, R, c9)
            return heat_index

        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return [random.uniform(20, 36) for _ in range(24)]  # Trả về giá trị giả lập nếu lỗi