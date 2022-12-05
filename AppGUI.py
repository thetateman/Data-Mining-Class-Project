import wx
import wx.xrc

import knn

###########################################################################
## Window Class
###########################################################################

class AppGUIWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(558, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"Enter patient info to classify as likely to have a stroke or not."),
            wx.VERTICAL)

        gSizer13 = wx.GridSizer(0, 2, 0, 100)

        gSizer18 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText34 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Age", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)

        gSizer18.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)

        gSizer18.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl9, 0, wx.ALL, 5)

        self.m_staticText37 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Hypertension", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)

        gSizer18.Add(self.m_staticText37, 0, wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl10, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Heart Disease", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)

        gSizer18.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        self.m_staticText39 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Ever Married", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)

        gSizer18.Add(self.m_staticText39, 0, wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer18.Add(self.m_textCtrl12, 0, wx.ALL, 5)

        gSizer18.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer13.Add(gSizer18, 1, wx.EXPAND, 5)

        gSizer181 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText341 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Residence Type", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText341.Wrap(-1)

        gSizer181.Add(self.m_staticText341, 0, wx.ALL, 5)

        self.m_textCtrl71 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer181.Add(self.m_textCtrl71, 0, wx.ALL, 5)

        self.m_staticText361 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Average Glucose Level",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText361.Wrap(-1)

        gSizer181.Add(self.m_staticText361, 0, wx.ALL, 5)

        self.m_textCtrl91 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer181.Add(self.m_textCtrl91, 0, wx.ALL, 5)

        self.m_staticText371 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"BMI", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText371.Wrap(-1)

        gSizer181.Add(self.m_staticText371, 0, wx.ALL, 5)

        self.m_textCtrl101 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        gSizer181.Add(self.m_textCtrl101, 0, wx.ALL, 5)

        self.m_staticText381 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Work Type", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText381.Wrap(-1)

        gSizer181.Add(self.m_staticText381, 0, wx.ALL, 5)

        self.m_textCtrl111 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        gSizer181.Add(self.m_textCtrl111, 0, wx.ALL, 5)

        self.m_staticText391 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Smoking Status", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText391.Wrap(-1)

        gSizer181.Add(self.m_staticText391, 0, wx.ALL, 5)

        self.m_textCtrl35 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer181.Add(self.m_textCtrl35, 0, wx.ALL, 5)

        gSizer181.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button62 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Predict", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        gSizer181.Add(self.m_button62, 0, wx.ALL, 5)

        gSizer13.Add(gSizer181, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer4.Add(gSizer13, 1, wx.ALL, 5)

        bSizer2.Add(sbSizer4, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"Advanced Users: Use your own dataset (.txt or .csv)"), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText62 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Path to file", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText62.Wrap(-1)

        fgSizer2.Add(self.m_staticText62, 0, wx.ALL, 15)

        self.m_textCtrl34 = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer2.Add(self.m_textCtrl34, 0, wx.ALL, 5)

        self.m_button59 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Load Dataset", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        fgSizer2.Add(self.m_button59, 0, wx.ALL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText66 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY,
                                            u"Using data file: C:\\lorem\\ipsum\\data.txt", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText66.Wrap(-1)

        fgSizer2.Add(self.m_staticText66, 0, wx.ALL, 15)

        sbSizer5.Add(fgSizer2, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer5, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Results"), wx.VERTICAL)

        self.m_staticText70 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"Analyzed <int> patient records.",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText70.Wrap(-1)

        sbSizer6.Add(self.m_staticText70, 0, wx.ALL, 5)

        self.m_staticText69 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY,
                                            u"This patient is <more/less> likely to have a stroke than the general population.",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText69.Wrap(-1)

        sbSizer6.Add(self.m_staticText69, 0, wx.ALL, 5)

        bSizer2.Add(sbSizer6, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button62.Bind(wx.EVT_BUTTON, self.m_buttonPredictOnButtonClick)
        self.m_button59.Bind(wx.EVT_BUTTON, self.m_button59OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def m_buttonPredictOnButtonClick(self, event):
        print("hellow workld")
        # read from input fields
        inputRecord = [99999]
        inputRecord.append(self.m_textCtrl9.GetValue())
        inputRecord.append(int(self.m_textCtrl7.GetValue()))
        inputRecord.append(int(self.m_textCtrl10.GetValue()))
        inputRecord.append(int(self.m_textCtrl11.GetValue()))
        inputRecord.append(self.m_textCtrl12.GetValue())
        inputRecord.append(self.m_textCtrl111.GetValue())
        inputRecord.append(self.m_textCtrl71.GetValue())
        inputRecord.append(float(self.m_textCtrl91.GetValue()))
        inputRecord.append(float(self.m_textCtrl101.GetValue()))
        inputRecord.append(self.m_textCtrl35.GetValue())
        result = ""
        # Make prediction
        pred = knn.knn_single_prediction(50, inputRecord, "train_strokes.txt")
        if pred:
            result = "more"
        else:
            result = "less"
        self.m_staticText69.SetLabelText(f"This patient is {result} likely to have a stroke than the general population.")

    def m_button59OnButtonClick(self, event):
        event.Skip()

