// 正規表現ライブラリのインポート
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
 public static void main(String[] args) {
    //正規表現ルールの宣言 Javaのルールに則って正規表現を宣言
    Pattern p = Pattern.compile("\\d{2,4}-\\d{2,4}-\\d{2,4}");
    
    //マッチするか検証する文字列、変更せずOK
    String subject = "012-345-6789";

    // よくありそうな処理(subjectの文字列がpatternで検知できるか)
    Matcher m = p.matcher(subject);
    System.out.println(m.find()); 
    }
}