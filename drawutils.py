from PySide6.QtWidgets import QGraphicsScene, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItemGroup, QGraphicsPolygonItem, QGraphicsSimpleTextItem, QGraphicsTextItem
from PySide6.QtGui import QPen, QColor, QPolygonF, QFont
from PySide6.QtCore import QPointF, Qt, QBuffer
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtGui import QTransform
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QByteArray
import re

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
        # Check for arithmetic operations (+/-)
        if '+' in val or '-' in val:
            # Find the operator position (should be after the axis specifier)
            operator_pos = -1
            operator = None
            
            # Look for + or - after the colon and axis
            for i, char in enumerate(val):
                if char in ['+', '-'] and i > 0:
                    # Make sure it's after a valid axis specifier (x or y)
                    if i > 0 and val[i-1] in ['x', 'y']:
                        operator_pos = i
                        operator = char
                        break
            
            if operator_pos > 0:
                # Split at the operator position
                port_ref = val[:operator_pos].strip()
                offset_str = val[operator_pos+1:].strip()
                
                # Parse the offset value
                try:
                    offset = float(offset_str)
                except ValueError:
                    raise ValueError(f"Invalid offset in expression: {val}")
                
                # Parse port reference (e.g., "bus1:u1:x")
                port_parts = port_ref.split(":")
                if len(port_parts) == 3:
                    key = f"{port_parts[0]}:{port_parts[1]}"
                    axis = port_parts[2]
                    if key in ports:
                        x, y = ports[key]
                        base_value = x if axis == "x" else y
                        
                        # Apply operator
                        if operator == '+':
                            return base_value + offset
                        elif operator == '-':
                            return base_value - offset
                    else:
                        raise ValueError(f"Port not found: {key}")
                else:
                    raise ValueError(f"Invalid port reference in expression: {port_ref}")
            else:
                raise ValueError(f"Invalid arithmetic expression: {val}")
        else:
            # Original logic for simple port reference
            parts = val.split(":")
            if len(parts) == 3:
                key = f"{parts[0]}:{parts[1]}"
                axis = parts[2]
                if key in ports:
                    x, y = ports[key]
                    return x if axis == "x" else y
                else:
                    raise ValueError(f"Port not found: {key}")
            else:
                raise ValueError(f"Invalid port reference format: {val}")
    
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
    upport = data.get("upport", {"margin": 0.2, "number": 3})
    downport = data.get("downport", {"margin": 0.2, "number": 3})
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


def draw_connection_point(scene, point, color="red", size=3):
    """
    Draw a small circle to indicate a connection point on a bus.
    
    Args:
        scene: QGraphicsScene to draw on
        point: QPointF location of the connection point
        color: Color of the connection point
        size: Radius of the connection point
    """
    circle = QGraphicsEllipseItem(point.x() - size, point.y() - size, 2 * size, 2 * size)
    circle.setBrush(QColor(color))
    circle.setPen(QPen(QColor(color)))
    scene.addItem(circle)
    return circle

def draw_line_from_json(scene, obj, ports):
    obj_type = obj.get("type")
    if obj_type != "line":
        raise ValueError("Only 'line' objects supported.")

    obj_id = obj.get("id")
    data = obj.get("data", {})

    name = data.get("name", obj_id)
    from_port = data.get("from")
    to_port = data.get("to")
    mid_points = data.get("point", [])  # list of intermediate points
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    cubicle1 = data.get("cubicle1", [])
    cubicle2 = data.get("cubicle2", [])
    
    # New options for connection points
    show_start_point = data.get("show_start_point", True)
    show_end_point = data.get("show_end_point", True)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 4)

    if from_port not in ports or to_port not in ports:
        print(f"Missing ports: {from_port}, {to_port}")
        return None

    # Build full list of points: start -> intermediate points -> end
    points = [QPointF(*ports[from_port])]
    
    # Add intermediate points
    for pt in mid_points:
        points.append(resolve_point(pt, ports))
    
    # Add end point
    points.append(QPointF(*ports[to_port]))

    pen = QPen(QColor(color))
    pen.setWidthF(2 * linescale)

    # Draw the line as multiple segments
    for i in range(len(points) - 1):
        line = QGraphicsLineItem(points[i].x(), points[i].y(), points[i+1].x(), points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)

    # Draw connection points
    if show_start_point:
        draw_connection_point(scene, points[0], connection_point_color, connection_point_size)
    
    if show_end_point:
        draw_connection_point(scene, points[-1], connection_point_color, connection_point_size)

    # Draw cubicles
    if len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        angle_end = angle_between(points[-1], points[-2])

        for cub in cubicle1:
            angle = angle_start - 90
            draw_cubicle(scene, cub, ports, points[0], angle, 2*linescale)

        for cub in cubicle2:
            angle = angle_end - 90
            draw_cubicle(scene, cub, ports, points[-1], angle, 2*linescale)


