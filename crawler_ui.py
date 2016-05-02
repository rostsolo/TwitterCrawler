import sys
import PyQt4
from PyQt4 import QtGui, QtCore
from crawler import TwitterCrawler


class Window(QtGui.QMainWindow):
    def __init__(self):
        #set null filenames
        self.track_words_filename = None
        self.langs_filename = None
        self.follows_filename = None
        self.locs_filename = None

        #params for crawler
        self.terms_filename = None
        self.contexts_filename = None
        self.log_filename = None

        self.preserve_var_percentage = None
        self.min_cos_value = None
        self.tweets_count = None
        self.training_sample_size = None

        #UI initialization
        super(Window, self).__init__()
        self.setGeometry(10, 10, 1500, 1000)
        self.setWindowTitle('Main window')

        #visualize layout
        self.default_layout()
        self.analysis_layout()
        self.result_layout()

        self.show()

    def reset_all(self):
        #set null filenames
        self.track_words_filename = None
        self.langs_filename = None
        self.follows_filename = None
        self.locs_filename = None

        #params for crawler
        self.terms_filename = None
        self.contexts_filename = None
        self.log_filename = None

        self.preserve_var_percentage = None
        self.min_cos_value = None
        self.tweets_count = None
        self.training_sample_size = None

        #reset TextBoxes
        self.txtTrainingSampleSize.setText('')
        self.txtLogFilePath.setText('')
        self.txtTweetsCount.setText('')
        self.txtMinCos.setText('')
        self.txtVarPercent.setText('')
        self.richTxt.setText('')

    #region Layouts
    def default_layout(self):
        # ----------- Upper label -----------
        lbl = QtGui.QLabel("Twitter clawler",self)
        lbl.setStyleSheet('font-size: 18pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(150,20)
        # ----------- Run button -----------
        btn = QtGui.QPushButton("Run crawler", self)
        btn.clicked.connect(self.run_click)
        btn.setStyleSheet('font-size:12pt')
        btn.resize(btn.sizeHint())
        btn.move(220, 90)
        # ----------- Reset button -----------
        btn = QtGui.QPushButton("Reset all", self)
        btn.clicked.connect(self.reset_all)
        btn.setStyleSheet('font-size:12pt')
        btn.resize(btn.sizeHint())
        btn.move(800, 20)
        # ----------- input WordsFilePath -----------
        lbl = QtGui.QLabel("Track words", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(20,70)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(20,90)
        btn.clicked.connect(self.show_file_dialog_track_words)
        # ----------- input LangsFilePath -----------
        lbl = QtGui.QLabel("Languages", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(20,130)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(20,150)
        btn.clicked.connect(self.show_file_dialog_langs)
        # ----------- input FollowsFilePath -----------
        lbl = QtGui.QLabel("Follows", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(20,190)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(20,210)
        btn.clicked.connect(self.show_file_dialog_follows)
        # ----------- input LocationsFilePath -----------
        lbl = QtGui.QLabel("Locations", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(20,250)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(20,270)
        btn.clicked.connect(self.show_file_dialog_locations)

    def analysis_layout(self):
        # ----------- input TermsFilePath -----------
        lbl = QtGui.QLabel("Terms", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(450,70)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(450,90)
        btn.clicked.connect(self.show_file_dialog_terms)
        # ----------- input ContextsFilePath -----------
        lbl = QtGui.QLabel("Contexts", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(450,130)
        btn = QtGui.QPushButton("Choose file", self)
        btn.setStyleSheet('font-size: 12pt;')
        btn.resize(btn.sizeHint())
        btn.move(450,150)
        btn.clicked.connect(self.show_file_dialog_contexts)
        # ----------- LogFilePath -----------
        lbl = QtGui.QLabel("Log file name", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(220,150)
        self.txtLogFilePath = QtGui.QLineEdit(self)
        self.txtLogFilePath.resize(self.txtLogFilePath.sizeHint())
        self.txtLogFilePath.move(220,170)
        # ----------- Tweets Count -----------
        lbl = QtGui.QLabel("Tweets number", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(220,200)
        self.txtTweetsCount = QtGui.QLineEdit(self)
        self.txtTweetsCount.resize(self.txtTweetsCount.sizeHint())
        self.txtTweetsCount.move(220,220)
        # ----------- Training sample size -----------
        lbl = QtGui.QLabel("Training sample size", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(220,250)
        self.txtTrainingSampleSize = QtGui.QLineEdit(self)
        self.txtTrainingSampleSize.resize(self.txtTweetsCount.sizeHint())
        self.txtTrainingSampleSize.move(220,270)
        # ----------- PreserveVariancePercentage -----------
        lbl = QtGui.QLabel("Variance percentage (%)", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(450,200)
        self.txtVarPercent = QtGui.QLineEdit(self)
        self.txtVarPercent.resize(self.txtVarPercent.sizeHint())
        self.txtVarPercent.move(450, 220)
        # ----------- MinCosValue -----------
        lbl = QtGui.QLabel("Min cos", self)
        lbl.setStyleSheet('font-size: 12pt;')
        lbl.resize(lbl.sizeHint())
        lbl.move(450,250)
        self.txtMinCos = QtGui.QLineEdit(self)
        self.txtMinCos.resize(self.txtVarPercent.sizeHint())
        self.txtMinCos.move(450, 270)

    def result_layout(self):
        # ----------- richTxt -----------
        self.richTxt = QtGui.QTextEdit(self)
        self.richTxt.resize(600, 550)
        self.richTxt.move(700, 90)
        self.richTxt.setStyleSheet('font-size: 12pt')
    #endregion

    #region ShowDialog Helpers
    def show_file_dialog_track_words(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.track_words_filename = fileName if '.txt' in fileName else fileName + '.txt'

    def show_file_dialog_langs(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.langs_filename = fileName if '.txt' in fileName else fileName + '.txt'

    def show_file_dialog_follows(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.follows_filename = fileName if '.txt' in fileName else fileName + '.txt'

    def show_file_dialog_locations(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.locs_filename = fileName if '.txt' in fileName else fileName + '.txt'

    def show_file_dialog_terms(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.terms_filename = fileName if '.txt' in fileName else fileName + '.txt'

    def show_file_dialog_contexts(self):
        fileName = QtGui.QFileDialog.getOpenFileName()
        self.contexts_filename = fileName if '.txt' in fileName else fileName + '.txt'
    #endregion

    #read files method
    def extract_lines(self, filename):
        lines = None
        if filename != None:
            input_filename = filename if '.txt' in filename else filename + '.txt'
            f = open(input_filename, 'r')
            text = f.read()
            lines = text.split('\n')
            f.close()

        return lines

    #TODO: finish reading params
    def run_click(self):
        try:
            #region set mining params
            #read tracking words
            tracking_words = None
            tracking_words = self.extract_lines(self.track_words_filename)

            #read langs
            langs = None
            langs = self.extract_lines(self.langs_filename)

            #read follows
            follows = None
            follows = self.extract_lines(self.follows_filename)

            #read locations
            locations = None
            locations = self.extract_lines(self.locs_filename)
            #endregion
            #region set crawler params
            tmp = self.txtLogFilePath.text()
            self.log_filename = tmp if '.txt' in tmp else tmp + '.txt'

            self.preserve_var_percentage = float(self.txtVarPercent.text()) / 100.0
            self.min_cos_value = float(self.txtMinCos.text())
            self.tweets_count = int(self.txtTweetsCount.text())
            self.training_sample_size = int(self.txtTrainingSampleSize.text())
            #endregion
        except Exception as ex:
            msg = QtGui.QMessageBox(self)
            msg.setText(ex.args[0])
            msg.show()
        ###################################
        # pass parameters to Crawler entity
        # requires following
        # 1) terms_filename
        # 2) contexts_filename
        # 3) log_filename
        # 4) var_percentage
        # 5) min_cos
        # 6) tweets_count
        # 7) training_sample_size
        ###################################
        if self.terms_filename is not None and \
            self.contexts_filename is not None and \
            self.log_filename != '' and \
            self.preserve_var_percentage is not None and \
            self.min_cos_value is not None and \
            self.tweets_count is not None and \
            self.training_sample_size is not None and \
            self.track_words_filename is not None:

            try:
                crawler = TwitterCrawler(terms_filename=self.terms_filename,
                                         contexts_filename=self.contexts_filename,
                                         log_filename=self.log_filename,
                                         preserve_var_percentage=self.preserve_var_percentage,
                                         min_cos_val=self.min_cos_value,
                                         tweets_count=self.tweets_count,
                                         training_sample_size=self.training_sample_size
                                         )
                crawler.filter_by_params(words=tracking_words, langs=langs, follows=follows, locations=locations)

                #visualize resilts
                self.richTxt.setText(crawler.get_result_str())
            except Exception as ex:
                msg = QtGui.QMessageBox(self)
                msg.setText(ex.args[0])
                msg.show()
        else:
            msg = QtGui.QMessageBox(self)
            msg.setText('Required: Terms, Contexts, log, Percentage, Cos, Number of tweets, Training sample size and Tracking words')
            msg.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
