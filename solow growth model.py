import numpy as np
import matplotlib.pyplot as plt


def simulate(initial: float, period: int, s_vec: np.array, a=0.5, d=0.15, n=0.01, g=0.02):

    k_vec = np.ones(period+1)
    k_vec[0] = initial
    speed_vec = np.ones(period)

    for ii in range(0, period):
        s = s_vec[ii]
        k_star = (s/(n+g+d))**2
        k = k_vec[ii]

        k_change = s*(k**a) - (n+g+d)*k
        speed_vec[ii] = (k_change)/(k_star-initial)
        # the definition of convergence speed is a little confusing.
        # the question emphasized that "every period", so I choose this formular.
        k_vec[ii+1] = (1-n-g-d)*k + s*(k**a)

    return k_vec[:-1], speed_vec


def draw(k_vec: np.array, speed_vec: np.array):
    fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax1.plot(k_vec, "-b")
    ax1.set_ylabel("per capital")
    ax1.set_xlabel("period")
    ax2.plot(speed_vec, "-r")
    ax2.set_ylabel("speed of convergence")
    ax2.set_xlabel("period")

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':

    # question a and b
    initial = 1
    period = 25
    s_vec = np.ones(period)*0.4
    k_vec_1, speed_vec_1 = simulate(initial=initial, period=period, s_vec=s_vec)
    draw(k_vec_1, speed_vec_1)

    # question c
    period = 75
    s_vec = np.ones(period)
    s_vec[:25] = 0.4
    s_vec[25:50] = 0.5
    s_vec[50:] = 0.3
    k_vec_2, speed_vec_2 = simulate(initial=initial, period=period, s_vec=s_vec)
    draw(k_vec_2, speed_vec_2)
