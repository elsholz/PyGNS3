from pygns3.Graphics import *
from pygns3.Nodes import *
import websockets


class GNS3Project:
    """A project is a collection of nodes, links, drawings and snapshots."""

    def __init__(self, project_id):
        self.project_id = project_id
        self._load_settings()
        # why not do the following inline? Why create another variable with a differnet name?
        self._drawings = GNS3API.get_request(f'/projects/{self.project_id}/drawings').json()
        self.drawings = [GNS3Drawing(d) for d in self._drawings]
        self._links = GNS3API.get_request(f'/projects/{self.project_id}/links').json()
        # print('This it self.links:\n')
        # print(len(self._links))
        self.links = [GNS3Link(l) for l in self._links]
        self._nodes = GNS3API.get_request(f'/projects/{self.project_id}/nodes').json()
        self.nodes = [GNS3Node(n) for n in self._nodes]
        self._snapshots = GNS3API.get_request(f'/projects/{self.project_id}/snapshots').json()
        self.snapshots = [GNS3Snapshot(s) for s in self._snapshots]

    def __repr__(self):
        return f'GNS3Project(\'{self.project_id}\')'

    def __str__(self):
        max_key_width = max(map(len, self._response.keys()))
        setting_items = [f'    {k:{max_key_width}} {v}' for k, v in self._response.items()]
        settings = '\n'.join(setting_items) + '\n'
        return ('GNS3Project settings:\n' + settings + ''
                                                       f'    drawings     {len(self.drawings)}\n'
                                                       f'    links        {len(self.links)}\n'
                                                       f'    nodes        {len(self.nodes)}\n'
                                                       f'    snapshots    {len(self.snapshots)}\n')

    @classmethod
    def create(cls, name, **kwargs):
        """Create a new project.

        Requires a name, additional properties may be given through **kwargs
        Returns a GNS3Project instance"""
        data = {'name': name}
        data.update(kwargs)
        response = GNS3API.post_request('/projects', json.dumps(data))

        if response.status_code == 201:
            project_id = json.loads(response.content)['project_id']
            return GNS3Project(project_id)
        else:
            msg = json.loads(response.content)['message']
            raise ValueError(msg)

    def delete(self):
        """Delete the project from the compute"""
        response = GNS3API.delete_request(f'/projects/{self.project_id}')
        if response.status_code == 404:
            msg = json.loads(response.content)['message']
            raise ValueError(msg)

    def _load_settings(self):
        response = GNS3API.get_request(f'/projects/{self.project_id}')
        if GNS3API.console_log_level == GNS3API.DEBUG:
            print(response.__dict__)
        if response.ok:
            self._response = response.json()
            self.__dict__.update(Struct(**self._response).__dict__)

    def add_drawing(self, drawing: GNS3Drawing):
        """adds a drawing to the project"""
        # TODO implement add_drawing
        pass

    def add_link(self, link: GNS3Link):
        """adds a link to the project"""
        # TODO implement add_link
        pass

    def add_snapshot(self, name):
        """Takes a snapshot of the project"""
        # TODO implement add_snapshot
        pass

    def close(self):
        """closes a project"""
        GNS3API.post_request(f'/projects/{self.project_id}/close', data={})
        self._load_settings()

    @staticmethod
    def load(path):
        """loads a project (local only)"""
        # TODO this needs to be more robust / x-platform with libpath or something
        # TODO Investigate what this does precisely and check for  dual (unload)
        data = {"path": path}
        response = GNS3API.post_request(f'/projects/load', data=data)
        if not response.ok:
            raise Exception('Unable to open project')

    def open(self):
        """opens a project"""
        GNS3API.post_request(f'/projects/{self.project_id}/open', data={})
        self._load_settings()

    def start_all_nodes(self):
        """Start all nodes in a project"""
        GNS3API.post_request(f'/projects/{self.project_id}/nodes/start', data={})
        self._load_settings()
        if GNS3API.console_log_level == GNS3API.DEBUG:
            print('All nodes have been started.')

    def stop_all_nodes(self):
        """Stop all nodes in a project"""
        GNS3API.post_request(f'/projects/{self.project_id}/nodes/stop', data={})
        self._load_settings()
        if GNS3API.console_log_level == GNS3API.DEBUG:
            print('All nodes have been stopped.')

    def suspend_all_nodes(self):
        """Suspend all nodes in a project"""
        GNS3API.post_request(f'/projects/{self.project_id}/nodes/suspend', data={})
        self._load_settings()
        if GNS3API.console_log_level == GNS3API.DEBUG:
            print('All nodes have been suspended.')

    @classmethod
    def import_project(cls, project_id):
        """import a project"""
        # TODO Implement import_project function
        res = GNS3API.post_request(path=f'/projects/{project_id}/import', data={})
        if res.ok:
            return cls(project_id)
        else:
            raise Exception(f'Project could not be imported. E: {res.status_code}')

    def export(self):
        """export a project"""
        # TODO Implement export function
        res = GNS3API.get_request(f'/projects/{self.project_id}/export')
        if res.ok:
            return json.loads(res)
        else:
            raise Exception(f'Exporting project failed. E: {res.status_code}')

    def duplicate(self, **kwargs):
        """duplicate a project"""
        # TODO Implement duplicate function
        assert 'name' in kwargs.keys(), 'The name for the duplicate must be specified'
        res = GNS3API.post_request(f'/projects/{self.project_id}/duplicate', data=json.dumps(kwargs))
        if res.ok:
            return GNS3Project(json.loads(res.content)['project_id'])
        else:
            raise Exception(f'The project could not be duplicated. E: {res.status_code}')

    def get_file(self, file):
        """Get a file from a project. Beware you have warranty to be able to access only to file
        global to the project (for example README.txt)
        """
        # TODO Implement get_file function
        res = GNS3API.get_request(path=f'/projects/{self.project_id}/files/{file}')
        if res.ok:
            return json.loads(res.content)
        else:
            raise Exception(f'The file could not be read. E: {res.content, res.status_code}')

    def write_file(self, file_path, content):
        """Write a file to a project"""
        # TODO Implement write_file function
        # Question: Doesn't the file need some content to be written to it?
        res = GNS3API.post_request(path=f'/projects/{self.project_id}/files/{file_path}', data=json.dumps({'content': content}))
        if res.ok:
            return
        else:
            raise Exception(f'File could not be written. E: {res.content, res.status_code}')

    @classmethod
    def from_name(cls, name):
        """Returns a GNS3Project with `name`"""

        response = GNS3API.get_request('/projects')
        all_projects = response.json()
        for p in all_projects:
            if p['name'] == name:
                # TODO check if project is opened in Controller
                # Problem: No way to access controller yet.
                # for exp in .projects:
                #    if exp.project_id == p['project_id']:
                #        return exp
                return cls(p['project_id'])

        raise FileNotFoundError(f'No project found with name {name}')

    # TODO check out notifications and how to implement
    async def get_notifications(self):
        async with websockets.connect(f'/v2/projects/{self.project_id}/notifications/ws') as ws:
            notification = await ws.recv()
            return notification


class GNS3Snapshot:
    """Project snapshot"""

    def __init__(self, snapshot):
        self._snapshot = snapshot
        self.project_id = snapshot['project_id']
        self.snapshot_id = snapshot['snapshot_id']
        self.__dict__.update(Struct(**snapshot).__dict__)

    def __str__(self):
        max_key_width = max(map(len, self._snapshot.keys()))
        items = [f'    {k:{max_key_width + 1}} {v}' for k, v in self._snapshot.items()]
        settings = '\n'.join(items) + '\n'
        return 'GNS3Snapshot settings:\n' + settings + ''

    def __repr__(self):
        return f'GNS3Snapshot({self._snapshot})'


import json
from pygns3.Struct import Struct
