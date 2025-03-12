# 필요한 라이브러리 가져오기
# Flask 라이브러리를 통해 웹 애플리케이션을 생성하고, 요청과 응답을 처리합니다.
from flask import Flask, render_template, request, jsonify, send_file
# qrcode 라이브러리를 통해 QR 코드를 생성합니다.
import qrcode
# io 라이브러리를 통해 메모리에서 파일을 임시로 저장합니다.
import io

# Flask 앱 만들기
app = Flask(__name__)

# 메인 페이지
@app.route('/')
def show_main_page():
    return render_template('index.html')  # HTML 템플릿 렌더링

# QR 코드 생성하기
@app.route('/make_qr', methods=['GET'])
def make_qr_code():
    # 사용자가 입력한 웹주소 가져오기
    web_address = request.args.get('url')

    # 웹주소가 없으면 에러 메시지 보내기
    if not web_address:
        return jsonify({"에러": "웹주소를 입력해주세요!"}), 400

    # QR 코드 이미지 만들기
    qr_image = qrcode.make(web_address)
    
    # 이미지를 메모리에 임시 저장
    image_memory = io.BytesIO()
    qr_image.save(image_memory, 'PNG')
    image_memory.seek(0)

    # QR 코드 이미지 보내주기
    return send_file(image_memory, mimetype='image/png')

# 프로그램 시작
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

