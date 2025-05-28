# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_connect.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(417, 115)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 3)

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_4, 1, 5, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_3, 0, 5, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy2.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy2)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Database Connection", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Database:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Port:", None))
    # retranslateUi

