import matplotlib.pyplot as plt

def plot_bar_show(d):
    """Displays a bar chart"""
    r = range(0, len(d))
    plt.figure()

    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.tight_layout()
    plt.show()

def plot_pie_show(d):
    """Displays a pie chart"""
    labels = d.keys
    sizes = d.values

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