def draw_cubicle(scene, cubicle_obj, ports, base_point, angle, linewidth=1):
    data = cubicle_obj.get("data", {})
    offset = data.get("offset", [0, 0])
    color = data.get("color", "red")
    scale = data.get("scale", 1.0)
    cubicle_rotation = data.get("rotation", 0)  # New rotation parameter for cubicle

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
        item.setRotation(angle + cubicle_rotation)  # Apply additional rotation
        scene.addItem(item)
        
    elif c_type == "recloser":
        size = 6 * scale
        # Create rectangle
        rect = QGraphicsRectItem(-size/2, -size/2, size, size)
        rect.setBrush(QColor(color))
        rect.setPen(QPen(Qt.NoPen))
        
        # Create text "R" with white color
        text = QGraphicsSimpleTextItem("R")
        font_size = int(size * 0.7)  # 70% of rectangle height
        font = QFont("Arial", font_size)
        text.setFont(font)
        text.setBrush(QColor("white"))
        
        # Center the text within the rectangle
        text_rect = text.boundingRect()
        text.setPos(-text_rect.width()/2, -text_rect.height()/2)
        
        # Apply text rotation relative to the rectangle
        # If cubicle_rotation is specified, apply it to keep text readable
        if cubicle_rotation != 0:
            # Calculate text rotation to keep it readable
            text_angle = cubicle_rotation
            # Normalize angle to [-180, 180] range
            while text_angle > 180:
                text_angle -= 360
            while text_angle < -180:
                text_angle += 360
            
            # If the text would be upside down, rotate it 180 degrees to keep it readable
            if abs(text_angle) > 90:
                text_angle += 180 if text_angle < 0 else -180
            
            text.setTransformOriginPoint(text_rect.width()/2, text_rect.height()/2)
            text.setRotation(text_angle)
        
        # Group them together
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        group.addToGroup(text)
        
        group.setPos(cx, cy)
        group.setRotation(angle + cubicle_rotation)  # Apply base angle + additional rotation
        scene.addItem(group)
        
    elif c_type == "lbs":
        size = 6 * scale
        # Create rectangle
        rect = QGraphicsRectItem(-size/2, -size/2, size, size)
        rect.setBrush(QColor(color))
        rect.setPen(QPen(Qt.NoPen))
        
        # Create text "SF6" with white color
        text = QGraphicsSimpleTextItem("SF6")
        font_size = int(size * 0.4)  # 40% of rectangle height
        font = QFont("Arial", font_size)
        text.setFont(font)
        text.setBrush(QColor("white"))
        
        # Center the text within the rectangle
        text_rect = text.boundingRect()
        text.setPos(-text_rect.width()/2, -text_rect.height()/2)
        
        # Apply text rotation relative to the rectangle
        # If cubicle_rotation is specified, apply it to keep text readable
        if cubicle_rotation != 0:
            # Calculate text rotation to keep it readable
            text_angle = cubicle_rotation
            # Normalize angle to [-180, 180] range
            while text_angle > 180:
                text_angle -= 360
            while text_angle < -180:
                text_angle += 360
            
            # If the text would be upside down, rotate it 180 degrees to keep it readable
            if abs(text_angle) > 90:
                text_angle += 180 if text_angle < 0 else -180
            
            text.setTransformOriginPoint(text_rect.width()/2, text_rect.height()/2)
            text.setRotation(text_angle)
        
        # Group them together
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        group.addToGroup(text)
        
        group.setPos(cx, cy)
        group.setRotation(angle + cubicle_rotation)  # Apply base angle + additional rotation
        scene.addItem(group)
        
    elif c_type == "switch":
        size = 6 * scale
        direction = data.get("direction", "up_right").lower()  # Default to up_right
        
        # Transparent square
        rect = QGraphicsRectItem(-size, -size / 2, 2*size, size)
        view = scene.views()[0] if scene.views() else None
        bg_color = view.backgroundBrush().color()
        rect.setBrush(QColor(bg_color))
        rect.setPen(Qt.NoPen)
        
        # Define line endpoints based on direction
        # Format: (start_x, start_y, end_x, end_y)
        direction_lines = {
            "up_right": (0, size/2, size, -size/2),      # From center to top-right
            "up_left": (0, size/2, -size, -size/2),      # From center to top-left
            "down_right": (0, -size/2, size, size/2),     # From center to bottom-right
            "down_left": (0, -size/2, -size, size/2)      # From center to bottom-left
        }
        
        if direction in direction_lines:
            x1, y1, x2, y2 = direction_lines[direction]
        else:
            print(f"Warning: Unknown switch direction '{direction}', using 'up_right'")
            x1, y1, x2, y2 = direction_lines["up_right"]
        
        # Create the diagonal line
        line = QGraphicsLineItem(x1, y1, x2, y2)
        line.setPen(QPen(QColor(color), linewidth))

        # Group them together
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        group.addToGroup(line)

        group.setPos(cx, cy)
        group.setRotation(angle + cubicle_rotation)  # Apply base angle + additional rotation
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
    
    # New options for connection points
    show_connection_point = data.get("show_connection_point", False)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 3)

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

    # Draw connection point at bus connection
    if show_connection_point:
        draw_connection_point(scene, points[0], connection_point_color, connection_point_size)

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
    
    # New options for connection points
    show_connection_point = data.get("show_connection_point", False)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 3)

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

    # Draw connection point at bus connection
    if show_connection_point:
        draw_connection_point(scene, points[0], connection_point_color, connection_point_size)

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
    
    # New options for connection points
    show_start_point = data.get("show_start_point", False)
    show_end_point = data.get("show_end_point", False)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 3)

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

    for i in range(len(to_points) - 1):
        line = QGraphicsLineItem(to_points[i].x(), to_points[i].y(), to_points[i+1].x(), to_points[i+1].y())
        line.setPen(QPen(QColor(color), 2 * linescale))
        scene.addItem(line)

    # Draw connection points
    if show_start_point:
        draw_connection_point(scene, from_points[0], connection_point_color, connection_point_size)
    
    if show_end_point:
        draw_connection_point(scene, to_points[-1], connection_point_color, connection_point_size)

    # Draw cubicle1 at the start of from-side
    if "cubicle1" in data and data["cubicle1"] and len(from_points) >= 2:
        angle_start = angle_between(from_points[0], from_points[1])
        for cub in data["cubicle1"]:
            draw_cubicle(scene, cub, ports, from_points[0], angle_start - 90)

    # Draw cubicle2 at the end of to-side
    if "cubicle2" in data and data["cubicle2"] and len(to_points) >= 2:
        angle_end = angle_between(to_points[-1], to_points[-2])
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

