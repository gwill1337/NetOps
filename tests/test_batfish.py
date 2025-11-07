#!/usr/bin/env python3
from pybatfish.client.session import Session
import os

# Настройки
bf_address = "127.0.0.1"
snapshot_path = "./snapshots/ci_net/s1"
output_dir = "./output"
network_name = "ci_net"

# Подключение к Batfish
bf = Session(host=bf_address)
bf.set_network(network_name)
bf.init_snapshot(snapshot_path, name="s1", overwrite=True)

os.makedirs(output_dir, exist_ok=True)

# 1. Nodes
nodes_df = bf.q.nodeProperties().answer().frame()
nodes_df.to_csv(f"{output_dir}/nodes.csv")
print("=== Nodes ===")
print(nodes_df)

# 2. Interfaces
interfaces_df = bf.q.interfaceProperties().answer().frame()
interfaces_df.to_csv(f"{output_dir}/interfaces.csv")
print("\n=== Interfaces ===")
print(interfaces_df)

# 3. Filter Line Reachability
try:
    filter_df = bf.q.filterLineReachability().answer().frame()
    filter_df.to_csv(f"{output_dir}/filter_line_reachability.csv")
    print("\n=== Filter Line Reachability ===")
    print(filter_df.head(5))
except Exception as e:
    print("Filter Line Reachability not available:", e)

# 4. BGP Session Compatibility
try:
    bgp_compat_df = bf.q.bgpSessionCompatibility().answer().frame()
    bgp_compat_df.to_csv(f"{output_dir}/bgp_session_compatibility.csv")
    print("\n=== BGP Session Compatibility ===")
    print(bgp_compat_df.head(5))
except Exception as e:
    print("BGP Session Compatibility not available:", e)

# 5. BGP Session Status
try:
    bgp_status_df = bf.q.bgpSessionStatus().answer().frame()
    bgp_status_df.to_csv(f"{output_dir}/bgp_session_status.csv")
    print("\n=== BGP Session Status ===")
    print(bgp_status_df.head(5))
except Exception as e:
    print("BGP Session Status not available:", e)

# 6. BGP Edges
try:
    bgp_edges_df = bf.q.bgpEdges().answer().frame()
    bgp_edges_df.to_csv(f"{output_dir}/bgp_edges.csv")
    print("\n=== BGP Edges ===")
    print(bgp_edges_df.head(5))
except Exception as e:
    print("BGP Edges not available:", e)

# 7. OSPF Session Compatibility
try:
    ospf_df = bf.q.ospfSessionCompatibility().answer().frame()
    ospf_df.to_csv(f"{output_dir}/ospf_session_compatibility.csv")
    print("\n=== OSPF Session Compatibility ===")
    print(ospf_df.head(5))
except Exception as e:
    print("OSPF Session Compatibility not available:", e)

# 8. OSPF Edges
try:
    ospf_edges_df = bf.q.ospfEdges().answer().frame()
    ospf_edges_df.to_csv(f"{output_dir}/ospf_edges.csv")
    print("\n=== OSPF Edges ===")
    print(ospf_edges_df.head(5))
except Exception as e:
    print("OSPF Edges not available:", e)



# #!/usr/bin/env python3
# from pybatfish.client.session import Session
# import os

# # Настройки
# bf_address = "127.0.0.1"
# snapshot_path = "./snapshots/ci_net/s1"
# output_dir = "./output"
# network_name = "ci_net"

# # Подключение к Batfish
# bf = Session(host=bf_address)
# bf.set_network(network_name)
# bf.init_snapshot(snapshot_path, name="s1", overwrite=True)

# os.makedirs(output_dir, exist_ok=True)

# # 1. Node Properties
# nodes_df = bf.q.nodeProperties().answer().frame()
# nodes_df.to_csv(f"{output_dir}/nodes.csv")
# print("=== Nodes ===")
# print(nodes_df)

# # 2. Интерфейсы
# interfaces_df = bf.q.interfaceProperties().answer().frame()
# interfaces_df.to_csv(f"{output_dir}/interfaces.csv")
# print("\n=== Interfaces ===")
# print(interfaces_df)

# # 3. BGP-сессии (замена устаревшего bgpNeighbors)
# try:
#     bgp_sessions_df = bf.q.bgpSession().answer().frame()
#     bgp_sessions_df.to_csv(f"{output_dir}/bgp_sessions.csv")
#     print("\n=== BGP Sessions ===")
#     print(bgp_sessions_df)
# except Exception as e:
#     print("BGP Sessions not available:", e)

# # 4. ACLs
# try:
#     acls_df = bf.q.accessLists().answer().frame()
#     acls_df.to_csv(f"{output_dir}/acls.csv")
#     print("\n=== ACLs ===")
#     print(acls_df)
# except Exception as e:
#     print("ACLs not available:", e)


# #!/usr/bin/env python3
# from pybatfish.client.session import Session
# import os

# # Настройки
# bf_address = "127.0.0.1"
# snapshot_path = "./snapshots/ci_net/s1"
# output_dir = "./output"
# network_name = "ci_net"

# # Подключение к Batfish
# bf = Session(host=bf_address)
# bf.set_network(network_name)
# bf.init_snapshot(snapshot_path, name="s1", overwrite=True)

# # Пример запроса nodeProperties
# res = bf.q.nodeProperties().answer().frame()
# print(res)

# # Сохраняем результат
# os.makedirs(output_dir, exist_ok=True)
# res.to_csv(f"{output_dir}/results.csv")



# #!/usr/bin/env python

# # Modules
# from pybatfish.client.commands import bf_init_snapshot, bf_session
# from pybatfish.question.question import load_questions
# from pybatfish.question import bfq
# import os

# # Variables
# bf_address = "127.0.0.1"
# snapshot_path = "./snapshot"
# output_dir = "./output"

# # Body
# if __name__ == "__main__":
#     # Setting host to connect
#     bf_session.host = bf_address

#     # Loading confgs and questions
#     bf_init_snapshot(snapshot_path, overwrite=True)
#     load_questions()

#     # Running questions
#     r = bfq.nodeProperties().answer().frame()
#     print(r)

#     # Saving output
#     if not os.path.exists(output_dir):
#         os.mkdir(output_dir)

#     r.to_csv(f"{output_dir}/results.csv")

# import time
# from pybatfish.client.session import Session

# def test_snapshot_parses():
#     bf = Session(host="localhost")
#     NETWORK = "ci_net"
#     bf.set_network(NETWORK)

#     # Retry init snapshot несколько раз
#     for _ in range(10):
#         try:
#             name = bf.init_snapshot("snapshots/ci_net/s1", name="s1", overwrite=True)
#             break
#         except FileNotFoundError:
#             time.sleep(1)
#     else:
#         raise RuntimeError("Snapshot folder not found after retries")

#     res = bf.q.fileParseStatus().answer().frame()
#     assert not res.empty
#     statuses = [str(s).lower() for s in res["Status"].astype(str).tolist()]
#     assert "pass" in statuses
