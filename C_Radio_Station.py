n, m = map(int, input().split())
    
ip_name = {}
for _ in range(n):
    name, ip = input().split()
    ip_name[ip] = name
    
result = []
for _ in range(m):
    command = input().strip()
    cmd, semicolon = command.split()
    ip = semicolon[:-1] 
    result.append(f"{cmd} {ip}; #{ip_name[ip]}")
    
print("\n".join(result))