def draw_inverter_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    if obj_type not in ("inv", "inverter"):
        raise ValueError("Only 'inv' or 'inverter' objects supported.")

    data = obj.get("data", {})
    from_port = data.get("from")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    symbol_size = data.get("inv_size", 32) * linescale
    
    # New options for connection points
    show_connection_point = data.get("show_connection_point", False)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 3)

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

    # Draw connection point at bus connection
    if show_connection_point:
        draw_connection_point(scene, points[0], connection_point_color, connection_point_size)

    # Draw cubicle (only one, at the start)
    if cubicle and len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        draw_cubicle(scene, cubicle[0], ports, points[0], angle_start - 90)

    # Draw inverter SVG at the end
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

        # The end of the line should be at the edge of the symbol
        center_x = p2.x() + dx * (symbol_size / 2)
        center_y = p2.y() + dy * (symbol_size / 2)

        svg_content = load_svg_with_color("inverter.svg", color, stroke_width=linescale)
        svg_item = create_colored_svg_item(svg_content)

        svg_item.setTransform(QTransform().scale(symbol_size / svg_item.boundingRect().width(),
                                                symbol_size / svg_item.boundingRect().height()))
        svg_item.setPos(center_x - symbol_size / 2, center_y - symbol_size / 2)

        # Calculate the angle of the last line segment (in degrees)
        angle = math.degrees(math.atan2(dy, dx))
        svg_item.setTransformOriginPoint(svg_item.boundingRect().width() / 2, svg_item.boundingRect().height() / 2)
        svg_item.setRotation(angle - 90)

        scene.addItem(svg_item)

