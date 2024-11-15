// 正規表現ルール宣言 javascriptのルールに則って宣言
let pattern = /^\d{3}-?\d{4}$/g;

// マッチするか検証する文字列、変更せずOK
let subject = '110-0003';

// よくありそうな処理(subjectの文字列がpatternで検知できるか)
var result = subject.match(pattern);