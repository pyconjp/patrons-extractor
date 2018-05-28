# patrons-extractor

Thank you for PyCon JP patron sponsors!

connpassのイベントページから、Patronの一覧を抽出してreStructuredText形式で出力するスクリプト.
出力したものをPyCon JP Websiteのページに貼り付けるとPatron Sponsorの一覧を以下のページのように出力出来ます。

- [Patronスポンサー | PyCon JP 2015 in Tokyo](https://pycon.jp/2015/ja/sponsors/patrons/)
- [Patronスポンサー | PyCon JP 2016 in Tokyo](https://pycon.jp/2016/ja/sponsors/patrons/)
- [Patronスポンサー | PyCon JP 2017 in Tokyo](https://pycon.jp/2017/ja/sponsors/patrons/)


## How to run

```
$ python --version
Python 3.5.1
$ pip install -r requirements.txt -c constraints.txt
$ python patrons_extractor.py
```


## Authors

- Masashi Shibata: @c-bata


## LICENSE

```
The MIT License (MIT)

Copyright (c) 2016 PyCon JP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
