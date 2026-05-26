import os
from flask import Flask, render_template, send_file

app = Flask(__name__)

# 1. 最終確認画面（特商法準拠）
@app.route('/confirm')
def confirm():
    # 審査用ダミーデータ：現在の沸騰記事に合わせます
    product = {
        "name": "NVIDIA フィジカルAI 戦略分析レポート（2026年5月版）",
        "price": "2,000",
        "id": "nv-001"
    }
    return render_template('confirm.html', product=product)

# 2. ダミーの支払い処理（Stripeをスキップして成功画面へ）
@app.route('/dummy_pay', methods=['POST'])
def dummy_pay():
    # 本来はここでStripe APIを呼び出しますが、今回は直接リダイレクト
    return render_template('success.html')

# 3. PDFのダウンロード処理
@app.route('/download')
def download_file():
    # filesフォルダ内のPDFを送信します
    path = "files/sample_report.pdf"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    # Railwayのポート設定に対応
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
