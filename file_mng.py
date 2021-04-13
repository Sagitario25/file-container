import os
import zipfile

class Manager:
	def __init__ (self, archivePath):
		self.archivePath = archivePath
		if not os.path.exists (self.archivePath):
			zipfile.ZipFile (self.archivePath, "w", zipfile.ZIP_DEFLATED).close ()

	def add (self, file):
		with zipfile.ZipFile (self.archivePath, "a", zipfile.ZIP_DEFLATED) as zip:
			if not file [1] == ":":#If the path isnt absolute
				raise Exception ("Priveded path must be absolute")
			if len (file.split ('/')) > 1:
				zip.write (file, file.split ('/')[-1])
			else:
				zip.write (file, file.split ('\\')[-1])
	def get (self, file, path):
		with zipfile.ZipFile (self.archivePath, "r", zipfile.ZIP_DEFLATED) as zip:
			zip.extract (file, path)
	
	def reset (self):
		zipfile.ZipFile (self.archivePath, "w", zipfile.ZIP_DEFLATED).close ()


if __name__ == "__main__":
	mng = Manager ("C:/Users/Admin/Desktop/test/stupid.dll")
	mng.add ("C:/Users/Admin/Desktop/Honeygain.exe")
	mng.get ("Honeygain.exe", "C:/Users/Admin/Desktop/test")
	mng.remove ()