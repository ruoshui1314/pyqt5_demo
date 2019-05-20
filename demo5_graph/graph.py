from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from PIL import Image
import numpy as np

plt = pg.plot(x=[0, 100, 500, 600, 700], y=[50, 100, 300, 200, 500], pen='r')

# add an image, scaled
image_data = np.asarray(Image.open('1.jpg').convert('RGB'))
# image_data = np.asarray(Image.open('map.png'))
pg.setConfigOptions(imageAxisOrder='row-major')
img = pg.ImageItem(image_data)
img.setZValue(-1)
plt.addItem(img)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()