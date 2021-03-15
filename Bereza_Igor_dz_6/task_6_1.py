with open("nginx_logs.txt", "r", encoding="UTF-8") as f:
    pars_list = []
    for line in f:
        line = line.strip().split('"')
        remote_addr = line[0].split()[0]
        request_type, requested_resource, _ = line[1].split()
        pars_list.append((remote_addr, request_type, requested_resource))

for i in range(5):
    print(pars_list[i])
