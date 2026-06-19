from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reloj Elegante</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Segoe UI',sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background:linear-gradient(135deg,#0f172a,#1e293b,#334155);
            overflow:hidden;
        }

        .bg{
            position:absolute;
            width:500px;
            height:500px;
            background:rgba(59,130,246,.25);
            filter:blur(120px);
            border-radius:50%;
            animation:float 8s ease-in-out infinite;
        }

        @keyframes float{
            0%,100%{transform:translateY(0);}
            50%{transform:translateY(-40px);}
        }

        .card{
            position:relative;
            z-index:10;
            backdrop-filter:blur(18px);
            background:rgba(255,255,255,.08);
            border:1px solid rgba(255,255,255,.15);
            border-radius:30px;
            padding:50px;
            width:90%;
            max-width:700px;
            text-align:center;
            color:white;
            box-shadow:0 20px 60px rgba(0,0,0,.4);
        }

        h1{
            font-size:2rem;
            margin-bottom:25px;
            font-weight:600;
            letter-spacing:1px;
        }

        #clock{
            font-size:5rem;
            font-weight:bold;
            color:#60a5fa;
            text-shadow:0 0 25px rgba(96,165,250,.7);
        }

        #date{
            margin-top:20px;
            font-size:1.4rem;
            color:#e2e8f0;
        }

        .footer{
            margin-top:30px;
            color:#94a3b8;
            font-size:.9rem;
        }

        @media(max-width:768px){
            #clock{
                font-size:3rem;
            }

            #date{
                font-size:1.1rem;
            }
        }
    </style>
</head>
<body>

<div class="bg"></div>

<div class="card">
    <h1>🕒 Reloj en Tiempo Real</h1>

    <div id="clock">00:00:00</div>
    <div id="date">Cargando fecha...</div>

    <div class="footer">
        Landing Page creada con Flask
    </div>
</div>

<script>
function updateClock() {
    const now = new Date();

    const time = now.toLocaleTimeString('es-ES');
    const date = now.toLocaleDateString('es-ES', {
        weekday:'long',
        year:'numeric',
        month:'long',
        day:'numeric'
    });

    document.getElementById('clock').innerText = time;
    document.getElementById('date').innerText =
        date.charAt(0).toUpperCase() + date.slice(1);
}

setInterval(updateClock, 1000);
updateClock();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)