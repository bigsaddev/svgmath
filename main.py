from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25, centered=True)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=12)

    functions = [
        #(lambda x: x*2+2, "green"),
        #(lambda x: -2*x+5, "blue"),
        #(lambda x: 2.5*x, "pink"),
        #(lambda x: -x+4, "black"),
    ]

    #for func, color in functions:
        #svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.line(-5, -2, 3, 2, stroke="red", stroke_width=1.5)
    svg.map_coord(3, 2, text="A", color="black", font_size=16, text_offset=3.0, radius=3.0)
    svg.map_coord(-5, -2, text="B", color="black", font_size=16, text_offset=-15.0, radius=3.0)


    svg.save("website/images/two_points.svg")


if __name__ == "__main__":
    main()
