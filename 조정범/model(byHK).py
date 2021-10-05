from fastapi import FastAPI, Form, Request
from pyngrok import ngrok
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import nest_asyncio

app = FastAPI()

# app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory = "C:\\Workspace\\python\\빅데이터 지능형서비스 개발 팀프로젝트(21.9.27~10.6)\\Project-1\\조정범\\Data\\시각화자료들\\홈페이지 템플릿\\bare-gh")

@app.get('/', response_class=HTMLResponse)
async def home(request : Request) :
    return templates.TemplateResponse("index.html", context={"request": request})


@app.post("/info", response_class=HTMLResponse)
async def info(request : Request, sex : str = Form(...), age : int = Form(...), sido : str = Form(...),
               type : str = Form(...), jucode : str = Form(...), bucode : str = Form(...),
               rate : str = Form(...), day : str = Form(...)) :
    # 변수 타입 처리
    sex = int(sex)
    sido = int(sido)
    type = int(type)
    rate = float(rate)
    day = int(day)

    age = (age//10)*10


    result = "입원 환자입니다."
    # result = model.predict(sex, age, sido, type, jucode, bucode, rate, day)

    return result
    # return templates.TemplateResponse("output.html",  {"request": request, "result" : result})

ngrok_tunnel = ngrok.connect(8000)
print ('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)