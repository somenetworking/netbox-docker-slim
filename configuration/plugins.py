# # Add your plugins and plugin settings here.
# # Of course uncomment this file out.

# # To learn how to build images with your required plugins
# # See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins 'netbox_topology_views',

#'netbox_secrets'
PLUGINS = ['slurpit_netbox','validity','netbox_kea','nb_risk','netbox_reorder_rack','netbox_floorplan','phonebox_plugin','netbox_dns','netbox_inventory','netbox_topology_views','netbox_bgp','netbox_lifecycle','netbox_acls']
# PLUGINS = ['phonebox_plugin', 'netbox_topology_views',
#            'netbox_dns','netbox_proxbox',
#            'netbox_bgp','netbox_floorplan',
#            'netbox_reorder_rack',
#            'nb_risk','netbox_secrets',
#            'netbox_inventory',
#            'netbox_kea','netbox_lifecycle',
#            'validity','slurpit_netbox']
PLUGINS_CONFIG = {
    # 'netbox_secrets':{ 
    #     'top_level_menu': True,
    #     'enable_contacts': True,
    #     'apps':[
    #         'dcim.device',
    #         'dcim.platform',
    #         'virtualization.virtualmachine',
    #     ]
    #     },
    'nb_risk':{
        'additional_assets': [
            'dcim.platform']
        },
    'netbox_bgp':{
        'top_level_menu': 'True'
        },
     "netbox_acls": {
        "top_level_menu": True
     },
    'netbox_topology_views': {
        'static_image_directory': 'netbox_topology_views/img',
        'allow_coordinates_saving': True,
        'always_save_coordinates': True
    },
    'netbox_inventory': {'used_status_name':'used',
                      'stored_status_name':'stored',
                      'sync_hardware_serial_asset_tag':'True',
                      'asset_import_create_purchase':'True',
                      'asset_import_create_device_type':'True',
                      'asset_import_create_module_type':'True',
                      'asset_import_create_inventoryitem_type':'True',
                      'asset_import_create_tenant':'True'}
}
# PLUGINS_CONFIG = {
#     # 'netbox_proxbox': {
#     #     'proxmox': 
#     #         {
#     #             'domain': '10.0.0.0',    # May also be IP address
#     #             'http_port': 8006,
#     #             'user': 'netbox-ex@pam',   # always required
#     #             # 'password': '', # only required, if you don't want to use token based authentication
#     #             'token': {
#     #                 'name': 'netbox-ex',	# Only type the token name and not the 'user@pam:tokenID' format
#     #                 'value': ''
#     #             },
#     #             'ssl': False
#     #         },
#         'netbox': {
#             'domain': 'netbox',     # Ensure localhost is added to ALLOWED_HOSTS
#             'http_port': 8080,     # Gunicorn port.
#             'token': 'd049f844897628854353359f4157bedabf01cf04',
#             'ssl': False,	# There is no support to SSL on Netbox yet, so let it always False.
#             'settings': {
#                 'virtualmachine_role_id' : 0,
#                 'node_role_id' : 0,
#                 'site_id': 0
#             }
#       }
# #  }
# ,'netbox_inventory': {'used_status_name':'used',
#                       'stored_status_name':'stored',
#                       'sync_hardware_serial_asset_tag':'True',
#                       'asset_import_create_purchase':'True',
#                       'asset_import_create_device_type':'True',
#                       'asset_import_create_module_type':'True',
#                       'asset_import_create_inventoryitem_type':'True',
#                       'asset_import_create_tenant':'True'}

