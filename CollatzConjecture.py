import matplotlib.pyplot as plt

def calculate_steps(number: int, needvisualization=False) -> int:
    """Collatz Conjecture problem: Does the Collatz sequence eventually reach 1 for all positive integer initial values?
    steps: take a positive integer, divide by 2 if its even or multiply it by 3 and increment 1 if odd"""

    totalsteps = 0
    valuechanges = []
    while number > 1:
        if needvisualization: valuechanges.append(number)
        number = (3 * number) + 1 if number % 2 else number / 2
        totalsteps += 1

    valuechanges.append(1)
    if needvisualization:
        plotsteps(totalsteps, valuechanges)
    return totalsteps


def plotsteps(totalsteps, valuechanges):
    steps = [num for num in range(totalsteps + 1)]
    plt.plot(steps, valuechanges, color="blue", linestyle="dotted", marker=".", markersize=10, markerfacecolor="red",
             markeredgecolor="red")
    plt.plot([], [], label=f"max value reached: {max(valuechanges)}")
    plt.plot([], [], label=f"total steps taken: {len(valuechanges)}")
    plt.grid(True)
    plt.xlabel("steps")
    plt.ylabel("value changes")
    plt.title("Collatz Conjecture")
    plt.legend()
    plt.show()


input = 50
print(f"total steps taken for the number: {input} to drop to 1 is: {calculate_steps(input, True)}")
