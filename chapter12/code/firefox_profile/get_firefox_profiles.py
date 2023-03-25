from firefox_profile import FirefoxProfile

for profile in FirefoxProfile.get_profiles():
    recovery_data = profile.get_recovery_data()
    if recovery_data is None:
        continue
    for i, window in enumerate(recovery_data.windows):
        print(f"window {i}")
        print(f"  workspace: {window.workspace}")
        print(f"  zindex: {window.zindex}")
        print(f"  size: {window.size!r}")
        print(f"  position: {window.position!r}")
        print(f"  mode: {window.mode}")
        print(f"  tabs:")
        for j, tab in enumerate(window.tabs):
            print(f"    tab {j}")
            print(f"      url: {tab.url}")
            print(f"      title: {tab.title}")
            print(f"      last_accessed: {tab.last_accessed}")
