#!/usr/bin/python3

import os.path
import syslog
from os import environ as env
from random import choice as random_choice
from sys import stdin


class RandomCow(object):
    """ An object representing a cow chosen randomly among the files in the cowsay package. """

    def __init__(self):
        self.cow_dir = self.set_cow_dir()
        self.cow_file = self.get_cow_file(self.cow_dir)
        self.cow_name = self.get_cow(self.cow_file)

        self.os_call()  # Finally, call cowsay with our chosen cow

    def set_cow_dir(self):
        """ Determine the directory where the cows are located. """
        # Begin with the default directory
        cow_dir = "/usr/share/cowsay/cows"
        try:
            assert (os.path.exists(cow_dir)  # Check that it exists...
                    and os.path.isdir(cow_dir)  # is a directory...
                    and os.listdir(cow_dir) is not [])  # and that it is not empty)
            return cow_dir
        except AssertionError:
            error_message = "".join(["ASCII files containing cows could not be found because the default directory,",
                                     "(" + cow_dir + ") does not exist, is not a directory, or is empty. ",
                                     "Consider reinstalling the cowsay package. Or, ",
                                     "if you are on a Debian based system, use the Synaptic application to find the ",
                                     "cowsay package  and check where it is installed.",
                                     "Alternatively, try the dpkg-reconfigure command."])
            syslog.syslog(syslog.LOG_ERR, error_message)  # Append to the system log
            print(error_message, "Checking environment variables for the cow directory...", end="\n\n")

        for key in ["COWDIR", 'cowdir', 'cow_dir']:
            try:
                self.cow_dir = env[key]  # This will also raise a KeyError
                if (len(self.cow_dir) is 0) or (not isinstance(env[key], str)):
                    raise KeyError
            except KeyError:
                syslog.syslog(syslog.LOG_ERR,
                              "{env_var_name} environment variable is unset or empty.".format(env_var_name=key))
                raise SystemExit("Unable to find the cow files. Quitting.")

    @staticmethod
    def get_cow_file(cow_dir):
        """ Choose a random cow ASCII file. """
        error_message = "Undefined search directory"
        try:
            if cow_dir is None or len(cow_dir) is 0:
                raise Exception(error_message)
        except NameError:
            raise SystemExit(error_message)
        # Force absolute path
        cow_dir = os.path.realpath(cow_dir)
        cows = os.listdir(cow_dir)
        cow_file = random_choice(cows)
        cow_file_path = os.path.join(cow_dir, os.path.basename(cow_file))
        return cow_file_path

    @staticmethod
    def get_cow(filename):
        return filename.split(os.path.extsep)[0]

    def os_call(self):
        command = "/usr/games/cowsay -f {0}".format(self.cow_file)
        with os.popen(command, mode='w') as pipe:
            pipe.write(stdin.read())


if __name__ == '__main__':
    r = RandomCow()
