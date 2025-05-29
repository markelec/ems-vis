from PySide6.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import QPointF, Qt

def draw_object_from_json(scene: QGraphicsScene, obj: dict):
    """
    Draws a 'bus' from JSON and returns connection points.
    
    Returns:
        line_item: the QGraphicsLineItem
        ports: dict of connection points (e.g., {'bus1:u0': (x, y), ...})
    """
    obj_type = obj.get("type")
    obj_id = obj.get("id")
    data = obj.get("data", {})

    if obj_type != "bus":
        raise ValueError(f"Unsupported type: {obj_type}")

    # Basic properties
    name = data.get("name", obj_id)
    direction = data.get("direction", "horizontal")
    position = data.get("position", [0, 0])
    widthscale = data.get("widthscale", 1.0)
    color = data.get("color", "blue")
    length = data.get("length", 200)

    # Port configuration
    upport = data.get("upport", {"size": 0.2, "number": 3})
    downport = data.get("downport", {"size": 0.2, "number": 3})
    up_size = upport.get("size", 0.2)
    up_count = upport.get("number", 0)
    down_size = downport.get("size", 0.2)
    down_count = downport.get("number", 0)

    x0, y0 = position
    pen = QPen(QColor(color))
    pen.setWidthF(4 * widthscale)

    ports = {}  # To collect connection points

    if direction == "horizontal":
        x1, y1 = x0 + length, y0
        line = QGraphicsLineItem(x0, y0, x1, y1)
        scene.addItem(line)

        up_start = x0 + length * up_size
        up_spacing = (length * (1 - 2 * up_size)) / max(1, up_count - 1)
        for i in range(up_count):
            xi = up_start + i * up_spacing
            ports[f"{obj_id}:u{i}"] = (xi, y0 - 1)  # above the bus

        down_start = x0 + length * down_size
        down_spacing = (length * (1 - 2 * down_size)) / max(1, down_count - 1)
        for i in range(down_count):
            xi = down_start + i * down_spacing
            ports[f"{obj_id}:d{i}"] = (xi, y0 + 1)  # below the bus

    elif direction == "vertical":
        x1, y1 = x0, y0 + length
        line = QGraphicsLineItem(x0, y0, x1, y1)
        scene.addItem(line)

        up_start = y0 + length * up_size
        up_spacing = (length * (1 - 2 * up_size)) / max(1, up_count - 1)
        for i in range(up_count):
            yi = up_start + i * up_spacing
            ports[f"{obj_id}:u{i}"] = (x0 - 1, yi)  # left of bus

        down_start = y0 + length * down_size
        down_spacing = (length * (1 - 2 * down_size)) / max(1, down_count - 1)
        for i in range(down_count):
            yi = down_start + i * down_spacing
            ports[f"{obj_id}:d{i}"] = (x0 + 1, yi)  # right of bus

    elif direction == "point":
        # Diameter same as default bus thickness
        diameter = 4 * widthscale
        radius = diameter / 2

        # Draw as a circle centered at (x0, y0)
        ellipse = QGraphicsEllipseItem(x0 - radius, y0 - radius, diameter, diameter)
        ellipse.setPen(pen)
        ellipse.setBrush(QColor(color))  # Fill the circle for visibility
        scene.addItem(ellipse)

        # All ports connect to the same center point
        for i in range(up_count):
            ports[f"{obj_id}:u{i}"] = (x0, y0)
        for i in range(down_count):
            ports[f"{obj_id}:d{i}"] = (x0, y0)

        line = ellipse  # for consistency with return

    line.setPen(pen)
    return line, ports

