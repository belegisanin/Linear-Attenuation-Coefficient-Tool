welcome_msg = "#" * 50 + "\nLinear Attenuation Coefficient Calculation, Visualisation and Analysis Tool.\n" + "#" * 50
measurements = []


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
