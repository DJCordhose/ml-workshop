fig, ax = plt.subplots(2, sharex='all', figsize=(10, 5))

ax[0].plot(t, s)
ax[0].set_ylabel('voltage (mV)')
ax[0].set_title('Linear')
ax[0].grid(True)
ax[0].set_yscale('linear')

ax[1].plot(t, s)
ax[1].set_xlabel('time (s)')
ax[1].set_ylabel('voltage (mV)')
ax[1].set_title('Log')
ax[1].grid(True)
ax[1].set_yscale('log')

fig.savefig("two-subplots.png")