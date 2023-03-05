ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}
import numpy as np
import pandas as pd
class LinearRegression{
    data;
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def readFile(self, filename):
        if fileName.endswith('.csv'):
            self.data = pd.read_csv(file)
        elif fileName.endswith('.xlsx') or fileName.endswith('.xls'):
            self.data = pd.read_excel(file)
        else:
            return {'message': 'File format not supported'}
}