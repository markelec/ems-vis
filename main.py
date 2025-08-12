import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QToolBar, QMenu, QMenuBar, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QTabWidget, QWidget
)
from PySide6.QtGui import QIcon, QAction, QFont, QColor, QPen, QBrush, QPainter
from PySide6.QtCore import Qt, QSize, QRect, QRectF

from database_connect_dialog import DatabaseConnectDialog  # Assuming this is the auto-generated class from your .ui file

from PySide6.QtGui import QWheelEvent, QMouseEvent
from drawutils import draw_diagram_from_dict, draw_diagram_from_file
from diagram_data import bus1_json, bus2_json, line_json, line_json2, load_json, gen_json, trafo_json, inv_json, bess_json, text_json1, text_json2  # Assuming this is your JSON data for the bus diagram

class ZoomPanGraphicsView(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._zoom = 1.0
        self._min_zoom = 0.1  # Minimum zoom level (10%)
        self._max_zoom = 2.0  # Maximum zoom level (200%)
        self._dragging = False
        self._last_pos = None

        self.setRenderHints(self.renderHints() | QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.NoDrag)  # We'll handle drag ourselves
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setBackgroundBrush(QColor("#1e1e1e"))
        
        # Enable scrollbars when needed
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def wheelEvent(self, event: QWheelEvent):
        zoom_factor = 1.15
        if event.angleDelta().y() > 0:
            zoom = zoom_factor
        else:
            zoom = 1 / zoom_factor
        
        # Calculate new zoom level
        new_zoom = self._zoom * zoom
        
        # Apply zoom limits
        if new_zoom < self._min_zoom:
            zoom = self._min_zoom / self._zoom
            new_zoom = self._min_zoom
        elif new_zoom > self._max_zoom:
            zoom = self._max_zoom / self._zoom
            new_zoom = self._max_zoom
        
        # Only apply zoom if it's within limits
        if zoom != 1.0:
            self._zoom = new_zoom
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
    
    def set_zoom_limits(self, min_zoom=0.1, max_zoom=2.0):
        """Set custom zoom limits"""
        self._min_zoom = min_zoom
        self._max_zoom = max_zoom
    
    def get_zoom_level(self):
        """Get current zoom level as percentage"""
        return self._zoom * 100
    
    def zoom_to_fit(self):
        """Zoom to fit all content in view"""
        self.fitInView(self.scene().sceneRect(), Qt.KeepAspectRatio)
        # Update internal zoom tracking
        transform = self.transform()
        self._zoom = transform.m11()  # Get the scale factor
    
    def reset_zoom(self):
        """Reset zoom to 100%"""
        self.resetTransform()
        self._zoom = 1.0
            
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
        # Remove the automatic fit in view on resize - let user control zoom
        # window.view.fitInView(window.scene.sceneRect(), Qt.KeepAspectRatio)

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
        
        # Create tab widget as central widget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Create 4 tabs
        self.create_tabs()

        # Menu bar
        self.create_menu_bar()

        # Toolbar
        self.create_toolbar()

    def create_tabs(self):
        # Tab 1: Single Line Diagram (original graphics view)
        self.tab1 = QWidget()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 2000, 1000)
        
        self.view = ZoomPanGraphicsView(self.scene)
        
        # Add the view to tab1
        from PySide6.QtWidgets import QVBoxLayout
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(self.view)
        tab1_layout.setContentsMargins(0, 0, 0, 0)
        self.tab1.setLayout(tab1_layout)
        
        # Draw complete diagram from file
        drawn_items, ports = draw_diagram_from_file(
            self.view.scene(), 
            self.view, 
            "complete_diagram.py"
        )
        
        # Store for later use if needed
        self.drawn_items = drawn_items
        self.ports = ports
        
        # Alternative: Draw from dictionary directly
        # from complete_diagram import diagram_dict
        # drawn_items, ports = draw_diagram_from_dict(self.view.scene(), self.view, diagram_dict)
        
        # Tab 2: Operation
        self.tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_content = QTextEdit()
        tab2_content.setText("Operation Tab Content - Add your operation controls here")
        tab2_layout.addWidget(tab2_content)
        self.tab2.setLayout(tab2_layout)
        
        # Tab 3: Monitoring
        self.tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_content = QTextEdit()
        tab3_content.setText("Monitoring Tab Content - Add your monitoring displays here")
        tab3_layout.addWidget(tab3_content)
        self.tab3.setLayout(tab3_layout)
        
        # Tab 4: Settings
        self.tab4 = QWidget()
        tab4_layout = QVBoxLayout()
        tab4_content = QTextEdit()
        tab4_content.setText("Settings Tab Content - Add your settings controls here")
        tab4_layout.addWidget(tab4_content)
        self.tab4.setLayout(tab4_layout)
        
        # Add tabs to tab widget
        self.tab_widget.addTab(self.tab1, "Single Line Diagram")
        self.tab_widget.addTab(self.tab2, "Operation")
        self.tab_widget.addTab(self.tab3, "Monitoring")
        self.tab_widget.addTab(self.tab4, "Settings")

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
