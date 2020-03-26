# 業績管理リポジトリ [![Build Status](https://travis-ci.org/yamaoka-kitaguchi-lab/publications.svg?branch=master)](https://travis-ci.org/yamaoka-kitaguchi-lab/publications) ![validator](https://github.com/yamaoka-kitaguchi-lab/publications/workflows/validator/badge.svg)
学生の研究業績（学位論文・学会誌論文・雑誌論文）を管理するリポジトリです．
1. masterブランチのJSONファイルは[業績ページ](https://www.net.ict.e.titech.ac.jp/publications/)からJavascript経由で動的に参照されます
1. masterブランチは保護されており，ローカルの変更を反映するにはプルリクエストを作成する必要があります
1. プルリクエスト作成時に自動で構文チェックが実行され，これに成功した場合のみマージすることができます

## 各JSONファイルの目的
業績の更新時に編集が必要となるJSONファイルを説明します．  
**新年度の業績登録など，新しくJSONファイルを追加する場合は，必ず前年度JSONファイルのコピーを元に作業してください．**（手で直打ちするとだいたいミスします）

### index.json
[業績ページ](https://www.net.ict.e.titech.ac.jp/publications/)で実行されるJavascriptに「何年度の業績を掲載するか」を指示します．  
例えば，以下のように記述すると

- 学位論文の2016年度・2017年度
- 国内学会誌論文の2018年度・2017年度
- 国際学会誌論文の2018年度・2017年度
- 雑誌論文の2018年度・2017年度

がWebに掲載されることになります．  

```
  "publications": {
    "degree": [2017, 2016],
    "domestic": [2018, 2017],
    "international": [2018, 2017],
    "journal": [2018, 2017]
  }
```

**構文チェックの対象外です．慎重に編集してください．**  
**このファイルが破壊されるとWebページが適切に表示されなくなります．**

### degree/degree_20??.json
学位論文を登録します．  

- *id*: 業績を一意特定可能な番号です．例えば2016年度学位論文の場合は，*160*をプレフィックスにしてください
- *degree*: 学士・修士・博士から選びます
- *name*: 学生の氏名です．姓と名の間は半角スペースを入れてください
- *title*: 学位論文の題目です
- *supervisor*: 主指導教員名です
- *previous*: 先行研究者となる学生の氏名です
- *tag*: 論文のキーワードです
- *url*: 論文をダウンロード可能なURLです．必ずintraゾーンに配置してください

```
    {
      "id": "16001",
      "degree": {"ja": "学士", "en": "Bachelor"},
      "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
      "title": {"ja": "情報通信ネットワークに関する研究", "en": ""},
      "supervisor": {"ja": "山岡 克式", "en": "Katsunori YAMAOKA"},
      "previous": {"ja": "東工 花子", "en": "Hanako TOUKOU"},
      "tag": [
        {"ja": "受付制御", "en": "Admission control"}
      ],
      "url": "http://s3.intra.net.ict.e.titech.ac.jp/minio/publications/16001/"
    },
```

末尾カンマ（ケツカンマ）に注意してください．  
**最後のエントリはカギ括弧末尾にカンマをつけてはいけません．**

```
[
  {
    ...
  },
  {
    ...
  },
  {
    ...
  }
]
```

### domestic/domestic_20??.json
国内学会誌論文を登録します．

- *id*: 業績を一意特定可能な番号です．例えば2016年度国内学会誌論文の場合は，*161*をプレフィックスにしてください
- *name*: 学生の氏名です．姓と名の間は半角スペースを入れてください
- *title*: 論文の題目です
- *conference*: 学会名です
- *coresearcher*: 共同研究者名です
- *location*: 学会開催地です
- *date*: 発表日です
- *url*: 論文をダウンロード可能なURLです．必ずintraゾーンに配置してください

```
    {
      "id": "16101",
      "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
      "title": {"ja": "情報通信ネットワークに関する研究", "en": ""},
      "conference": {"ja": "情報通信ネットワーク研究会", "en": ""},
      "coresearcher": [
        {"ja": "リサーチ・ラボ", "en": ""},
        {"ja": "山岡 克式", "en": "Katsunori Yamaoka"}
      ],
      "location": {"ja": "東京工業大学 大岡山キャンパス", "en": ""},
      "date": {"ja": "2016年9月", "en": "Sep., 2016"},
      "url": "http://s3.intra.net.ict.e.titech.ac.jp/minio/publications/16101/"
    },
```

### international/international_20??.json
国際学会誌論文を登録します．

- *id*: 業績を一意特定可能な番号です．例えば2016年度国際学会誌論文の場合は，*162*をプレフィックスにしてください
- *name*: 学生の氏名です．姓と名の間は半角スペースを入れてください
- *title*: 論文の題目です
- *conference*: 学会名です
- *coresearcher*: 共同研究者名です
- *location*: 学会開催地です（国名と都市名）
- *date*: 発表日です
- *url*: 論文をダウンロード可能なURLです．必ずintraゾーンに配置してください

```
    {
      "id": "16201",
      "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
      "title": {"ja": "", "en": "Research on information communication networks"},
      "conference": {"ja": "", "en": "Information Network Conference"},
      "coresearcher": [
        {"ja": "", "en": "Research Lab Co., Ltd."},
        {"ja": "山岡 克式", "en": "Katsunori Yamaoka"}
      ],
      "location": {"ja": "", "en": "Las Vegas, US"},
      "date": {"ja": "2017年1月", "en": "Jan., 2017"},
      "url": "http://s3.intra.net.ict.e.titech.ac.jp/minio/publications/16201/"
    },
```

### journal/journal_20??.json
雑誌論文を登録します．

- *id*: 業績を一意特定可能な番号です．例えば2016年度雑誌論文の場合は，*163*をプレフィックスにしてください
- *name*: 学生の氏名です．姓と名の間は半角スペースを入れてください
- *title*: 論文の題目です
- *journal*: 論文誌名です
- *coresearcher*: 共同研究者名です
- *vol*: ボリューム番号です
- *pp*: ページ番号です
- *date*: 発表日です
- *url*: 論文をダウンロード可能なURLです．必ずintraゾーンに配置してください

```
    {
      "id": "16301",
      "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
      "title": {"ja": "", "en": "Research on information communication networks"},
      "journal": {"ja": "", "en": "Transaction on Information Networks"},
      "coresearcher": [
        {"ja": "", "en": "Research Lab Co., Ltd."},
        {"ja": "山岡 克式", "en": "Katsunori Yamaoka"}
      ],
      "vol": "A101",
      "no": "1",
      "pp": "123-131",
      "date": {"ja": "2016", "en": "2016"},
      "url": "http://s3.intra.net.ict.e.titech.ac.jp/minio/publications/16301/"
    },
```
