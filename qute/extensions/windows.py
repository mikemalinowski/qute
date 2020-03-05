from ..vendor import Qt
from ..vendor import scribble


# ------------------------------------------------------------------------------
# noinspection PyPep8Naming,PyUnresolvedReferences
class MemorableWindow(Qt.QtWidgets.QMainWindow):

    # --------------------------------------------------------------------------
    def __init__(self, identifier=None, offsetX=7, offsetY=32, *args, **kwargs):
        super(MemorableWindow, self).__init__(*args, **kwargs)

        self._offsetX = offsetX
        self._offsetY = offsetY

        # -- If we're given an id, set this object name
        if identifier:
            self.setObjectName(identifier)

            # -- If there is any scribble data for this id we should
            # -- update this windows geometry accordingly.
            self.restoreSize()

    # --------------------------------------------------------------------------
    def restoreSize(self):
        stored_data = scribble.get(self.objectName())

        if 'geometry' in stored_data:
            geom = stored_data.get(
                'geometry',
                [
                    300,
                    300,
                    400,
                    400,
                ],
            )

            self.setGeometry(
                geom[0],
                geom[1],
                geom[2],
                geom[3],
            )

    # --------------------------------------------------------------------------
    def storeSize(self):
        stored_data = scribble.get(self.objectName())
        stored_data['geometry'] = [
            self.pos().x() + self._offsetX,
            self.pos().y() + self._offsetY,
            self.width(),
            self.height(),
        ]
        stored_data.save()

    # --------------------------------------------------------------------------
    def resizeEvent(self, event):
        self.storeSize()
        super(MemorableWindow, self).resizeEvent(event)

    # --------------------------------------------------------------------------
    def moveEvent(self, event):
        self.storeSize()
        super(MemorableWindow, self).moveEvent(event)

    # --------------------------------------------------------------------------
    def hideEvent(self, event):
        self.storeSize()
        super(MemorableWindow, self).hideEvent(event)
