import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

welcome_msg = "#" * 50 + "\nLinear Attenuation Coefficient Calculation, Visualisation and Analysis Tool.\n" + "#" * 50
measurements = []

test_measurements = [(0, 10), (1, 5), (2, 2.5), (3, 1.25)]


def generate_axes(ms_data):
    x_ax = []
    y_ax = []
    for dp in ms_data:
        x, y = dp
        x_ax.append(x)
        y_ax.append(y)

    return np.array(x_ax), np.array(y_ax)


def show_plot(measurement_data):
    x_axis, y_axis = generate_axes(measurement_data)

    fig, ax = plt.subplots()

    plt.xlabel("x [cm]")
    plt.ylabel("N [imp/min]")
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("N [imp/min]")

    try:
        trendline = np.polyfit(x_axis, np.log(y_axis), 1)
        exp_func = np.exp(trendline[1]) * np.exp(trendline[0] * x_axis)

        plt.plot(x_axis, exp_func, c="#609bd6")
        ax.scatter(x_axis, y_axis, marker="o")
        plt.text(max(x_axis) - 1, max(y_axis) - 1, rf"$f(x)={round(trendline[1], 4)} e^{ {round(trendline[0], 4)} }$",
                 ha="left", va="bottom")

        plt.show()
    except TypeError:
        print("Invalid Input.", "\n")


def measurements_input():
    counter = 0
    while True:
        inp = input(f"Measurement {counter}: ")

        if inp.lower() == "end":
            break

        try:
            abs_thickness, gm_reading = [float(item) for item in inp.split()]
            measurements.append((abs_thickness, gm_reading))
            counter += 1
        except ValueError:
            print("Invalid Input! Format: (Absorber Thickness)[cm] (G-M Counter Reading)[impulses/minute]")
            continue


if __name__ == '__main__':
    print(welcome_msg, "\n")
    print("Input measurements using the following format: (Absorber Thickness)[cm] (G-M Counter Reading)["
          "impulses/minute]")
    print("Enter 'END' to end input.", "\n")

    measurements_input()

    show_plot(measurements)
