# Contour Visualization and Interaction Tool

This Python application visualizes geometric contours and allows for interactive selection and manipulation of contour elements. The application uses `matplotlib` for graphical representation and `mplcursors` for creating tooltips and handling interactive events. Users can interact with lines and arcs in the plot, select them with a `Shift`+click, and reset the selections with the `Esc` key.

## Features

- **Contour Visualization**: Renders lines and arcs defined by their geometric properties.
- **Interactive Tooltips**: Displays coordinate information when hovering over key points.
- **Line Selection**: Enables line highlighting on `Shift`+click with color and width changes.
- **Selection Reset**: Allows clearing of selected lines with the `Esc` key.

## Requirements

- Python 3.x
- `matplotlib`
- `mplcursors`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/contour-visualization.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application to visualize and interact with the contour plot:

```bash
python contour_visualization.py
```

## License

This project is licensed under the MIT License.
