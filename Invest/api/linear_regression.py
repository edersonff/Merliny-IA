from rest_framework import viewsets
from rest_framework.response import Response
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

class LinearRegressionViewSet(viewsets.ViewSet):
    def create(self, request):
        response = {}
        files = self.request.FILES
        data = request.data

        for file in files:
            fileName = file.filename
            linearRegression = LinearRegression()
            if file and allowed_file(fileName):
                readFile = pd.read_excel(file)
                X = readFile.iloc[:, :-1].values
                y = readFile.iloc[:, -1].values
                model = LinearRegression()
                model.fit(X, y)
                y_pred = model.predict(data)
                prob = model.predict_proba(data)
                r2 = r2_score(y, y_pred)
                response[fileName] = {'resposta': y_pred, 'probabilidade': prob}
            else:
                return Response({'message': 'File format not supported'}, status=status.HTTP_400_BAD_REQUEST)        
        return Response(response, status=status.HTTP_200_OK)
