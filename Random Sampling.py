from types import FunctionType
import numpy as np
import matplotlib.pyplot as plt


def sampling(times: int, sample_size: int):
    result_li = [np.random.uniform(0, 1, sample_size) for ii in range(times)]
    return result_li


def standardize(sample):
    mean = 1/2
    std = ((1/12)/len(sample))**0.5
    return (sample-mean)/std


def get_mean(sample: np.array):
    return np.mean(sample)


def get_mean_li(sample_li: list):
    return np.array([get_mean(sample=sample) for sample in sample_li])


def draw(trans_name: str, data_li: list, N_li: list):
    ax_num = len(data_li)
    figsize = (4.3*ax_num, ax_num)

    fig, axs = plt.subplots(nrows=1, ncols=ax_num,
                            figsize=figsize, sharex=True, sharey=True)
    fig.suptitle("transformation: %s" % trans_name, fontsize=20)

    task_li = zip(axs, data_li, N_li)

    for task in task_li:
        task[0].hist(task[1], bins=25)
        task[0].set_title("N=%d" % task[2])

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    R = 300
    N1, N2, N3 = 10, 100, 500
    N_li = [N1, N2, N3]

    def trans_none(x):
        """no transformation"""
        return x

    def trans_square(x):
        """squared transformation"""
        return x**2

    def trans_root(x):
        """square-root transformation"""
        return x**0.5

    trans_li = [trans_none, trans_square, trans_root]

    for trans in trans_li:
        data_li_0 = []
        data_li_1 = []
        name_li = ["sample mean", "standardized sample mean"]

        for N in N_li:
            sample_li = sampling(times=R, sample_size=N)
            standard_sample_li = [standardize(sample) for sample in sample_li]

            sample_mean_li = get_mean_li(sample_li)
            sample_mean_li = trans(sample_mean_li)

            standard_mean_li = get_mean_li(standard_sample_li)
            standard_mean_li = trans(standard_mean_li)

            data_li_0.append(sample_mean_li)
            data_li_1.append(standard_mean_li)

        draw(trans_name=trans.__doc__+"\n" +
             name_li[0], data_li=data_li_0, N_li=N_li)
        draw(trans_name=trans.__doc__+"\n" +
             name_li[1], data_li=data_li_1, N_li=N_li)
