# Overview of Endpoints and their functionality

List of endpoints copied from [gns3-server documentation](https://gns3-server.readthedocs.io/en/latest/endpoints.html) on 2019-08-22.

### Appliance
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/appliances` |  | × |<br>
| `/v2/appliances/templates` |  | × |<br>
| `/v2/projects/{project_id}/appliances/{appliance_id}` |  | × |<br>
### Compute
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/computes` |  | × |<br>
| `/v2/computes/endpoint/{compute_id}/{emulator}/{action:.+}` |  | × |<br>
| `/v2/computes/{compute_id}` |  | × |<br>
| `/v2/computes/{compute_id}/auto_idlepc` |  | × |<br>
| `/v2/computes/{compute_id}/{emulator}/{action:.+}` |  | × |<br>
| `/v2/computes/{compute_id}/{emulator}/images` |  | × |<br>
### Drawing
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/drawings` |  | × |<br>
| `/v2/projects/{project_id}/drawings/{drawing_id}` |  | × |<br>
### Gns3 vm
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/gns3vm` |  | × |<br>
| `/v2/gns3vm/engines` |  | × |<br>
| `/v2/gns3vm/engines/{engine}/vms` |  | × |<br>
### Link
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/links` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/available_filters` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/pcap` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/start_capture` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/stop_capture` |  | × |<br>
### Node
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/nodes` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}` |  | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/duplicate` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/dynamips/auto_idlepc` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/dynamips/idlepc_proposals` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/files/{path:.+}` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/links` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/reload` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/start` |  | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/stop` |  | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/suspend` |  | × |<br>
| `/v2/projects/{project_id}/nodes/reload` |  | × |<br>
| `/v2/projects/{project_id}/nodes/start` |  | × |<br>
| `/v2/projects/{project_id}/nodes/stop` |  | × |<br>
| `/v2/projects/{project_id}/nodes/suspend` |  | × |<br>
### Project
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects` |  | × |<br>
| `/v2/projects/load` |  | ✓ |<br>
| `/v2/projects/{project_id}` |  | ✓ |<br>
| `/v2/projects/{project_id}/close` |  | ✓ |<br>
| `/v2/projects/{project_id}/duplicate` |  | × |<br>
| `/v2/projects/{project_id}/export` |  | × |<br>
| `/v2/projects/{project_id}/files/{path:.+}` |  | × |<br>
| `/v2/projects/{project_id}/import` |  | × |<br>
| `/v2/projects/{project_id}/notifications` |  | × |<br>
| `/v2/projects/{project_id}/notifications/ws` |  | × |<br>
| `/v2/projects/{project_id}/open` |  | ✓ |<br>
### Server
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/debug` |  | × |<br>
| `/v2/settings` |  | × |<br>
| `/v2/shutdown` |  | × |<br>
| `/v2/version` |  | × |<br>
### Snapshot
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/snapshots` |  | × |<br>
| `/v2/projects/{project_id}/snapshots/{snapshot_id}` |  | × |<br>
| `/v2/projects/{project_id}/snapshots/{snapshot_id}/restore` |  | × |<br>
### Symbol
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/symbols` |  | × |<br>
| `/v2/symbols/{symbol_id:.+}/raw` |  | × |<br>