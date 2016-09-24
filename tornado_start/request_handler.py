import os

from tornado_start.web import StaticFileHandler, HTTPError


class SmartStaticFileHandler(StaticFileHandler):

    file_finder = None

    def initialize(self, path, default_filename=None):
        self.root = u'<bad root>'


    @classmethod
    def get_absolute_path(cls, root, path):
        return cls.file_finder.get_absolute_path(path)

    def validate_absolute_path(self, root, absolute_path):
        self.file_finder.validate_absolute_path(absolute_path)

        if not os.path.exists(absolute_path):
            raise HTTPError(404)
        if not os.path.isfile(absolute_path):
            raise HTTPError(403, "%s is not a file", self.path)
        return absolute_path


class FileFinder(object):
    def get_absolute_path(self, path):
        raise NotImplementedError()

    def validate_absolute_path(self, path):
        '''
        take care of the fs side problem
        :param path:
        :return:
        '''
        raise NotImplementedError()


class MultiFileFinder(FileFinder):

    def __init__(self, roots, default_root):
        self.roots = tuple(map(os.path.normpath, roots))
        self.default_root = os.path.normpath(default_root)

    def get_absolute_path(self, path):
        for root in self.roots:
            absolute_path = os.path.abspath(os.path.join(root, path))
            if os.path.exists(absolute_path):
                return absolute_path
        return os.path.abspath(os.path.join(self.default_root, path))

    def validate_absolute_path(self, absolute_path):
        for root in self.roots + (self.default_root,):
            if not (absolute_path + os.path.sep).startswith(root):
                continue
            return
        raise HTTPError(403, "%s is not in root static directory", absolute_path)

