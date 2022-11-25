import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from pltstyle import make_axs, add_inset, ls_main

opinions_end = False
convergence = False
accuracy = False
plot_dual = False
opinion_track = True

if opinions_end:
    # Plot number of unique opinions at the end of each simulation run against k
    data1 = pd.read_csv("data/eps3_ev5_ops.csv", header=None).to_numpy()
    # data1a = pd.read_csv("data/eps4_ev5_strat_error.csv", header=None).to_numpy()
    # data1sd = pd.read_csv("data/eps4_ev5_stddev.csv", header=None).to_numpy()
    data2 = pd.read_csv("data/eps3_ev1_ops.csv", header=None).to_numpy()
    # data2a = pd.read_csv("data/eps4_ev1_strat_error.csv", header=None).to_numpy()
    # data2sd = pd.read_csv("data/eps4_ev1_stddev.csv", header=None).to_numpy()
    data3 = pd.read_csv("data/eps3_ev05_ops.csv", header=None).to_numpy()
    # data3a = pd.read_csv("data/eps4_ev05_strat_error.csv", header=None).to_numpy()
    # data3sd = pd.read_csv("data/eps4_ev05_stddev.csv", header=None).to_numpy()
    data4 = pd.read_csv("data/eps3_ev01_ops.csv", header=None).to_numpy()
    # data4a = pd.read_csv("data/eps4_ev01_strat_error.csv", header=None).to_numpy()
    # data4sd = pd.read_csv("data/eps4_ev01_stddev.csv", header=None).to_numpy()
    data5 = pd.read_csv("data/eps3_ev005_ops.csv", header=None).to_numpy()
    # data5a = pd.read_csv("data/eps4_ev005_strat_error.csv", header=None).to_numpy()
    # data5sd = pd.read_csv("data/eps4_ev005_stddev.csv", header=None).to_numpy()
    #
    k = np.linspace(3, 98, 97)

    plt.plot(k, data1, label='$r=0.5$', color='tab:blue')
    # plt.plot(k, data1a, linestyle='dashed', color='tab:blue')
    # plt.fill_between(k, np.reshape(data1+data1sd, (97, )), np.reshape(data1-data1sd, (97,)), color='tab:blue', alpha=0.5)
    plt.plot(k, data2, label='$r=0.1$', color='tab:orange')
    # plt.plot(k, data2a, linestyle='dashed', color='tab:orange')
    # plt.fill_between(k, np.reshape(data2+data2sd, (97, )), np.reshape(data2-data2sd, (97,)), color='tab:orange', alpha=0.5)
    plt.plot(k, data3, label='$r=0.05$', color='tab:green')
    # plt.plot(k, data3a, linestyle='dashed', color='tab:green')
    # plt.fill_between(k, np.reshape(data3+data3sd, (97, )), np.reshape(data3-data3sd, (97,)), color='tab:green', alpha=0.5)
    plt.plot(k, data4, label='$r=0.01$', color='tab:red')
    # plt.plot(k, data4a, linestyle='dashed', color='tab:red')
    # plt.fill_between(k, np.reshape(data4+data4sd, (97, )), np.reshape(data4-data4sd, (97,)), color='tab:red', alpha=0.5)
    plt.plot(k, data5, label='$r=0.005$', color='tab:purple')
    # plt.plot(k, data5a, linestyle='dashed', color='tab:purple')
    # plt.fill_between(k, np.reshape(data5+data5sd, (97, )), np.reshape(data5-data5sd, (97,)), color='tab:purple', alpha=0.5)

    plt.xlim(0, 50)
    #
    plt.xlabel('$k$')
    plt.ylabel('No. of Opinions')
    plt.legend(loc='lower right')

    plt.show()