def load_svg_with_color(svg_path, color, stroke_width=None, text_color="white"):
    try:
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()
    except Exception as e:
        print(f"Error reading SVG: {e}")
        return None

    # Replace stroke and fill colors for non-text elements
    # Replace all stroke colors
    svg_content = re.sub(r'stroke="[^"]*"', f'stroke="{color}"', svg_content)
    
    # Replace fill colors ONLY for elements that already have fill attribute, BUT NOT fill="none"
    svg_content = re.sub(r'fill="(?!none")[^"]*"', f'fill="{color}"', svg_content)

    # Handle text elements specifically
    if text_color is not None:
        # For text elements, override stroke and fill with text_color and remove stroke-width
        # Replace stroke color for text elements
        svg_content = re.sub(r'(<text[^>]*?)stroke="[^"]*"', rf'\1stroke="{text_color}"', svg_content)
        # Add stroke color if text doesn't have it
        svg_content = re.sub(r'(<text(?![^>]*stroke=)[^>]*?)>', rf'\1 stroke="{text_color}">', svg_content)
        
        # Replace fill color for text elements (only if they already have fill and it's not "none")
        svg_content = re.sub(r'(<text[^>]*?)fill="(?!none")[^"]*"', rf'\1fill="{text_color}"', svg_content)
        # Add fill color if text doesn't have it
        svg_content = re.sub(r'(<text(?![^>]*fill=)[^>]*?)>', rf'\1 fill="{text_color}">', svg_content)
        
        # Remove stroke-width from text elements
        svg_content = re.sub(r'(<text[^>]*?)stroke-width="[^"]*"([^>]*?>)', rf'\1\2', svg_content)

    # Apply stroke-width to non-text elements only
    if stroke_width is not None:
        # This will replace stroke-width for all elements first
        svg_content = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{stroke_width}"', svg_content)
        
        # Then remove stroke-width from text elements again (in case they got it added above)
        if text_color is not None:
            svg_content = re.sub(r'(<text[^>]*?)stroke-width="[^"]*"([^>]*?>)', rf'\1\2', svg_content)

    return svg_content

def create_colored_svg_item(svg_content):
    renderer = QSvgRenderer(QByteArray(svg_content.encode('utf-8')))
    
    if not renderer.isValid():
        print("SVG renderer failed to load the SVG!")
        return None
    # buffer = QBuffer()
    # buffer.setData(QByteArray(svg_content.encode('utf-8')))
    # buffer.open(QBuffer.ReadOnly)
    item = QGraphicsSvgItem()
    # item.renderer().load(buffer)
    item.setSharedRenderer(renderer)
    item._renderer = renderer
    return item

def draw_svg_element_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    data = obj.get("data", {})
    from_port = data.get("from")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    linescale = data.get("linescale", 1.0)
    symbol_size = data.get(f"{obj_type}_size", 32)  # e.g., battery_size, inverter_size
    
    # New options for connection points
    show_connection_point = data.get("show_connection_point", False)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 3)

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

    # Draw connection point at bus connection
    if show_connection_point:
        draw_connection_point(scene, points[0], connection_point_color, connection_point_size)

    # Draw cubicle (only one, at the start)
    cubicle = data.get("cubicle", [])
    if cubicle and len(points) >= 2:
        angle_start = angle_between(points[0], points[1])
        draw_cubicle(scene, cubicle[0], ports, points[0], angle_start - 90)

    # Draw SVG at the end
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

        # The end of the line should be at the edge of the symbol
        center_x = p2.x() + dx * (symbol_size / 2)
        center_y = p2.y() + dy * (symbol_size / 2)

        svg_filename = f"{obj_type}.svg"
        svg_content = load_svg_with_color(svg_filename, color, stroke_width=2*linescale)
        svg_item = create_colored_svg_item(svg_content)

        if svg_item:
            svg_item.setTransform(QTransform().scale(
                symbol_size / svg_item.boundingRect().width(),
                symbol_size / svg_item.boundingRect().height()))
            svg_item.setPos(center_x - symbol_size / 2, center_y - symbol_size / 2)
            angle = math.degrees(math.atan2(dy, dx))
            svg_item.setTransformOriginPoint(svg_item.boundingRect().width() / 2, svg_item.boundingRect().height() / 2)
            svg_item.setRotation(angle - 90)
            scene.addItem(svg_item)

