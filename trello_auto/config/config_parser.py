# coding=utf-8
"""
Parser to config file containing UI elements value
"""
import configparser as Cp
import sys


class TrelloConfigParser:
    """
    Contains method to parse config file
    """

    def __init__(self, config_name):
        self.config_name = config_name
        self.scp = Cp.SafeConfigParser()
        if not any(self.scp.read(self.config_name)):
            raise IOError("File not found: '%s'" % self.config_name)

    def _section_error(self, err):
        msg = "Error: %s" % err
        msg += "\nFile: '%s'" % self.config_name
        sys.exit(msg)

    def _option_error(self, section, option):
        msg = "Error: Option '%s' not found under section '%s'" % \
              (option, section)
        msg += "\nFile: '%s'" % self.config_name
        sys.exit(msg)

    def _value_error(self, err, section, option):
        msg = "Error: %s" % err
        msg += "\nSection: '%s'" % section
        msg += "\nOption : '%s'" % option
        msg += "\nFile   : '%s'" % self.config_name
        sys.exit(msg)

    def get(self, section, option, **kwargs):
        """Get an option value for a given section.

        parameters
            kwargs: Possible keywords raw=False, vars=None
            - raw=True returns value of option without interpolation
            - If `vars' is provided, it must be a dictionary. The option is
            looked up
            in `vars' (if provided), `section', and in `defaults' in that
            order.

            section: Name of the section under which the option must be
                     searched(case-sensitive)
            option: Name of the option whose value is to be returned
                    (case-insensitive)
        return: Value of the respective option
        """
        try:
            return self.scp.get(section, option, **kwargs)
        except Cp.NoSectionError as err:
            self._section_error(err)
        except Cp.NoOptionError:
            self._option_error(section, option)

    def getboolean(self, section, option):
        """Get the value of option as type bool
        parameter:
            section: Name of the section under which the option must be
                    searched(case-sensitive)
            option: Name of the option whose value is to be returned
                    (case-insensitive)
        return:
            Value of the respective option which is either True/False
        """
        try:
            return self.scp.getboolean(section, option)
        except Cp.NoSectionError as err:
            self._section_error(err)
        except Cp.NoOptionError:
            self._option_error(section, option)
        except ValueError as err:
            self._value_error(err, section, option)

    def getint(self, section, option):
        """Get the value of option as type bool
        parameter :
                section: Name of the section under which the option must be
                        searched(case-sensitive)
                option: Name of the option whose value is to be returned
                        (case-insensitive)
        return: Value of the respective option which is an integer
        """
        try:
            return self.scp.getint(section, option)
        except Cp.NoSectionError as err:
            self._section_error(err)
        except Cp.NoOptionError:
            self._option_error(section, option)
        except ValueError as err:
            self._value_error(err, section, option)
