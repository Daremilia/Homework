import numpy as np
import matplotlib.pyplot as plt
import time

time_start = time.time()

beta = 0.95

w_num = 100
w_vec = np.linspace(0.1, 100, w_num)
c_min = (1-beta)*w_vec[0]

e_num = 3
e_vec = np.array([1, 2, 5])
e_matrix = np.array([0.8, 0.1, 0.1, 0.15, 0.7, 0.15,
                    0.2, 0.2, 0.6]).reshape(3, 3)

v_new = np.zeros(shape=[w_num, e_num])
v_old = np.ones(shape=[w_num, e_num])
v_ctr = 0
v_tol = 10**-5

policy = np.zeros(shape=[w_num, e_num], dtype=int)

while np.max(np.abs(v_old-v_new)) > v_tol:
    v_old = np.copy(v_new)
    
    for w_curr in range(w_num):
        current_cake_size = w_vec[w_curr]
        for e_curr in range(e_num):
            current_taste = e_vec[e_curr]
            v_old_expected = v_old @ e_matrix[e_curr].T
            v_new[w_curr, e_curr] = np.max(current_taste*np.log(current_cake_size-w_vec[w_vec <= current_cake_size]+c_min) +
                                           beta*v_old_expected[w_vec <= current_cake_size])
            policy[w_curr, e_curr] = w_vec[np.argmax(current_taste*np.log(current_cake_size-w_vec[w_vec <= current_cake_size]+c_min) +
                                               beta*v_old_expected[w_vec <= current_cake_size])]

    v_ctr += 1

time_end = time.time()

print('Value counter :: ', v_ctr)
print('Time elasped  :: ', time_end-time_start)

fig, [ax1, ax2] = plt.subplots(nrows=1, ncols=2, figsize=[12, 6], sharex=True)

ax1.plot(w_vec, v_old[:, 0], w_vec, v_old[:, 1],
         w_vec, v_old[:, 2], linewidth=0.5)
ax1.legend(["taste = 1", "taste = 2", "taste = 5"])
ax1.set_title("value function")

ax2.plot(w_vec, policy[:, 0], w_vec, policy[:, 1],
         w_vec, policy[:, 2], linewidth=0.5)
ax2.legend(["taste = 1", "taste = 2", "taste = 5"])
ax2.set_title("decision function")

fig.tight_layout()

plt.savefig(
    r"C:\file\汇丰\module - 2\advanced macroeconomics 2\homework\homework 2\figure_1")
