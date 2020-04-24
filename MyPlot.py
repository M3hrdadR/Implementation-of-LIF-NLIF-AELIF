import matplotlib.pyplot as plt


def my_plot(bool_marker, no_fig, x_lst, y_lst, title, x_label, y_label, no_subplots, *args):
    plt.figure(no_fig)
    plt.subplot(no_subplots, 1, 1, title=title, xlabel=x_label, ylabel=y_label)
    if bool_marker:
        plt.plot(x_lst, y_lst, marker='o')
    else:
        plt.plot(x_lst, y_lst)
    if no_subplots > 1:
        for i in range(no_subplots - 1):
            plt.subplot(no_subplots, 1, i+2, title=args[5*i + 2], xlabel=args[5*i + 3], ylabel=args[5*i +4])
            plt.plot(args[5*i+0], args[5*i + 1])
    return
