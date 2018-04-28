#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def process_titanic(df, type):
    '''
    Titanicのデータの前処理を行う

    @param  df    : input data (Data.Frame)
    @param  type  : process type (str, "train"/"test")
    @return id    : passenger ID (list)
    @return df_p  : processed data (Data.Frame)

    データ型と変換の方法
    @PassengerId : int、除外する
    @Survived    : int、目的変数として返す
    @Pclass      : int、
    @Name        : str
    @Sex         : str、欠損あり、ダミー変数化して返す
    @Age         : int、年代別 (10年) でカテゴリ変数化して返す
    @SibSp       : int
    @Parch       : int
    @Ticket      : str、
    @Fare        : float
    @Cabin       : 欠損あり
    @Embarked    : 欠損あり
    '''

    id = df.PassengerId

    # remove
    df.drop(["PassengerId", "Name"], axis=1, inplace=True)

    # Sex (to dummy)
    sex_dummy = pd.get_dummies(df["Sex"])


    return id, df_p


def convert_input(df, y_name):
    '''
    pd.DataFrameからsklearnに入れる形に変換する

    @param  df     : input data (pd.Data.Frame)
    @param  y_name : column of objective variable (str)
    @return X      : feature variable (np.ndarray)
    @return y      : objective variable (np.array)
    '''


    return X, y
