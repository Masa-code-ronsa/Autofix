# 正規表現ライブラリのインポート
import re

# 正規表現ルールの宣言 Pythonのルールに則って宣言
pattern = '^\s*(.*?)\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*\(\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*x\s*(\d+)\s*\)```^\s*(.*?)\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*\(\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*x\s*(\d+)\s*\)$'

# マッチするか検証する文字列 特に変更せずOK
subject = "test@example.com"

# よくありそうな処理(subjectの文字列がpatternで検知できるか)
result = re.match(pattern, subject)
