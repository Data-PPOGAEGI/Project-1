from fastapi import FastAPI, Form, Request
from pyngrok import ngrok
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import nest_asyncio
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory = "C:\\Workspace\\python\\빅데이터 지능형서비스 개발 팀프로젝트(21.9.27~10.6)\\Project-1\\조정범\\static"), name = "static")
templates = Jinja2Templates(directory = "C:\\Workspace\\python\\빅데이터 지능형서비스 개발 팀프로젝트(21.9.27~10.6)\\Project-1\\조정범\\templates")

@app.get('/', response_class=HTMLResponse)
async def home(request : Request) :
    return templates.TemplateResponse("Input.html", context={"request": request})


@app.post("/info")
async def info(request : Request, sex: int = Form(...), age: int = Form(...), sido: int = Form(...),
                   type: int = Form(...), jucode: str = Form(...), bucode: str = Form(...),
                   rate: int = Form(...), day: int = Form(...)):


    # 주상병코드, 부상병코드 처리
    eng_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']
    code_dict = dict(zip(eng_list, [i for i in range(len(eng_list))]))
    jucode = code_dict[jucode]
    bucode = code_dict[bucode]

    # 나이 처리
    age = (age//10)*10

    # 가산율 처리
    rate = float(rate)

    # 모델 불러오기
    import joblib
    load_model = joblib.load('C:\\Workspace\\python\\빅데이터 지능형서비스 개발 팀프로젝트(21.9.27~10.6)\\Project-1\\손학영\\tree_model.pkl')

    # 예측하기
    predict= load_model.predict([[sex, age, sido, type, jucode, bucode, rate, day]])
    result = int(predict[0])

    if result == 0 :
        answer = "비입원 환자입니다"
    elif result == 1 :
        answer = "입원환자입니다."


    return templates.TemplateResponse("Test(Output).html", {"request":request, "answer" : answer})

ngrok_tunnel = ngrok.connect(8000)
print ('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)