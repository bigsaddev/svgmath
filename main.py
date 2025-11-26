from lib.svgmath import SVGMath

def main():
    svg = SVGMath(400, 400, scale=25, centered=True)

    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=12)

    functions = [
        #(lambda x: x*2+2, "green"),
        #(lambda x: -2*x+5, "blue"),
        (lambda x: 2*x+3, "red"),
        (lambda x: -x+6, "blue"),
    ]

    for func, color in functions:
        svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.map_coord(1, 5, color="black", radius=4, font_size=14, text="Schnittpunkt: ")
    svg.text(-6, 5, "y=2x+3", font_size=14, color="red")
    svg.text(-6, 2, "y=-x+6", font_size=14, color="blue")

    svg.save("website/images/schnittpunkt.svg")


if __name__ == "__main__":
    main()
