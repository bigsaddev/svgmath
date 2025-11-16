from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 300, scale=10)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=4)

    #svg.plot_function(lambda x: 0.5*x+2, color="red", stroke_width=1)
    svg.plot_function(lambda x: -1*x+4, color="blue", stroke_width=1)
    #svg.plot_function(lambda x: x*2-4, color="green", stroke_width=1)
    #svg.plot_function(lambda x: -x*3-4, color="black", stroke_width=1)

    svg.text(-6.5, 4, "y = mx+b", color="black", font_size=8)

    svg.save("plot.svg")


if __name__ == "__main__":
    main()
