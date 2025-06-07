from PySide6.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItemGroup, QGraphicsPolygonItem, QGraphicsSimpleTextItem, QGraphicsTextItem
from PySide6.QtGui import QPen, QColor, QPolygonF, QFont
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

def resolve_axis(val, ports):
    if isinstance(val, (int, float)):
        return val
    if isinstance(val, str):
        parts = val.split(":")
        if len(parts) == 3:
            key = f"{parts[0]}:{parts[1]}"
            axis = parts[2]
            if key in ports:
                x, y = ports[key]
                return x if axis == "x" else y
    raise ValueError(f"Cannot resolve axis: {val}")

def resolve_point(pt, ports):
    if isinstance(pt, (list, tuple)) and len(pt) == 2:
        x = resolve_axis(pt[0], ports)
        y = resolve_axis(pt[1], ports)
        return QPointF(x, y)
    elif isinstance(pt, str):
        # Full port reference, e.g. "bus1:u1"
        parts = pt.split(":")
        if len(parts) == 2:
            key = f"{parts[0]}:{parts[1]}"
            if key in ports:
                x, y = ports[key]
                return QPointF(x, y)
    raise ValueError(f"Cannot resolve point: {pt}")

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
    # from_port = data.get("from")
    # to_port = data.get("to")
    # mid_points = data.get("point", [])  # list of [x, y]
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    cubicle1 = data.get("cubicle1", [])
    cubicle2 = data.get("cubicle2", [])

    # if from_port not in ports or to_port not in ports:
    #     print(f"Missing ports: {from_port}, {to_port}")
    #     return None

    # Build full list of points
    points = []
    for pt in data.get("point", []):
        if isinstance(pt, str) and (pt.endswith(":x") or pt.endswith(":y")):
            # For axis-specific, collect as float
            val = resolve_point(pt, ports)
            points.append(val)
        else:
            points.append(resolve_point(pt, ports))

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
        view = scene.views()[0] if scene.views() else None
        bg_color = view.backgroundBrush().color()
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

def draw_load_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    if obj_type != "load":
        raise ValueError("Only 'load' objects supported.")

    obj_id = obj.get("id")
    data = obj.get("data", {})

    from_port = data.get("from")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    cubicle = data.get("cubicle", [])
    tri_base = data.get("tri_base", 24)
    tri_height = data.get("tri_height", 30)

    if from_port not in ports:
        print(f"Missing port: {from_port}")
        return None

    # Build full list of points
    points = [QPointF(*ports[from_port])]
    points += [resolve_point(pt, ports) for pt in points_data]

    pen = QPen(QColor(color))
    pen.setWidthF(2 * linescale)

    # Draw the line as multiple segments (like line)
    for i in range(len(points) - 1):
        line = QGraphicsLineItem(points[i].x(), points[i].y(), points[i+1].x(), points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)

    # Draw cubicle (only one, at the start)
    if cubicle and len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        draw_cubicle(scene, cubicle[0], ports, points[0], angle_start - 90)

    # Draw triangle at the end
    if len(points) >= 2:
        p1 = points[-2]
        p2 = points[-1]
        # Direction vector
        dx = p2.x() - p1.x()
        dy = p2.y() - p1.y()
        length = (dx**2 + dy**2) ** 0.5
        if length == 0:
            return
        dx /= length
        dy /= length

        

        # Perpendicular vector (for base)
        perp_dx = -dy
        perp_dy = dx

        # Base center is p2
        base_cx = p2.x()
        base_cy = p2.y()

        # Tip point (in direction of line)
        tip_x = base_cx + dx * tri_height
        tip_y = base_cy + dy * tri_height

        # Base endpoints (perpendicular to line, centered at p2)
        pt2 = QPointF(base_cx + perp_dx * tri_base / 2, base_cy + perp_dy * tri_base / 2)
        pt3 = QPointF(base_cx - perp_dx * tri_base / 2, base_cy - perp_dy * tri_base / 2)
        pt1 = QPointF(tip_x, tip_y)  # tip

        triangle = QGraphicsPolygonItem(QPolygonF([pt1, pt2, pt3]))
        triangle.setBrush(QColor(color))
        triangle.setPen(QPen(QColor(color), 1.5))
        scene.addItem(triangle)

