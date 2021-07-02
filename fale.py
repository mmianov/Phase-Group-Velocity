import numpy
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import sys
# cases
while True:
    case_list = [
        ["1. group velocity > phase velocity", [9, 7, 12, 11]],
        ["2. group velocity < phase velocity", [3, 2, 4, 2]],
        ["3. group velocity = phase velocity", [3, 2, 3, 2]],
        ["4. group velocity = - phase velocity", [2, 5, 5, 2]],
        ["5. group velocity =  0", [2, 2, 2, 5]],
        ["6. phase velocity = 0", [1, -1, 6, 2]]
    ]
    case_len = len(case_list)

    # available cases
    print("---- GROUP AND PHASE VELOCITY --------")
    print("Available cases:")
    print("--------------------------------------")
    for case in case_list:
        print(case[0])
    print("Type 0 to quit.")
    print("--------------------------------------")

    # user input
    while True:
        try:
            n = int(input("Please choose case (1-{}): ".format(case_len)))
            while n - 1 not in range(case_len):
                if n == 0:
                    sys.exit()
                print("Please choose a case from a list above.")
                n = int(input("Please choose case (1-{}): ".format(case_len)))
            break
        except Exception as e:
            print("Invalid input")

    # constants
    GROUP_COLOR = '#0066ff'
    PHASE_COLOR = '#ffa31a'
    A = 1
    w1 = case_list[n - 1][1][0]
    w2 = case_list[n - 1][1][1]
    k1 = case_list[n - 1][1][2]
    k2 = case_list[n - 1][1][3]
    vg = (w1 - w2) / (k1 - k2)
    FPS = 60

    # graph lines and graphs
    figure, (ax1, ax2, ax3) = plot.subplots(3, 1)
    figure.set_size_inches(9, 7)
    line1, = ax1.plot([], [], lw=2)
    line2, = ax2.plot([], [], lw=2, color='r')
    line3, = ax3.plot([], [], lw=2, color='#8000ff')
    line4, = ax3.plot([], [], 'g--', lw=1.5)
    line5, = ax3.plot([], [], 'g--', lw=1.5)
    for ax in [ax1, ax2, ax3]:
        ax.set_ylim(-4, 4)
        ax.set_xlim(0, 2 * numpy.pi)

    ax1.set_title("y1 = cos(w1*t - k1*x)")
    ax2.set_title("y2 = cos(w2*t - k2*x)")
    ax3.set_title("y3 = y1 + y2")
    figure.tight_layout()
    plot.subplots_adjust(bottom=0.1)

    group_speed, = ax3.plot([], [], marker='o', ls="", color=GROUP_COLOR)
    phase_speed, = ax3.plot([], [], marker='o', ls="", color=PHASE_COLOR)
    group_speed.set_data(0, 2 * A)

    # phase speed of wave 1
    vp1 = w1 / k1
    # phase speed of wave 2
    vp2 = w2 / k2
    vp = (w1 + w2) / (k1 + k2)

    # speed display and axis title
    ax3.set_xlabel('x [units]', fontsize=11)
    plot.annotate('Group speed: {}'.format(round(vg, 3)), (0, 0), (0, -35), xycoords='axes fraction',
                  textcoords='offset points', va='top', fontsize=11, color=GROUP_COLOR)
    plot.annotate('Phase speed: {}'.format(round(vp, 3)), (0, 0), (120, -35), xycoords='axes fraction',
                  textcoords='offset points', va='top', fontsize=11, color=PHASE_COLOR)

    # animation
    x = numpy.arange(0, 2 * numpy.pi, 0.01)


    def animate(t):
        y1 = A * numpy.cos((w1 * t) / FPS - k1 * x)
        y2 = A * numpy.cos((w2 * t) / FPS - k2 * x)
        y3 = y1 + y2
        envelope = 2 * A * numpy.cos(((w1 * t) / FPS - (k1 * x) - (w2 * t) / FPS + (k2 * x)) / 2)
        line1.set_data(x, y1)
        line2.set_data(x, y2)
        line3.set_data(x, y3)
        line4.set_data(x, envelope)
        line5.set_data(x, -envelope)

        group_speed.set_data((t * vg / (FPS)) % (2 * numpy.pi), 2 * A)
        phase = 2 * A * numpy.cos((t * (w1 - w2) - vp * t * (k1 - k2)) / (2 * FPS))
        phase_speed.set_data((t * vp / (FPS)) % (2 * numpy.pi), phase)

        return line1, line2, line3, line4, line5, group_speed, phase_speed


    wave = animation.FuncAnimation(figure, animate, interval=1 / FPS, blit=True)
    plot.show()
    print("\n\n")
