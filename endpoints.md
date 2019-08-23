# Overview of Endpoints and their functionality

List of endpoints copied from [gns3-server documentation](https://gns3-server.readthedocs.io/en/latest/endpoints.html) on 2019-08-22.

### Appliance
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/appliances` | List appliances?  | × |<br>
| `/v2/appliances/templates` | List appliance templates (which can be instantiated). Very detailed. | × |<br>
| `/v2/projects/{project_id}/appliances/{appliance_id}` | Create node from appliance. | × |<br>
### Compute
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/computes` | POST: Add compute server by specifying host and port. <br> GET: List compute servers.| × |<br>
| `/v2/computes/endpoint/{compute_id}/{emulator}/{action:.+}` | Experimental. | × |<br>
| `/v2/computes/{compute_id}` | PUT: Get info (with authorization.) <br> GET: Get compute information. <br> DELETE: Delete compute instance.| × |<br>
| `/v2/computes/{compute_id}/auto_idlepc` |  | × |<br>
| `/v2/computes/{compute_id}/{emulator}/{action:.+}` |  | × |<br>
| `/v2/computes/{compute_id}/{emulator}/images` |  | × |<br>
### Drawing
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/drawings` | GET: Gets a list of drawings. <br> POST: Creates a new drawing. | × |<br>
| `/v2/projects/{project_id}/drawings/{drawing_id}` | GET: Get a drawing instance. <br> PUT: Update drawing instance. DELETE: Remove instance. <br>  | × |<br>
### Gns3 vm
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/gns3vm` | GET: Get the GNS3 Settings. <br> PUT: Update the GNS3 Settings. | × |<br>
| `/v2/gns3vm/engines` | GET: Returns list of supported engines, e.g. VirtualBox. | × |<br>
| `/v2/gns3vm/engines/{engine}/vms` | GET: List all available VMs for the selected engine. | × |<br>
### Link
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/links` | GET: Lists all links, which connect nodes. <br> POST: Creates a new Link| × |<br>
| `/v2/projects/{project_id}/links/{link_id}` | GET: Gets link instance <br> PUT: Update link instance. <br> DELETE: Remove link.| × |<br>
| `/v2/projects/{project_id}/links/{link_id}/available_filters` | GET: List of available filters to be applied on the link. | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/pcap` |  | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/start_capture` | POST: Start capture. | × |<br>
| `/v2/projects/{project_id}/links/{link_id}/stop_capture` | POST: Stop capture. | × |<br>
### Node
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/nodes` | POST: Create node instance. <br> GET: List all nodes of a project. | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}` | GET: Get node instance. <br> PUT: Update node instance. <br> DELETE: Remove node. | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/duplicate` | POST: Duplicate specified node at specified position. | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/dynamips/auto_idlepc` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/dynamips/idlepc_proposals` |  | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/files/{path:.+}` | GET: Retrieve file from node directory. POST: Write file to node directory. | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/links` | GET: List links connected to the node. | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/reload` | POST: Reloads node. | × |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/start` | POST: Start node. | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/stop` | POST: Stop node. | ✓ |<br>
| `/v2/projects/{project_id}/nodes/{node_id}/suspend` | POST: Suspends node. | × |<br>
| `/v2/projects/{project_id}/nodes/reload` | POST: Reload all nodes of project. | × |<br>
| `/v2/projects/{project_id}/nodes/start` | POST: Start all nodes of project. | × |<br>
| `/v2/projects/{project_id}/nodes/stop` | POST: Stop all nodes of project. | × |<br>
| `/v2/projects/{project_id}/nodes/suspend` | POST: Suspend all nodes of project. | × |<br>
### Project
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects` | POST: Create new project on server. <br> GET: List projects. | × |<br>
| `/v2/projects/load` | POST: Open project on local server. | ✓ |<br>
| `/v2/projects/{project_id}` | GET: Get project. <br> PUT: Update project. <br> DELETE: Delete project. | ✓ |<br>
| `/v2/projects/{project_id}/close` | POST: Close project. | ✓ |<br>
| `/v2/projects/{project_id}/duplicate` | POST: Duplicate Project. | × |<br>
| `/v2/projects/{project_id}/export` | GET: Export project as portable archive. | × |<br>
| `/v2/projects/{project_id}/files/{path:.+}` | GET: Receive files (up to global directory, it seems.) <br> POST: Write File.| × |<br>
| `/v2/projects/{project_id}/import` | POST: Import Project from portable archive. | × |<br>
| `/v2/projects/{project_id}/notifications` | GET: Receive project notifications. | × |<br>
| `/v2/projects/{project_id}/notifications/ws` | GET: Receive project notifications via a websocket. | × |<br>
| `/v2/projects/{project_id}/open` | POST: Open project. | ✓ |<br>
### Server
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/debug` | POST: Dump debug information to disk. | × |<br>
| `/v2/settings` | GET: Gets server settings. <br> POST: Write settings to server. Don't use. | × |<br>
| `/v2/shutdown` | POST: Shutdown local server. | × |<br>
| `/v2/version` | GET: Receive version. POST: | × |<br>
### Snapshot
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/projects/{project_id}/snapshots` |  | × |<br>
| `/v2/projects/{project_id}/snapshots/{snapshot_id}` |  | × |<br>
| `/v2/projects/{project_id}/snapshots/{snapshot_id}/restore` |  | × |<br>
### Symbol
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/symbols` | GET: Retrieve List of symbols. | × |<br>
| `/v2/symbols/{symbol_id:.+}/raw` | GET: Get symbol file. <br> POST: Write Symbol file. | × |<br>