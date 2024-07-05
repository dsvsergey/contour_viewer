import matplotlib.pyplot as plt
import numpy as np
import mplcursors
from matplotlib.backend_bases import MouseEvent


contour = [
    {
        "edge": 0,
        "length": 100.0,
        "type": "line",
        "x1": 550.0,
        "x2": 650.0,
        "y1": 400.0,
        "y2": 400.0,
    },
    {
        "dir": True,
        "edge": None,
        "length": 78.5,
        "r": 50.0,
        "type": "arc",
        "x1": 650.0,
        "x2": 700.0,
        "xc": 700.0,
        "y1": 400.0,
        "y2": 350.0,
        "yc": 400.0,
    },
    {
        "edge": 3,
        "length": 350.0,
        "type": "line",
        "x1": 700.0,
        "x2": 700.0,
        "y1": 350.0,
        "y2": 0.0,
    },
    {
        "edge": 1,
        "length": 700.0,
        "type": "line",
        "x1": 700.0,
        "x2": 0.0,
        "y1": 0.0,
        "y2": 0.0,
    },
    {
        "edge": 1,
        "length": 500.0,
        "type": "line",
        "x1": 0.0,
        "x2": 0.0,
        "y1": 0.0,
        "y2": 500.0,
    },
    {
        "edge": 2,
        "length": 100.0,
        "type": "line",
        "x1": 0.0,
        "x2": 100.0,
        "y1": 500.0,
        "y2": 500.0,
    },
    {
        "edge": 2,
        "length": 200.0,
        "type": "line",
        "x1": 100.0,
        "x2": 100.0,
        "y1": 500.0,
        "y2": 700.0,
    },
    {
        "edge": 2,
        "length": 100.0,
        "type": "line",
        "x1": 100.0,
        "x2": 0.0,
        "y1": 700.0,
        "y2": 700.0,
    },
    {
        "edge": 1,
        "length": 200.0,
        "type": "line",
        "x1": 0.0,
        "x2": 0.0,
        "y1": 700.0,
        "y2": 900.0,
    },
    {
        "edge": 1,
        "length": 600.0,
        "type": "line",
        "x1": 0.0,
        "x2": 600.0,
        "y1": 900.0,
        "y2": 900.0,
    },
    {
        "dir": False,
        "edge": None,
        "length": 157.1,
        "r": 100.0,
        "type": "arc",
        "x1": 600.0,
        "x2": 700.0,
        "xc": 600.0,
        "y1": 900.0,
        "y2": 800.0,
        "yc": 800.0,
    },
    {
        "edge": 1,
        "length": 200.0,
        "type": "line",
        "x1": 700.0,
        "x2": 700.0,
        "y1": 800.0,
        "y2": 600.0,
    },
    {
        "edge": 0,
        "length": 100.0,
        "type": "line",
        "x1": 700.0,
        "x2": 600.0,
        "y1": 600.0,
        "y2": 600.0,
    },
    {
        "dir": True,
        "edge": None,
        "length": 157.1,
        "r": 100.0,
        "type": "arc",
        "x1": 600.0,
        "x2": 500.0,
        "xc": 600.0,
        "y1": 600.0,
        "y2": 500.0,
        "yc": 500.0,
    },
    {
        "edge": 0,
        "length": 50.0,
        "type": "line",
        "x1": 500.0,
        "x2": 500.0,
        "y1": 500.0,
        "y2": 450.0,
    },
    {
        "dir": True,
        "edge": None,
        "length": 78.5,
        "r": 50.0,
        "type": "arc",
        "x1": 500.0,
        "x2": 550.0,
        "xc": 550.0,
        "y1": 450.0,
        "y2": 400.0,
        "yc": 450.0,
    },
]


def plot_arc(xc, yc, r, x1, y1, x2, y2, clockwise=True):
    theta1 = np.arctan2(y1 - yc, x1 - xc)
    theta2 = np.arctan2(y2 - yc, x2 - xc)
    if clockwise:
        if theta2 < theta1:
            theta2 += 2 * np.pi
    else:
        if theta2 > theta1:
            theta2 -= 2 * np.pi
    theta = np.linspace(theta1, theta2, 100)
    x = xc + r * np.cos(theta)
    y = yc + r * np.sin(theta)
    return plt.plot(x, y, "b", picker=5)


fig, ax = plt.subplots(figsize=(10, 10))
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.grid(color="gray", linestyle="--", linewidth=0.5)

key_points = []
lines = []

for element in contour:
    if element["type"] == "line":
        (line,) = ax.plot(
            [element["x1"], element["x2"]],
            [element["y1"], element["y2"]],
            "b",
            picker=5,
        )
        lines.append(line)
        key_points.append((element["x1"], element["y1"]))
        key_points.append((element["x2"], element["y2"]))
    elif element["type"] == "arc":
        arc_line = plot_arc(
            element["xc"],
            element["yc"],
            element["r"],
            element["x1"],
            element["y1"],
            element["x2"],
            element["y2"],
            clockwise=element.get("dir", True),
        )[0]
        lines.append(arc_line)
        key_points.append((element["x1"], element["y1"]))
        key_points.append((element["x2"], element["y2"]))

key_point_markers = ax.plot(
    [pt[0] for pt in key_points], [pt[1] for pt in key_points], "ro"
)

# for x, y in key_points:
#     ax.text(x, y, f"({x}, {y})", fontsize=8, ha="right")

current_annotation = None

cursor = mplcursors.cursor(key_point_markers, hover=True)


@cursor.connect("add")
def on_add(sel):
    global current_annotation
    if current_annotation:
        current_annotation.annotation.set_visible(False)
    x, y = sel.target
    sel.annotation.set(text=f"({x:.2f}, {y:.2f})", fontsize=8)
    current_annotation = sel


selected_lines = []


# Processing of line click events
def on_pick(e0):
    # print(f"Event: {event}")
    if isinstance(e0.mouseevent, MouseEvent):
        if e0.mouseevent.key == "shift":
            line = e0.artist
            if line in selected_lines:
                line.set_color("b")
                line.set_linewidth(1)
                selected_lines.remove(line)
            else:
                line.set_color("r")
                line.set_linewidth(3)
                selected_lines.append(line)
            fig.canvas.draw()


# Handling of key events
def on_key(e0):
    global current_annotation
    print(f"Key Event: {e0.key}")
    if e0.key == "escape":
        if current_annotation:
            current_annotation.annotation.set_visible(False)
            current_annotation = None
        for line in selected_lines:
            line.set_color("b")
            line.set_linewidth(1)
        selected_lines.clear()
        fig.canvas.draw()


# Connecting event handlers
fig.canvas.mpl_connect("pick_event", on_pick)
fig.canvas.mpl_connect("key_press_event", on_key)

plt.gca().set_aspect("equal", adjustable="box")
plt.xlabel("X")
plt.ylabel("Y")
# plt.title("Visualization of Contour")
plt.show()
