import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

welcome_msg = "#" * 50 + "\nLinear Attenuation Coefficient Calculation, Visualisation and Analysis Tool.\n" + "#" * 50
measurements = []


def generate_axes(ms_data):
    x_ax = y_ax = []
    for dp in ms_data:
        x, y = dp
        x_ax.append(x)
        y_ax.append(y)

    return x_ax, y_ax


def show_plot(measurement_data):
    plt.style.use('_mpl-gallery')
    x_axes, y_axes = generate_axes(measurement_data)

    fig, ax = plt.subplots()

    plt.xlabel("x [cm]")
    plt.ylabel("N [imp/min]")

    #ax.set_xlabel("x [cm]")
    #ax.set_ylabel("N [imp/min]")

    ax.scatter(x_axes, y_axes)
    plt.show()


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
