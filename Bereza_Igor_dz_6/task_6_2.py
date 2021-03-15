from collections import Counter

with open("nginx_logs.txt", "r", encoding="UTF-8") as f:
    ip_list = []
    for line in f:
        line = line.strip().split('"')
        remote_addr = line[0].split()[0]
        ip_list.append(remote_addr)

ip_spam, count_spam = Counter(ip_list).most_common(1)[0]
print(f"IP спаммера: {ip_spam}, кол-во запросов: {count_spam}")