def draw_two_terminal_svg_element_from_json(scene, view, obj, ports):
    obj_type = obj.get("type")
    data = obj.get("data", {})
    from_port = data.get("from")
    to_port = data.get("to")
    points_data = data.get("point", [])
    color = data.get("color", "black")
    text_color = data.get("text_color", None)  # New parameter for text color
    linescale = data.get("linescale", 1.0)
    
    # New options for connection points
    show_start_point = data.get("show_start_point", True)
    show_end_point = data.get("show_end_point", True)
    connection_point_color = data.get("connection_point_color", color)
    connection_point_size = data.get("connection_point_size", 4)

    if from_port not in ports or to_port not in ports:
        print(f"Missing port: {from_port} or {to_port}")
        return None

    # Split points into from-side and to-side using "split" marker
    if "split" in points_data:
        split_idx = points_data.index("split")
        from_points = [QPointF(*ports[from_port])] + [resolve_point(pt, ports) for pt in points_data[:split_idx]]
        to_points = [resolve_point(pt, ports) for pt in points_data[split_idx+1:]] + [QPointF(*ports[to_port])]
    else:
        from_points = [QPointF(*ports[from_port])]
        to_points = [QPointF(*ports[to_port])]

    # Draw lines for from-side and to-side
    pen = QPen(QColor(color))
    pen.setWidthF(2 * linescale)
    for i in range(len(from_points) - 1):
        line = QGraphicsLineItem(from_points[i].x(), from_points[i].y(), from_points[i+1].x(), from_points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)
    for i in range(len(to_points) - 1):
        line = QGraphicsLineItem(to_points[i].x(), to_points[i].y(), to_points[i+1].x(), to_points[i+1].y())
        line.setPen(pen)
        scene.addItem(line)

    # Draw connection points
    if show_start_point:
        draw_connection_point(scene, from_points[0], connection_point_color, connection_point_size)
    
    if show_end_point:
        draw_connection_point(scene, to_points[-1], connection_point_color, connection_point_size)

    # Get the two points that define the symbol's placement
    pf = from_points[-1]
    pt = to_points[0]

    # Vector and distance
    dx = pt.x() - pf.x()
    dy = pt.y() - pf.y()
    length = (dx**2 + dy**2) ** 0.5
    if length == 0:
        return
    angle = math.degrees(math.atan2(dy, dx))

    # Center point for the symbol
    center_x = (pf.x() + pt.x()) / 2
    center_y = (pf.y() + pt.y()) / 2

    # Load SVG with text_color parameter
    svg_filename = f"{obj_type}.svg"
    svg_content = load_svg_with_color(svg_filename, color, stroke_width=2*linescale, text_color=text_color)
    svg_item = create_colored_svg_item(svg_content)

    if svg_item:
        # Scale so that the SVG's height matches the length between pf and pt
        br = svg_item.boundingRect()
        scale_factor = length / br.height() if br.height() != 0 else 1.0

        # Center the SVG at the midpoint between pf and pt
        svg_item.setTransform(QTransform()
            .translate(center_x - br.width() * scale_factor / 2, center_y - br.height() * scale_factor / 2)
            .scale(scale_factor, scale_factor)
        )
        svg_item.setTransformOriginPoint(br.width() / 2, br.height() / 2)
        svg_item.setRotation(angle - 90)  # -90 to align vertical SVGs with the connection

        scene.addItem(svg_item)

    # Optionally, handle cubicles as in your transformer code
    if "cubicle1" in data and data["cubicle1"] and len(from_points) >= 2:
        angle_start = angle_between(from_points[0], from_points[1])
        for cub in data["cubicle1"]:
            draw_cubicle(scene, cub, ports, from_points[0], angle_start - 90, 2*linescale)
    if "cubicle2" in data and data["cubicle2"] and len(to_points) >= 2:
        angle_end = angle_between(to_points[-1], to_points[-2])
        for cub in data["cubicle2"]:
            draw_cubicle(scene, cub, ports, to_points[-1], angle_end - 90, 2*linescale)

