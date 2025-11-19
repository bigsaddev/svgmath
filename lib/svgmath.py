class SVGMath:
    def __init__(self, width: float, height: float, scale: float = 20.0, centered: bool = True, padding: float = 20.0):
        self.width = width
        self.height = height
        self.scale = scale
        self.centered = centered
        self.padding = padding

        self.background_color = "white"
        self.elements = []

        # Origin position in SVG space
        if centered:
            self.origin_x = width / 2
            self.origin_y = height / 2
        else:
            self.origin_x = padding
            self.origin_y = height - padding

    # -------------------------------------------------------
    # Helper conversions
    # -------------------------------------------------------

    def to_svg_xy(self, x, y):
        """Convert math coords → SVG coords."""
        x_svg = self.origin_x + x * self.scale
        y_svg = self.origin_y - y * self.scale
        return x_svg, y_svg

    # -------------------------------------------------------
    # Grid
    # -------------------------------------------------------

    def grid(self, spacing: float = 1.0, color: str = "#ddd", stroke_width: float = 0.5):
        if self.centered:
            # ----- centered mode -----
            x_min = -self.origin_x / self.scale
            x_max = (self.width - self.origin_x) / self.scale
            y_min = -self.origin_y / self.scale
            y_max = (self.height - self.origin_y) / self.scale
        else:
            # ----- non-centered mode (first quadrant) -----
            x_min = 0
            x_max = (self.width - self.padding - self.origin_x) / self.scale
            y_min = 0
            y_max = (self.origin_y - self.padding) / self.scale

        # Vertical grid lines
        x = x_min
        while x <= x_max:
            x_svg = self.origin_x + x * self.scale
            self.elements.append(
                f'<line x1="{x_svg}" y1="0" x2="{x_svg}" y2="{self.height}" '
                f'stroke="{color}" stroke-width="{stroke_width}" />'
            )
            x += spacing

        # Horizontal grid lines
        y = y_min
        while y <= y_max:
            y_svg = self.origin_y - y * self.scale
            self.elements.append(
                f'<line x1="0" y1="{y_svg}" x2="{self.width}" y2="{y_svg}" '
                f'stroke="{color}" stroke-width="{stroke_width}" />'
            )
            y += spacing

    # -------------------------------------------------------
    # Axis
    # -------------------------------------------------------

    def axis(self, color: str = "black", stroke_width: float = 1.0):
        # Horizontal axis
        self.elements.append(
            f'<line x1="0" y1="{self.origin_y}" x2="{self.width}" y2="{self.origin_y}" '
            f'stroke="{color}" stroke-width="{stroke_width}" />'
        )

        # Vertical axis
        self.elements.append(
            f'<line x1="{self.origin_x}" y1="0" x2="{self.origin_x}" y2="{self.height}" '
            f'stroke="{color}" stroke-width="{stroke_width}" />'
        )

    # -------------------------------------------------------
    # Ticks + Labels
    # -------------------------------------------------------

    def ticks(self, spacing: float = 1.0, color: str = "black", font_size: int = 8):
        if self.centered:
            # centered coordinate range
            x_min = -self.origin_x / self.scale
            x_max = (self.width - self.origin_x) / self.scale
            y_min = -self.origin_y / self.scale
            y_max = (self.height - self.origin_y) / self.scale
        else:
            # first quadrant
            x_min = 0
            x_max = (self.width - self.padding - self.origin_x) / self.scale
            y_min = 0
            y_max = (self.origin_y - self.padding) / self.scale

        # --- X ticks ---
        x = x_min
        while x <= x_max:
            x_svg = self.origin_x + x * self.scale

            # tick
            self.elements.append(
                f'<line x1="{x_svg}" y1="{self.origin_y-3}" '
                f'x2="{x_svg}" y2="{self.origin_y+3}" '
                f'stroke="{color}" stroke-width="0.5" />'
            )
            # label
            self.elements.append(
                f'<text x="{x_svg - 1.25}" y="{self.origin_y + 8}" '
                f'font-size="{font_size}" fill="{color}">{x:g}</text>'
            )
            x += spacing

        # --- Y ticks ---
        y = y_min
        while y <= y_max:
            y_svg = self.origin_y - y * self.scale

            self.elements.append(
                f'<line x1="{self.origin_x-3}" y1="{y_svg}" '
                f'x2="{self.origin_x+3}" y2="{y_svg}" '
                f'stroke="{color}" stroke-width="0.5" />'
            )

            self.elements.append(
                f'<text x="{self.origin_x - 8}" y="{y_svg + 1.25}" '
                f'font-size="{font_size}" fill="{color}">{y:g}</text>'
            )

            y += spacing

    # -------------------------------------------------------
    # Function plotting
    # -------------------------------------------------------

    def plot_function(self, func, color="blue", stroke_width=1.0, step=0.5):
        points = []
        x = 0
        while x <= self.width:
            # Convert screen x → math x
            math_x = (x - self.origin_x) / self.scale
            y = func(math_x)
            y_svg = self.origin_y - (y * self.scale)
            points.append(f"{x},{y_svg}")
            x += step

        self.elements.append(
            f'<polyline points="{" ".join(points)}" fill="none" '
            f'stroke="{color}" stroke-width="{stroke_width}" />'
        )

    # -------------------------------------------------------
    # Points + Labels
    # -------------------------------------------------------

    def map_coord(self, x: float, y: float, color: str = "black", font_size: int = 8, text_offset: float = 2.0, text: str = "", radius: float = 2.0):
        x_svg, y_svg = self.to_svg_xy(x, y)
        self.elements.append(
            f'<circle cx="{x_svg}" cy="{y_svg}" r="{radius}" fill="{color}" />'
            + f'<text x="{x_svg + text_offset}" y="{y_svg - text_offset}" '
            f'font-size="{font_size}" fill="{color}">{text + f"({x:g}/{y:g})"}</text>'
        )

    def map_blank(self, x: float, y: float, color: str = "black", font_size: int = 8, text_offset: float = 2.0, text: str = "", radius: float = 2.0):
        x_svg, y_svg = self.to_svg_xy(x, y)
        self.elements.append(
            f'<circle cx="{x_svg}" cy="{y_svg}" r="{radius}" fill="{color}" />'
            + f'<text x="{x_svg + text_offset}" y="{y_svg - text_offset}" '
            f'font-size="{font_size}" fill="{color}">{text}</text>'
        )

    # -------------------------------------------------------
    # Text
    # -------------------------------------------------------

    def text(self, x: float, y: float, content: str, color: str = "black", font_size: int = 8):
        x_svg, y_svg = self.to_svg_xy(x, y)
        self.elements.append(
            f'<text x="{x_svg}" y="{y_svg}" font-size="{font_size}" fill="{color}">{content}</text>'
        )

    def fraction(self, prefix: str, numerator: str, denominator: str, x: float, y: float, color: str = "black", font_size: int = 8, line_thickness: float = 0.5):
        x_svg, y_svg = self.to_svg_xy(x, y)
        # Prefix
        self.elements.append(
            f'<text x="{x_svg - font_size * 1.2}" y="{y_svg + font_size/4}" '
            f'font-size="{font_size}" fill="{color}" text-anchor="end">{prefix}</text>'
        )
        # Numerator
        self.elements.append(
            f'<text x="{x_svg}" y="{y_svg - font_size * 0.3}" '
            f'font-size="{font_size}" fill="{color}" text-anchor="middle">{numerator}</text>'
        )
        # Denominator
        self.elements.append(
            f'<text x="{x_svg}" y="{y_svg + font_size * 0.7}" '
            f'font-size="{font_size}" fill="{color}" text-anchor="middle">{denominator}</text>'
        )
        # Fraction line
        self.elements.append(
            f'<line x1="{x_svg - font_size}" y1="{y_svg}" '
            f'x2="{x_svg + font_size}" y2="{y_svg}" '
            f'stroke="{color}" stroke-width="{line_thickness}" />'
        )

    # -------------------------------------------------------
    # Rendering / Saving
    # -------------------------------------------------------

    def render(self) -> str:
        return (
            f'<svg width="{self.width}" height="{self.height}" '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'style="background:{self.background_color};">\n'
            + "\n".join(f"    {el}" for el in self.elements)
            + "\n</svg>"
        )

    def save(self, filename: str):
        with open(filename, "w") as f:
            f.write(self.render())
            print("SVG saved to", filename)
