# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PLSDR/PLSDR_GUI_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 786)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.control_widget = QtWidgets.QWidget(self.widget)
        self.control_widget.setObjectName("control_widget")
        self.gridLayout_3a = QtWidgets.QGridLayout(self.control_widget)
        self.gridLayout_3a.setContentsMargins(0, 0, 0, 4)
        self.gridLayout_3a.setHorizontalSpacing(4)
        self.gridLayout_3a.setVerticalSpacing(0)
        self.gridLayout_3a.setObjectName("gridLayout_3a")
        self.digit_widget = QtWidgets.QWidget(self.control_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.digit_widget.sizePolicy().hasHeightForWidth())
        self.digit_widget.setSizePolicy(sizePolicy)
        self.digit_widget.setObjectName("digit_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.digit_widget)
        self.gridLayout_2.setContentsMargins(8, 0, 8, 0)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_dot_1 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_dot_1.setFont(font)
        self.label_dot_1.setObjectName("label_dot_1")
        self.gridLayout_2.addWidget(self.label_dot_1, 0, 8, 1, 1)
        self.label_digit_6 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_6.setFont(font)
        self.label_digit_6.setObjectName("label_digit_6")
        self.gridLayout_2.addWidget(self.label_digit_6, 0, 3, 1, 1)
        self.label_digit_3 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_3.setFont(font)
        self.label_digit_3.setObjectName("label_digit_3")
        self.gridLayout_2.addWidget(self.label_digit_3, 0, 7, 1, 1)
        self.label_digit_8 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_digit_8.setFont(font)
        self.label_digit_8.setObjectName("label_digit_8")
        self.gridLayout_2.addWidget(self.label_digit_8, 0, 1, 1, 1)
        self.label_digit_2 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_2.setFont(font)
        self.label_digit_2.setObjectName("label_digit_2")
        self.gridLayout_2.addWidget(self.label_digit_2, 0, 9, 1, 1)
        self.label_digit_1 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_1.setFont(font)
        self.label_digit_1.setObjectName("label_digit_1")
        self.gridLayout_2.addWidget(self.label_digit_1, 0, 10, 1, 1)
        self.label_dot_2 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_dot_2.setFont(font)
        self.label_dot_2.setObjectName("label_dot_2")
        self.gridLayout_2.addWidget(self.label_dot_2, 0, 4, 1, 1)
        self.label_digit_4 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_4.setFont(font)
        self.label_digit_4.setObjectName("label_digit_4")
        self.gridLayout_2.addWidget(self.label_digit_4, 0, 6, 1, 1)
        self.label_digit_0 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_0.setFont(font)
        self.label_digit_0.setObjectName("label_digit_0")
        self.gridLayout_2.addWidget(self.label_digit_0, 0, 11, 1, 1)
        self.label_digit_9 = QtWidgets.QLabel(self.digit_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_digit_9.sizePolicy().hasHeightForWidth())
        self.label_digit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(24)
        self.label_digit_9.setFont(font)
        self.label_digit_9.setObjectName("label_digit_9")
        self.gridLayout_2.addWidget(self.label_digit_9, 0, 0, 1, 1)
        self.label_digit_7 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_7.setFont(font)
        self.label_digit_7.setObjectName("label_digit_7")
        self.gridLayout_2.addWidget(self.label_digit_7, 0, 2, 1, 1)
        self.label_digit_5 = QtWidgets.QLabel(self.digit_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_digit_5.setFont(font)
        self.label_digit_5.setObjectName("label_digit_5")
        self.gridLayout_2.addWidget(self.label_digit_5, 0, 5, 1, 1)
        self.gridLayout_3a.addWidget(self.digit_widget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            108,
            17,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3a.addItem(spacerItem, 0, 1, 1, 1)
        self.label_af_gain = QtWidgets.QLabel(self.control_widget)
        self.label_af_gain.setObjectName("label_af_gain")
        self.gridLayout_3a.addWidget(self.label_af_gain, 0, 2, 1, 1)
        self.run_stop_button = QtWidgets.QPushButton(self.control_widget)
        self.run_stop_button.setCheckable(True)
        self.run_stop_button.setObjectName("run_stop_button")
        self.gridLayout_3a.addWidget(self.run_stop_button, 0, 9, 1, 1)
        self.af_gain_slider = QtWidgets.QSlider(self.control_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.af_gain_slider.sizePolicy().hasHeightForWidth())
        self.af_gain_slider.setSizePolicy(sizePolicy)
        self.af_gain_slider.setMinimumSize(QtCore.QSize(200, 0))
        self.af_gain_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.af_gain_slider.setOrientation(QtCore.Qt.Horizontal)
        self.af_gain_slider.setObjectName("af_gain_slider")
        self.gridLayout_3a.addWidget(self.af_gain_slider, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.control_widget, 0, 0, 1, 1)
        self.splitter_h = QtWidgets.QSplitter(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.splitter_h.sizePolicy().hasHeightForWidth())
        self.splitter_h.setSizePolicy(sizePolicy)
        self.splitter_h.setToolTip("")
        self.splitter_h.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_h.setObjectName("splitter_h")
        self.splitter_v = QtWidgets.QSplitter(self.splitter_h)
        self.splitter_v.setToolTip("")
        self.splitter_v.setOrientation(QtCore.Qt.Vertical)
        self.splitter_v.setObjectName("splitter_v")
        self.fft_disp = QtWidgets.QWidget(self.splitter_v)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.fft_disp.sizePolicy().hasHeightForWidth())
        self.fft_disp.setSizePolicy(sizePolicy)
        self.fft_disp.setMinimumSize(QtCore.QSize(0, 64))
        self.fft_disp.setToolTip("")
        self.fft_disp.setObjectName("fft_disp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fft_disp)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.fft_disp_layout = QtWidgets.QHBoxLayout()
        self.fft_disp_layout.setObjectName("fft_disp_layout")
        self.gridLayout_6.addLayout(self.fft_disp_layout, 0, 0, 1, 1)
        self.freq_waterfall_tabwidget = QtWidgets.QTabWidget(self.splitter_v)
        self.freq_waterfall_tabwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.freq_waterfall_tabwidget.setTabPosition(
            QtWidgets.QTabWidget.South)
        self.freq_waterfall_tabwidget.setObjectName("freq_waterfall_tabwidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.freq_table = QtWidgets.QTableView(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.freq_table.sizePolicy().hasHeightForWidth())
        self.freq_table.setSizePolicy(sizePolicy)
        self.freq_table.setAutoScroll(True)
        self.freq_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.freq_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.freq_table.setObjectName("freq_table")
        self.gridLayout_5.addWidget(self.freq_table, 0, 0, 1, 1)
        self.freq_waterfall_tabwidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.waterfall_widget = QtWidgets.QWidget(self.tab_6)
        self.waterfall_widget.setObjectName("waterfall_widget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.waterfall_widget)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.waterfall_layout = QtWidgets.QHBoxLayout()
        self.waterfall_layout.setObjectName("waterfall_layout")
        self.gridLayout_10.addLayout(self.waterfall_layout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.waterfall_widget, 0, 0, 1, 1)
        self.freq_waterfall_tabwidget.addTab(self.tab_6, "")
        self.controls_tabwidget = QtWidgets.QTabWidget(self.splitter_h)
        self.controls_tabwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.controls_tabwidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.controls_tabwidget.setObjectName("controls_tabwidget")
        self.control_tab = QtWidgets.QWidget()
        self.control_tab.setObjectName("control_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.control_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.control_tab)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.bandwidth_label = QtWidgets.QLabel(self.widget_2)
        self.bandwidth_label.setObjectName("bandwidth_label")
        self.gridLayout.addWidget(self.bandwidth_label, 13, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.averaging_slider = QtWidgets.QSlider(self.widget_2)
        self.averaging_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.averaging_slider.setOrientation(QtCore.Qt.Horizontal)
        self.averaging_slider.setObjectName("averaging_slider")
        self.gridLayout.addWidget(self.averaging_slider, 15, 1, 1, 2)
        self.gain_label_a = QtWidgets.QLabel(self.widget_2)
        self.gain_label_a.setObjectName("gain_label_a")
        self.gridLayout.addWidget(self.gain_label_a, 7, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.agc_combo = QtWidgets.QComboBox(self.widget_2)
        self.agc_combo.setObjectName("agc_combo")
        self.gridLayout_11.addWidget(self.agc_combo, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 16, 1, 1, 2)
        self.gain_label_b = QtWidgets.QLabel(self.widget_2)
        self.gain_label_b.setObjectName("gain_label_b")
        self.gridLayout.addWidget(self.gain_label_b, 9, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 21, 0, 1, 1)
        self.gain_slider_b = QtWidgets.QSlider(self.widget_2)
        self.gain_slider_b.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gain_slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.gain_slider_b.setObjectName("gain_slider_b")
        self.gridLayout.addWidget(self.gain_slider_b, 9, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 386, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 22, 1, 1, 1)
        self.gain_label_c = QtWidgets.QLabel(self.widget_2)
        self.gain_label_c.setObjectName("gain_label_c")
        self.gridLayout.addWidget(self.gain_label_c, 10, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 17, 0, 1, 1)
        self.gain_slider_c = QtWidgets.QSlider(self.widget_2)
        self.gain_slider_c.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gain_slider_c.setOrientation(QtCore.Qt.Horizontal)
        self.gain_slider_c.setObjectName("gain_slider_c")
        self.gridLayout.addWidget(self.gain_slider_c, 10, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 15, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.if_bw_wide_button = QtWidgets.QRadioButton(self.widget_2)
        self.if_bw_wide_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.if_bw_wide_button.setObjectName("if_bw_wide_button")
        self.if_bw_button_group = QtWidgets.QButtonGroup(MainWindow)
        self.if_bw_button_group.setObjectName("if_bw_button_group")
        self.if_bw_button_group.addButton(self.if_bw_wide_button)
        self.horizontalLayout_2.addWidget(self.if_bw_wide_button)
        self.if_bw_medium_button = QtWidgets.QRadioButton(self.widget_2)
        self.if_bw_medium_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.if_bw_medium_button.setChecked(True)
        self.if_bw_medium_button.setObjectName("if_bw_medium_button")
        self.if_bw_button_group.addButton(self.if_bw_medium_button)
        self.horizontalLayout_2.addWidget(self.if_bw_medium_button)
        self.if_bw_narrow_button = QtWidgets.QRadioButton(self.widget_2)
        self.if_bw_narrow_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.if_bw_narrow_button.setObjectName("if_bw_narrow_button")
        self.if_bw_button_group.addButton(self.if_bw_narrow_button)
        self.horizontalLayout_2.addWidget(self.if_bw_narrow_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 17, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dc_offset_checkbox = QtWidgets.QCheckBox(self.widget_2)
        self.dc_offset_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dc_offset_checkbox.setObjectName("dc_offset_checkbox")
        self.horizontalLayout.addWidget(self.dc_offset_checkbox)
        self.iq_balance_checkbox = QtWidgets.QCheckBox(self.widget_2)
        self.iq_balance_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.iq_balance_checkbox.setObjectName("iq_balance_checkbox")
        self.horizontalLayout.addWidget(self.iq_balance_checkbox)
        self.gridLayout.addLayout(self.horizontalLayout, 21, 1, 1, 2)
        self.gain_slider_a = QtWidgets.QSlider(self.widget_2)
        self.gain_slider_a.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gain_slider_a.setOrientation(QtCore.Qt.Horizontal)
        self.gain_slider_a.setObjectName("gain_slider_a")
        self.gridLayout.addWidget(self.gain_slider_a, 7, 1, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 16, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 14, 0, 1, 1)
        self.squelch_slider = QtWidgets.QSlider(self.widget_2)
        self.squelch_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.squelch_slider.setOrientation(QtCore.Qt.Horizontal)
        self.squelch_slider.setObjectName("squelch_slider")
        self.gridLayout.addWidget(self.squelch_slider, 14, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 19, 0, 1, 1)
        self.fft_size_combo = QtWidgets.QComboBox(self.widget_2)
        self.fft_size_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fft_size_combo.setObjectName("fft_size_combo")
        self.gridLayout.addWidget(self.fft_size_combo, 19, 1, 1, 2)
        self.device_combo = QtWidgets.QComboBox(self.widget_2)
        self.device_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_combo.setObjectName("device_combo")
        self.gridLayout.addWidget(self.device_combo, 0, 1, 1, 2)
        self.bandwidth_combo = QtWidgets.QComboBox(self.widget_2)
        self.bandwidth_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bandwidth_combo.setObjectName("bandwidth_combo")
        self.gridLayout.addWidget(self.bandwidth_combo, 13, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 20, 0, 1, 1)
        self.mode_combo = QtWidgets.QComboBox(self.widget_2)
        self.mode_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mode_combo.setObjectName("mode_combo")
        self.gridLayout.addWidget(self.mode_combo, 2, 1, 1, 2)
        self.framerate_combo = QtWidgets.QComboBox(self.widget_2)
        self.framerate_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.framerate_combo.setObjectName("framerate_combo")
        self.gridLayout.addWidget(self.framerate_combo, 20, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.antenna_combo = QtWidgets.QComboBox(self.widget_2)
        self.antenna_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.antenna_combo.setObjectName("antenna_combo")
        self.gridLayout.addWidget(self.antenna_combo, 1, 1, 1, 2)
        self.gain_label_d = QtWidgets.QLabel(self.widget_2)
        self.gain_label_d.setObjectName("gain_label_d")
        self.gridLayout.addWidget(self.gain_label_d, 12, 0, 1, 1)
        self.gain_slider_d = QtWidgets.QSlider(self.widget_2)
        self.gain_slider_d.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gain_slider_d.setOrientation(QtCore.Qt.Horizontal)
        self.gain_slider_d.setObjectName("gain_slider_d")
        self.gridLayout.addWidget(self.gain_slider_d, 12, 1, 1, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.controls_tabwidget.addTab(self.control_tab, "")
        self.configure_tab = QtWidgets.QWidget()
        self.configure_tab.setObjectName("configure_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.configure_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.audio_rate_text = QtWidgets.QLineEdit(self.configure_tab)
        self.audio_rate_text.setObjectName("audio_rate_text")
        self.gridLayout_9.addWidget(self.audio_rate_text, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 436, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem2, 12, 1, 1, 1)
        self.offset_freq_text = QtWidgets.QLineEdit(self.configure_tab)
        self.offset_freq_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.offset_freq_text.setObjectName("offset_freq_text")
        self.gridLayout_9.addWidget(self.offset_freq_text, 10, 1, 1, 1)
        self.offset_checkbox = QtWidgets.QCheckBox(self.configure_tab)
        self.offset_checkbox.setObjectName("offset_checkbox")
        self.gridLayout_9.addWidget(self.offset_checkbox, 9, 0, 1, 1)
        self.upconversion_checkbox = QtWidgets.QCheckBox(self.configure_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.upconversion_checkbox.sizePolicy().hasHeightForWidth())
        self.upconversion_checkbox.setSizePolicy(sizePolicy)
        self.upconversion_checkbox.setObjectName("upconversion_checkbox")
        self.gridLayout_9.addWidget(self.upconversion_checkbox, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.configure_tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 6, 0, 1, 1)
        self.upconvert_trans_text = QtWidgets.QLineEdit(self.configure_tab)
        self.upconvert_trans_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.upconvert_trans_text.setObjectName("upconvert_trans_text")
        self.gridLayout_9.addWidget(self.upconvert_trans_text, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.configure_tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 7, 0, 1, 1)
        self.upconvert_freq_text = QtWidgets.QLineEdit(self.configure_tab)
        self.upconvert_freq_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.upconvert_freq_text.setObjectName("upconvert_freq_text")
        self.gridLayout_9.addWidget(self.upconvert_freq_text, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.configure_tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.configure_tab)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.configure_tab)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 9, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.configure_tab)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.configure_tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.configure_tab)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 3, 0, 1, 1)
        self.audio_device_text = QtWidgets.QLineEdit(self.configure_tab)
        self.audio_device_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.audio_device_text.setObjectName("audio_device_text")
        self.gridLayout_9.addWidget(self.audio_device_text, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.configure_tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 2, 0, 1, 1)
        self.corr_ppm_text = QtWidgets.QLineEdit(self.configure_tab)
        self.corr_ppm_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.corr_ppm_text.setObjectName("corr_ppm_text")
        self.gridLayout_9.addWidget(self.corr_ppm_text, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.configure_tab)
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 4, 0, 1, 1)
        self.cw_base_text = QtWidgets.QLineEdit(self.configure_tab)
        self.cw_base_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cw_base_text.setObjectName("cw_base_text")
        self.gridLayout_9.addWidget(self.cw_base_text, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.configure_tab)
        self.label_23.setObjectName("label_23")
        self.gridLayout_9.addWidget(self.label_23, 8, 0, 1, 1)
        self.corr_ppm_upc_text = QtWidgets.QLineEdit(self.configure_tab)
        self.corr_ppm_upc_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.corr_ppm_upc_text.setObjectName("corr_ppm_upc_text")
        self.gridLayout_9.addWidget(self.corr_ppm_upc_text, 8, 1, 1, 1)
        self.sample_rate_combo = QtWidgets.QComboBox(self.configure_tab)
        self.sample_rate_combo.setObjectName("sample_rate_combo")
        self.gridLayout_9.addWidget(self.sample_rate_combo, 1, 1, 1, 1)
        self.controls_tabwidget.addTab(self.configure_tab, "")
        self.help_tab = QtWidgets.QWidget()
        self.help_tab.setObjectName("help_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.help_tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.help_tab)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_12.setContentsMargins(0, 0, -1, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.help_text_browser = QtWidgets.QTextBrowser(self.widget_3)
        self.help_text_browser.setObjectName("help_text_browser")
        self.gridLayout_12.addWidget(self.help_text_browser, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 1)
        self.controls_tabwidget.addTab(self.help_tab, "")
        self.gridLayout_3.addWidget(self.splitter_h, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setMinimumSize(QtCore.QSize(300, 0))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_3.addWidget(self.status_label)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.signal_progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.signal_progress_bar.setMaximumSize(QtCore.QSize(16777215, 24))
        self.signal_progress_bar.setProperty("value", 24)
        self.signal_progress_bar.setObjectName("signal_progress_bar")
        self.horizontalLayout_3.addWidget(self.signal_progress_bar)
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setObjectName("quit_button")
        self.horizontalLayout_3.addWidget(self.quit_button)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.freq_waterfall_tabwidget.setCurrentIndex(0)
        self.controls_tabwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dot_1.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_dot_1.setText(_translate("MainWindow", "."))
        self.label_digit_6.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_6.setText(_translate("MainWindow", "0"))
        self.label_digit_3.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_3.setText(_translate("MainWindow", "0"))
        self.label_digit_8.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_8.setText(_translate("MainWindow", "0"))
        self.label_digit_2.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_2.setText(_translate("MainWindow", "0"))
        self.label_digit_1.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_1.setText(_translate("MainWindow", "0"))
        self.label_dot_2.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_dot_2.setText(_translate("MainWindow", "."))
        self.label_digit_4.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_4.setText(_translate("MainWindow", "0"))
        self.label_digit_0.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_0.setText(_translate("MainWindow", "0"))
        self.label_digit_9.setAccessibleName(
            _translate("MainWindow", "FreqDigitDark"))
        self.label_digit_9.setText(_translate("MainWindow", "0"))
        self.label_digit_7.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_7.setText(_translate("MainWindow", "0"))
        self.label_digit_5.setAccessibleName(
            _translate("MainWindow", "FreqDigit"))
        self.label_digit_5.setText(_translate("MainWindow", "0"))
        self.label_af_gain.setToolTip(
            _translate(
                "MainWindow",
                "Audio-Frequency Gain"))
        self.label_af_gain.setText(_translate("MainWindow", "AF Gain:"))
        self.run_stop_button.setToolTip(
            _translate(
                "MainWindow",
                "Start/Stop data processing"))
        self.run_stop_button.setText(_translate("MainWindow", "Start/Stop"))
        self.af_gain_slider.setToolTip(_translate(
            "MainWindow", "Audio Frequency Gain"))
        self.freq_waterfall_tabwidget.setTabText(
            self.freq_waterfall_tabwidget.indexOf(
                self.tab_5), _translate(
                "MainWindow", "Frequencies"))
        self.freq_waterfall_tabwidget.setTabText(
            self.freq_waterfall_tabwidget.indexOf(
                self.tab_6), _translate(
                "MainWindow", "Waterfall"))
        self.label_2.setText(_translate("MainWindow", "Device"))
        self.bandwidth_label.setText(_translate("MainWindow", "RF BW Hz"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.averaging_slider.setToolTip(
            _translate(
                "MainWindow",
                "A moving average makes the display easier to interpret"))
        self.gain_label_a.setToolTip(
            _translate(
                "MainWindow",
                "Radio-Frequency Gain"))
        self.gain_label_a.setText(_translate("MainWindow", "Gain A"))
        self.gain_label_b.setToolTip(
            _translate(
                "MainWindow",
                "Intermediate Frequency Gain"))
        self.gain_label_b.setText(_translate("MainWindow", "Gain B"))
        self.label_22.setToolTip(
            _translate(
                "MainWindow",
                "These features may not be present in a given device"))
        self.label_22.setText(_translate("MainWindow", "Tune:"))
        self.gain_slider_b.setToolTip(
            _translate(
                "MainWindow",
                "Intermediate Frequency Gain"))
        self.gain_label_c.setToolTip(_translate("MainWindow", "Baseband Gain"))
        self.gain_label_c.setText(_translate("MainWindow", "Gain C"))
        self.label_24.setToolTip(
            _translate(
                "MainWindow",
                "Intemediate Frequency Bandwidth"))
        self.label_24.setText(_translate("MainWindow", "IF BW"))
        self.gain_slider_c.setToolTip(
            _translate("MainWindow", "Baseband Gain"))
        self.label_3.setToolTip(
            _translate(
                "MainWindow",
                "A moving average makes the display easier to interpret"))
        self.label_3.setText(_translate("MainWindow", "Averaging"))
        self.if_bw_wide_button.setToolTip(_translate("MainWindow", "Wide"))
        self.if_bw_wide_button.setText(_translate("MainWindow", "W"))
        self.if_bw_medium_button.setToolTip(_translate("MainWindow", "Medium"))
        self.if_bw_medium_button.setText(_translate("MainWindow", "M"))
        self.if_bw_narrow_button.setToolTip(_translate("MainWindow", "Narrow"))
        self.if_bw_narrow_button.setText(_translate("MainWindow", "&N"))
        self.dc_offset_checkbox.setToolTip(
            _translate(
                "MainWindow",
                "DC Offset -- not supported by all devices"))
        self.dc_offset_checkbox.setText(_translate("MainWindow", "DCO"))
        self.iq_balance_checkbox.setToolTip(
            _translate(
                "MainWindow",
                "IQ Balance -- not supported by all devices"))
        self.iq_balance_checkbox.setText(_translate("MainWindow", "IQB"))
        self.gain_slider_a.setToolTip(
            _translate(
                "MainWindow",
                "Radio Frequency Gain"))
        self.label_20.setToolTip(
            _translate(
                "MainWindow",
                "Automatic Gain Control"))
        self.label_20.setText(_translate("MainWindow", "AGC"))
        self.label_21.setToolTip(
            _translate(
                "MainWindow",
                "A signal strength threshhold above which audio is enabled"))
        self.label_21.setText(_translate("MainWindow", "Squelch"))
        self.squelch_slider.setToolTip(
            _translate(
                "MainWindow",
                "A signal strength threshhold above which audio is enabled"))
        self.label.setText(_translate("MainWindow", "FFT Size"))
        self.fft_size_combo.setToolTip(
            _translate(
                "MainWindow",
                "The size of the FFT buffer (must be a power of 2)"))
        self.device_combo.setToolTip(
            _translate(
                "MainWindow",
                "Select a hardware device"))
        self.bandwidth_combo.setToolTip(
            _translate("MainWindow", "Front-end bandwidth"))
        self.label_7.setText(_translate("MainWindow", "Rate FPS"))
        self.mode_combo.setToolTip(
            _translate(
                "MainWindow",
                "Receiver operating mode"))
        self.framerate_combo.setToolTip(
            _translate(
                "MainWindow",
                "The rate at which new spectra are created"))
        self.label_12.setText(_translate("MainWindow", "Antenna"))
        self.antenna_combo.setToolTip(
            _translate(
                "MainWindow",
                "The currently active antenna"))
        self.gain_label_d.setText(_translate("MainWindow", "Gain D"))
        self.controls_tabwidget.setTabText(
            self.controls_tabwidget.indexOf(
                self.control_tab), _translate(
                "MainWindow", "Control"))
        self.audio_rate_text.setToolTip(
            _translate(
                "MainWindow",
                "The rate at which the audio stream is created"))
        self.offset_freq_text.setToolTip(
            _translate(
                "MainWindow",
                "Must be less than +- Audio Rate/2"))
        self.offset_checkbox.setText(
            _translate(
                "MainWindow",
                "Use offset tuning"))
        self.upconversion_checkbox.setText(
            _translate("MainWindow", "Use upconversion"))
        self.label_9.setText(_translate("MainWindow", "Transition freq."))
        self.upconvert_trans_text.setToolTip(
            _translate(
                "MainWindow",
                "The receiving frequency below which upconversion is activated"))
        self.label_10.setText(_translate("MainWindow", "Upconversion freq."))
        self.upconvert_freq_text.setToolTip(_translate(
            "MainWindow", "The specified upconversion frequency"))
        self.label_11.setText(_translate("MainWindow", "Offset freq."))
        self.label_13.setText(_translate("MainWindow", "Units Hz"))
        self.label_14.setText(_translate("MainWindow", "Units Hz"))
        self.label_15.setText(_translate("MainWindow", "Sample Rate"))
        self.label_16.setText(_translate("MainWindow", "Corr. PPM"))
        self.label_18.setText(_translate("MainWindow", "Audio Device"))
        self.audio_device_text.setToolTip(_translate(
            "MainWindow", "This field can be left blank"))
        self.label_17.setText(_translate("MainWindow", "Audio Rate"))
        self.corr_ppm_text.setToolTip(
            _translate(
                "MainWindow",
                "Frequency correction, parts per million"))
        self.label_19.setText(_translate("MainWindow", "CW Base Freq."))
        self.cw_base_text.setToolTip(
            _translate(
                "MainWindow",
                "This is the CW receiving pitch in Hz"))
        self.label_23.setText(_translate("MainWindow", "Upc. Corr. PPM"))
        self.corr_ppm_upc_text.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Applied only when upconversion is in effect</p></body></html>"))
        self.sample_rate_combo.setToolTip(
            _translate(
                "MainWindow",
                "The rate at which data samples are produced"))
        self.controls_tabwidget.setTabText(
            self.controls_tabwidget.indexOf(
                self.configure_tab), _translate(
                "MainWindow", "Configure"))
        self.controls_tabwidget.setTabText(
            self.controls_tabwidget.indexOf(
                self.help_tab), _translate(
                "MainWindow", "Help"))
        self.quit_button.setToolTip(_translate("MainWindow", "Exit PLSDR"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
