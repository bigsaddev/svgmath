from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25, centered=False)

    # svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    # svg.ticks(spacing=1, font_size=8)

    #functions = [
        #(lambda x: x*2+2, "green"),
        #(lambda x: -2*x+5, "blue"),
        #(lambda x: 2.5*x, "pink"),
        #(lambda x: -x+4, "black"),
    #]

    #for func, color in functions:
        #svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.text(10, 0, "4x - 10 = 2x + 20", font_size=18, color="black")
    svg.text(160, 0, "| +10", font_size=18, color="red")
    svg.text(10, 20, "4x = 2x + 30", font_size=18, color="black")
    svg.text(160, 20, "| -2x", font_size=18, color="red")
    svg.text(10, 40, "2x = 30", font_size=18, color="black")
    svg.text(160, 40, "| : 2", font_size=18, color="red")
    svg.text(10, 60, "x = 15", font_size=18, color="black")
    svg.line(10, 80, 60, 80, stroke="black", stroke_width=1.0)
    svg.line(10, 82, 60, 82, stroke="black", stroke_width=1.0)

    # new approach
    svg.text(10, 100, "4x - 10 = 2x + 20", font_size=18, color="black")
    svg.line(70, 120, 70, 240, stroke="black", stroke_width=1.0)
    svg.text(32, 120, "+10", font_size=18, color="red")
    svg.text(103, 120, "+10", font_size=18, color="red")
    svg.text(43, 140, "4x = 2x + 30", font_size=18, color="black")
    svg.text(32, 160, "-2x", font_size=18, color="red")
    svg.text(103, 160, "-2x", font_size=18, color="red")
    svg.text(43, 180, "2x = 30", font_size=18, color="black")
    svg.text(32, 200, ": 2", font_size=18, color="red")
    svg.text(103, 200, ": 2", font_size=18, color="red")
    svg.text(50, 220, "x = 15", font_size=18, color="black")

    svg.map_coord(300, 300, color="blue", font_size=12, text_offset=3.0, blank_coords=True, radius=3.0)

    svg.save("equation.svg")


if __name__ == "__main__":
    main()