if convergence:
    # Plot the number of timesteps required for the system to converge.
    # If system does not converge, convergence time = 10,000
    data1 = pd.read_csv("data/eps3_ev5_convtime.csv", header=None).to_numpy()
    # data1a = pd.read_csv("data/eps4_ev5_strat_error.csv", header=None).to_numpy()
    # data1sd = pd.read_csv("data/eps4_ev5_stddev.csv", header=None).to_numpy()
    data2 = pd.read_csv("data/eps3_ev1_convtime.csv", header=None).to_numpy()
    # data2a = pd.read_csv("data/eps4_ev1_strat_error.csv", header=None).to_numpy()
    # data2sd = pd.read_csv("data/eps4_ev1_stddev.csv", header=None).to_numpy()
    data3 = pd.read_csv("data/eps3_ev05_convtime.csv", header=None).to_numpy()
    # data3a = pd.read_csv("data/eps4_ev05_strat_error.csv", header=None).to_numpy()
    # data3sd = pd.read_csv("data/eps4_ev05_stddev.csv", header=None).to_numpy()
    data4 = pd.read_csv("data/eps3_ev01_convtime.csv", header=None).to_numpy()
    # data4a = pd.read_csv("data/eps4_ev01_strat_error.csv", header=None).to_numpy()
    # data4sd = pd.read_csv("data/eps4_ev01_stddev.csv", header=None).to_numpy()
    data5 = pd.read_csv("data/eps3_ev005_convtime.csv", header=None).to_numpy()
    # data5a = pd.read_csv("data/eps4_ev005_strat_error.csv", header=None).to_numpy()
    # data5sd = pd.read_csv("data/eps4_ev005_stddev.csv", header=None).to_numpy()
    #
    k = np.linspace(3, 98, 97)

    plt.plot(k, data1, label='$r=0.5$', color='tab:blue')
    # plt.plot(k, data1a, linestyle='dashed', color='tab:blue')
    # plt.fill_between(k, np.reshape(data1+data1sd, (97, )), np.reshape(data1-data1sd, (97,)), color='tab:blue', alpha=0.5)
    plt.plot(k, data2, label='$r=0.1$', color='tab:orange')
    # plt.plot(k, data2a, linestyle='dashed', color='tab:orange')
    # plt.fill_between(k, np.reshape(data2+data2sd, (97, )), np.reshape(data2-data2sd, (97,)), color='tab:orange', alpha=0.5)
    plt.plot(k, data3, label='$r=0.05$', color='tab:green')
    # plt.plot(k, data3a, linestyle='dashed', color='tab:green')
    # plt.fill_between(k, np.reshape(data3+data3sd, (97, )), np.reshape(data3-data3sd, (97,)), color='tab:green', alpha=0.5)
    plt.plot(k, data4, label='$r=0.01$', color='tab:red')
    # plt.plot(k, data4a, linestyle='dashed', color='tab:red')
    # plt.fill_between(k, np.reshape(data4+data4sd, (97, )), np.reshape(data4-data4sd, (97,)), color='tab:red', alpha=0.5)
    plt.plot(k, data5, label='$r=0.005$', color='tab:purple')
    # plt.plot(k, data5a, linestyle='dashed', color='tab:purple')
    # plt.fill_between(k, np.reshape(data5+data5sd, (97, )), np.reshape(data5-data5sd, (97,)), color='tab:purple', alpha=0.5)

    # plt.ylim(0.0, 0.6)
    #
    plt.xlabel('$k$')
    plt.ylabel('Convergence Time')
    plt.legend(loc='upper right')

    plt.show()

if accuracy:
    # Plots the average consensus error at the end of the simulation against k
    data1a = pd.read_csv("data/eps4_ev5_error.csv", header=None).to_numpy()
    data1sd = pd.read_csv("data/eps4_ev5_stddev.csv", header=None).to_numpy()
    data2a = pd.read_csv("data/eps4_ev1_error.csv", header=None).to_numpy()
    data2sd = pd.read_csv("data/eps4_ev1_stddev.csv", header=None).to_numpy()
    data3a = pd.read_csv("data/eps4_ev05_error.csv", header=None).to_numpy()
    data3sd = pd.read_csv("data/eps4_ev05_stddev.csv", header=None).to_numpy()
    data4a = pd.read_csv("data/eps4_ev01_error.csv", header=None).to_numpy()
    data4sd = pd.read_csv("data/eps4_ev01_stddev.csv", header=None).to_numpy()
    data5a = pd.read_csv("data/eps4_ev005_error.csv", header=None).to_numpy()
    data5sd = pd.read_csv("data/eps4_ev005_stddev.csv", header=None).to_numpy()

    data6a = pd.read_csv("data/eps2_ev5_error.csv", header=None).to_numpy()
    data6sd = pd.read_csv("data/eps2_ev5_stddev.csv", header=None).to_numpy()
    data7a = pd.read_csv("data/eps2_ev1_error.csv", header=None).to_numpy()
    data7sd = pd.read_csv("data/eps2_ev1_stddev.csv", header=None).to_numpy()
    data8a = pd.read_csv("data/eps2_ev05_error.csv", header=None).to_numpy()
    data8sd = pd.read_csv("data/eps2_ev05_stddev.csv", header=None).to_numpy()
    data9a = pd.read_csv("data/eps2_ev01_error.csv", header=None).to_numpy()
    data9sd = pd.read_csv("data/eps2_ev01_stddev.csv", header=None).to_numpy()
    data10a = pd.read_csv("data/eps2_ev005_error.csv", header=None).to_numpy()
    data10sd = pd.read_csv("data/eps2_ev005_stddev.csv", header=None).to_numpy()
    #
    k = np.linspace(3, 98, 97)

    #
    # plt.plot(k, data1a, linestyle='solid', color='tab:blue', label='$r=0.5$')
    # plt.fill_between(k, np.reshape(data1a+data1sd, (97, )), np.reshape(data1a-data1sd, (97,)), color='tab:blue', alpha=0.5)
    # plt.plot(k, data2a, linestyle='solid', color='tab:orange', label='$r=0.1$')
    # plt.fill_between(k, np.reshape(data2a+data2sd, (97, )), np.reshape(data2a-data2sd, (97,)), color='tab:orange', alpha=0.5)
    # plt.plot(k, data3a, linestyle='solid', color='tab:green', label='$r=0.05$')
    # plt.fill_between(k, np.reshape(data3a+data3sd, (97, )), np.reshape(data3a-data3sd, (97,)), color='tab:green', alpha=0.5)
    # plt.plot(k, data4a, linestyle='solid', color='tab:red', label='$r=0.01$')
    # plt.fill_between(k, np.reshape(data4a+data4sd, (97, )), np.reshape(data4a-data4sd, (97,)), color='tab:red', alpha=0.5)
    # plt.plot(k, data5a, linestyle='solid', color='tab:purple', label='$r=0.005$')
    # plt.fill_between(k, np.reshape(data5a+data5sd, (97, )), np.reshape(data5a-data5sd, (97,)), color='tab:purple', alpha=0.5)
    #
    # #
    # plt.xlabel('$k$')
    # plt.ylabel('Average Error')
    # plt.legend(loc='lower right')
    plt.rcParams['font.family'] = 'serif'
    fig, axs = plt.subplots(2, 1, figsize=(8, 5.5))
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.97, top=0.95)

    axs[0].plot(k, data1a, linestyle='solid', color='tab:blue', label='$r=0.5$')
    axs[0].fill_between(k, np.reshape(data1a+data1sd, (97, )), np.reshape(data1a-data1sd, (97,)), color='tab:blue',
                        alpha=0.5)
    axs[0].plot(k, data2a, linestyle='solid', color='tab:orange', label='$r=0.1$')
    axs[0].fill_between(k, np.reshape(data2a+data2sd, (97, )), np.reshape(data2a-data2sd, (97,)), color='tab:orange',
                        alpha=0.5)
    axs[0].plot(k, data3a, linestyle='solid', color='tab:green', label='$r=0.05$')
    axs[0].fill_between(k, np.reshape(data3a+data3sd, (97, )), np.reshape(data3a-data3sd, (97,)), color='tab:green',
                        alpha=0.5)
    axs[0].plot(k, data4a, linestyle='solid', color='tab:red', label='$r=0.01$')
    axs[0].fill_between(k, np.reshape(data4a+data4sd, (97, )), np.reshape(data4a-data4sd, (97,)), color='tab:red',
                        alpha=0.5)
    axs[0].plot(k, data5a, linestyle='solid', color='tab:purple', label='$r=0.005$')
    axs[0].fill_between(k, np.reshape(data5a+data5sd, (97, )), np.reshape(data5a-data5sd, (97,)), color='tab:purple',
                        alpha=0.5)

    axs[0].set_title('$\epsilon=0.4$')
    axs[0].set_ylabel('Average Error', fontsize=15)

    axs[1].plot(k, data6a, linestyle='solid', color='tab:blue', label='$r=0.5$')
    axs[1].fill_between(k, np.reshape(data6a + data6sd, (97,)), np.reshape(data6a - data6sd, (97,)), color='tab:blue',
                     alpha=0.5)
    axs[1].plot(k, data7a, linestyle='solid', color='tab:orange', label='$r=0.1$')
    axs[1].fill_between(k, np.reshape(data7a + data7sd, (97,)), np.reshape(data7a - data7sd, (97,)), color='tab:orange',
                     alpha=0.5)
    axs[1].plot(k, data8a, linestyle='solid', color='tab:green', label='$r=0.05$')
    axs[1].fill_between(k, np.reshape(data8a + data8sd, (97,)), np.reshape(data8a - data8sd, (97,)), color='tab:green',
                     alpha=0.5)
    axs[1].plot(k, data9a, linestyle='solid', color='tab:red', label='$r=0.01$')
    axs[1].fill_between(k, np.reshape(data9a + data9sd, (97,)), np.reshape(data9a - data9sd, (97,)), color='tab:red',
                     alpha=0.5)
    axs[1].plot(k, data10a, linestyle='solid', color='tab:purple', label='$r=0.005$')
    axs[1].fill_between(k, np.reshape(data10a + data10sd, (97,)), np.reshape(data10a - data10sd, (97,)), color='tab:purple',
                     alpha=0.5)

    axs[1].set_title('$\epsilon=0.2$')
    axs[1].set_ylabel('Average Error', fontsize=15)
    axs[1].set_xlabel('$k$', fontsize=15)
    axs[1].legend(loc='lower right')

    plt.show()

