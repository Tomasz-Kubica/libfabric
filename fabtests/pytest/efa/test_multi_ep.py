import pytest

@pytest.mark.functional
@pytest.mark.parametrize("shared_cq", [True, False])
def test_multi_ep(cmdline_args, shared_cq, fabric):
    from common import ClientServerTest
    cmd = "fi_multi_ep -e rdm"
    if shared_cq:
        cmd += "  -Q"
    test = ClientServerTest(cmdline_args, cmd, fabric=fabric)
    test.run()