def draw_cubicle_svg(scene, cubicle_obj, ports, base_point, angle, linescale=None):
    """
    Draws a cubicle symbol using an SVG file named after c_type.
    The offset is measured from base_point to the top middle of the SVG.
    The symbol is rotated to align with the path (angle).
    """
    data = cubicle_obj.get("data", {})
    offset = data.get("offset", [0, 0])
    color = data.get("color", "red")
    scale = data.get("scale", 1.0)

    c_type = cubicle_obj.get("type")
    svg_filename = f"{c_type}.svg"

    # Load SVG content and create item
    svg_content = load_svg_with_color(svg_filename, color, stroke_width=linescale)
    svg_item = create_colored_svg_item(svg_content)
    if svg_item is None:
        print(f"SVG for cubicle type '{c_type}' could not be loaded.")
        return

    # Scale SVG by 'scale' factor
    br = svg_item.boundingRect()
    if br.width() == 0 or br.height() == 0:
        print(f"SVG bounding rect is invalid for '{svg_filename}'")
        return
    symbol_width = br.width() * scale
    symbol_height = br.height() * scale

    # Offset is measured from base_point to the top middle of the SVG (before rotation)
    # So, the anchor point is (0.5*width, 0) in SVG local coordinates
    dx, dy = rotated_offset(offset, angle)
    cx = base_point.x() + dx
    cy = base_point.y() + dy

    # Set transform: scale, then move so that (0.5*width, 0) is at (cx, cy), then rotate
    svg_item.setTransform(
        QTransform()
        .translate(cx - symbol_width / 2, cy)
        .scale(scale, scale)
    )
    svg_item.setTransformOriginPoint(br.width() / 2, 0)  # top middle
    svg_item.setRotation(angle)

    scene.addItem(svg_item)

def align_bus_x(aligned_bus, ref_bus, aligned_port, ref_port, ports):
    """
    Move aligned_bus so that aligned_port (of aligned_bus) is aligned in x with ref_port (of ref_bus).
    Modifies aligned_bus['data']['position'] in place.
    """
    # Get current positions of the ports
    if aligned_port not in ports or ref_port not in ports:
        raise ValueError(f"Port not found: {aligned_port} or {ref_port}")

    aligned_x, aligned_y = ports[aligned_port]
    ref_x, ref_y = ports[ref_port]

    # Get current bus position
    pos = aligned_bus['data'].get('position', [0, 0])
    dx = ref_x - aligned_x  # How much to move in x

    # Move the bus in x so that aligned_port.x == ref_port.x
    new_pos = [pos[0] + dx, pos[1]]
    aligned_bus['data']['position'] = new_pos

    return aligned_bus

def align_bus_y(aligned_bus, ref_bus, aligned_port, ref_port, ports):
    """
    Move aligned_bus so that aligned_port (of aligned_bus) is aligned in y with ref_port (of ref_bus).
    Modifies aligned_bus['data']['position'] in place.
    """
    # Get current positions of the ports
    if aligned_port not in ports or ref_port not in ports:
        raise ValueError(f"Port not found: {aligned_port} or {ref_port}")

    aligned_x, aligned_y = ports[aligned_port]
    ref_x, ref_y = ports[ref_port]

    # Get current bus position
    pos = aligned_bus['data'].get('position', [0, 0])
    dy = ref_y - aligned_y  # How much to move in y

    # Move the bus in y so that aligned_port.y == ref_port.y
    new_pos = [pos[0], pos[1] + dy]
    aligned_bus['data']['position'] = new_pos

    return aligned_bus

