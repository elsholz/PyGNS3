# PyGNS3

Python package to interact with [GNS3](http://gns3.com). Usage requires a single call to initialize the GNS3API object.

    $pip install pygns3
    
    >>> from pygns3 import *
    >>> GNS3API.load_configuration()

It leverages the GNS3 built in API and aims to provide some additional functionality such as custom/bulk interaction
with projects and nodes. I have started using GNS3 recently so walking multiple learning curves here. Any ideas /
suggestions / constructive criticism is more than welcome.

For now it is Python 3.6 (I think) only. It is what I use, and it is way too early to start thinking about compatibility
with older versions.

I am using the [API documentation](https://gns3-server.readthedocs.io/en/latest/endpoints.html#controller-api-endpoints)
as a starting point, and implement the Controller endpoints only (for now). The implemented functionality is shown in an
[example Jupyter Notebook](https://github.com/mvdwoord/PyGNS3/blob/master/Example.ipynb).

[The package is available on PyPi](https://pypi.python.org/pypi/PyGNS3) but right now I am still discovering and
changing a lot. Things change and break fast so Github may be more up to date.

## Classes

A number of classes are available once the GNS3API class has been initialized.

### GNS3Controller

is the main component interacting with GNS3. After a successful connection the controller object holds some basic
properties and allows for further inspection and interaction with GNS3.

    >>> print(GNS3Controller())
    
    GNS3 Controller API endpoint
        Host    http://127.0.0.1:3080
        Version 2.0.3
        Running 2 Computes
 
### Other

for now, check the Example jupyter notebook..

## What is the purpose?

As I am learning and working with GNS3 I'm not sure what exactly this should lead to, but the first thing that comes to
mind is parallel commands towards nodes, or other (bulk) manipulations. Not sure what other scenario's will look like
but I guess being able to interact with GNS3 from python could come in handy here or there.

## Issues

At the moment mostly my lack of a complete understanding and familiarity with GNS3. There are some (perceived) 
inconsistencies in the underlying API. Once I have implemented all (or most) classes I will dive deeper and see if I can
clarify.

## Next steps

Implement some sub components and methods on them. Then add some custom functions which operate on multiple nodes or
provide command line visualization. Oh and telnet interaction of course. Perhaps some configuration diffing or
synchronization? who knows.

Plus also perhaps... improvements, error handling, docstrings etc etc etc... and other yak shaving.

# TODO

- [ ] update readme
- [x] remove unused/ deprecated files
- [ ] separate development functionality from end-user functionality
    - [ ] improve logging
    - [ ] enable/ disable developer mode by provision of developer file
- [x] make a list of GNS3 API calls that have been or are yet to be implemented 
- [ ] improve test coverage
    
# Overview of Endpoints and their functionality

List of endpoints copied from [gns3-server documentation](https://gns3-server.readthedocs.io/en/latest/endpoints.html) on 2019-08-22.

### Appliance
| Endpoint | Functionality | status |
|---|---|---|
| `/v2/appliances` | GET: List appliances.  | × |<br>
| `/v2/appliances/templates` | GET: List appliance templates (which can be instantiated). Very detailed. | × |<br>
| `/v2/projects/{project_id}/appliances/{appliance_id}` | POST: Create node from appliance. | × |<br>
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