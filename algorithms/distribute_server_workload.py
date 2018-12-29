"""
http://www.codewars.com/kata/distribute-server-workload
"""

def distribute(servers, jobs):
    min_jobs_per_server = jobs // servers

    result = [[] for _ in range(servers)]

    current_job = 0

    for server in range(servers):
        server_jobs = min_jobs_per_server + (jobs % servers > server)
        result[server] = list(range(current_job, current_job + server_jobs))
        current_job += server_jobs

    return result
