# Training_of_data_science
データ分析のトレーニング
## はじめに (インストール～起動まで)
1. Python (Anaconda) のインストール<br>
以下のサイトからAnaconda (Python3.6版) をダウンロードする<br>
https://www.anaconda.com/download/<br>
※Python3.xと2.xは互換性がないため、間違えないように<br>
ダウンロードしたら、インストーラに従ってインストールする (初期設定のままでよい)
2. Jupyter Labのインストール (optional)<br>
今回のトレーニングは基本的にJupyterを使う<br>
Anacondaでは、Jupyter Notebookが標準でインストールされているが、Jupyter Labが後継版として開発されている<br>
- Anaconda Promptを起動
- > pip install jupyterlab
- [y]/nの質問が来たら、yを押してEnter
(Jupyter Notebookでも同じことができるので、Jupyter Labは必須ではない)
3. Jupyter Labを起動する
- Anaconda Promptを起動
- > jupyter lab
- webブラウザが起動し、Jupyterのページが開く

## Jupyterを動かす
1. ノートブックの作成
起動するとLauncherが表示されるので、Notebook->Python3を選択
2. テキストボックス内に適当に打ち込んでみる
- 例)
- > a = [1, 2]
- > a
3. セル内にカーソルがある状態 (文字を書ける状態) でEscもしくはCtrl+Mを押し、コマンドモードに移る
4. コマンドモードでの基本的なショートカットコマンドを試す
- よく使うコマンド (コマンド一覧はJupyter Labの左端のCommandsを押すと表示される)
- > A: 選択中のセルの上に新しいセルを作る
- > B: 選択中のセルの下に新しいセルを作る
- > D, D: 選択中のセルを削除する
- > C: 選択中のセルをコピーする
- > X: 選択中のセルをカットする
- > V: コピーorカットしたセルを選択中のセルの下にペーストする
- > Ctrl+Enter: 選択中のセルを実行する (2で書いたセルを選択すると、実行して最終行の返り値である[1, 2]がセルの直下に出力される)
- > M: 選択中のセルをマークダウンにする (コードの説明などを書くのに使う)
- > Y: 選択中のセルをPythonコマンドにする (間違えてM押したら使う)
- > Shift+M: 選択中のセルを結合する
- > Ctrl+Shift+-: セルを分割する(※これはコマンドモードでなく、セルの編集中にやる)
5. 一通り動かしたら、Notebookをリネームして保存する (File->Rename Notebook, File->Save)
6. Anaconda PromptでCtrl+Cを押して、Jupyter Labを終了する

## 補足
- データ分析用のライブラリ (numpy, pandas, scikit-learnなど) は標準Pythonには付属していないため、それらを含んでいるAnacondaを推奨している
- Jupyter Labの白背景が見づらい場合、Settings->Advance Settings Editor->Theme->右側のUser Overridesの{}内に以下の設定を書き込んで保存すると黒背景になる
- > "theme": "JupyterLab Dark"