if plot_dual:
    # Plot the average error of all beliefs and number of unique opinions against k
    # at the end of each simulation run.
    data1 = pd.read_csv("data/eps4_ev5_error.csv", header=None).to_numpy()
    data1a = pd.read_csv("data/eps4_ev5_ops.csv", header=None).to_numpy()
    data2 = pd.read_csv("data/eps4_ev1_error.csv", header=None).to_numpy()
    data2a = pd.read_csv("data/eps4_ev1_ops.csv", header=None).to_numpy()
    data3 = pd.read_csv("data/eps4_ev05_error.csv", header=None).to_numpy()
    data3a = pd.read_csv("data/eps4_ev05_ops.csv", header=None).to_numpy()
    data4 = pd.read_csv("data/eps4_ev01_error.csv", header=None).to_numpy()
    data4a = pd.read_csv("data/eps4_ev01_ops.csv", header=None).to_numpy()
    data5 = pd.read_csv("data/eps4_ev005_error.csv", header=None).to_numpy()
    data5a = pd.read_csv("data/eps4_ev005_ops.csv", header=None).to_numpy()

    k = np.linspace(3, 98, 97)

    plt.rcParams.update({'font.size': 13, 'font.family': 'serif'})
    # plt.rcParams['font.family'] = 'serif'
    fig, ax1 = plt.subplots()

    ax1.plot(k, data1, color='tab:blue')
    ax1.plot(k, data2, color='tab:orange')
    ax1.plot(k, data3, color='tab:green')
    ax1.plot(k, data4, color='tab:red')
    ax1.plot(k, data5, color='tab:purple')

    ax1.set_xlabel('$k$')
    ax1.set_ylabel('Average Error')

    ax2 = ax1.twinx()
    ax2.plot(k, data1a, color='tab:blue', linestyle='dashed')
    ax2.plot(k, data2a, color='tab:orange', linestyle='dashed')
    ax2.plot(k, data3a, color='tab:green', linestyle='dashed')
    ax2.plot(k, data4a, color='tab:red', linestyle='dashed')
    ax2.plot(k, data5a, color='tab:purple', linestyle='dashed')

    ax2.set_ylabel('Average No. of Belief Sets')

    plt.title('Noise 0.4')

    plt.show()

if opinion_track:
    # Plots the number of unique opinions in the system over time
    data1 = pd.read_csv("data/k10_eps3_ev1_opinion_track.csv", header=None).to_numpy()
    data2 = pd.read_csv("data/k20_eps3_ev1_opinion_track.csv", header=None).to_numpy()
    data3 = pd.read_csv("data/k30_eps3_ev1_opinion_track.csv", header=None).to_numpy()

    data1a = pd.read_csv("data/k10_eps3_ev01_opinion_track.csv", header=None).to_numpy()
    data2a = pd.read_csv("data/k20_eps3_ev01_opinion_track.csv", header=None).to_numpy()
    data3a = pd.read_csv("data/k30_eps3_ev01_opinion_track.csv", header=None).to_numpy()

    t = range(10000)

    plt.rcParams.update({'font.size': 13, 'font.family': 'serif'})
    fig, axs = plt.subplots(2, 1, figsize=(8, 5.5))
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.97, top=0.95)

    axs[0].plot(t, data1, label='$k=10$')
    axs[0].plot(t, data2, label='$k=20$')
    axs[0].plot(t, data3, label='$k=30$')

    axs[1].plot(t, data1a, label='$k=10$')
    axs[1].plot(t, data2a, label='$k=20$')
    axs[1].plot(t, data3a, label='$k=30$')

    # axs[0].set_xlabel('$k$')
    axs[0].set_ylabel('No. of Unique Belief Sets')
    axs[0].set_title('$r=0.1$')
    axs[1].set_ylabel('No. of Unique Belief Sets')
    axs[1].set_xlabel('$t$')
    axs[1].set_title('$r=0.01$')
    axs[1].legend()

    plt.show()
