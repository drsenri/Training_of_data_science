#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from myfunc import *
from sklearn.ensemble import RandomForestClassifier

## 実行ブロック

### train
train = pd.read_csv("data/train.csv")
id_train, df_train = process_titanic(train, "train")
X, y = convert_input(df_train, "Survived")
# あとでハイパーパラメータの設定を入れる
model = RandomForestClassifier()
model.fit(X, y)

### test
test = pd.read_csv("data/test.csv")
id_test, df_test = process_titanic(train, "test")
X_test = convert_input(df_test, None)
pred = model.predict(X_test)
result = pd.DataFrame({"PassengerId": id_test, "Survived": pred})
result.to_csv("result.csv", index = False)
