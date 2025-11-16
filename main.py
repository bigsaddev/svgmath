from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=4)

    functions = [
        (lambda x: -x+2, "pink"),
        (lambda x: -4*x+4, "blue"),
        (lambda x: -x*3-5, "green"),
        (lambda x: x-3, "black"),
    ]

    for func, color in functions:
        svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.text(-6.5, 4, "y = mx+b", color="black", font_size=18)
    svg.fraction("m = ", "y - b", "x", -4.5, 2, color="black", font_size=18)

    svg.save("plot2.svg")


if __name__ == "__main__":
    main()
