# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]
PLUGINS = ['phonebox_plugin','netbox_topology_views', 'netbox_dns', 'netbox_proxbox','netbox_bgp']

PLUGINS_CONFIG = {
    'netbox_topology_views': {
        'static_image_directory': 'netbox_topology_views/img',
        'allow_coordinates_saving': True,
        'always_save_coordinates': True
    },
    'netbox_proxbox': {
        'proxmox': 
            {
                'domain': '10.0.0.0',    # May also be IP address
                'http_port': 8006,
                'user': 'netbox-ex@pam',   # always required
                # 'password': '', # only required, if you don't want to use token based authentication
                'token': {
                    'name': 'netbox-ex',	# Only type the token name and not the 'user@pam:tokenID' format
                    'value': ''
                },
                'ssl': False
            },
        'netbox': {
            'domain': 'netbox',     # Ensure localhost is added to ALLOWED_HOSTS
            'http_port': 8080,     # Gunicorn port.
            'token': 'd049f844897628854353359f4157bedabf01cf04',
            'ssl': False,	# There is no support to SSL on Netbox yet, so let it always False.
            'settings': {
                'virtualmachine_role_id' : 0,
                'node_role_id' : 0,
                'site_id': 0
            }
      }
 }
}
# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }
