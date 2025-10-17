import time
from collections import deque
import random

def leaky_bucket_simulator(burst_packets, bucket_capacity, leak_rate):

    bucket = deque()
    dropped_packets = 0
    packets_sent = 0
    
    print("Leaky Bucket Simulation")
    print(f"Bucket Capacity: {bucket_capacity}, Leak Rate: {leak_rate} packets/sec")
    
    start_time = time.time()
    next_leak_time = start_time + 1.0 / leak_rate

    for i, packet in enumerate(burst_packets):
        current_time = time.time()
        
        if len(bucket) < bucket_capacity:
            bucket.append(packet)
            print(f"[{current_time - start_time:.2f}s] Packet {i+1} arrived and was buffered.")
        else:
            dropped_packets += 1
            print(f"[{current_time - start_time:.2f}s] Packet {i+1} arrived, but bucket is full. Dropped.")

        if time.time() >= next_leak_time and len(bucket) > 0:
            sent_packet = bucket.popleft()
            packets_sent += 1
            print(f"[{time.time() - start_time:.2f}s] ➡️ Leaked {sent_packet}.")
            next_leak_time += 1.0 / leak_rate
        
        time.sleep(random.uniform(0.0, 0.2)) 

    while len(bucket) > 0:
        if time.time() >= next_leak_time:
            sent_packet = bucket.popleft()
            packets_sent += 1
            print(f"[{time.time() - start_time:.2f}s] ➡️ Leaked {sent_packet}.")
            next_leak_time += 1.0 / leak_rate
        time.sleep(0.1)

    print(f"\nLeaky Bucket: Total packets dropped = {dropped_packets}")
    print(f"Leaky Bucket: Total packets sent = {packets_sent}")

num_packets = 50
burst_size = 15 
bursty_traffic = []
for i in range(num_packets):
    bursty_traffic.append(f"Pkt_{i+1}")
print("Case 1 :")
leaky_bucket_simulator(bursty_traffic, bucket_capacity=10, leak_rate=8)

print("Case 1 :")
leaky_bucket2simulator(bursty_traffic, bucket_capacity=10, leak_rate=12)

print("Case 3 :")
leaky_bucket_simulator(bursty_traffic, bucket_capacity=10, leak_rate=5)
