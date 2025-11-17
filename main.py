from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=8)

    functions = [
        (lambda x: x*2-6, "green"),
        (lambda x: -0.5*x+2, "blue"),
        (lambda x: 3*x, "pink"),
        (lambda x: -6*x-4, "black"),
    ]

    for func, color in functions:
        svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.text(-6.5, 4, "y = mx+b", color="black", font_size=18)
    svg.fraction("m = ", "y - b", "x", -4.5, 2, color="black", font_size=18)

    svg.map_coord(1, 3, text="A", color="black", font_size=12)
    #svg.map_coord(-4, 7, text="B", color="black", font_size=12)


    svg.save("plot.svg")


if __name__ == "__main__":
    main()
