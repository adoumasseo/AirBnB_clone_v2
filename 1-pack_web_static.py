#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive
    from the contents of the web_static folder of your AirBnB Clone repo,
    using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        This fct make all the work describe in this module doc
    """
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} ./web_static".format(archive_name))
    if result.failed:
        return None
    return "versions/{}".format(archive_name)
