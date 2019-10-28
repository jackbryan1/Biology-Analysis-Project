import matplotlib.pyplot as plt

def plot_bar_show(d):
    """Displays a bar chart"""
    r = range(0, len(d))
    plt.figure()

    plt.bar(r, d.values())
    plt.xticks(r, d.keys(), rotation='vertical')
    plt.tight_layout()
    plt.show()

def plot_pie_show(d):
    """Displays a pie chart"""
    labels = d.keys()
    sizes = d.values()

    pie, axis = plt.subplots()
    axis.pie(sizes, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')

    plt.show()