def draw_text_from_json(scene, obj, ports):
    """
    Draws text from JSON specification with flexible positioning.
    
    Args:
        scene: QGraphicsScene to add text to
        obj: JSON object with text data
        ports: Dictionary of connection points for reference positioning
        
    JSON format:
    {
        "type": "text",
        "id": "text1",
        "data": {
            "text": "Hello World",
            "position": [100, 100] or "bus1:d0" or ["bus1:d0:x", "bus2:u1:y"],  # Base position
            "font": {
                "family": "Arial",
                "size": 12,
                "bold": false,
                "italic": false
            },
            "color": "black",
            "anchor": "center",  # Reference point: topleft, topmid, topright, midleft, center, midright, bottomleft, bottommid, bottomright
            "offset": [10, -5],  # Offset from anchor point
            "rotation": 0        # Rotation angle in degrees
        }
    }
    """
    obj_type = obj.get("type")
    if obj_type != "text":
        raise ValueError("Only 'text' objects supported.")

    obj_id = obj.get("id")
    data = obj.get("data", {})

    # Required fields
    text_content = data.get("text", "")
    if not text_content:
        print(f"Warning: Empty text content for {obj_id}")
        return None

    # Position resolution - now supports multiple formats
    position = data.get("position", [0, 0])
    
    if isinstance(position, str):
        # Check if it's an axis reference like "bus1:u1:x" or "bus1:u1:y"
        if position.count(':') == 2:
            # Axis reference - use resolve_axis
            try:
                # For axis reference, we need both x and y, so we'll extract the base port
                parts = position.split(':')
                if len(parts) == 3:
                    base_port = f"{parts[0]}:{parts[1]}"
                    axis = parts[2]
                    
                    if base_port in ports:
                        port_x, port_y = ports[base_port]
                        if axis == 'x':
                            # Use the x from the specified port, but we need a y coordinate
                            # We'll use the same port's y coordinate
                            base_x = resolve_axis(position, ports)
                            base_y = port_y
                        elif axis == 'y':
                            # Use the y from the specified port, but we need an x coordinate  
                            # We'll use the same port's x coordinate
                            base_x = port_x
                            base_y = resolve_axis(position, ports)
                        else:
                            raise ValueError(f"Invalid axis '{axis}' in position: {position}")
                    else:
                        print(f"Port not found: {base_port}")
                        return None
                else:
                    raise ValueError(f"Invalid axis reference format: {position}")
            except Exception as e:
                print(f"Error resolving axis position '{position}': {e}")
                return None
        else:
            # Regular port reference like "bus1:d0"
            if position in ports:
                base_x, base_y = ports[position]
            else:
                print(f"Port not found: {position}")
                return None
                
    elif isinstance(position, (list, tuple)) and len(position) == 2:
        # Could be direct coordinates or axis references
        try:
            base_x = resolve_axis(position[0], ports)
            base_y = resolve_axis(position[1], ports)
        except Exception as e:
            print(f"Error resolving position {position}: {e}")
            return None
    else:
        print(f"Invalid position format: {position}")
        return None

    # Font configuration
    font_data = data.get("font", {})
    font_family = font_data.get("family", "Arial")
    font_size = font_data.get("size", 12)
    font_bold = font_data.get("bold", False)
    font_italic = font_data.get("italic", False)

    # Create font
    font = QFont(font_family, font_size)
    font.setBold(font_bold)
    font.setItalic(font_italic)

    # Text styling
    color = data.get("color", "black")
    anchor = data.get("anchor", "center").lower()
    offset = data.get("offset", [0, 0])
    rotation = data.get("rotation", 0)

    # Create text item
    text_item = QGraphicsTextItem(text_content)
    text_item.setFont(font)
    text_item.setDefaultTextColor(QColor(color))

    # Get bounding rectangle for anchor calculations
    br = text_item.boundingRect()
    
    # Calculate anchor point offsets within the text bounding rectangle
    anchor_offsets = {
        "topleft": (0, 0),
        "topmid": (br.width() / 2, 0),
        "topright": (br.width(), 0),
        "midleft": (0, br.height() / 2),
        "center": (br.width() / 2, br.height() / 2),
        "midright": (br.width(), br.height() / 2),
        "bottomleft": (0, br.height()),
        "bottommid": (br.width() / 2, br.height()),
        "bottomright": (br.width(), br.height())
    }

    if anchor not in anchor_offsets:
        print(f"Warning: Unknown anchor '{anchor}', using 'center'")
        anchor = "center"

    anchor_dx, anchor_dy = anchor_offsets[anchor]
    offset_dx, offset_dy = offset

    # Calculate final position
    # The anchor point of the text should be at (base_x + offset_dx, base_y + offset_dy)
    final_x = base_x + offset_dx - anchor_dx
    final_y = base_y + offset_dy - anchor_dy

    # Set position and rotation
    text_item.setPos(final_x, final_y)
    
    if rotation != 0:
        # Set rotation around the anchor point
        text_item.setTransformOriginPoint(anchor_dx, anchor_dy)
        text_item.setRotation(rotation)

    scene.addItem(text_item)
    return text_item

