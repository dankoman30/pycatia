#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.collection import Collection
from pycatia.system_interfaces.setting_controller import SettingController


class SettingControllers(Collection):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SettingControllers
                | 
                | A collection of all the setting controllers objects currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_controllers = com_object

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATBSTR iIndex) As SettingController
                | 
                |     Returns a setting controller using its name from the setting controllers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The name of the window to retrieve from the collection of setting
                |             controller. As a string. 
                | 
                |     Returns:
                |         The retrieved setting controller.

        :param str i_index:
        :return: SettingController
        """
        return SettingController(self.setting_controllers.Item(i_index))

    def __repr__(self):
        return f'SettingControllers(name="{ self.name }")'