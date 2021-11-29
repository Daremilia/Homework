from types import FunctionType
import numpy as np
import matplotlib.pyplot as plt


def sampling(times: int, sample_size: int):
    result_li = [np.random.random(sample_size) for ii in range(times)]
    return result_li


def get_sample_mean(sample: np.array, transformation: FunctionType):
    sample = transformation(sample)
    return np.mean(sample)


def draw(trans_name: str, li: list, N_li: list):
    num = len(li)
    fig, axs = plt.subplots(nrows=1, ncols=num)
    fig.set_size_inches(4*num, num+1)
    fig.suptitle("transformation: %s" % trans_name, fontsize=16)

    task_li = zip(axs, li, N_li)
    for task in task_li:
        task[0].hist(task[1], bins=100)
        task[0].set_title("N=%d" % task[2])
    plt.show()


if __name__ == '__main__':
    R = 300
    N1, N2, N3 = 10, 100, 500
    N_li = [N1, N2, N3]

    def sample_no_transformation(x):
        """no transformation"""
        return x

    def sample_squared(x):
        """squared transformation"""
        return x**2

    def sample_square_root(x):
        """square_root transformation"""
        return x**0.5

    sample_trans_li = [sample_no_transformation,
                       sample_squared, sample_square_root]

    for sample_trans in sample_trans_li:
        array_li = []
        for N in N_li:
            sample_li = sampling(times=R, sample_size=N)
            sample_mean_li = np.array([get_sample_mean(
                sample=sample, transformation=sample_trans) for sample in sample_li])
            array_li.append(sample_mean_li)
        draw(trans_name=sample_trans.__doc__, li=array_li, N_li=N_li)
