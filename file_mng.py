import os
import shutil

def createPath (path):
	dir = os.path.basename (os.path.normpath (path))
	root = path [:-len (dir)]
	if os.path.exists (root):
		os.mkdir (path)
	else:
		createPath (root)

class Manager:
	def __init__ (self, path):
		self.path = path
		if not os.path.exists (self.path):
			createPath (self.path)

	def add (self, src):
		"""Adds to archive"""
		if os.path.isfile (src):
			shutil.copy (src, self.path)
		else:
			shutil.copytree (src, os.path.join (self.path, os.path.basename (src)))

	def get (self, name, outpath):
		"""Exports files and dirs to the desired path"""
		if os.path.isfile (os.path.join (self.path, name)):
			shutil.copy (os.path.join (self.path, name), outpath)
		else:
			shutil.copytree (os.path.join (self.path, name), os.path.join (outpath, name))

	def rm (self, name):
		"""Removes from archive"""
		if os.path.isfile (os.path.join (self.path, name)):
			os.remove (os.path.join (self.path, name))
		else:
			shutil.rmtree (os.path.join (self.path, name))

	def kidnap (self, src):
		"""Adds to archive and deletes original version"""
		self.add (src)
		if os.path.isfile (src):
			os.remove (src)
		else:
			shutil.rmtree (src)

	def getout (self, name, outpath):
		"""Gets put and deletes archive version"""
		self.get (name, outpath)
		self.rm (name)
if __name__ == "__main__":
	mng = Manager (os.path.join (os.getenv ("localappdata"), "escudoweb"))