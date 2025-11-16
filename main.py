from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=4)

    svg.plot_function(lambda x: 0.5*x+2, color="pink", stroke_width=1)
    svg.plot_function(lambda x: -1*x+4, color="blue", stroke_width=1)
    svg.plot_function(lambda x: x*2-4, color="green", stroke_width=1)
    svg.plot_function(lambda x: -x*3-4, color="black", stroke_width=1)

    svg.text(-6.5, 4, "y = mx+b", color="black", font_size=18)
    svg.fraction("m = ", "y - b", "x", -4.5, 2, color="black", font_size=18)

    svg.text(1, -7, "-7 + 4 : 1 = -3", color="black", font_size=12)
    svg.text(-5, 0.5, "0 - 2 : -4 = 0.5", color="pink", font_size=12)
    svg.text(1, -4, "0 - (-4) : 2 = 2", color="green", font_size=12)
    svg.text(4, 0.2, "0 - 4 : 4 = -1", color="blue", font_size=12)

    svg.save("plot.svg")


if __name__ == "__main__":
    main()
