from PySide6.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItemGroup
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import QPointF, Qt

import math

def angle_between(p1, p2):
    dx = p2.x() - p1.x()
    dy = p2.y() - p1.y()
    return math.degrees(math.atan2(dy, dx))  # angle in degrees

def rotated_offset(offset, angle_deg):
    angle_rad = math.radians(angle_deg)
    dx, dy = offset
    x = dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
    y = dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
    return x, y


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
    up_margin = upport.get("margin", 0.2)
    up_count = upport.get("number", 0)
    down_margin = downport.get("margin", 0.2)
    down_count = downport.get("number", 0)

    x0, y0 = position
    pen = QPen(QColor(color))
    pen.setWidthF(4 * widthscale)

    ports = {}  # To collect connection points

    if direction == "horizontal":
        x1, y1 = x0 + length, y0
        line = QGraphicsLineItem(x0, y0, x1, y1)
        scene.addItem(line)

        up_start = x0 + length * up_margin
        up_spacing = (length * (1 - 2 * up_margin)) / up_count 
        for i in range(up_count):
            xi = up_start + (i+0.5) * up_spacing
            ports[f"{obj_id}:u{i}"] = (xi, y0)  # above the bus

        down_start = x0 + length * down_margin
        down_spacing = (length * (1 - 2 * down_margin)) / down_count
        for i in range(down_count):
            xi = down_start + (i+0.5) * down_spacing
            ports[f"{obj_id}:d{i}"] = (xi, y0)  # below the bus

    elif direction == "vertical":
        x1, y1 = x0, y0 + length
        line = QGraphicsLineItem(x0, y0, x1, y1)
        scene.addItem(line)

        up_start = y0 + length * up_margin
        up_spacing = (length * (1 - 2 * up_margin)) / up_count
        for i in range(up_count):
            yi = up_start + (i+0.5) * up_spacing
            ports[f"{obj_id}:u{i}"] = (x0, yi)  # left of bus

        down_start = y0 + length * down_margin
        down_spacing = (length * (1 - 2 * down_margin)) / down_count
        for i in range(down_count):
            yi = down_start + (i+0.5) * down_spacing
            ports[f"{obj_id}:d{i}"] = (x0, yi)  # right of bus

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


def draw_line_from_json(scene, obj, ports):
    obj_type = obj.get("type")
    if obj_type != "line":
        raise ValueError("Only 'line' objects supported.")

    obj_id = obj.get("id")
    data = obj.get("data", {})

    name = data.get("name", obj_id)
    from_port = data.get("from")
    to_port = data.get("to")
    mid_points = data.get("point", [])  # list of [x, y]
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    cubicle1 = data.get("cubicle1", [])
    cubicle2 = data.get("cubicle2", [])

    if from_port not in ports or to_port not in ports:
        print(f"Missing ports: {from_port}, {to_port}")
        return None

    # Build full list of points
    points = [QPointF(*ports[from_port])]
    points += [QPointF(*pt) for pt in mid_points]
    points.append(QPointF(*ports[to_port]))

    pen = QPen(QColor(color))
    pen.setWidthF(2 * linescale)

    # Draw the line as multiple segments
    for i in range(len(points) - 1):
        line = QGraphicsLineItem(points[i].x(), points[i].y(), points[i+1].x(), points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)

    # Draw cubicles
    if len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        angle_end = angle_between(points[-1], points[-2])

        for cub in cubicle1:
            angle = angle_start - 90
            draw_cubicle(scene, cub, ports, points[0], angle)

        for cub in cubicle2:
            angle = angle_end - 90
            draw_cubicle(scene, cub, ports, points[-1], angle)


def draw_cubicle(scene, cubicle_obj, ports, base_point, angle):
    data = cubicle_obj.get("data", {})
    offset = data.get("offset", [0, 0])
    color = data.get("color", "red")
    scale = data.get("scale", 1.0)

    dx, dy = rotated_offset(offset, angle)
    cx = base_point.x() + dx
    cy = base_point.y() + dy

    c_type = cubicle_obj.get("type")

    if c_type == "breaker":
        size = 6 * scale
        item = QGraphicsRectItem(-size/2, -size/2, size, size)
        item.setBrush(QColor(color))
        item.setPen(QPen(Qt.NoPen))
        item.setPos(cx, cy)
        item.setRotation(angle)
        scene.addItem(item)
    elif c_type == "switch":
        size = 6 * scale
        # Transparent square
        rect = QGraphicsRectItem(-size / 2, -size / 2, size, size)
        # rect.setBrush(Qt.transparent)
        bg_color = scene.backgroundBrush().color()
        rect.setBrush(QColor(bg_color))
        rect.setPen(Qt.NoPen)
        # Diagonal line from top center to bottom right
        line = QGraphicsLineItem(0, -size / 2, size / 2, size / 2)
        line.setPen(QPen(QColor(color), 1.5))

        # Group them together
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        group.addToGroup(line)

        group.setPos(cx, cy)
        group.setRotation(angle)
        scene.addItem(group)
    else:
        return

    


