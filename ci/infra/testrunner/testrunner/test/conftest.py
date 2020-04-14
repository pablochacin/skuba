def pytest_addoption(parser):
    """
    Adds the option pytest option list.
    This options can be used to initilize fixtures.
    """
    parser.addoption("--vars", action="store", help="vars yaml")
    parser.addoption("--platform", action="store", help="target platform")
    parser.addoption("--skip-setup",
                     choices=['provisioned', 'bootstrapped', 'deployed'],
                     help="Skip the given setup step.\n"
                          "'provisioned' For when you have already provisioned the nodes.\n"
                          "'bootstrapped' For when you have already bootstrapped the cluster.\n"
                          "'deployed' For when you already have a fully deployed cluster.")