def draw_diagram_from_dict(scene, view, diagram_dict):
    """
    Draws all elements from a diagram dictionary by dispatching to appropriate draw functions.
    
    Args:
        scene: QGraphicsScene to draw on
        view: QGraphicsView for elements that need view reference
        diagram_dict: Dictionary containing all diagram elements
        
    Expected diagram_dict structure:
    {
        "buses": [bus1_json, bus2_json, ...],
        "lines": [line1_json, line2_json, ...],
        "loads": [load1_json, load2_json, ...],
        "generators": [gen1_json, gen2_json, ...],
        "transformers": [trafo1_json, trafo2_json, ...],
        "inverters": [inv1_json, inv2_json, ...],
        "svg_elements": [bess1_json, bess2_json, ...],
        "two_terminal_elements": [trafo1_json, switch1_json, ...],
        "texts": [text1_json, text2_json, ...]
    }
    """
    ports = {}  # Collect all connection points
    drawn_items = {}  # Track drawn items by ID
    
    # Function mapping for different element types
    draw_functions = {
        "bus": draw_object_from_json,
        "line": lambda scene, obj, ports: draw_line_from_json(scene, obj, ports),
        "load": lambda scene, obj, ports: draw_load_from_json(scene, view, obj, ports),
        "generator": lambda scene, obj, ports: draw_generator_from_json(scene, view, obj, ports),
        "transformer": lambda scene, obj, ports: draw_transformer_from_json(scene, view, obj, ports),
        "inverter": lambda scene, obj, ports: draw_inverter_from_json(scene, view, obj, ports),
        "svg_element": lambda scene, obj, ports: draw_svg_element_from_json(scene, view, obj, ports),
        "two_terminal_svg": lambda scene, obj, ports: draw_two_terminal_svg_element_from_json(scene, view, obj, ports),
        "text": lambda scene, obj, ports: draw_text_from_json(scene, obj, ports)
    }
    
    # Drawing order - buses first to establish connection points
    drawing_order = [
        ("buses", "bus"),
        ("lines", "line"),
        ("loads", "load"), 
        ("generators", "generator"),
        ("transformers", "transformer"),
        ("inverters", "inverter"),
        ("svg_elements", "svg_element"),
        ("two_terminal_elements", "two_terminal_svg"),
        ("texts", "text")
    ]
    
    # Draw elements in order
    for category, element_type in drawing_order:
        if category in diagram_dict:
            elements = diagram_dict[category]
            if not isinstance(elements, list):
                elements = [elements]  # Handle single element
                
            for element in elements:
                try:
                    obj_id = element.get("id", f"unknown_{element_type}")
                    
                    # Special handling for buses - they return ports
                    if element_type == "bus":
                        result = draw_functions[element_type](scene, element)
                        if result and len(result) == 2:
                            line_item, element_ports = result
                            ports.update(element_ports)
                            drawn_items[obj_id] = line_item
                        else:
                            print(f"Warning: Bus {obj_id} didn't return expected format")
                    
                    # All other elements
                    else:
                        draw_function = draw_functions.get(element_type)
                        if draw_function:
                            if element_type in ["line", "text"]:
                                # Functions that don't need view parameter
                                result = draw_function(scene, element, ports)
                            else:
                                # Functions that need view parameter
                                result = draw_function(scene, element, ports)
                            drawn_items[obj_id] = result
                        else:
                            print(f"Warning: No draw function for element type '{element_type}'")
                            
                except Exception as e:
                    print(f"Error drawing {element_type} {obj_id}: {str(e)}")
                    continue
    
    return drawn_items, ports


def load_diagram_from_file(file_path):
    """
    Load diagram dictionary from a Python file.
    
    Args:
        file_path: Path to Python file containing diagram_dict variable
        
    Returns:
        Dictionary containing all diagram elements
    """
    import importlib.util
    import sys
    
    try:
        spec = importlib.util.spec_from_file_location("diagram_module", file_path)
        diagram_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(diagram_module)
        
        # Look for 'diagram_dict' variable in the module
        if hasattr(diagram_module, 'diagram_dict'):
            return diagram_module.diagram_dict
        else:
            print(f"Error: No 'diagram_dict' variable found in {file_path}")
            return {}
            
    except Exception as e:
        print(f"Error loading diagram from {file_path}: {str(e)}")
        return {}


def draw_diagram_from_file(scene, view, file_path):
    """
    Convenience function to load and draw diagram from file in one call.
    
    Args:
        scene: QGraphicsScene to draw on
        view: QGraphicsView for elements that need view reference  
        file_path: Path to Python file containing diagram_dict
        
    Returns:
        Tuple of (drawn_items, ports)
    """
    diagram_dict = load_diagram_from_file(file_path)
    if diagram_dict:
        return draw_diagram_from_dict(scene, view, diagram_dict)
    else:
        return {}, {}



