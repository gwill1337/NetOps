from pybatfish.client.session import Session
import time

def test_snapshot_parses():
    bf = Session(host="localhost")  # Batfish API на localhost:9996
    NETWORK = "ci_net"

    bf.set_network(NETWORK)
    # Инициализируем snapshot из локальной папки, overwrite=True
    name = bf.init_snapshot("snapshots/ci_net/s1", name="s1", overwrite=True)
    assert name is not None

    # Небольшая пауза, чтобы Batfish успел проанализировать (обычно быстро)
    time.sleep(1)

    res = bf.q.fileParseStatus().answer().frame()
    assert not res.empty
    statuses = [str(s).lower() for s in res["Status"].astype(str).tolist()]
    assert "pass" in statuses, f"no 'pass' in parse statuses: {statuses}"
