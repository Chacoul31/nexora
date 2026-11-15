import nexora as nx


def test_info_has_expected_keys():
    info = nx.system.info()
    assert {"platform", "system", "release", "machine", "python", "cpu_count"} <= info.keys()
