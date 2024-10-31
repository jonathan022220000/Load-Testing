from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_form(result: str = ""):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator</title>
    </head>
    <body>
        <h1>Calculator</h1>
        <form action="/calculate" method="post">
            <label for="num1">Number 1:</label>
            <input type="text" id="num1" name="num1" required><br><br>
            
            <label for="num2">Number 2:</label>
            <input type="text" id="num2" name="num2" required><br><br>
            
            <label for="operation">Operation:</label>
            <select id="operation" name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select><br><br>
            
            <input type="submit" value="Calculate">
        </form>
        {f'<h2>Result: {result}</h2>' if result else ''}
    </body>
    </html>
    """

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    num1: float = Form(...),
    num2: float = Form(...),
    operation: str = Form(...)
):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return HTMLResponse(content="<h2 style='color: red;'>Error: Division by zero</h2>" + read_form(), status_code=400)
        result = num1 / num2
    else:
        return HTMLResponse(content="<h2 style='color: red;'>Error: Invalid operation</h2>" + read_form(), status_code=400)
    
    return HTMLResponse(content=read_form(result=result))
