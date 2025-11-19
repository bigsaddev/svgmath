from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=8)

    #functions = [
        #(lambda x: x*2+2, "green"),
        #(lambda x: -2*x+5, "blue"),
        #(lambda x: 2.5*x, "pink"),
        #(lambda x: -x+4, "black"),
    #]

    #for func, color in functions:
        #svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    #svg.text(-6.5, 4, "y = mx+b", color="black", font_size=18)
    #svg.fraction("m = ", "y - b", "x", -4.5, 2, color="black", font_size=18)

    svg.text(-8, 6, "Bestimme die Punkte (x/y)", font_size=14)
    svg.map_blank(1, 4, text="A(_/_)")
    svg.map_blank(-4, 1, text="B(_/_)")
    svg.map_blank(3, 6, text="C(_/_)")
    svg.map_blank(-3, -6, text="D(_/_)")
    svg.map_blank(-2, -4, text="E(_/_)")
    svg.map_blank(-3, 5, text="F(_/_)")
    svg.map_blank(5, -3, text="G(_/_)")

    svg.save("plot4.svg")


if __name__ == "__main__":
    main()
