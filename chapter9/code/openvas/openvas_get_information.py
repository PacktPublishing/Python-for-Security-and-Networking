import gvm
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print

# path to unix socket
path = '/var/lib/docker/volumes/greenbone-community-edition_gvmd_socket_vol/_data/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeTransform()

    
with Gmp(connection, transform=transform) as gmp:
    # Retrieve GMP version supported by the remote daemon
    version = gmp.get_version()
    print(version)

    # Prints the XML in beautiful form
    pretty_print(version)

    # Login
    gmp.authenticate('admin', 'admin')

    users = gmp.get_users()
    tasks = gmp.get_tasks()
    targets = gmp.get_targets()
    scanners = gmp.get_scanners()
    configs = gmp.get_scan_configs()
    feeds = gmp.get_feeds()
    nvts = gmp.get_nvts()
    print("Users\n------------")
    for user in users.xpath('user'):
    	print(user.find('name').text)
    print("\nTasks\n------------")
    for task in tasks.xpath('task'):
    	print(task.find('name').text)
    print("\nTargets\n-------------")
    for target in targets.xpath('target'):
    	print(target.find('name').text)
    	print(target.find('hosts').text)
    print("\nScanners\n-------------")
    for scanner in scanners.xpath('scanner'):
    	print(scanner.find('name').text)
    print("\nConfigs\n-------------")
    for config in configs.xpath('config'):
    	print(config.find('name').text)
    print("\nFeeds\n-------------")
    for feed in feeds.xpath('feed'):
    	print(feed.find('name').text)
    print("\nNVTs\n-------------")
    for nvt in nvts.xpath('nvt'):
    	print(nvt.attrib.get('oid'),"-->",nvt.find('name').text)       
