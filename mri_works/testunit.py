import unittest
import sys

from Config import Config
from main import Project_Irmage
from NodeEditor.python.PipeLine_Irmage import NodeEdit

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class TestMRIWorks(unittest.TestCase):

    def setUp(self):
        config = Config()
        self.app = QApplication(sys.argv)
        self.window = Project_Irmage()
        textInfo = QLineEdit(QWidget())
#         textInfo.resize(500,40)
        self.nodeedit = NodeEdit(textInfo)
        self.window.show()

    def tearDown(self):
        self.window.close()
        self.app.exit()

    def test_action1(self):
        print('action1')
        self.nodeedit.textInf.setText('test unitaire')

    def test_action2(self):
        print('action2')


if __name__ == '__main__':
    unittest.main()
