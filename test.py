from lib.svgmath import SVGMath

def main():
    svg = SVGMath(800, 800, scale=10, centered=True)
    svg.axis()
    svg.grid(spacing=1, color="#eee", stroke_width=0.5)
    svg.ticks(spacing=1, font_size=8)

    functions = [
        (lambda x: x*2+5, "green"),
        (lambda x: x*1.5+10, "blue"),
    ]

    for func, color in functions:
        svg.plot_function(func, color, stroke_width=1.5, step=0.5)

    svg.save("test.svg")

if __name__ == "__main__":
    main()
