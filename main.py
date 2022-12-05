import knn
import AppGUI

import wx


if __name__ == '__main__':
    #knn_accuracy_testing(35)
    '''
    pred = knn.knn_single_prediction(50, [30468, 'Male', 73.0, 1, 0, 'Yes', 'Self-employed', 'Rural', 194.99, 39.8, 'never smoked'], "train_strokes.txt")
    print(pred)
    pred = knn.knn_single_prediction(50, [30468, 'Female', 18.0, 0, 0, 'Yes', 'Private', 'Urban', 87.96, 30.2, 'never smoked'], "train_strokes.txt")
    print(pred)
    '''
    app = wx.App()
    frm = AppGUI.AppGUIWindow(None)
    frm.Show()
    app.MainLoop()