def draw_generator_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    if obj_type not in ("gen", "generator"):
        raise ValueError("Only 'gen' or 'generator' objects supported.")

    obj_id = obj.get("id")
    data = obj.get("data", {})

    from_port = data.get("from")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    cubicle = data.get("cubicle", [])
    gen_radius = data.get("gen_radius", 16) * linescale

    if from_port not in ports:
        print(f"Missing port: {from_port}")
        return None

    # Build full list of points
    points = [QPointF(*ports[from_port])]
    points += [resolve_point(pt, ports) for pt in points_data]

    pen = QPen(QColor(color))
    pen.setWidthF(2 * linescale)

    # Draw the line as multiple segments (like line)
    for i in range(len(points) - 1):
        line = QGraphicsLineItem(points[i].x(), points[i].y(), points[i+1].x(), points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)

    # Draw cubicle (only one, at the start)
    if cubicle and len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        draw_cubicle(scene, cubicle[0], ports, points[0], angle_start - 90)

    # Draw generator symbol (circle with 'G')
    if len(points) >= 2:
        p1 = points[-2]
        p2 = points[-1]
        dx = p2.x() - p1.x()
        dy = p2.y() - p1.y()
        length = (dx**2 + dy**2) ** 0.5
        if length == 0:
            return
        dx /= length
        dy /= length

        # The end of the line should be on the circumference
        center_x = p2.x() + dx * gen_radius
        center_y = p2.y() + dy * gen_radius

        # Draw circle (no fill)
        ellipse = QGraphicsEllipseItem(center_x - gen_radius, center_y - gen_radius, 2 * gen_radius, 2 * gen_radius)
        ellipse.setPen(QPen(QColor(color), 2 * linescale))
        ellipse.setBrush(Qt.NoBrush)
        scene.addItem(ellipse)

        # Draw 'G' in the center, rotated
        text = QGraphicsTextItem("G")
        font = QFont("Arial", int(gen_radius * 0.9))
        text.setFont(font)
        text.setDefaultTextColor(QColor(color))

        # Center the text
        br = text.boundingRect()
        text.setPos(center_x - br.width() / 2, center_y - br.height() / 2)

        # Calculate the angle of the last line segment (in degrees)
        angle = math.degrees(math.atan2(dy, dx))
        # The baseline should be perpendicular, so add 90 degrees
        text.setRotation(angle - 90)

        scene.addItem(text)

def draw_transformer_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    if obj_type not in ("trafo", "transformer"):
        raise ValueError("Only 'trafo' or 'transformer' objects supported.")

    data = obj.get("data", {})
    from_port = data.get("from")
    to_port = data.get("to")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)

    if from_port not in ports or to_port not in ports:
        print(f"Missing port: {from_port} or {to_port}")
        return None

    # Split points into from-side and to-side using "split" marker
    if "split" in points_data:
        split_idx = points_data.index("split")
        from_points = [QPointF(*ports[from_port])] + [resolve_point(pt, ports) for pt in points_data[:split_idx]]
        to_points = [resolve_point(pt, ports) for pt in points_data[split_idx+1:]] + [QPointF(*ports[to_port])]
    else:
        # If no split, just connect directly
        from_points = [QPointF(*ports[from_port])]
        to_points = [QPointF(*ports[to_port])]

    # Find pf and pt (end of from-side, start of to-side)
    pf = from_points[-1]
    pt = to_points[0]

    # Vector from pf to pt
    dx = pt.x() - pf.x()
    dy = pt.y() - pf.y()
    length = (dx**2 + dy**2) ** 0.5
    if length == 0:
        return
    dx /= length
    dy /= length

    # Calculate trafo_radius dynamically
    trafo_radius = length / 3.2

    # Centers of circles
    margin = 1 * trafo_radius
    c1x = pf.x() + dx * margin
    c1y = pf.y() + dy * margin
    c2x = pt.x() - dx * margin
    c2y = pt.y() - dy * margin

    # Draw from-side lines (end at circumference of first circle)
    for i in range(len(from_points) - 1):
        line = QGraphicsLineItem(from_points[i].x(), from_points[i].y(), from_points[i+1].x(), from_points[i+1].y())
        line.setPen(QPen(QColor(color), 2 * linescale))
        scene.addItem(line)
    # Draw line from pf to circumference of first circle
    # pf_circ_x = c1x - dx * trafo_radius
    # pf_circ_y = c1y - dy * trafo_radius
    # line = QGraphicsLineItem(pf.x(), pf.y(), pf_circ_x, pf_circ_y)
    # line.setPen(QPen(QColor(color), 2 * linescale))
    # scene.addItem(line)

    for i in range(len(to_points) - 1):
        line = QGraphicsLineItem(to_points[i].x(), to_points[i].y(), to_points[i+1].x(), to_points[i+1].y())
        line.setPen(QPen(QColor(color), 2 * linescale))
        scene.addItem(line)

    # Draw cubicle1 at the start of from-side
    if "cubicle1" in data and data["cubicle1"] and len(from_points) >= 2:
        angle_start = angle_between(from_points[0], from_points[1])
        # angle_start = math.degrees(math.atan2(from_points[0].y() - from_points[1].y(), from_points[0].x() - from_points[1].x()))
        for cub in data["cubicle1"]:
            draw_cubicle(scene, cub, ports, from_points[0], angle_start - 90)

    # Draw cubicle2 at the end of to-side
    if "cubicle2" in data and data["cubicle2"] and len(to_points) >= 2:
        angle_end = angle_between(to_points[-1], to_points[-2])
        # angle_end = math.degrees(math.atan2(to_points[-1].y() - to_points[-2].y(), to_points[-1].x() - to_points[-2].x()))
        for cub in data["cubicle2"]:
            draw_cubicle(scene, cub, ports, to_points[-1], angle_end - 90)

    # Draw transformer symbol (two intersecting circles)
    ellipse1 = QGraphicsEllipseItem(c1x - trafo_radius, c1y - trafo_radius, 2 * trafo_radius, 2 * trafo_radius)
    ellipse1.setPen(QPen(QColor(color), 2 * linescale))
    ellipse1.setBrush(Qt.NoBrush)
    scene.addItem(ellipse1)

    ellipse2 = QGraphicsEllipseItem(c2x - trafo_radius, c2y - trafo_radius, 2 * trafo_radius, 2 * trafo_radius)
    ellipse2.setPen(QPen(QColor(color), 2 * linescale))
    ellipse2.setBrush(Qt.NoBrush)
    scene.addItem(ellipse2)



