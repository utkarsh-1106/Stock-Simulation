# from yahoo_fin import stock_info
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

# brand = input("Enter the company: ")

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Price')

    plt.plot(x, y1, label='Stock 1')
    plt.plot(x, y2, label='Stock 2')
    # price = stock_info.get_live_price(brands)
    # plt.plot(x, price, label='{}'.format(brand))

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()