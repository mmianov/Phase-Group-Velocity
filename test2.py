import numpy
import matplotlib.pyplot as plot
import matplotlib.animation as animation

figure = plot.figure()
plot.xlim(0, 2 * numpy.pi), plot.ylim(-4, 4)
line1, = plot.plot([])
line2, = plot.plot([])
line3, = plot.plot([])
group_speed, = plot.plot([], [], marker='o', ls="")
phase_speed, = plot.plot([], [], marker='o', ls="")

A = 1
w1 = 8
w2 = 7
k1 = 12
k2 = 11
vg = (w1-w2)/(k1-k2)
x = numpy.arange(0, 2 * numpy.pi, 0.01)
print(vg)
FPS = 60
group_speed.set_data(0, 2*A)
phase_speed.set_data(0, 0)
def animate(t):

    y1 = A*numpy.cos((w1*t)/FPS - k1*x)
    y2 = A*numpy.cos((w2*t)/FPS - k2*x)
    y3 = y1 + y2
    #line1.set_data(x, y1)
    #line2.set_data(x, y2)
    line3.set_data(x, y3)
    # s = v*t = vg * t
    group_speed.set_data((t % len(x))*vg/FPS, 2*A)
    phase = A*numpy.cos((w2*t)/FPS - k2*x)
    phase_speed.set_data((t % len(x))/FPS, phase)

    return line1,line2, line3, group_speed, phase_speed


wave = animation.FuncAnimation(figure, animate, interval=1/FPS, blit=True)
plot.show()