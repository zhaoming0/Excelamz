
from flask import Flask, request, render_template, send_file
import pandas as pd
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/transform', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    data = pd.read_excel(request_file)
    # TODO: 对数据进行处理
    # data = process_data(data)

    result = BytesIO()
    data.to_excel(result, index=False)
    result.seek(0)

    return send_file(result, download_name='output.xlsx', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

