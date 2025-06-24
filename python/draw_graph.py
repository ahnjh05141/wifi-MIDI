import pandas as pd
import matplotlib.pyplot as plt

def analyze(filename):
    df = pd.read_csv(filename, names=["seq", "send_time", "recv_time", "delay"])
    total_sent = df['seq'].max() + 1
    total_recv = len(df)
    loss_rate = 100 * (total_sent - total_recv) / total_sent
    avg_delay = df['delay'].mean()
    jitter = df['delay'].std()
    return avg_delay, jitter, loss_rate

# Analyze both logs
udp_avg, udp_jitter, udp_loss = analyze('udp_recv_log.csv')
tcp_avg, tcp_jitter, tcp_loss = analyze('tcp_recv_log.csv')

# Data for plotting
protocols = ['UDP', 'TCP']
avg_delay = [udp_avg, tcp_avg]
jitter = [udp_jitter, tcp_jitter]
loss_rate = [udp_loss, tcp_loss]

# Plot Average Delay
plt.figure(figsize=(6,4))
plt.bar(protocols, avg_delay)
plt.ylabel('Average Delay (s)')
plt.title('Average Delay by Protocol')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('src/avg_delay.png')

# Plot Jitter
plt.figure(figsize=(6,4))
plt.bar(protocols, jitter)
plt.ylabel('Jitter (s)')
plt.title('Jitter by Protocol')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('src/jitter.png')

# Plot Packet Loss Rate
plt.figure(figsize=(6,4))
plt.bar(protocols, loss_rate)
plt.ylabel('Loss Rate (%)')
plt.title('Packet Loss Rate by Protocol')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('src/loss_rate.png')