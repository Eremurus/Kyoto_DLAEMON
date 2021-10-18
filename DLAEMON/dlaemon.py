import tkinter
import tkinter.filedialog
import torch
import torch.nn as nn
import torchvision
from torchvision import  transforms, models
from PIL import Image, ImageTk
import tkinter.font as f
import numpy as np

WIDTH  = 640        
HEIGHT = 400       

main = tkinter.Tk()
main.title("DLAEMON produced by iGEM Kyoto 2021")
main.geometry("640x440")


net = models.resnet18()
fc_input_dim = net.fc.in_features
net.fc = nn.Linear(fc_input_dim, 2)

device = torch.device("cpu")
model = 0
model = net.to(device)

model.load_state_dict(
    torch.load("./Cherry_model_Fine_Tuning.pth", map_location=lambda storage, loc: storage)
)
model = model.eval()

font_result = f.Font(family="Lucida Console", weight="bold", size=30)
font_app_name = f.Font(family="Lucida Console", weight="bold", size=35, slant="italic")

def choose():
    ### グローバル変数
    global image_tk
    global image_pil

    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="choose file")
    ### 画像ロード
    image_pil = Image.open(open(name, 'rb'))
    image_pil = image_pil.resize((224, 224))
    transform = transforms.Compose([
                transforms.ToTensor()
    ])
    image_tk = ImageTk.PhotoImage(image_pil)
    image_pil = transform(image_pil).unsqueeze(0)
    
    ### キャンバスに表示
    canvas.create_image(WIDTH/2, HEIGHT/2, image=image_tk)


def judge():

    output = model(image_pil)
    _max, prediction_max = torch.max(output, 1)
    _min, prediction_min = torch.min(output, 1)

    result = prediction_max[0].item()

    if result == 0:
        Label = tkinter.Label(main, text="HEALTHY",foreground='dark green')
        Label["font"] = font_result
        Label.place(x=250, y=25)
        label_pred = tkinter.Label(main, text=np.exp(_max.item())/(np.exp(_max.item()+np.exp(_min.item()))))
        label_pred.place(x=100, y=10)
    elif result == 1:
        Label = tkinter.Label(main, text="INFECTED",foreground='gray5')
        Label["font"] = font_result
        Label.place(x=250, y=25)
        label_pred = tkinter.Label(main, text=np.exp(_max.item())/(np.exp(_max.item()+np.exp(_min.item()))))
        label_pred.place(x=100, y=10)

### ボタン作成・配置
button1 = tkinter.Button(main, text="Choose image (*^^*)",command=choose)

button2 = tkinter.Button(main, bg='SteelBlue1',text="Diagnose٩( ᐛ )و",command=judge)
button2.pack(side='bottom')
button1.pack(side='bottom')

### キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
logo_igem = Image.open('Middle5-min.png')
logo_igem = ImageTk.PhotoImage(logo_igem)
logo_dla = Image.open('doraemon.png')
logo_dla = ImageTk.PhotoImage(logo_dla)
canvas.place(x=100, y=50) 
canvas.create_image(470, 200, image=logo_igem, anchor=tkinter.NW)
canvas.create_image(440, 330, image=logo_dla, anchor=tkinter.NW)

canvas.pack()

### イベントループ
main.mainloop()