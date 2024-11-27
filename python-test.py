# 正規表現ライブラリのインポート
import re

# 正規表現ルールの宣言 Pythonのルールに則って宣言
pattern = '(?P<name>.+?)\s(?P<total_weight>\d+(\.\d+)?)\s?(?P<total_weight_unit>\S+)\s\((?P<unitWeight>\d+(\.\d+)?)\s?(?P<unitWeight_unit>\S+)\sx\s(?P<portion_no>\d+)\)'

# マッチするか検証する文字列 特に変更せずOK
subject = "test@example.com"

# よくありそうな処理(subjectの文字列がpatternで検知できるか)
result = re.match(pattern, subject)
