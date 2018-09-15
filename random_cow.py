#!/usr/bin/python3

from os import environ as environment_variable
import syslog
from random import choice as random_choice

class Cow(object):
	""" An object representing a cow chosen randomly among the files in the cowsay package. """
	def __init__(self, cow_dir = None, cow_name = None):
		self.cow_dir = self.getself.cow_dir()
		self.cow_file = self.getCowFile(self.cow_dir())
		self.cow_name = self.getCow(self.cow_file())
		
	def getself.cow_dir(self):
		""" Determine the directory where the cow files are located. """
		try:
			self.cow_dir = environment_variable['self.cow_dir']
			if len(self.cow_dir) is 0: raise KeyError
		except KeyError:
			syslog.syslog(syslog.LOG_ERR, "self.cow_dir environment variable is unset or empty. Trying default path...")
			pass

		try:
			self.cow_dir = "/usr/share/cowsay/cows"
			assert os.path.exists(self.cow_dir) and os.path.isdir(self.cow_dir) and os.listdir(self.cow_dir) is not []
		except AssertionError:
				errorMessage = "".join(["Directory containing cows could not be found in environment variables, ",
				"and the default directory to look for cows (" + 'self.cow_dir' + ") does not exist, ",
				"is not a directory, or is empty. Consider reinstalling the cowsay package. Or, ",
				"if you are on a Debian based system, use the Synaptic GUI application to find the cowsay package ",
				"and check where it is installed. Alternatively, try the dpkg-reconfigure command."])
			syslog.syslog(syslog.LOG_ERR, errorMessage)
			raise SystemExit(errorMessage)
