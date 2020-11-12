"""
This module is specifically intended for use when in environments where
you're actively trying to share/develop tools across multiple applications
which support PyQt, PySide or PySide2. 

The premise is that you can request the main application window using 
a common function regardless of the actual application - making it trivial
to implement a tool which works in multiple host applications without any
bespoke code.

The current list of supported applications are:

    * Native Python
    * Maya
    * 3dsmax
    * Motion Builder

"""
import sys

from ..vendor import Qt


# Python 2/3 compat
# TODO: Use six.
try:
    long

except NameError:
    long = int


# ------------------------------------------------------------------------------
def get_host():

    global HOST

    if HOST:
        pass

    elif ('maya.exe' in sys.executable or
          'mayapy.exe' in sys.executable):
        HOST = 'Maya'

    elif ('motionbuilder.exe' in sys.executable or
          'mobupy.exe' in sys.executable):
        HOST = 'Mobu'

    elif '3dsmax.exe' in sys.executable:
        HOST = 'Max'

    elif any(houdini_exec in sys.executable
             for houdini_exec in ['houdini.exe',
                                  'houdinifx.exe',
                                  'houdinicore.exe']):
        HOST = 'Houdini'

    return HOST


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming
def mainWindow():
    """
    Returns the main window regardless of what the host is
    
    :return: 
    """
    return HOST_MAPPING[get_host()]()


# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences,PyPep8Naming
def returnNativeWindow():
    for candidate in Qt.QtWidgets.QApplication.topLevelWidgets():
        if isinstance(candidate, Qt.QtWidgets.QMainWindow):
            return candidate


# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences,PyPep8Naming
def _findWindowByTitle(title):
    # -- Find the main application window
    for candidate in Qt.QtWidgets.QApplication.topLevelWidgets():
        # noinspection PyBroadException
        try:
            if title in candidate.windowTitle():
                return candidate

        except Exception:
            pass


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming
def returnModoMainWindow():
    pass


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming
def returnMaxMainWindow():
    return _findWindowByTitle('Autodesk 3ds Max')


# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences,PyPep8Naming
def returnMayaMainWindow():
    from maya import OpenMayaUI as omui

    return Qt.QtCompat.wrapInstance(
        long(omui.MQtUtil.mainWindow()),
        Qt.QtWidgets.QWidget,
    )


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming
def returnHoudiniMainWindow():
    import hou
    return hou.qt.mainWindow()


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming
def returnMobuMainWindow():
    return _findWindowByTitle('MotionBuilder 20')


# ------------------------------------------------------------------------------
HOST = None
HOST_MAPPING = {
    None: returnNativeWindow,
    'Maya': returnMayaMainWindow,
    'Max': returnMaxMainWindow,
    'Modo': returnModoMainWindow,
    'Mobu': returnMobuMainWindow,
    'Houdini': returnHoudiniMainWindow,
}
