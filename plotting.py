plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


def animate(i):
    x = [5, 10, 22, 33, 21]
    y1 = [4, 6, 3, 4, 5]

    plt.cla()

    plt.plot(x, y1, label='Channel 1')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
