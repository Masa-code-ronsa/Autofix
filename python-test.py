# 正規表現ライブラリのインポート
import re

# 正規表現ルールの宣言 Pythonのルールに則って宣言
pattern = '^(\d+)-([a-z]{3})-alert-(\d+\1)$'

# マッチするか検証する文字列 特に変更せずOK
subject = "test@example.com"

# よくありそうな処理(subjectの文字列がpatternで検知できるか)
result = re.match(pattern, subject)
