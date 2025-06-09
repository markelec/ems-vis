import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QToolBar, QMenu, QMenuBar, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem
)
from PySide6.QtGui import QIcon, QAction, QFont, QColor, QPen, QBrush, QPainter
from PySide6.QtCore import Qt, QSize, QRect, QRectF

from database_connect_dialog import DatabaseConnectDialog  # Assuming this is the auto-generated class from your .ui file

from PySide6.QtGui import QWheelEvent, QMouseEvent
from drawutils import draw_object_from_json, draw_line_from_json, draw_load_from_json, draw_generator_from_json, draw_transformer_from_json, draw_inverter_from_json, draw_svg_element_from_json, draw_two_terminal_svg_element_from_json
from diagram_data import bus1_json, bus2_json, line_json, line_json2, load_json, gen_json, trafo_json, inv_json, bess_json   # Assuming this is your JSON data for the bus diagram

class ZoomPanGraphicsView(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._zoom = 1.0
        self._dragging = False
        self._last_pos = None

        self.setRenderHints(self.renderHints() | QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.NoDrag)  # We'll handle drag ourselves
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setBackgroundBrush(QColor("#1e1e1e"))

    def wheelEvent(self, event: QWheelEvent):
        zoom_factor = 1.15
        if event.angleDelta().y() > 0:
            zoom = zoom_factor
        else:
            zoom = 1 / zoom_factor
        self._zoom *= zoom
        self.scale(zoom, zoom)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._last_pos = event.pos()
            self.setCursor(Qt.ClosedHandCursor)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._dragging:
            delta = self._last_pos - event.pos()
            self._last_pos = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + delta.y())
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            self.setCursor(Qt.ArrowCursor)
        else:
            super().mouseReleaseEvent(event)
            
    def draw_sld(self):
        bus_pen = QPen(QColor("red"), 8)  # DeepSkyBlue
        line_pen = QPen(QColor("red"), 3)  # Light gray

        # Draw busbar (a thick horizontal line)
        busbar_y = 100
        busbar = QGraphicsLineItem(100, busbar_y, 600, busbar_y)
        busbar.setPen(bus_pen)
        busbar.setZValue(1)
        self.scene().addItem(busbar)
        

        # Draw 3 feeder lines connected to the busbar
        for i in range(3):
            x = 150 + i * 150
            feeder = QGraphicsLineItem(x, busbar_y, x, busbar_y + 100)
            feeder.setPen(line_pen)
            feeder.setZValue(0)
            self.scene().addItem(feeder)

            # Draw load (gray box)
            load = QGraphicsRectItem(QRectF(x - 10, busbar_y + 100, 20, 20))
            load.setBrush(QBrush(QColor("red")))
            load.setPen(QPen(Qt.NoPen))
            load.setZValue(0)
            self.scene().addItem(load)
            
    def resizeEvent(self, event):
        super().resizeEvent(event)
        print("Updated viewport size:", self.viewport().size())
        window.view.fitInView(window.scene.sceneRect(), Qt.KeepAspectRatio)

class SLDCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)

        # Set dark background
        self.setBackgroundBrush(QColor("#1e1e1e"))

        self.draw_sld()

    def draw_sld(self):
        bus_pen = QPen(QColor("red"), 8)  # DeepSkyBlue
        line_pen = QPen(QColor("#CCCCCC"), 3)  # Light gray

        # Draw busbar (a thick horizontal line)
        busbar_y = 100
        busbar = QGraphicsLineItem(100, busbar_y, 600, busbar_y)
        busbar.setPen(bus_pen)
        busbar.setZValue(1)
        self.scene.addItem(busbar)
        

        # Draw 3 feeder lines connected to the busbar
        for i in range(3):
            x = 150 + i * 150
            feeder = QGraphicsLineItem(x, busbar_y, x, busbar_y + 100)
            feeder.setPen(line_pen)
            feeder.setZValue(0)
            self.scene.addItem(feeder)

            # Draw load (gray box)
            load = QGraphicsRectItem(QRectF(x - 10, busbar_y + 100, 20, 20))
            load.setBrush(QBrush(QColor("#888888")))
            load.setPen(QPen(Qt.NoPen))
            load.setZValue(0)
            self.scene.addItem(load)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Microgrid Energy Management System")
        
        # mfont = QFont("Arial", 8)
        # self.setFont(mfont)

        # Central widget
        # self.view = SLDCanvas()
        # self.setCentralWidget(self.canvas)

        # self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 2000, 1000)

        self.view = ZoomPanGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        # self.view.draw_sld()
       

        l1, p1 =  draw_object_from_json(self.view.scene(), bus1_json)
        l2, p2 = draw_object_from_json(self.view.scene(), bus2_json)
        ports = {**p1, **p2}
        draw_line_from_json(self.view.scene(), line_json, ports)
        draw_line_from_json(self.view.scene(), line_json2, ports)
        draw_load_from_json(self.view.scene(), self.view, load_json, ports)
        draw_generator_from_json(self.view.scene(), self.view, gen_json, ports)
        # draw_transformer_from_json(self.view.scene(), self.view, trafo_json, ports)
        draw_inverter_from_json(self.view.scene(), self.view, inv_json, ports)
        draw_svg_element_from_json(self.view.scene(), self.view, bess_json, ports)
        draw_two_terminal_svg_element_from_json(self.view.scene(), self.view, trafo_json, ports)
        # Example item
        # line = QGraphicsLineItem(100, 100, 400, 100)
        # line.setPen(QPen(QColor("blue"), 5))
        # self.scene.addItem(line)

        # Menu bar
        self.create_menu_bar()

        # Toolbar
        self.create_toolbar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setGeometry(QRect(0, 0, 800, 35))  # Set height to 30px
        
        
        # Minimal style sheet to reduce height without ruining native appearance
        # menu_bar.setStyleSheet("""
        #     QMenuBar {
        #         font-size: 8pt; * Reduced font size */
        #         spacing: 0px;
        #         padding: 2px 0px; 
        #         margin-right: 0px;
        #     }
        #     QMenuBar::item {
        #         padding: 2px 0px;  /* top/bottom padding reduced */
        #         margin-right: 0px;
        #     }
        # """)

        db_menu = menu_bar.addMenu("Database")
        conn_action = QAction("Connection", self)
        conn_action.triggered.connect(lambda: DatabaseConnectDialog(self).exec())
        modbus_action = QAction("Modbus", self)
        exit_action = QAction("Exit", self)
        db_menu.addAction(conn_action)
        db_menu.addAction(modbus_action)
        db_menu.addAction(exit_action)
        
        sys_menu = menu_bar.addMenu("System")
        elm_action = QAction("Elements Mapping", self)
        layer_action = QAction("Layer", self)
        sys_menu.addAction(elm_action)
        sys_menu.addAction(layer_action)
        
        op_menu = menu_bar.addMenu("Operation")
        seq_action = QAction("Sequence", self)
        load_action = QAction("Load Forecast", self)
        op_menu.addAction(seq_action)
        op_menu.addAction(load_action)
        
        set_menu = menu_bar.addMenu("Setting")
        col_action = QAction("Color", self)
        font_action = QAction("Font", self)
        set_menu.addAction(col_action)
        set_menu.addAction(font_action)
       

        help_menu = menu_bar.addMenu("Help")
        doc_action = QAction("Document", self)
        about_action = QAction("About", self)
        help_menu.addAction(doc_action)
        help_menu.addAction(about_action)


    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        new_icon = QAction(QIcon(), "New", self)
        new_icon.triggered.connect(lambda: self.editor.setText(""))
        toolbar.addAction(new_icon)

        exit_icon = QAction(QIcon(), "Exit", self)
        exit_icon.triggered.connect(self.close)
        toolbar.addAction(exit_icon)

    def show_about(self):
        self.editor.setText("This is a sample PySide6 app with menu and toolbar.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")  # Optional: Set a style for the app
    app.setApplicationName("Microgrid Energy Management System")
    window = MyApp()
    window.showMaximized()
    # window.view.fitInView(window.scene.sceneRect(), Qt.KeepAspectRatio)
    # size = window.view.viewport().size()
    # print(f"Viewport size: {size.width()}x{size.height()}")
    sys.exit(app.exec())
