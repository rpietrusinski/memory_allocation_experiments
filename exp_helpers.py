from matplotlib import pyplot as plt


def make_double_plot(snapshots):
    plt.figure(figsize=(20, 10))
    plt.suptitle("Summary statistics")

    plt.subplot(1, 2, 1)
    plt.plot(snapshots['memory'], label="Total", c="black")
    plt.plot(snapshots['df_memory'], label="DataFrame", c="red")
    plt.legend()
    plt.title("Total memory allocation in Python process [MB]")
    plt.xlabel("Iter")
    plt.ylabel("Memory alloc [MB]")

    plt.subplot(1, 2, 2)
    plt.plot(snapshots['duration'])
    plt.title("Duration of each iteration [microseconds]")
    plt.xlabel("Iter")
    plt.ylabel("Duration [microseconds]")


def make_single_plot(snapshots):
    fig, ax1 = plt.subplots(figsize=(20, 10))
    plt.title("Summary stats")

    # color = 'tab:red'
    ax1.set_xlabel('iter')
    ax1.set_ylabel('memory alloc')
    ax1.plot(snapshots['memory'], color="black", alpha=0.5)
    ax1.plot(snapshots['df_memory'], color="red", alpha=0.5)
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('duration', color=color)
    ax2.plot(snapshots['duration'], color=color, alpha=0.5)
    ax2.tick_params(axis='y', labelcolor=color)
